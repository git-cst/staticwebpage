import unittest

from inline_converter import *
from textnode import *

class TestConverter(unittest.TestCase):
    #SPLIT_ON_DELIMITER TESTING
    def test_split_on_code(self):
        test_textnode = TextNode("this `is` text", text_type_text)
        test_textnode2 = TextNode("this is code", text_type_code)
        list_of_testtextnodes = [test_textnode, test_textnode2]
        self.assertEqual(split_nodes_delimiter(list_of_testtextnodes, "`"),
                         [TextNode("this ", text_type_text), TextNode("is", text_type_code), TextNode(" text", text_type_text), TextNode("this is code", text_type_code)])

    def test_split_on_bold(self):
        test_textnode = TextNode("The word **is** is bold", text_type_text)
        test_textnode2 = TextNode("this is bold text", text_type_bold)
        list_of_testtextnodes = [test_textnode, test_textnode2]
        self.assertEqual(split_nodes_delimiter(list_of_testtextnodes, "**"),
                         [TextNode("The word ", text_type_text), TextNode("is", text_type_bold), TextNode(" is bold", text_type_text), TextNode("this is bold text", text_type_bold)])

    def test_split_on_italics(self):
        test_textnode = TextNode("The word *is* is italic", text_type_text)
        test_textnode2 = TextNode("this is italic text", text_type_italic)
        list_of_testtextnodes = [test_textnode, test_textnode2]
        self.assertEqual(split_nodes_delimiter(list_of_testtextnodes, "*"),
                         [TextNode("The word ", text_type_text), TextNode("is", text_type_italic), TextNode(" is italic", text_type_text), TextNode("this is italic text", text_type_italic)])

    def test_split_on_all_delimiters(self):
        test_textnode = TextNode("this is code", text_type_code)
        test_textnode_code = TextNode("this `is` text", text_type_text)
        test_textnode_bold = TextNode("The word **is** is bold", text_type_text)
        test_textnode_italic = TextNode("The word *is* is italic", text_type_text)
        list_of_testtextnodes = [test_textnode, test_textnode_italic, test_textnode_bold, test_textnode_code]
        split_nodes = []
        split_nodes = split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(list_of_testtextnodes, "**"),"*"),"`")
        self.assertEqual(split_nodes,
                         [TextNode("this is code", text_type_code, None), TextNode("The word ", text_type_text, None), TextNode("is", text_type_italic, None), TextNode(" is italic", text_type_text, None), TextNode("The word ", text_type_text, None), TextNode("is", text_type_bold, None), TextNode(" is bold", text_type_text, None), TextNode("this ", text_type_text, None), TextNode("is", text_type_code, None), TextNode(" text", text_type_text, None)])

    def test_split_incorrect_delimiter(self):
        test_textnode = TextNode("this `is` text", text_type_text)
        test_textnode2 = TextNode("this is code", text_type_code)
        list_of_testtextnodes = [test_textnode, test_textnode2]
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(list_of_testtextnodes,"/")
        self.assertEqual("Invalid markdown syntax", str(context.exception))

    #IMAGE EXTRACTION TESTING
    def test_image_extraction(self):
        test_text = '![Excellent](https://imgur.com/gallery/excellent-mr-burns-hzaJ4Hn)'
        self.assertEqual([("Excellent", "https://imgur.com/gallery/excellent-mr-burns-hzaJ4Hn")], extract_image_props(test_text))

    #LINK EXTRACTION TESTING
    def test_link_extraction(self):
        test_text = '[D\'oh](https://imgur.com/gallery/d-d-d-doh-Y4a1MRU)'
        self.assertEqual([("D'oh", "https://imgur.com/gallery/d-d-d-doh-Y4a1MRU")], extract_link_props(test_text))

if __name__ == "__main__":
    unittest.main()