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
        raise NotImplemented
    
    def props_to_html(self):
        prop_array = []
        for key in self.props:
            prop_array.append(f'{key}="{self.props[key]}"')
        return " ".join(prop_array)

    def __eq__(self, other):
        return(
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"