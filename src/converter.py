from textnode import *
import regex as re

accepted_delimiters = ['`', '*', '**']

def get_text_type(delimiter):
    match delimiter:
        case '`':
            return text_type_code
        case '*':
            return text_type_italic
        case '**':
            return text_type_bold

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
        
def extract_image_props(text):
    image_list = []
    images = re.findall('!\[(.*?)\]\((.*?)\)', text)
    for image in images:
        image_list.append(image)
    return image_list

def extract_link_props(text):
    link_list = []
    links = re.findall('\[(.*?)\]\((.*?)\)', text)
    for link in links:
        link_list.append(link)
    return link_list