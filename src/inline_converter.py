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
        if node.text_type != text_type_text:
            new_nodes.append(node) 
            continue
        split_node = node.text.split(delimiter)
        for i in range(len(split_node)):
            if i % 2 != 0:
                new_nodes.append(TextNode(split_node[i], text_type_delimiter))
            else:
                new_nodes.append(TextNode(split_node[i], text_type_text))

    return new_nodes

########## IMAGE HANDLING       
def extract_image_props(text):
    image_list = []
    images = re.findall('!\[(.*?)\]\((.*?)\)', text)
    for image in images:
        image_list.append(image)
    return image_list

def split_nodes_images(old_nodes):
    new_nodes = []
    split_node = []

    #Handle if old_nodes is just 1 node
    if isinstance(old_nodes, TextNode) == 1:
        node = old_nodes
        image_prop = extract_image_props(node.text)
        for i in range(len(image_prop)):
            prop_alt = image_prop[i][0]
            prop_src = image_prop[i][1]

            if i == 0:
                split_node = node.text.split(f"![{prop_alt}]({prop_src})", 1)
            else:
                split_node = "".join(split_node[1:]).split(f"![{prop_alt}]({prop_src})", 1)

            new_nodes.append(TextNode(split_node[0], text_type_text))
            new_nodes.append(TextNode(prop_alt, text_type_image, prop_src))
        return new_nodes

    #Handle old nodes == multiple nodes
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        image_prop = extract_image_props(node.text)

        if len(image_prop) == 0:
            new_nodes.append(node)
            continue

        original_text = node.text

        for i in range(len(image_prop)):
            prop_alt = image_prop[i][0]
            prop_src = image_prop[i][1]

            if i == 0:
                split_node = original_text.split(f"![{prop_alt}]({prop_src})", 1)
            else:
                split_node = "".join(split_node[1:]).split(f"![{prop_alt}]({prop_src})", 1)

            new_nodes.append(TextNode(split_node[0], text_type_text))
            new_nodes.append(TextNode(prop_alt, text_type_image, prop_src))

    return new_nodes

########## LINK HANDLING      
def extract_link_props(text):
    link_list = []
    links = re.findall('\[(.*?)\]\((.*?)\)', text)
    for link in links:
        link_list.append(link)
    return link_list

def split_nodes_links(old_nodes):
    new_nodes = []
    split_node = []

    #Handle if old_nodes is just 1 node
    if isinstance(old_nodes, TextNode) == 1:
        node = old_nodes
        link_prop = extract_link_props(node.text)
        for i in range(len(link_prop)):
            prop_text = link_prop[i][0]
            prop_href = link_prop[i][1]

            if i == 0:
                split_node = node.text.split(f"[{prop_text}]({prop_href})", 1)
            else:
                split_node = "".join(split_node[1:]).split(f"[{prop_text}]({prop_href})", 1)

            new_nodes.append(TextNode(split_node[0], text_type_text))
            new_nodes.append(TextNode(prop_text, text_type_link, prop_href))
        return new_nodes

    #Handle old nodes == multiple nodes
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        link_prop = extract_link_props(node.text)

        if len(link_prop) == 0:
            new_nodes.append(node)
            continue

        original_text = node.text

        for i in range(len(link_prop)):
            prop_text = link_prop[i][0]
            prop_href = link_prop[i][1]

            if i == 0:
                split_node = original_text.split(f"[{prop_text}]({prop_href})", 1)
            else:
                split_node = "".join(split_node[1:]).split(f"[{prop_text}]({prop_href})", 1)

            new_nodes.append(TextNode(split_node[0], text_type_text))
            new_nodes.append(TextNode(prop_text, text_type_link, prop_href))

    return new_nodes