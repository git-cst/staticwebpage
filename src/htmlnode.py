#######################################################################
tag_hyperlink = "<a>"
tag_abbreviation = "<abbr>"
tag_bold = "<b>"
tag_text_direction = "<bdo>"
tag_break = "<br>"
tag_button = "<button>"
tag_cite = "<cite>"
tag_code = "<code>"
tag_definition = "<dfn>"
tag_emphasize = "<em>"
tag_embed = "<embed>"
tag_italicize = "<i>"
tag_image = "<img>"
tag_input = "<input>"
tag_keyboard = "<kbd>"
tag_label = "<label>"
tag_image_map = "<map>"
tag_external_object = "<object>"
tag_output = "<output>"
tag_quote = "<q>"
tag_sample = "<samp>"
tag_script = "<script>"
tag_dropdown_box = "<select>"
tag_small = "<small>"
tag_span = "<span>"
tag_strong = "<strong>"
tag_subscript = "<sub>"
tag_superscript = "<sup>"
tag_textblock = "textarea"
tag_time = "<time>"
tag_var = "<var>"
#REF = https://www.w3schools.com/html/html_blocks.asp
#######################################################################

class TextNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented
    
    ####### IMPLEMENT THIS ########
    def props_to_html(self):
        pass
    ###############################

    def __eq__(self, other):
        return(
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"