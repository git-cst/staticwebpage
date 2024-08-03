from textnode import TextNode, text_type_bold
from htmlnode import HTMLNode, tag_bold, LeafNode, tag_hyperlink, ParentNode, tag_paragraph, tag_div
from inline_converter import *

def main():
    old_nodes = TextNode("This is text with an image ![boot dev](https://www.boot.dev) and so is this text ![Excellent](https://imgur.com/gallery/excellent-mr-burns-hzaJ4Hn)", text_type_text)  
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

        print(new_nodes)
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

main()
