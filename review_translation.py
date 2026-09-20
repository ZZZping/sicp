"""Second, bilingual fidelity pass over the v3 translation cache.

Checks every unique block for omissions, additions and mistranslations.
Only validated corrections enter the cache; run translate_v3.py --write
afterwards to validate and materialize the reviewed pages.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
import os
from pathlib import Path
import re
import time

import requests

from translate_v3 import (PROMPT, ROOT, MARK, Translator, describe_token, units,
                          validate_translation)

REVIEW_PROMPT = PROMPT + '''
现在执行译后对照校审，而不是初译。每项包含 source（英文原文）、translation（待审中文）与 tokens（占位符含义）。
仔细对照原文，检查漏掉的限定词、否定、逻辑条件、句子或引用，以及新增的解释、括注、事实和评价。也检查错译、专名、术语、不完整句子和因行内标签造成的断句错误。保留原书本来的事实与表述，不得以现代知识擅自订正原书。不要仅因为个人风格偏好改动正确的译文。
不得修改占位符及其次数，可按中文语序移动完整行内元素，必须保持标签成对和正确嵌套。
对于每一项返回 {"ok":true}（已忠实且通顺）或 {"ok":false,"translation":"完整的修正译文","issue":"简短的问题说明"}。
只返回 JSON 对象，键与输入项完全相同；每一项都必须有结果。issue 仅作校审记录，不能写入 translation。
'''


class Reviewer(Translator):
    def __init__(self, *args, **kwargs):
        self.focus = kwargs.pop('focus', 'all')
        super().__init__(*args, **kwargs)
        self.original = dict(self.cache)
        self.review_path = ROOT / ('translation_logic_review_v3.json' if self.focus == 'logic' else 'translation_review_v3.json')
        self.reviews = json.loads(self.review_path.read_text(encoding='utf-8')) if self.review_path.exists() else {}
        self.reviewed_outputs = {(item['source_key'], item['after']) for item in self.reviews.values()}

    def review_key(self, unit):
        return hashlib.sha256((unit.key + '\0' + self.original[unit.key] + '\0review-2-' + self.focus).encode()).hexdigest()

    def reviewed(self, unit):
        return (self.review_key(unit) in self.reviews
                or (unit.key, self.original[unit.key]) in self.reviewed_outputs)

    def batch(self, batch, attempts=3):
        payload = {str(i): {'source': unit.text, 'translation': self.original[unit.key],
                           'tokens': {f'⟦{j}⟧': describe_token(t) for j, t in enumerate(unit.tokens)}}
                   for i, unit in enumerate(batch)}
        prompt = REVIEW_PROMPT
        if self.focus == 'logic':
            prompt += '\n本轮特别检查逻辑：否定是否丢失，less/more 是否译反，if/unless/only 是否改变必要或充分条件，分子分母或主体客体是否交换，each/all/any 是否遗漏，以及原文有而译文没有或译文凭空增加的事实。逐句对照，不要因为整体流畅就判定正确。readable_source 和 readable_translation 展开了占位符，便于理解真实的程序名、数学符号和数值；修正仍必须使用原有占位符。'
            for i, unit in enumerate(batch):
                def readable(text):
                    return MARK.sub(lambda m: '[' + describe_token(unit.tokens[int(m[1])]) + ']', text)
                payload[str(i)]['readable_source'] = readable(unit.text)
                payload[str(i)]['readable_translation'] = readable(self.original[unit.key])
        last_error = None
        for attempt in range(attempts):
            try:
                response = requests.post(self.endpoint, headers={'Authorization': f'Bearer {self.api_key}'},
                    json={'model': self.model, 'messages': [{'role': 'system', 'content': prompt},
                          {'role': 'user', 'content': json.dumps(payload, ensure_ascii=False)}],
                          'temperature': 0, 'max_tokens': 8192,
                          'response_format': {'type': 'json_object'}}, timeout=(15, 240))
                response.raise_for_status()
                choice = response.json()['choices'][0]
                if choice.get('finish_reason') != 'stop':
                    raise ValueError('Review response truncated')
                result = json.loads(choice['message']['content'])
                if set(result) != set(payload):
                    raise ValueError('Incomplete review response')
                corrections, reviewed, invalid = {}, {}, []
                for i, unit in enumerate(batch):
                    item = result[str(i)]
                    try:
                        if not isinstance(item, dict) or type(item.get('ok')) is not bool:
                            raise ValueError('Invalid review status')
                        value = self.original[unit.key] if item['ok'] else item['translation']
                        validate_translation(unit, value)
                        corrections[unit.key] = value
                        reviewed[self.review_key(unit)] = {'source_key': unit.key, 'before': self.original[unit.key],
                            'after': value, 'issue': item.get('issue', ''), 'changed': value != self.original[unit.key]}
                    except (KeyError, ValueError, TypeError):
                        invalid.append(unit)
                self.save(corrections)
                with self.lock:
                    self.reviews.update(reviewed)
                    temporary = self.review_path.with_suffix('.tmp')
                    temporary.write_text(json.dumps(self.reviews, ensure_ascii=False, indent=2), encoding='utf-8')
                    temporary.replace(self.review_path)
                if invalid:
                    if len(batch) == 1:
                        raise ValueError('Review violated content-preservation rules')
                    for unit in invalid:
                        self.batch([unit], attempts=attempts)
                return
            except (requests.RequestException, KeyError, ValueError, TypeError) as exc:
                last_error = exc
                time.sleep(2 ** attempt)
        if len(batch) > 1:
            middle = len(batch) // 2
            self.batch(batch[:middle], attempts=2)
            self.batch(batch[middle:], attempts=2)
            return
        raise RuntimeError(f'Review failed for {batch[0].key[:12]}: {last_error}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workers', type=int, default=8)
    parser.add_argument('--batch-chars', type=int, default=7500)
    parser.add_argument('--cache', type=Path, default=ROOT / 'translation_cache_v3.json')
    parser.add_argument('--focus', choices=['all', 'logic'], default='all')
    parser.add_argument('--model', default=os.environ.get('DEEPSEEK_MODEL', 'deepseek-chat'))
    args = parser.parse_args()
    key = os.environ.get('DEEPSEEK_API_KEY')
    if not key:
        parser.error('Set DEEPSEEK_API_KEY')
    reviewer = Reviewer(args.cache, key, args.model,
                        os.environ.get('DEEPSEEK_API_URL', 'https://api.deepseek.com/v1/chat/completions'), focus=args.focus)
    unique = {}
    for path in sorted((ROOT / 'html').glob('*.xhtml')):
        if not path.stem.endswith('_zh'):
            unique.update((unit.key, unit) for unit in units(path.read_text(encoding='utf-8')))
    if args.focus == 'logic':
        risky = re.compile(r'\b(not|no|never|only|less|more|fewer|greater|least|most|unless|if|except|both|neither|either|instead|rather|each|all|before|after|than|since|because)\b', re.I)
        unique = {key: unit for key, unit in unique.items() if len(unit.text) > 100 and risky.search(unit.text)}
    missing = set(unique) - set(reviewer.cache)
    if missing:
        parser.error(f'{len(missing)} blocks have not been translated')
    pending = [u for u in unique.values() if not reviewer.reviewed(u)]
    batches, batch, size = [], [], 0
    for unit in pending:
        length = len(unit.text) + len(reviewer.original[unit.key])
        if batch and size + length > args.batch_chars:
            batches.append(batch)
            batch, size = [], 0
        batch.append(unit)
        size += length
    if batch:
        batches.append(batch)
    print(f'Reviewing {len(pending)} unique blocks in {len(batches)} batches', flush=True)
    errors = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        jobs = [pool.submit(reviewer.batch, batch) for batch in batches]
        for i, future in enumerate(as_completed(jobs), 1):
            try:
                future.result()
                print(f'Reviewed batch {i}/{len(batches)}; blocks={len(reviewer.reviews)}', flush=True)
            except Exception as exc:
                errors.append(str(exc))
                print(f'ERROR: {exc}', flush=True)
    if errors:
        raise RuntimeError(f'{len(errors)} review batches failed; rerun to resume')
    changed = sum(item['changed'] for item in reviewer.reviews.values())
    print(f'Review complete: {len(unique)} unique blocks; {changed} corrections recorded.', flush=True)


if __name__ == '__main__':
    main()
