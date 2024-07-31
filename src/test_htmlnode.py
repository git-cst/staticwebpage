import unittest

from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode,
    tag_hyperlink,
    tag_bold,
    tag_code,
    tag_image,
    tag_italicize,
    tag_text,
    tag_heading,
    tag_span,
    tag_div,
    tag_paragraph
)

class TestHTMLNode(unittest.TestCase):
    #GENERAL HTML NODE TESTING
    def test_eq(self):
        node = HTMLNode(tag_text, "This is a text line", None)
        node2 = HTMLNode(tag_text, "This is a text line", None)
        self.assertEqual(node, node2)

    def test_ne(self):
        node = HTMLNode(tag_bold, "bolded text")
        node2 = HTMLNode(tag_italicize, "italic text")
        self.assertNotEqual(node, node2)

    def test_values(self):
        node = HTMLNode(tag_div, "Hello world!", None, {"class": "greeting", "href": "https://boot.dev"})
        self.assertEqual("Hello world!", node.value)
        self.assertEqual('div', node.tag)
        self.assertEqual(None, node.children)
        self.assertEqual({"class": "greeting", "href": "https://boot.dev"}, node.props)

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
        self.assertEqual(f'HTMLNode(code, this is code, children: None, {prop_test})', repr(node))

    #LEAF NODE TESTING
    def test_leaf_values(self):
        leafnode = LeafNode(tag_bold, "This is bold!", 'href="https://www.google.com" target="_blank"')
        self.assertEqual("This is bold!", leafnode.value)
        self.assertEqual("b", leafnode.tag)
        self.assertEqual(None, leafnode.children)
        self.assertEqual('href="https://www.google.com" target="_blank"', leafnode.props)

    def test_leaf_no_tag(self):
        leafnode = LeafNode(None, "No tags")
        self.assertEqual("No tags", leafnode.to_html())

    def test_leaf_to_html(self):
        leafnode = LeafNode(tag_hyperlink, "My GitHub!", {"href": "https://github.com/git-cst"})
        self.assertEqual('<a href="https://github.com/git-cst">My GitHub!</a>', leafnode.to_html())

    #PARENT NODE TESTING
    def test_parent_no_tag(self):
        testParentNode = ParentNode(
            None, 
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ],
        )
        with self.assertRaises(ValueError) as context:
            testParentNode.to_html()
        self.assertEqual("Parent nodes must have a tag", str(context.exception))

    def test_parent_no_children(self):
        testParentNode = ParentNode(tag_paragraph, None, )
        with self.assertRaises(ValueError) as context:
            testParentNode.to_html()
        self.assertEqual("Parent nodes must have children", str(context.exception))

    def test_parent_to_html(self):
        testLeaf = LeafNode(tag_bold, "This is bold!")
        testLeaf2 = LeafNode(tag_hyperlink, "My GitHub!", {"href": "https://github.com/git-cst"})
        testParentNode = ParentNode(
                                tag_paragraph, 
                                [
                                    LeafNode("b", "Bold text"),
                                    LeafNode(None, "Normal text"),
                                    LeafNode("i", "italic text"),
                                    LeafNode(None, "Normal text")
                                ])

        testParent2Node = ParentNode(tag_paragraph,[LeafNode("b", "Bold text")])
        testNestedParentNode = ParentNode(
                                        tag_div, 
                                        [
                                            testLeaf,
                                            testLeaf2,
                                            testParentNode
                                        ])
        
        testNested2ParentNode = ParentNode(
                                        tag_div, 
                                        [
                                            testNestedParentNode,
                                            testLeaf,
                                            testLeaf2,
                                            testParentNode
                                        ])

        self.assertEqual('<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>',testParentNode.to_html())
        self.assertEqual('<p><b>Bold text</b></p>', testParent2Node.to_html())
        self.assertEqual('<div><b>This is bold!</b><a href="https://github.com/git-cst">My GitHub!</a><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div>', testNestedParentNode.to_html())
        self.assertEqual('<div><div><b>This is bold!</b><a href="https://github.com/git-cst">My GitHub!</a><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div><b>This is bold!</b><a href="https://github.com/git-cst">My GitHub!</a><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div>', testNested2ParentNode.to_html())

if __name__ == "__main__":
    unittest.main()