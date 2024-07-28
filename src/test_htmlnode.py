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

    def test_props_to_html(self):
        props_test = {
            "href": "https://www.google.com", 
            "target": "_blank"
        }
        node = HTMLNode(tag_hyperlink, "Link to google", None, props_test)
        props_to_html =  node.props_to_html()
        self.assertEqual(props_to_html, 'href="https://www.google.com" target="_blank"')

    def test_repr(self):
        prop_test = {
            "code:" "python3 main.py"
            "test:" "Test"
        }
        node = HTMLNode(tag_code, "this is code", None, prop_test)
        self.assertEqual(f'HTMLNode(<code>, this is code, None, {prop_test})', repr(node))

if __name__ == "__main__":
    unittest.main()