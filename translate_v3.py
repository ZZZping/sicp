"""Translate SICP prose as complete blocks, preserving the original XHTML.

Run without --write to audit only. Translation requires DEEPSEEK_API_KEY.
Existing Chinese pages are backed up before replacement. The English pages
are the source of truth; the fragment-based v1/v2 cache is deliberately unused.
"""
from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import datetime
import hashlib
import html
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
import threading
import time
import xml.etree.ElementTree as ET

import requests

ROOT = Path(__file__).resolve().parent
VERSION = "whole-block-v3.2"
TAG = re.compile(r'<!--[\s\S]*?-->|<!\[CDATA\[[\s\S]*?\]\]>|<\?[\s\S]*?\?>|<!DOCTYPE[^>]*>|</?[A-Za-z_][^>]*>')
ATTR = re.compile(r'([\w:.-]+)\s*=\s*([\"\'])(.*?)\2', re.S)
MARK = re.compile(r'⟦(\d+)⟧')
BLOCK = set('html head body section nav article header footer div p ul ol li dl dt dd table thead tbody tfoot tr td th blockquote figure figcaption caption h1 h2 h3 h4 h5 h6 title pre'.split())
PROTECTED = set('script style pre code math var samp kbd object svg'.split())
PROTECTED_CLASSES = {'lisp', 'prettyprinted', 'footnote_link', 'footnote_backlink', 'secnum', 'jump'}
PROMPT = '''你是《计算机程序的构造和解释》（SICP）第二版的专业中文译者。
逐条忠实翻译输入 JSON 中 text 字段的完整语义块，仅输出相同键的 JSON 对象，值为译文字符串。tokens 字段说明各占位符的含义，帮助理解上下文，不能把该说明复制进译文。
必须完整保留原文的每一个事实、条件、否定、限定、例子、引用和语气。不得概括、扩写、解释、评价、添加小标题或删减重复内容。不得增加原文没有的中英文对照括注。
整段理解后再翻译，不能把标签两侧的短语当作独立句子；中文表达自然准确。
⟦数字⟧ 是不可修改的 XHTML 标签或代码、公式、脚注、编号占位符，必须逐个原样保留，出现次数完全不变。可以为中文语序调整完整行内元素的位置，但开始和结束标签必须正确成对，不能改变标签嵌套关系或强调范围。占位符不是段落分隔符，不要把它们当成待翻译内容。数字占位符也必须保留，不能换成汉字数字。
保留程序标识符、语言名称、网址、作者姓名和书目中的出版信息，不要翻译成无关的日常词义。数字和编号原样保留。只翻译自然语言，不能给程序代码或数学符号增删任何内容。
术语统一：procedure=过程，process=计算过程（并发语境按原意译为进程），primitive procedure=基本过程，compound procedure=复合过程，abstraction=抽象，combination=组合式，expression=表达式，evaluation=求值，evaluator=求值器，interpreter=解释器，environment=环境，frame=框架，binding=绑定，substitution model=代换模型，applicative order=应用序，normal order=正则序，special form=特殊形式，higher-order procedure=高阶过程，pair=序对，list=表，stream=流，closure=闭合性（抽象代数意义；表示含自由变量的过程的技术才译为闭包），assignment=赋值，mutation=修改，dispatch=分派，constraint=约束，continuation=继续过程，register machine=寄存器机器，garbage collection=垃圾回收，metacircular evaluator=元循环求值器，metalinguistic abstraction=元语言抽象，nondeterministic=非确定性，memoization=记忆化。operator=运算符，operand=运算对象，constructor=构造函数，selector=选择函数，consequent expression=结果表达式，alternative expression=替代表达式，data path=数据通路，mutex=互斥量，unification=合一，agenda=日程表，picture language=图画语言。形参和实参需要区分时，parameter=形参，argument=实参。
已有的 Scheme、Lisp、MIT、API 等专名保持原样。The MIT Press 译为“麻省理工学院出版社”。
不得输出 Markdown 代码围栏、前言或翻译说明。'''


@dataclass
class Node:
    name: str
    start: int
    inner: int
    end_inner: int
    end: int
    attrs: dict = field(default_factory=dict)
    children: list = field(default_factory=list)


@dataclass
class Unit:
    start: int
    end: int
    text: str
    tokens: list[str]
    key: str


def parse(source: str) -> Node:
    """Record lexical offsets instead of reserializing code or MathML."""
    ET.fromstring(source)
    root = Node('document', 0, 0, len(source), len(source))
    stack = [root]
    for m in TAG.finditer(source):
        raw = m.group()
        if raw.startswith(('<!--', '<!', '<?')):
            continue
        name = re.match(r'</?([^\s/>]+)', raw)[1]
        if raw.startswith('</'):
            if stack[-1].name != name:
                raise ValueError(f'Unexpected closing tag: {name}')
            node = stack.pop()
            node.end_inner, node.end = m.start(), m.end()
        else:
            node = Node(name, m.start(), m.end(), m.end(), m.end(),
                        {a[0]: html.unescape(a[2]) for a in ATTR.findall(raw)})
            stack[-1].children.append(node)
            if not raw.endswith('/>'):
                stack.append(node)
    if len(stack) != 1:
        raise ValueError('Unclosed XHTML tag')
    return root


def protected(node: Node, source: str) -> bool:
    classes = set(node.attrs.get('class', '').split())
    if node.name in PROTECTED or classes & PROTECTED_CLASSES:
        return True
    if node.name == 'a':
        visible = html.unescape(TAG.sub('', source[node.inner:node.end_inner])).strip()
        return not visible or bool(re.fullmatch(r'(?:https?://|www\.)\S+', visible))
    return False


def units(source: str) -> list[Unit]:
    root = parse(source)
    result = []

    def emit(start, end, children):
        if start >= end:
            return
        spans = []

        def protect(n):
            if protected(n, source):
                spans.append((n.start, n.end))
            else:
                for child in n.children:
                    protect(child)

        for child in children:
            protect(child)
        cursor, parts, tokens = start, [], []

        def fragment(a, b):
            def prose(raw):
                decoded = html.unescape(raw)
                last_number = 0
                for number in re.finditer(r'\d+(?:[.,]\d+)*', decoded):
                    parts.append(decoded[last_number:number.start()])
                    parts.append(f'⟦{len(tokens)}⟧')
                    tokens.append(number.group())
                    last_number = number.end()
                parts.append(decoded[last_number:])
            last = a
            for m in TAG.finditer(source, a, b):
                prose(source[last:m.start()])
                parts.append(f'⟦{len(tokens)}⟧')
                tokens.append(m.group())
                last = m.end()
            prose(source[last:b])

        for a, b in sorted(spans):
            fragment(cursor, a)
            parts.append(f'⟦{len(tokens)}⟧')
            tokens.append(source[a:b])
            cursor = b
        fragment(cursor, end)
        text = re.sub(r'\s+', ' ', ''.join(parts)).strip()
        plain = MARK.sub('', text)
        if not re.search(r'[A-Za-z]', plain):
            return
        key = hashlib.sha256(json.dumps([VERSION, text, tokens], ensure_ascii=False).encode()).hexdigest()
        result.append(Unit(start, end, text, tokens, key))

    def walk(n):
        if protected(n, source) or n.name in {'meta', 'link'}:
            return
        start, inline = n.inner, []
        for child in n.children:
            if child.name in BLOCK or child.name in {'meta', 'link'}:
                emit(start, child.start, inline)
                walk(child)
                start, inline = child.end, []
            else:
                inline.append(child)
        emit(start, n.end_inner, inline)

    # Ignore XML declarations, doctype and document comments outside <html>.
    for child in root.children:
        if child.name == 'html':
            walk(child)
    return sorted(result, key=lambda u: u.start)


def validate_translation(unit: Unit, translated: str):
    if not isinstance(translated, str) or not translated.strip():
        raise ValueError('Empty translation')
    if Counter(MARK.findall(translated)) != Counter(MARK.findall(unit.text)):
        raise ValueError('Missing or duplicated protected tokens')
    before, after = MARK.sub('', unit.text), MARK.sub('', translated)
    if Counter(re.findall(r'\d+(?:[.,]\d+)*', before)) != Counter(re.findall(r'\d+(?:[.,]\d+)*', after)):
        raise ValueError('Numbers changed during translation')
    if '```' in translated:
        raise ValueError('Markdown wrapper in translation')
    if re.search(r'[\u4e00-\u9fff]', after) and re.search(r'(?:以下是.*?翻译|译者注|翻译如下)', after):
        raise ValueError('Unexpected translator commentary')
    fragment = _restore_unchecked(unit, translated)
    try:
        ET.fromstring('<span xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">' + fragment + '</span>')
    except ET.ParseError as exc:
        raise ValueError('Inline markup was not kept balanced') from exc


def restore(unit: Unit, translated: str) -> str:
    validate_translation(unit, translated)
    return _restore_unchecked(unit, translated)


def _restore_unchecked(unit: Unit, translated: str) -> str:
    output, cursor = [], 0
    for m in MARK.finditer(translated):
        output.extend([html.escape(translated[cursor:m.start()], quote=False), unit.tokens[int(m[1])]])
        cursor = m.end()
    output.append(html.escape(translated[cursor:], quote=False))
    return ''.join(output)


def local_translation(text: str) -> str | None:
    """Deterministic UI labels; do not send isolated navigation fragments."""
    fixed = {'Footnotes': '脚注', 'Next:': '下一节：', 'Prev:': '上一节：',
             'Up:': '上一级：', 'Contents': '目录', 'Index': '索引',
             'Table of Contents': '目录', 'Short Table of Contents': '简目',
             'Acknowledgments': '致谢', 'References': '参考文献',
             'Exercises': '习题', 'Figures': '插图', 'Term Index': '术语索引',
             'List of Exercises': '习题目录', 'List of Figures': '插图目录',
             'Foreword': '序言', 'Preface': '前言',
             'Preface to the Second Edition': '第二版前言',
             'Preface to the First Edition': '第一版前言',
             'Dedication': '献词', 'Colophon': '版本说明'}
    if text in fixed:
        return fixed[text]
    bare = MARK.sub('', text).strip()
    if bare in fixed:
        return text.replace(bare, fixed[bare])
    if text.startswith('Structure and Interpretation of Computer Programs, '):
        title = text.replace('Structure and Interpretation of Computer Programs, ⟦0⟧e: ',
                             '计算机程序的构造和解释，第⟦0⟧版：')
        for english, chinese in sorted(fixed.items(), key=lambda x: -len(x[0])):
            title = title.replace(english, chinese)
        title = re.sub(r'Chapter (⟦\d+⟧)', r'第\1章', title)
        return title.replace(': Top', '：总览').replace('：Top', '：总览')
    if text.startswith(('Next:', 'Prev:', 'Up:', 'Jump to:')):
        translated = text
        for english, chinese in {'Next:': '下一节：', 'Prev:': '上一节：',
                                 'Up:': '上一级：', 'Jump to:': '跳转至：',
                                 'Contents': '目录', 'Index': '索引'}.items():
            translated = translated.replace(english, chinese)
        return re.sub(r'Chapter (⟦\d+⟧)', r'第\1章', translated)
    return None


def describe_token(token: str) -> str:
    if token.startswith('<') and not re.fullmatch(r'</?[^>]+>', token):
        name = re.match(r'<([^\s/>]+)', token)
        return (name[1] + ': ' if name else '') + re.sub(r'\s+', ' ', html.unescape(TAG.sub(' ', token))).strip()
    return token


def normalize_translation(unit: Unit, text: str) -> str:
    if 'exercise' in unit.text.lower():
        text = re.sub(r'练习(?=\s*⟦\d+⟧)', '习题', text)
    return text


def align_heading_translations(sources, work, cache):
    """Use the same title in chapter headings and their table-of-contents links."""
    headings = {}
    for path, source in sources.items():
        by_start = {unit.start: unit for unit in work[path]}
        def visit(node):
            if node.name in {'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}:
                unit = by_start.get(node.inner)
                if unit and not any(re.match(r'<(?:code|math|var|samp)\b|^\d', token) for token in unit.tokens):
                    english = MARK.sub('', unit.text).strip()
                    chinese = MARK.sub('', cache[unit.key]).strip()
                    if english and chinese:
                        headings[english] = chinese
            for child in node.children:
                visit(child)
        visit(parse(source))
    updates = {}
    for entries in work.values():
        for unit in entries:
            english = MARK.sub('', unit.text).strip()
            if english in headings and english in unit.text:
                candidate = unit.text.replace(english, headings[english])
                validate_translation(unit, candidate)
                updates[unit.key] = candidate
    return updates


def localize_links(output: str, english_names: set[str]) -> str:
    def replace(m):
        prefix, target, suffix = m.groups()
        filename, sep, anchor = target.partition('#')
        if filename in english_names:
            target = filename[:-6] + '_zh.xhtml' + (sep + anchor if sep else '')
        return prefix + target + suffix
    return re.sub(r'(\bhref=[\"\'])([^\"\']+)([\"\'])', replace, output)


def validate_page(source: str, output: str, english_names: set[str]):
    """Check the full tree, anchors and byte-exact protected subtrees."""
    original, translated = parse(source), parse(output)

    def flattened(n, raw):
        rows, frozen, blocks = [], [], []
        def visit(x):
            attrs = dict(x.attrs)
            for key in ('lang', 'xml:lang'):
                if x.name == 'html':
                    attrs.pop(key, None)
            href = attrs.get('href', '')
            if href:
                filename, sep, anchor = href.partition('#')
                if filename.endswith('_zh.xhtml') and filename.replace('_zh.xhtml', '.xhtml') in english_names:
                    attrs['href'] = filename.replace('_zh.xhtml', '.xhtml') + sep + anchor
            rows.append((x.name, attrs))
            if x.name in BLOCK:
                blocks.append((x.name, attrs))
            if protected(x, raw):
                # Local chapter links may be localized even inside footnote text.
                frozen.append(localize_links(raw[x.start:x.end], english_names))
            else:
                for child in x.children:
                    visit(child)
        visit(n)
        return Counter(json.dumps(row, sort_keys=True) for row in rows), Counter(frozen), blocks
    if flattened(original, source) != flattened(translated, output):
        raise ValueError('XHTML structure, attributes, code, formulas or anchors changed')


class Translator:
    def __init__(self, cache_path, api_key, model, endpoint):
        self.cache_path = cache_path
        self.cache = json.loads(cache_path.read_text(encoding='utf-8')) if cache_path.exists() else {}
        self.api_key, self.model, self.endpoint = api_key, model, endpoint
        self.lock = threading.Lock()

    def save(self, updates):
        with self.lock:
            self.cache.update(updates)
            temporary = self.cache_path.with_suffix('.tmp')
            temporary.write_text(json.dumps(self.cache, ensure_ascii=False, indent=2), encoding='utf-8')
            temporary.replace(self.cache_path)

    def batch(self, batch, attempts=3):
        payload = {str(i): {'text': unit.text, 'tokens': {f'⟦{j}⟧': describe_token(token) for j, token in enumerate(unit.tokens)}} for i, unit in enumerate(batch)}
        last_error = None
        for attempt in range(attempts):
            try:
                response = requests.post(self.endpoint, headers={'Authorization': f'Bearer {self.api_key}'},
                    json={'model': self.model, 'messages': [{'role': 'system', 'content': PROMPT},
                          {'role': 'user', 'content': json.dumps(payload, ensure_ascii=False)}],
                          'temperature': 0, 'max_tokens': 8192,
                          'response_format': {'type': 'json_object'}}, timeout=(15, 240))
                response.raise_for_status()
                data = response.json()['choices'][0]
                if data.get('finish_reason') != 'stop':
                    raise ValueError('Response truncated')
                result = json.loads(data['message']['content'])
                if set(result) != set(payload):
                    raise ValueError('Missing or extra translation units')
                updates, invalid = {}, []
                for i, unit in enumerate(batch):
                    try:
                        value = result[str(i)]
                        # Some JSON-mode models mirror the input object despite
                        # being asked for string values. Only its text is output.
                        if isinstance(value, dict):
                            value = value.get('text')
                        validate_translation(unit, value)
                        updates[unit.key] = value
                    except ValueError:
                        invalid.append(unit)
                if updates:
                    self.save(updates)
                if invalid:
                    if len(batch) == 1:
                        raise ValueError('Protected token or number validation failed')
                    for unit in invalid:
                        self.batch([unit], attempts=attempts)
                return
            except (requests.RequestException, KeyError, ValueError, TypeError) as exc:
                last_error = exc
                if isinstance(exc, requests.HTTPError) and exc.response.status_code in {401, 402, 403}:
                    raise RuntimeError(f'Translation service rejected request ({exc.response.status_code})') from None
                time.sleep(2 ** attempt)
        if len(batch) > 1:
            middle = len(batch) // 2
            self.batch(batch[:middle], attempts=2)
            self.batch(batch[middle:], attempts=2)
            return
        raise RuntimeError(f'Translation failed for {batch[0].key[:12]}: {type(last_error).__name__}: {last_error}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='Translate and replace Chinese pages after validation')
    parser.add_argument('--files', nargs='*', help='English XHTML filenames; defaults to every page')
    parser.add_argument('--workers', type=int, default=8)
    parser.add_argument('--batch-chars', type=int, default=5500)
    parser.add_argument('--cache', type=Path, default=ROOT / 'translation_cache_v3.json')
    parser.add_argument('--backup', type=Path)
    args = parser.parse_args()
    paths = sorted(p for p in (ROOT / 'html').glob('*.xhtml') if not p.stem.endswith('_zh'))
    names = {p.name for p in paths}
    if args.files:
        unknown = set(args.files) - names
        if unknown:
            parser.error(f'Unknown source files: {sorted(unknown)}')
        paths = [p for p in paths if p.name in args.files]
    sources = {p: p.read_text(encoding='utf-8') for p in paths}
    work = {p: units(source) for p, source in sources.items()}
    unique = {u.key: u for items in work.values() for u in items}
    print(json.dumps({'pages': len(paths), 'blocks': sum(map(len, work.values())),
                      'unique_blocks': len(unique), 'source_characters': sum(len(u.text) for u in unique.values())}), flush=True)
    if not args.write:
        return
    api_key = os.environ.get('DEEPSEEK_API_KEY', '')
    translator = Translator(args.cache, api_key, os.environ.get('DEEPSEEK_MODEL', 'deepseek-chat'),
                            os.environ.get('DEEPSEEK_API_URL', 'https://api.deepseek.com/v1/chat/completions'))
    local = {u.key: local_translation(u.text) for u in unique.values() if local_translation(u.text) is not None}
    translator.save(local)
    overrides_path = ROOT / 'translation_overrides.json'
    if overrides_path.exists():
        overrides = json.loads(overrides_path.read_text(encoding='utf-8'))
        # Hashes bind each correction to the exact English text and markup.
        translator.save({key: value for key, value in overrides.items() if key in unique})
    pending = []
    for unit in unique.values():
        cached = translator.cache.get(unit.key)
        if cached is not None:
            validate_translation(unit, cached)
        else:
            pending.append(unit)
    if pending and not api_key:
        parser.error('Set DEEPSEEK_API_KEY; credentials are never stored in this script')
    batches, batch, size = [], [], 0
    for unit in pending:
        if batch and size + len(unit.text) > args.batch_chars:
            batches.append(batch)
            batch, size = [], 0
        batch.append(unit)
        size += len(unit.text)
    if batch:
        batches.append(batch)
    print(f'Pending: {len(pending)} blocks, {len(batches)} requests, workers={args.workers}', flush=True)
    errors = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        jobs = {pool.submit(translator.batch, batch): i for i, batch in enumerate(batches)}
        for count, future in enumerate(as_completed(jobs), 1):
            try:
                future.result()
                print(f'Translated batch {count}/{len(batches)}; cached={len(translator.cache)}', flush=True)
            except Exception as exc:
                errors.append(str(exc))
                print(f'ERROR batch {jobs[future]}: {exc}', flush=True)
    if errors:
        raise RuntimeError(f'{len(errors)} translation batches failed; no pages replaced. Completed results are cached.')
    translator.save({u.key: normalize_translation(u, translator.cache[u.key]) for u in unique.values()})
    translator.save(align_heading_translations(sources, work, translator.cache))
    outputs = {}
    for path, source in sources.items():
        output = source
        for unit in reversed(work[path]):
            translated = restore(unit, translator.cache[unit.key])
            output = output[:unit.start] + translated + output[unit.end:]
        output = re.sub(r'(<html\b[^>]*\b(?:xml:)?lang=\")en(\")', r'\1zh\2', output)
        output = output.replace(' xml:lang="en"', ' xml:lang="zh"').replace(' lang="en"', ' lang="zh"')
        output = localize_links(output, names)
        validate_page(source, output, names)
        outputs[path.with_name(path.stem + '_zh.xhtml')] = output
    backup = args.backup or Path(tempfile.gettempdir()) / ('sicp-translation-backup-' + datetime.now().strftime('%Y%m%d-%H%M%S'))
    backup.mkdir(parents=True, exist_ok=True)
    for path in outputs:
        if path.exists():
            target = backup / path.name
            if target.exists():
                raise FileExistsError(f'Refusing to overwrite backup: {target}')
            shutil.copy2(path, target)
    for path, output in outputs.items():
        temporary = path.with_suffix('.xhtml.tmp')
        temporary.write_text(output, encoding='utf-8', newline='')
        temporary.replace(path)
    print(f'Validated and wrote {len(outputs)} pages. Original Chinese pages: {backup}', flush=True)


if __name__ == '__main__':
    main()
