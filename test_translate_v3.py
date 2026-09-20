"""Content-preservation checks for the SICP translator (no API calls)."""
import unittest
from pathlib import Path

from translate_v3 import (ROOT, localize_links, restore, units,
                          validate_page, validate_translation)
from review_sentences import reviewed_values


class TranslationIntegrityTests(unittest.TestCase):
    def test_inline_phrase_is_one_unit_and_protected_content_is_exact(self):
        source = '<html><body><p>The <abbr>MIT</abbr> Press uses <code>(+ 1 2)</code>.<a id="x"/><math><mi>x</mi></math></p></body></html>'
        blocks = units(source)
        self.assertEqual(len(blocks), 1)
        unit = blocks[0]
        self.assertIn('MIT', unit.text)
        self.assertNotIn('(+ 1 2)', unit.text)
        translated = restore(unit, '⟦0⟧麻省理工学院⟦1⟧出版社使用⟦2⟧。⟦3⟧⟦4⟧')
        output = source[:unit.start] + translated + source[unit.end:]
        validate_page(source, output, set())
        self.assertIn('<code>(+ 1 2)</code>', output)
        self.assertIn('<math><mi>x</mi></math>', output)

    def test_dropped_or_duplicated_tokens_and_numbers_are_rejected(self):
        unit = units('<html><body><p>Take 12 <em>steps</em>.</p></body></html>')[0]
        for translation in ['走 12 步。', '走 13 ⟦0⟧⟦1⟧步⟦2⟧。', '走 ⟦0⟧⟦1⟧步⟦2⟧⟦2⟧。']:
            with self.assertRaises(ValueError):
                validate_translation(unit, translation)

    def test_inline_code_can_follow_chinese_word_order(self):
        source = '<html><body><p>The value of <code>not</code> is true when <var>x</var> is false.</p></body></html>'
        unit = units(source)[0]
        translated = restore(unit, '当⟦1⟧为假时，⟦0⟧的值为真。')
        validate_page(source, source[:unit.start] + translated + source[unit.end:], set())

    def test_cache_key_includes_protected_code(self):
        first = units('<html><body><p>Call <code>car</code>.</p></body></html>')[0]
        second = units('<html><body><p>Call <code>cdr</code>.</p></body></html>')[0]
        self.assertEqual(first.text, second.text)
        self.assertNotEqual(first.key, second.key)

    def test_unbalanced_inline_markup_is_rejected(self):
        unit = units('<html><body><p>A <em>special</em> case.</p></body></html>')[0]
        with self.assertRaises(ValueError):
            validate_translation(unit, '一个⟦1⟧特殊⟦0⟧情况。')

    def test_nested_lists_have_no_overlapping_units(self):
        source = '<html><body><li>First <b>item</b><p>A paragraph.</p><ul><li>Nested item.</li></ul>Last part.</li></body></html>'
        blocks = units(source)
        self.assertEqual(len(blocks), 4)
        for left, right in zip(blocks, blocks[1:]):
            self.assertLessEqual(left.end, right.start)

    def test_links_keep_anchors_and_external_urls(self):
        source = '<a href="1.xhtml#id">Next</a><a href="https://example.com/1.xhtml">External</a><a href="#id">Local</a>'
        output = localize_links(source, {'1.xhtml'})
        self.assertIn('href="1_zh.xhtml#id"', output)
        self.assertIn('href="https://example.com/1.xhtml"', output)
        self.assertIn('href="#id"', output)

    def test_all_book_pages_round_trip_and_preserve_their_tree(self):
        paths = [p for p in (ROOT / 'html').glob('*.xhtml') if not p.stem.endswith('_zh')]
        names = {p.name for p in paths}
        for path in paths:
            with self.subTest(page=path.name):
                source = path.read_text(encoding='utf-8')
                output = source
                blocks = units(source)
                for left, right in zip(blocks, blocks[1:]):
                    self.assertLessEqual(left.end, right.start)
                for unit in reversed(blocks):
                    output = output[:unit.start] + restore(unit, unit.text) + output[unit.end:]
                validate_page(source, localize_links(output, names), names)

    def test_changes_inside_code_or_deleted_paragraph_are_rejected(self):
        source = '<html><body><p>Text.</p><pre>(+ 1 2)</pre></body></html>'
        for output in [source.replace('(+ 1 2)', '(+ 1 3)'), source.replace('<p>Text.</p>', '')]:
            with self.assertRaises(ValueError):
                validate_page(source, output, set())

    def test_model_suggestions_cannot_substitute_for_editor_review(self):
        unit = units('<html><body><p>A value.</p></body></html>')[0]
        row = {'id': 'page:0001', 'source': unit.text, 'tokens': unit.tokens,
               'key': unit.key, 'sentences': ['A value.']}
        data = {'units': [row]}
        with self.assertRaises(ValueError):
            reviewed_values(data, {})
        decision = {'key': unit.key, 'translation': '一个值。', 'sentence_verdicts': []}
        with self.assertRaises(ValueError):
            reviewed_values(data, {row['id']: decision})
        decision['sentence_verdicts'] = ['checked']
        self.assertEqual(reviewed_values(data, {row['id']: decision}), {unit.key: '一个值。'})

    def test_stale_or_conflicting_editor_decisions_are_rejected(self):
        unit = units('<html><body><p>A value.</p></body></html>')[0]
        row = {'id': 'page:0001', 'source': unit.text, 'tokens': unit.tokens,
               'key': unit.key, 'sentences': ['A value.']}
        decision = {'key': 'old-source-key', 'translation': '一个值。', 'sentence_verdicts': ['checked']}
        with self.assertRaises(ValueError):
            reviewed_values({'units': [row]}, {row['id']: decision})
        second = {**row, 'id': 'page:0002'}
        decision['key'] = unit.key
        with self.assertRaises(ValueError):
            reviewed_values({'units': [row, second]}, {
                row['id']: decision, second['id']: {**decision, 'translation': '一个数值。'}})


if __name__ == '__main__':
    unittest.main()
