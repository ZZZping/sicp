"""Prepare sentence-level SICP comparisons and collect local Ollama suggestions.

Local model suggestions cannot approve or change book pages. The apply command
requires a complete, separately recorded editor review and unchanged sources.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import html
import json
from pathlib import Path
import re
import time
from datetime import datetime
import shutil
import tempfile
import xml.etree.ElementTree as ET

import requests

from translate_v3 import (ROOT, MARK, TAG, Unit, units, validate_translation,
                          restore, localize_links, validate_page)

LEDGER = ROOT / 'sentence_review.json'
SUGGESTIONS = ROOT / 'sentence_suggestions.json'
PROGRESS = ROOT / 'sentence_review_progress.json'
EDITOR = ROOT / 'sentence_editor_decisions.json'


def math_text(element):
    tag = element.tag.rsplit('}', 1)[-1]
    children = [math_text(c) for c in element if isinstance(c.tag, str)]
    if tag == 'mfrac' and len(children) == 2:
        return f'({children[0]})/({children[1]})'
    if tag == 'msup' and len(children) == 2:
        return f'{children[0]}^({children[1]})'
    if tag == 'msub' and len(children) == 2:
        return children[0] + '_{' + children[1] + '}'
    if tag == 'msqrt':
        return 'sqrt(' + ''.join(children) + ')'
    if tag in {'mtd', 'mtr'}:
        return ' '.join(children)
    return (element.text or '') + ''.join(children)


def readable(unit, text):
    def token(m):
        value = unit.tokens[int(m[1])]
        if value.startswith('<math'):
            return '$' + re.sub(r'\s+', '', math_text(ET.fromstring(value))) + '$'
        if value.startswith(('<code', '<var', '<samp', '<kbd')):
            return '`' + html.unescape(TAG.sub('', value)) + '`'
        if 'footnote_link' in value or 'footnote_backlink' in value:
            return '[注' + TAG.sub('', value).strip() + ']'
        if value.startswith('<span class="secnum"'):
            return TAG.sub('', value) + ' '
        if value.startswith('<object'):
            return '[原图]'
        if value.startswith('<'):
            return ''
        return value
    return re.sub(r'\s+', ' ', MARK.sub(token, text)).strip()


def sentences(text):
    """Sentence spans, retaining all characters and common English abbreviations."""
    protected = set()
    for match in re.finditer(r'\b(?:e\.g\.|i\.e\.|et al\.|etc\.|Mr\.|Mrs\.|Dr\.|Prof\.|Jr\.|Sr\.|St\.|A\.D\.|B\.C\.|[A-Z]\.)(?=\s|$)', text):
        protected.update(range(match.start(), match.end()))
    cuts = [0]
    for match in re.finditer(r'[.!?][”’"\')]*(?:\[注\d+\])*(?:\s+|$)', text):
        if match.start() not in protected and match.end() < len(text):
            cuts.append(match.end())
    cuts.append(len(text))
    return [text[a:b] for a, b in zip(cuts, cuts[1:]) if text[a:b].strip()]


def atomic_json(path, data):
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8', newline='')
    temporary.replace(path)


def record_editor_review(start, end, corrections=None, notes=None):
    """Record an explicitly inspected range; never called by the local model."""
    data = json.loads(LEDGER.read_text(encoding='utf-8'))
    saved = json.loads(EDITOR.read_text(encoding='utf-8')) if EDITOR.exists() else {}
    corrections, notes = corrections or {}, notes or {}
    if not 0 <= start < end <= len(data['units']):
        raise ValueError('Invalid review range')
    for i in range(start, end):
        row = data['units'][i]
        value = corrections.get(i, row['translation'])
        unit = Unit(0, 0, row['source'], row['tokens'], row['key'])
        validate_translation(unit, value)
        saved[row['id']] = {'key': row['key'], 'translation': value,
                            'sentence_verdicts': ['checked'] * len(row['sentences']),
                            'changed': value != row['translation'],
                            'note': notes.get(i, '')}
    atomic_json(EDITOR, saved)
    print(f'Editor checked units [{start}, {end}); total={len(saved)}; '
          f'sentences={sum(len(v["sentence_verdicts"]) for v in saved.values())}; '
          f'corrected={sum(v["changed"] for v in saved.values())}')


def prepare():
    if LEDGER.exists():
        data = json.loads(LEDGER.read_text(encoding='utf-8'))
        print(f'Existing ledger: {len(data["units"])} units; {data["sentence_count"]} source sentences/fragments')
        return
    cache = json.loads((ROOT / 'translation_cache_v3.json').read_text(encoding='utf-8'))
    data = {'version': 1, 'pages': {}, 'units': [], 'sentence_count': 0}
    for path in sorted((ROOT / 'html').glob('*.xhtml')):
        if path.stem.endswith('_zh'):
            continue
        chinese = path.with_name(path.stem + '_zh.xhtml')
        data['pages'][path.name] = {'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                                  'translation_sha256': hashlib.sha256(chinese.read_bytes()).hexdigest()}
        for i, unit in enumerate(units(path.read_text(encoding='utf-8')), 1):
            source = readable(unit, unit.text)
            target = readable(unit, cache[unit.key])
            parts = sentences(source)
            row = {'id': f'{path.stem}:{i:04d}', 'file': path.name, 'key': unit.key,
                   'source': unit.text, 'translation': cache[unit.key], 'tokens': unit.tokens,
                   'source_readable': source, 'translation_readable': target,
                   'sentences': parts, 'editor_status': 'pending'}
            data['units'].append(row)
            data['sentence_count'] += len(parts)
    atomic_json(LEDGER, data)
    print(f'Prepared {len(data["units"])} units; {data["sentence_count"]} source sentences/fragments')


SYSTEM = '''你是 SICP 英汉翻译的校对助手。只检查原文与已有译文是否准确对应，不改写正确的内容，不增加原文没有的解释、答案或事实。
每个输入条目提供按句编号的英文 sentences 和整段中文 translation。请逐句检查原文的每个事实、限定、否定、比较方向、条件、主客体、运算关系、术语和引用是否完整准确地出现在译文中，同时检查译文有没有凭空添加内容。
术语：procedure=过程，process=计算过程，expression=表达式，evaluation=求值，environment=环境，binding=绑定，pair=序对，list=表，stream=流，continuation=继续过程。人名、程序标识符、公式、书目原始出版信息允许保留英文。
输出 JSON 对象，键与输入条目相同。每个值必须为 {"sentences":[true或false,...],"issues":[{"sentence":从1开始的编号,"problem":"具体错误","suggestion":"仅给相关中文句子的修正建议"}]}。
sentences 数组必须覆盖该条目每个英文句子，顺序和数量完全对应；true表示该句完整准确，false表示存在需修订的问题。发现多译应在对应句子中标false。只报告确实存在的问题，不要为了润色而声称原文被漏译。此任务不需要返回整段中文，也不要返回原文。'''


def suggest(model, batch_chars, limit):
    data = json.loads(LEDGER.read_text(encoding='utf-8'))
    saved = json.loads(SUGGESTIONS.read_text(encoding='utf-8')) if SUGGESTIONS.exists() else {}
    pending = [r for r in data['units'] if r['id'] not in saved]
    if limit:
        pending = pending[:limit]
    batches, batch, size = [], [], 0
    for row in pending:
        n = len(row['source_readable']) + len(row['translation_readable'])
        if batch and (size + n > batch_chars or len(batch) >= 20):
            batches.append(batch)
            batch, size = [], 0
        batch.append(row)
        size += n
    if batch:
        batches.append(batch)
    print(f'Ollama {model}: {len(pending)} blocks in {len(batches)} requests', flush=True)
    for number, rows in enumerate(batches, 1):
        payload = {str(i): {'sentences': row['sentences'], 'translation': row['translation_readable']} for i, row in enumerate(rows)}
        for attempt in range(3):
            response = requests.post('http://127.0.0.1:11434/api/chat', json={
                'model': model, 'think': False, 'stream': False, 'format': 'json',
                'messages': [{'role': 'system', 'content': SYSTEM},
                             {'role': 'user', 'content': json.dumps(payload, ensure_ascii=False)}],
                'options': {'temperature': 0, 'num_ctx': 8192, 'num_predict': 3500},
                'keep_alive': '30m'}, timeout=(10, 300))
            response.raise_for_status()
            try:
                result = json.loads(response.json()['message']['content'])
                if not isinstance(result, dict):
                    raise ValueError('Expected a JSON object')
            except (ValueError, KeyError):
                # A small model can truncate a long reply. Keep completed work
                # and leave failed rows pending, never mark them reviewed.
                print(f'Invalid model JSON in batch {number}, attempt {attempt + 1}', flush=True)
                continue
            good = {}
            for i, row in enumerate(rows):
                item = result.get(str(i), {})
                flags = item.get('sentences', [])
                issues = item.get('issues', [])
                if len(flags) != len(row['sentences']) or any(type(flag) is not bool for flag in flags):
                    continue
                if not isinstance(issues, list):
                    continue
                good[row['id']] = {'model': model, 'sentences': flags, 'issues': issues}
            saved.update(good)
            atomic_json(SUGGESTIONS, saved)
            if len(good) == len(rows):
                break
            rows = [row for row in rows if row['id'] not in good]
            payload = {str(i): {'sentences': row['sentences'], 'translation': row['translation_readable']} for i, row in enumerate(rows)}
        print(f'Batch {number}/{len(batches)}; suggestions={len(saved)}/{len(data["units"])}', flush=True)


def show(start, chars):
    data = json.loads(LEDGER.read_text(encoding='utf-8'))
    saved = json.loads(SUGGESTIONS.read_text(encoding='utf-8')) if SUGGESTIONS.exists() else {}
    size = 0
    end = start
    for i, row in enumerate(data['units'][start:], start):
        en = ' '.join(f'({j}) {s.strip()}' for j, s in enumerate(row['sentences'], 1))
        text = f'[{i}] {row["id"]}\nEN {en}\nZH {row["translation_readable"]}\n'
        issues = saved.get(row['id'], {}).get('issues', [])
        if issues:
            text += 'LOCAL ' + json.dumps(issues, ensure_ascii=False) + '\n'
        if size + len(text) > chars and end > start:
            break
        print(text)
        size += len(text)
        end = i + 1
    print(f'NEXT={end} TOTAL={len(data["units"])}')


def reviewed_values(data, decisions):
    """Reject incomplete, stale, conflicting, or structurally invalid reviews."""
    if set(decisions) != {row['id'] for row in data['units']}:
        raise ValueError('Every source unit must have an editor decision')
    values = {}
    for row in data['units']:
        decision = decisions[row['id']]
        if decision['key'] != row['key']:
            raise ValueError(f'Stale editor decision: {row["id"]}')
        if decision['sentence_verdicts'] != ['checked'] * len(row['sentences']):
            raise ValueError(f'Incomplete sentence review: {row["id"]}')
        value = decision['translation']
        validate_translation(Unit(0, 0, row['source'], row['tokens'], row['key']), value)
        if row['key'] in values and values[row['key']] != value:
            raise ValueError(f'Conflicting repeated source: {row["id"]}')
        values[row['key']] = value
    return values


def apply_review():
    data = json.loads(LEDGER.read_text(encoding='utf-8'))
    decisions = json.loads(EDITOR.read_text(encoding='utf-8'))
    values = reviewed_values(data, decisions)
    names = set(data['pages'])
    actual_names = {p.name for p in (ROOT / 'html').glob('*.xhtml') if not p.stem.endswith('_zh')}
    if names != actual_names:
        raise ValueError('Source page inventory changed since review began')
    outputs = {}
    for name, hashes in data['pages'].items():
        path = ROOT / 'html' / name
        target = path.with_name(path.stem + '_zh.xhtml')
        if hashlib.sha256(path.read_bytes()).hexdigest() != hashes['source_sha256']:
            raise ValueError(f'English source changed: {name}')
        if hashlib.sha256(target.read_bytes()).hexdigest() != hashes['translation_sha256']:
            raise ValueError(f'Chinese page changed since review began: {target.name}')
        source = path.read_text(encoding='utf-8')
        work = units(source)
        rows = [row for row in data['units'] if row['file'] == name]
        if [u.key for u in work] != [row['key'] for row in rows]:
            raise ValueError(f'Review no longer matches source blocks: {name}')
        output = source
        for unit in reversed(work):
            output = output[:unit.start] + restore(unit, values[unit.key]) + output[unit.end:]
        output = output.replace(' xml:lang="en"', ' xml:lang="zh"').replace(' lang="en"', ' lang="zh"')
        output = localize_links(output, names)
        validate_page(source, output, names)
        outputs[target] = output
    # Resolve every internal link before the first write.
    anchors = {path.name: {e.attrib['id'] for e in ET.fromstring(output).iter() if 'id' in e.attrib}
               for path, output in outputs.items()}
    for path, output in outputs.items():
        for element in ET.fromstring(output).iter():
            href = element.attrib.get('href', '')
            if not href or re.match(r'(?:[a-z]+:|//)', href):
                continue
            filename, sep, anchor = href.partition('#')
            filename = filename or path.name
            if filename in names:
                raise ValueError(f'Link to English page: {path.name}: {href}')
            if filename in anchors and sep and anchor and anchor not in anchors[filename]:
                raise ValueError(f'Broken anchor: {path.name}: {href}')
    backup = Path(tempfile.gettempdir()) / ('sicp-sentence-review-' + datetime.now().strftime('%Y%m%d-%H%M%S'))
    backup.mkdir()
    for path in outputs:
        shutil.copy2(path, backup / path.name)
    cache_path = ROOT / 'translation_cache_v3.json'
    overrides_path = ROOT / 'translation_overrides.json'
    for path in (cache_path, overrides_path):
        if path.exists():
            shutil.copy2(path, backup / path.name)
    cache = json.loads(cache_path.read_text(encoding='utf-8'))
    cache.update(values)
    overrides = json.loads(overrides_path.read_text(encoding='utf-8'))
    changed = [row for row in data['units'] if values[row['key']] != row['translation']]
    overrides.update({row['key']: values[row['key']] for row in changed})
    atomic_json(cache_path, cache)
    atomic_json(overrides_path, overrides)
    for path, output in outputs.items():
        temporary = path.with_suffix('.xhtml.tmp')
        temporary.write_text(output, encoding='utf-8', newline='')
        temporary.replace(path)
    model = json.loads(SUGGESTIONS.read_text(encoding='utf-8')) if SUGGESTIONS.exists() else {}
    summary = {'pages': len(outputs), 'reviewed_blocks': len(data['units']),
               'source_sentences_and_fragments': data['sentence_count'],
               'corrected_blocks': len(changed), 'local_model_suggested_blocks': len(model),
               'backup': str(backup), 'source_hashes_unchanged': True,
               'structure_and_protected_content_unchanged': True,
               'output_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in outputs}}
    atomic_json(ROOT / 'sentence_review_result.json', summary)
    report = ['# 中文译文逐句校订记录', '',
              '本次在现有中文译文上校订。Ollama 的 qwen3:8b 仅提供建议；编辑复核原文后单独记录决定，建议不会自动写入正文。', '',
              f'- 对照范围：{len(outputs)} 个页面，{len(data["units"])} 个文本块，{data["sentence_count"]} 个英文句子及短文本片段。',
              f'- 修订文本块：{len(changed)}；其余保留原有译文。',
              '- 计数包含标题、导航、术语及保留原始出版信息的参考文献条目；句子切分器也会把部分缩写和代码片段单独计数。',
              '- 英文文件哈希保持不变；中文页面均通过 XML、块结构、属性、代码、公式、插图、脚注及内部锚点校验。',
              '- 本记录位于书籍页面之外，不向正文添加解释、答案或译者注。', '',
              '## 修改前后对照', '']
    for row in changed:
        unit = Unit(0, 0, row['source'], row['tokens'], row['key'])
        report.extend([f'### {row["id"]}', '', '**原文**', '', row['source_readable'], '',
                       '**校订前**', '', row['translation_readable'], '', '**校订后**', '',
                       readable(unit, values[row['key']]), ''])
    (ROOT / 'TRANSLATION_REVIEW.md').write_text('\n'.join(report), encoding='utf-8')
    print(json.dumps(summary, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('prepare')
    sub.add_parser('apply', help='Apply fully reviewed editor decisions; never auto-accept model suggestions')
    local = sub.add_parser('suggest')
    local.add_argument('--model', default='qwen3:8b')
    local.add_argument('--batch-chars', type=int, default=6500)
    local.add_argument('--limit', type=int)
    view = sub.add_parser('show')
    view.add_argument('--start', type=int, default=0)
    view.add_argument('--chars', type=int, default=20000)
    args = parser.parse_args()
    if args.command == 'prepare':
        prepare()
    elif args.command == 'suggest':
        suggest(args.model, args.batch_chars, args.limit)
    elif args.command == 'show':
        show(args.start, args.chars)
    elif args.command == 'apply':
        apply_review()


if __name__ == '__main__':
    main()
