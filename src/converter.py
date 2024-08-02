from textnode import *

accepted_delimiters = ['`', '*', '**']

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if delimiter not in accepted_delimiters:
        raise Exception("Invalid markdown syntax")
    
    match delimiter:
        case '`':
            text_type_delimiter = text_type_code
        case '*':
            text_type_delimiter = text_type_italic
        case '**':
            text_type_delimiter = text_type_bold

    
    new_nodes = []
    split_node = []
    for node in old_nodes:
        if node.text_type == text_type_text:
            split_node = node.text.split(delimiter)
            new_nodes.append(TextNode(split_node[0], text_type_text))
            new_nodes.append(TextNode(split_node[1], text_type_delimiter))
            new_nodes.append(TextNode(split_node[2], text_type_text))
        else:
            new_nodes.append(node) 
    return new_nodes