import unittest

from inline_converter import *
from textnode import *

class TestDelimiterConverter(unittest.TestCase):
    def test_split_on_code(self):
        test_textnode = TextNode("this `is` text", text_type_text)
        test_textnode2 = TextNode("this is code", text_type_code)
        list_of_testtextnodes = [test_textnode, test_textnode2]
        self.assertEqual([TextNode("this ", text_type_text),
                          TextNode("is", text_type_code),
                          TextNode(" text", text_type_text),
                          TextNode("this is code", text_type_code)],
                          split_nodes_delimiter(list_of_testtextnodes, "`"))

    def test_split_on_bold(self):
        test_textnode = TextNode("The word **is** is bold", text_type_text)
        test_textnode2 = TextNode("this is bold text", text_type_bold)
        list_of_testtextnodes = [test_textnode, test_textnode2]
        self.assertEqual([TextNode("The word ", text_type_text),
                          TextNode("is", text_type_bold),
                          TextNode(" is bold", text_type_text),
                          TextNode("this is bold text", text_type_bold)],
                          split_nodes_delimiter(list_of_testtextnodes, "**"))

    def test_split_on_italics(self):
        test_textnode = TextNode("The word *is* is italic", text_type_text)
        test_textnode2 = TextNode("this is italic text", text_type_italic)
        list_of_testtextnodes = [test_textnode, test_textnode2]
        self.assertEqual([TextNode("The word ", text_type_text),
                          TextNode("is", text_type_italic),
                          TextNode(" is italic", text_type_text),
                          TextNode("this is italic text", text_type_italic)],
                          split_nodes_delimiter(list_of_testtextnodes, "*"))

    def test_split_on_all_delimiters(self):
        test_textnode = TextNode("this is code", text_type_code)
        test_textnode_code = TextNode("this `is` text", text_type_text)
        test_textnode_bold = TextNode("The word **is** is bold", text_type_text)
        test_textnode_italic = TextNode("The word *is* is italic", text_type_text)
        list_of_testtextnodes = [test_textnode, test_textnode_italic, test_textnode_bold, test_textnode_code]
        split_nodes = []
        split_nodes = split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(list_of_testtextnodes, "**"),"*"),"`")
        self.assertEqual([TextNode("this is code", text_type_code, None),
                          TextNode("The word ", text_type_text, None),
                          TextNode("is", text_type_italic, None),
                          TextNode(" is italic", text_type_text, None),
                          TextNode("The word ", text_type_text, None),
                          TextNode("is", text_type_bold, None),
                          TextNode(" is bold", text_type_text, None),
                          TextNode("this ", text_type_text, None),
                          TextNode("is", text_type_code, None),
                          TextNode(" text", text_type_text, None)],
                          split_nodes)

    def test_split_incorrect_delimiter(self):
        test_textnode = TextNode("this `is` text", text_type_text)
        test_textnode2 = TextNode("this is code", text_type_code)
        list_of_testtextnodes = [test_textnode, test_textnode2]
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(list_of_testtextnodes,"/")
        self.assertEqual("Invalid markdown syntax", str(context.exception))

class TestImageConverter(unittest.TestCase):
    def test_image_props_extraction(self):
        test_text = '![Excellent](https://imgur.com/gallery/excellent-mr-burns-hzaJ4Hn)'
        self.assertEqual([("Excellent", "https://imgur.com/gallery/excellent-mr-burns-hzaJ4Hn")],
                         extract_image_props(test_text))

    def test_singular_image_split(self):
        test_node = TextNode("This is text with an image ![boot dev](https://www.boot.dev)", text_type_text)
        self.assertEqual([TextNode("This is text with an image ", text_type_text, None),
                          TextNode("boot dev", text_type_image, "https://www.boot.dev")],
                           split_nodes_images(test_node))

    def test_multiple_image_split(self):
        test_node = TextNode("This is text with an image ![boot dev](https://www.boot.dev) and so is this text ![Excellent](https://imgur.com/gallery/excellent-mr-burns-hzaJ4Hn)", text_type_text)
        self.assertEqual([TextNode("This is text with an image ", text_type_text, None),
                          TextNode("boot dev", text_type_image, "https://www.boot.dev"),
                          TextNode(" and so is this text ", text_type_text, None),
                          TextNode("Excellent", text_type_image, "https://imgur.com/gallery/excellent-mr-burns-hzaJ4Hn")],
                          split_nodes_images(test_node))

    def multiple_nodes_image_split(self):
        test_node = TextNode("This is text with an image ![boot dev](https://www.boot.dev) and so is this text ![Excellent](https://imgur.com/gallery/excellent-mr-burns-hzaJ4Hn)", text_type_text)
        test_node2 = TextNode("This is an image ![D\'oh](https://imgur.com/gallery/d-d-d-doh-Y4a1MRU)")
        test_nodes = [test_node, test_node2]
        self.assertEqual([TextNode("This is text with an image ", text_type_text, None),
                          TextNode("boot dev", text_type_image, "https://www.boot.dev"),
                          TextNode(" and so is this text ", text_type_text, None),
                          TextNode("Excellent", text_type_image, "https://imgur.com/gallery/excellent-mr-burns-hzaJ4Hn"),
                          TextNode("This is an image ", text_type_text, None,),
                          TextNode("D\'oh", text_type_image, "https://imgur.com/gallery/d-d-d-doh-Y4a1MRU")],
                          split_nodes_images(test_nodes))

class TestLinkConverter(unittest.TestCase):
    def test_link_props_extraction(self):
        test_text = '[D\'oh](https://imgur.com/gallery/d-d-d-doh-Y4a1MRU)'
        self.assertEqual([("D'oh", "https://imgur.com/gallery/d-d-d-doh-Y4a1MRU")],
                         extract_link_props(test_text))

    def test_singular_link_split(self):
        test_node = TextNode("This is text with a link [boot dev](https://www.boot.dev)", text_type_text)
        self.assertEqual([TextNode("This is text with a link ", text_type_text, None),
                          TextNode("boot dev", text_type_link, "https://www.boot.dev")],
                           split_nodes_links(test_node))

    def test_multiple_link_split(self):
        test_node = TextNode("This is text with a link [boot dev](https://www.boot.dev) and so is this text [Excellent](https://imgur.com/gallery/excellent-mr-burns-hzaJ4Hn)", text_type_text)
        self.assertEqual([TextNode("This is text with a link ", text_type_text, None),
                          TextNode("boot dev", text_type_link, "https://www.boot.dev"),
                          TextNode(" and so is this text ", text_type_text, None),
                          TextNode("Excellent", text_type_link, "https://imgur.com/gallery/excellent-mr-burns-hzaJ4Hn")],
                          split_nodes_links(test_node))

    def multiple_nodes_link_split(self):
        test_node = TextNode("This is text with a link [boot dev](https://www.boot.dev) and so is this text [Excellent](https://imgur.com/gallery/excellent-mr-burns-hzaJ4Hn)", text_type_text)
        test_node2 = TextNode("This is a link [D\'oh](https://imgur.com/gallery/d-d-d-doh-Y4a1MRU)")
        test_nodes = [test_node, test_node2]
        self.assertEqual([TextNode("This is text with a link ", text_type_text, None),
                          TextNode("boot dev", text_type_link, "https://www.boot.dev"),
                          TextNode(" and so is this text ", text_type_text, None),
                          TextNode("Excellent", text_type_link, "https://imgur.com/gallery/excellent-mr-burns-hzaJ4Hn"),
                          TextNode("This is a link ", text_type_text, None,),
                          TextNode("D\'oh", text_type_link, "https://imgur.com/gallery/d-d-d-doh-Y4a1MRU")],
                          split_nodes_links(test_nodes))

class TestTextToTextNode(unittest.TestCase):
    def test_all_types(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://docs.python.org/3/reference/)"
        self.assertEqual([TextNode("This is ", text_type_text),
                        TextNode("text", text_type_bold),
                        TextNode(" with an ", text_type_text),
                        TextNode("italic", text_type_italic),
                        TextNode(" word and a ", text_type_text),
                        TextNode("code block", text_type_code),
                        TextNode(" and an ", text_type_text),
                        TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
                        TextNode(" and a ", text_type_text),
                        TextNode("link", text_type_link, "https://docs.python.org/3/reference/")],
                        text_to_textnode(text))

if __name__ == "__main__":
    unittest.main()