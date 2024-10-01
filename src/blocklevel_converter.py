import regex as re
from inline_converter import *
from htmlnode import (ParentNode, LeafNode, HTMLNode,
                    tag_paragraph, tag_ordered_list, tag_unordered_list, tag_list_element, tag_code_block, tag_code, tag_blockquote, tag_div, tag_heading)

def markdown_to_blocks(markdown):
    split_blocks = []
    for line in markdown.split("\n"):
        if len(line.strip()) == 0:
            continue
        split_blocks.append(line.strip())
    return split_blocks

def block_to_blocktype(block):
    #Check if string starts with digits followed by a . character
    regex_search = re.search(r"^(\d+\.)(.+)", block)
    if regex_search:
        return "ordered_list", regex_search.group(2)
    
    #Check if string starts with a - or * character
    regex_search = re.search(r"^(\*+)(.+)", block)
    if regex_search:
        return "unordered_list", regex_search.group(2)
    regex_search = re.search(r"^(-+)(.+)", block)
    if regex_search:
        return "unordered_list", regex_search.group(2)
    
    #Check if string starts with an amount of # characters
    regex_search = re.search(r"^(#+) (.+)", block)
    if regex_search:
        return "heading", regex_search.group(2), str(len(regex_search.group(1)))
    
    #Check if a string starts with a > character
    regex_search = re.search(r"^(>)(.+)", block)
    if regex_search:
        return "quote", regex_search.group(2)
    
    #Check if a string starts and ends with ```
    regex_search = re.search(r"```(.*?)```", block)
    if regex_search:
        return "code", regex_search.group(1)
    return "paragraph", block

def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        inline_nodes = []
        block_identification = block_to_blocktype(block)
        block_type = block_identification[0]
        block_text_nodes = text_to_textnode(block_identification[1])

        for textnode in block_text_nodes:
            inline_nodes.append(text_node_to_html_node(textnode))

        match block_type:
            case 'ordered_liste':
                htmlnode = ""
            case 'unordered_list':
                htmlnode = ""
            case 'heading':
                heading_level = block_identification[2]
                htmlnode = ParentNode(tag_heading + heading_level, inline_nodes)
            case 'quote':
                htmlnode = ParentNode(tag_blockquote, inline_nodes)
            case 'code': 
                htmlnode = ParentNode(tag_code_block, ParentNode(tag_code, inline_nodes))
            case 'paragraph':
                htmlnode = ParentNode(tag_paragraph, inline_nodes)

    return htmlnode

markdown_text1 = """# My Static Site

Welcome to my **static site** generator.

## Features
- Easy to use
- Fast
- Customizable

## Code Sample
```python def hello_world(): print("Hello, World!")```"""

text_test = "## Code Sample"
print(markdown_to_html(text_test))