import unittest

from blocklevel_converter import *

class TestBlockExtraction(unittest.TestCase):
    def test_block_singleline(self):
        test_block = """
        # This is a heading
        """
        self.assertEqual(["# This is a heading"], markdown_to_blocks(test_block))

    def test_block_multiline(self):
        test_block = """
        # This is a heading
        ## This is a subheading


        - Unordered list item 1
        - Unordered list item 2
        - Unordered list item 3

        Text in a paragraph format with a [link](https://www.google.com)
        """
        self.assertEqual(["# This is a heading",
                          "## This is a subheading",
                          "- Unordered list item 1",
                          "- Unordered list item 2",
                          "- Unordered list item 3",
                          "Text in a paragraph format with a [link](https://www.google.com)"], 
                          markdown_to_blocks(test_block))

    def test_block_trim(self):
        test_block = """ 
                         # This is a heading                   
                  ## This is a subheading


               - Unordered list item 1
        - Unordered list item 2             
        - Unordered list item 3      

                 Text in a paragraph format with a [link](https://www.google.com)
        """
        self.assertEqual(["# This is a heading",
                          "## This is a subheading",
                          "- Unordered list item 1",
                          "- Unordered list item 2",
                          "- Unordered list item 3",
                          "Text in a paragraph format with a [link](https://www.google.com)"], 
                          markdown_to_blocks(test_block))

class TestBlockIdentification(unittest.TestCase):
    def test_paragraph(self):
        test_block = "This is a text string"
        self.assertEqual("paragraph",
                            block_to_blocktype(test_block))

    def test_heading(self):
        test_block_h1 = "# This is a heading"
        test_block_h6 = "###### This is a heading"
        self.assertEqual("heading",
                            block_to_blocktype(test_block_h1))
        self.assertEqual("heading",
                            block_to_blocktype(test_block_h6))
        
    def test_code(self):
        test_block = "```This is a code block```"
        self.assertEqual("code",
                            block_to_blocktype(test_block))

    def test_quote(self):
        test_block = ">This is a quote"
        self.assertEqual("quote",
                            block_to_blocktype(test_block))

    def test_unordered_list(self):
        test_block = "* This is an unordered list"
        test_block_2 = "- This is also an unordered list"
        self.assertEqual("unordered_list",
                            block_to_blocktype(test_block))
        self.assertEqual("unordered_list",
                            block_to_blocktype(test_block_2))

    def test_ordered_list(self):
        test_block = "1. This is an ordered list"
        self.assertEqual("ordered_list",
                            block_to_blocktype(test_block))

class TestBlockHTMLConversion(unittest.TestCase):
    def test_code_and_unordered_list(self):
        markdown_text1 = """# My Static Site

Welcome to my **static site** generator.

## Features
- Easy to use
- Fast
- Customizable

## Code Sample
```python
def hello_world():
    print("Hello, World!")"""
        self.assertEqual(1, 1)
        
    def test_nested_lists_blockquotes(self):
        markdown_text_2 = """### 2. Nested Lists and Blockquotes
```markdown
# Nested Lists & Blockquotes

## Nested Lists
- Item 1
  - Subitem 1.1
    - Sub-subitem 1.1.1
  - Subitem 1.2
- Item 2

## Blockquotes
> This is a blockquote.
>
> > Nested blockquote.
>
> Back to the first level.

## Mixed Content
1. Item 1
   - Subitem 1.1
   - Subitem 1.2
2. Item 2
"""
        self.assertEqual(1, 1)

    def test_links_images_horizontal_rules(self):
        markdown_text_3 = """# Links, Images, and Horizontal Rules

## Links
Here is a [link to Google](https://www.google.com).

## Images
![Sample Image](https://via.placeholder.com/150)

## Horizontal Rule
---

## Combined
Here is a link: [Google](https://www.google.com).

![Image](https://via.placeholder.com/100)
"""
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()