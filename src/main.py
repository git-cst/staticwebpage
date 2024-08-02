from textnode import TextNode, text_type_bold
from htmlnode import HTMLNode, tag_bold, LeafNode, tag_hyperlink, ParentNode, tag_paragraph, tag_div
from converter import *

def main():
    temp_textnode = TextNode("this *is* text", text_type_text)
    temp_textnode2 = TextNode("**this is text**", text_type_bold)
    list_of_textnodes = [temp_textnode, temp_textnode2]

    print(split_nodes_delimiter(list_of_textnodes, "*", text_type_bold))

main()

