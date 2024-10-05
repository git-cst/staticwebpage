import unittest

from blocklevel_converter import *

class TestBlockExtraction(unittest.TestCase):
    def test_block_singleline(self):
        test_block = """
        # This is a heading
        """
        self.assertEqual(["# This is a heading"], markdown_to_blocks(test_block))
    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )
        
class TestBlockIdentification(unittest.TestCase):
    def test_paragraph(self):
        test_block = "This is a text string"
        self.assertEqual("p",
                            block_to_block_type(test_block)[0])

    def test_heading(self):
        test_block_h1 = "# This is a heading"
        test_block_h6 = "###### This is a heading"
        self.assertEqual("h",
                            block_to_block_type(test_block_h1)[0])
        self.assertEqual("h",
                            block_to_block_type(test_block_h6)[0])
        
    def test_code(self):
        test_block = "```This is a code block```"
        self.assertEqual("p",
                            block_to_block_type(test_block)[0])

    def test_quote(self):
        test_block = ">This is a quote"
        self.assertEqual("q",
                            block_to_block_type(test_block)[0])

    def test_unordered_list(self):
        test_block = "* This is an unordered list"
        test_block_2 = "- This is also an unordered list"
        self.assertEqual("u",
                            block_to_block_type(test_block)[0])
        self.assertEqual("u",
                            block_to_block_type(test_block_2)[0])

    def test_ordered_list(self):
        test_block = "1. This is an ordered list"
        self.assertEqual("o",
                            block_to_block_type(test_block)[0])

class TestBlockHTMLConversion(unittest.TestCase):
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

if __name__ == "__main__":
    unittest.main()