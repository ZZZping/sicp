"""Add static reading controls after rebuilding HTML: python prepare_reader_ui.py.

Book prose is left byte-for-byte intact. Both editions use the same bilingual
toolbar, which the translation pipeline protects as a complete unit.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
TOOLBAR = re.compile(r'<nav class="reader-toolbar"[^>]*>.*?</nav>\s*', re.S)


def add_reader_ui(source: str, english_name: str) -> str:
    chinese_name = english_name.removesuffix('.xhtml') + '_zh.xhtml'
    source = TOOLBAR.sub('', source)
    source = re.sub(r'<link href="css/reader\.css[^"\n]*"[^>]*>\s*', '', source)
    source = re.sub(r'<script src="js/language-switch\.js[^"\n]*"[^>]*></script>\s*', '', source)
    source = source.replace('</head>',
        '<link href="css/reader.css?v=3" rel="stylesheet" type="text/css" />\n'
        '<script src="js/language-switch.js?v=3" defer="defer" type="text/javascript"></script>\n</head>')
    toolbar = (
        '<nav class="reader-toolbar" aria-label="Language / 语言" translate="no">\n'
        '  <div class="reader-toolbar-inner"><span class="reader-brand">SICP</span>\n'
        '  <div class="reader-languages"><span class="reader-language-label">语言 / Language</span>\n'
        f'  <a href="{english_name}" hreflang="en" lang="en">English</a>\n'
        f'  <a href="{chinese_name}" hreflang="zh" lang="zh">中文</a>\n'
        '  </div></div>\n</nav>\n')
    return source.replace('<body>\n', '<body>\n' + toolbar, 1)


if __name__ == '__main__':
    count = 0
    for path in sorted((ROOT / 'html').glob('*.xhtml')):
        english_name = path.name.replace('_zh.xhtml', '.xhtml')
        if not (path.parent / english_name.replace('.xhtml', '_zh.xhtml')).exists():
            continue
        original = path.read_bytes()
        source = original.decode('utf-8').replace('\r\n', '\n')
        output = add_reader_ui(source, english_name)
        newline = '\r\n' if b'\r\n' in original else '\n'
        encoded = output.replace('\n', newline).encode('utf-8')
        if encoded != original:
            path.write_bytes(encoded)
            count += 1
    print(f'Updated reading controls in {count} pages.')
