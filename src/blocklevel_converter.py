text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

def markdown_to_blocks(markdown):
    markdown.split("\n")
    for line in markdown:
        print(line)

markdown_to_blocks(text)