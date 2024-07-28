import unittest

from htmlnode import (
    HTMLNode,
    tag_hyperlink,
    tag_bold,
    tag_code,
    tag_image,
    tag_italicize,
    tag_text,
    tag_heading1,
    tag_heading2,
    tag_heading3
)

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag_text, "This is a text line")
        node2 = HTMLNode(tag_text, "This is a text line")
        self.assertEqual(node, node2)

    def test_ne(self):
        node = HTMLNode(tag_bold, "bolded text")
        node2 = HTMLNode(tag_italicize, "italic text")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode(tag_bold, "this is code", None, {"code: python3 main.py"})
        self.assertEqual(node, repr(node))

if __name__ == "__main__":
    unittest.main()