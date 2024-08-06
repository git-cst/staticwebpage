import regex as re

def markdown_to_blocks(markdown):
    split_blocks = []
    for line in markdown.split("\n"):
        if len(line.strip()) == 0:
            continue
        split_blocks.append(line.strip())
    return split_blocks

def block_to_blocktype(block):
    check_heading = re.findall(r"^(#+)", block)
    check_ordered_list = re.findall(r"^(\d+\.)", block)
    check_unordered_list = re.findall(r"^(\*+)|^(-+)", block)
    check_code_block = re.findall(r"^(```)|(```)$", block)
    check_quote_block = re.findall(r"^(>)", block)

    if len(check_heading) != 0:
        return "heading"
    if len(check_code_block) != 0:
        return "code"
    if len(check_quote_block) != 0:
        return "quote"
    if len(check_unordered_list) != 0:
        return "unordered_list"
    if len(check_ordered_list) != 0:
        return "ordered_list"
    return "paragraph"

def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        current_block_type = block_to_blocktype(block)
        match current_block_type:
            case "paragraph":
                pass
            case "heading":
                pass
            case "code":
                pass
            case "quote":
                pass
            case "unordered list":
                pass
            case "ordered_list":
                pass
    pass 