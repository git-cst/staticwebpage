from textnode import TextNode, text_type_bold
from htmlnode import HTMLNode, tag_bold, LeafNode, tag_hyperlink, ParentNode, tag_paragraph, tag_div

def main():
    testParentNode = ParentNode(
        tag_paragraph, 
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text")
        ],
    )

    testLeaf = LeafNode(tag_bold, "This is bold!")
    testLeaf2 = LeafNode(tag_hyperlink, "My GitHub!", {"href": "https://github.com/git-cst"})
    testNestedParentNode = ParentNode(tag_div, 
                                      [
                                          testLeaf,
                                          testLeaf2,
                                          testParentNode
                                      ])
    
    testNested2ParentNode = ParentNode(tag_div, 
                            [
                                testNestedParentNode,
                                testLeaf,
                                testLeaf2,
                                testParentNode
                            ])

    print(testParentNode.to_html())
    print(testNestedParentNode.to_html())
    print(testNested2ParentNode.to_html())

main()

