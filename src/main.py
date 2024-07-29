from textnode import TextNode, text_type_bold
from htmlnode import HTMLNode, tag_bold, LeafNode, tag_hyperlink

def main():
    textnode = TextNode("This is a text node", text_type_bold, "https://www.boot.dev")
    print(textnode)
    htmlnode = HTMLNode(tag_bold, "Hello", None, {"href": "https://www.google.com", "target": "_blank"})
    print(htmlnode.props_to_html())
    leafnode = LeafNode(tag=tag_hyperlink, value="My GitHub!", props={"href": "https://github.com/git-cst"})
    print(leafnode.tag, leafnode.value, leafnode.props)
    print(leafnode.to_html())


main()

