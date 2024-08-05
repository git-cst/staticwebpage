def markdown_to_blocks(markdown):
    split_blocks = []
    for line in markdown.split("\n"):
        if len(line.strip()) == 0:
            continue
        split_blocks.append(line.strip())
    return split_blocks