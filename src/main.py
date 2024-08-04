from textnode import TextNode, text_type_bold
from htmlnode import HTMLNode, tag_bold, LeafNode, tag_hyperlink, ParentNode, tag_paragraph, tag_div
from inline_converter import *

def main():
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://docs.python.org/3/reference/)"
    text_to_transform = TextNode(text, text_type_text)
    textnodes = split_nodes_images(text_to_transform)
    print(textnodes)
    textnodes = split_nodes_links(textnodes)
    print(textnodes)
    textnodes = split_nodes_delimiter(textnodes, "**")
    print(textnodes)
    textnodes = split_nodes_delimiter(textnodes, "*")
    print(textnodes)
    textnodes = split_nodes_delimiter(textnodes, "`")
    print(textnodes)


main()
