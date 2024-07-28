from textnode import TextNode, text_type_bold
from htmlnode import HTMLNode, tag_bold

def main():
    textnode = TextNode("This is a text node", text_type_bold, "https://www.boot.dev")
    print(textnode)
    htmlnode = HTMLNode(tag_bold, "Hello", None, {"href": "https://www.google.com", "target": "_blank"})
    print(htmlnode.props_to_html())



main()

