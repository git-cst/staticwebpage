import unittest

from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
    text_type_text
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node_with_url = TextNode("This is a text node", text_type_bold, "https://docs.python.org/3/reference/")
        node2_with_url = TextNode("This is a text node", text_type_bold, "https://docs.python.org/3/reference/")
        self.assertEqual(node_with_url, node_with_url)

    def test_ne(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is another text nodes", text_type_italic)
        self.assertNotEqual(node, node2)

    def test_ne_url(self):
        node_with_url = TextNode("This is a text node", text_type_bold, "https://docs.python.org/3/reference/")
        node2_with_url = TextNode("This is another text nodes", text_type_italic, "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        self.assertNotEqual(node_with_url, node2_with_url)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https://docs.python.org/3/reference/")
        self.assertEqual("TextNode(This is a text node, text, https://docs.python.org/3/reference/)", repr(node))


if __name__ == "__main__":
    unittest.main()