from textnode import TextNode, text_type_bold
from htmlnode import HTMLNode, tag_bold, LeafNode, tag_hyperlink, ParentNode

def main():
    testParentNode = ParentNode(
        tag_bold, 
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text")
        ],
    ) 
    print(testParentNode.__repr__())
    print(testParentNode.children)
    print(len(testParentNode.children))
    for i in range(len(testParentNode.children)):
        print(testParentNode.children[i].to_html())

main()

