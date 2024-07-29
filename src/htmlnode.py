tag_paragraph = "p"
tag_div = "div"
tag_span = "span"
tag_hyperlink = "a"
tag_bold = "b"
tag_code = "code"
tag_image = "img"
tag_text = "text"
tag_italicize = "i"
tag_heading = "h"

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        prop_html = []
        for prop in self.props:
            prop_html.append(f'{prop}="{self.props[prop]}"')
        return " ".join(prop_html)

    def __eq__(self, other):
        return(
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf nodes must have a value")
        if self.tag == None:
            return f"{self.value}"
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"