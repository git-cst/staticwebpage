import unittest

from textnode import (
    TextNode,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
    text_type_text,
    text_node_to_html_node
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

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_to_html(self):
        node_text = TextNode("This is a text node", text_type_text)
        node_with_url = TextNode("Click me!", text_type_link, "https://docs.python.org/3/reference/")
        node_with_image = TextNode("Github!", text_type_image, "github.com")

        html_text = text_node_to_html_node(node_text)
        html_url = text_node_to_html_node(node_with_url)
        html_image = text_node_to_html_node(node_with_image)

        #test node_text
        self.assertEqual(html_text.tag, None)
        self.assertEqual(html_text.value, "This is a text node")
        #test node_with_url
        self.assertEqual(html_url.tag, "a")
        self.assertEqual(html_url.value, "Click me!")
        self.assertEqual(html_url.props, {"href": "https://docs.python.org/3/reference/"})
        #test node_with_image
        self.assertEqual(html_image.tag, "img")
        self.assertEqual(html_image.value, '')
        self.assertEqual(html_image.props, {"src": "github.com", "alt": "Github!"})

if __name__ == "__main__":
    unittest.main()