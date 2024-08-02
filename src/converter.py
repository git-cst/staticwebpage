from textnode import *

accepted_delimiters = ['`', '*', '**']

def split_nodes_delimiter(old_nodes, delimiter):
    if delimiter not in accepted_delimiters:
        raise Exception("Invalid markdown syntax")
    
    text_type_delimiter = get_text_type(delimiter)

    new_nodes = []
    split_node = []
    for node in old_nodes:
        if node.text_type == text_type_text:
            split_node = node.text.split(delimiter)
            for i in range(len(split_node)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(split_node[i], text_type_text))
                else:
                    new_nodes.append(TextNode(split_node[i], text_type_delimiter))
        else:
            new_nodes.append(node) 
    return new_nodes

def get_text_type(delimiter):
    match delimiter:
        case '`':
            return text_type_code
        case '*':
            return text_type_italic
        case '**':
            return text_type_bold