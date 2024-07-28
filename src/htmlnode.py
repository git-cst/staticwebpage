tag_div = "<div>"
tag_span = "<span>"
tag_hyperlink = "<a>"
tag_bold = "<b>"
tag_code = "<code>"
tag_image = "<img>"
tag_text = "text"
tag_italicize = "<i>"
tag_heading1 = "<h1>"
tag_heading2 = "<h2>"
tag_heading3 = "<h3>"

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
    def __init__(self, tag, value, props):
        super().__init__(tag, value, props)
        if value == None:
            raise ValueError("Leaf nodes must have a value")
    
    def to_html(self):
        return ""