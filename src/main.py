from textnode import TextNode, text_type_bold
from htmlnode import HTMLNode, tag_bold, LeafNode, tag_hyperlink, ParentNode, tag_paragraph, tag_div
from converter import *

def main():
    test_textnode = TextNode("this is code", text_type_code)
    test_textnode_code = TextNode("this `is` text", text_type_text)
    test_textnode_bold = TextNode("The word **is** is bold", text_type_text)
    test_textnode_italic = TextNode("The word *is* is italic", text_type_text)
    list_of_testtextnodes = [test_textnode, test_textnode_italic, test_textnode_bold, test_textnode_code]
    split_nodes = []
    split_nodes = split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(list_of_testtextnodes, "**"),"*"),"`")

    print(split_nodes)

main()

