import unittest

from blocklevel_converter import *

class TestBlockExtraction(unittest.TestCase):
    #TEST BLOCK EXTRACTION
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
        
    #TEST BLOCK TYPE IDENTIFICATION
    def test_paragraph(self):
        test_block = "This is a text string"
        self.assertEqual("paragraph",
                            block_to_blocktype(test_block))

    def test_heading(self):
        test_block = "# This is a heading"
        self.assertEqual("heading",
                            block_to_blocktype(test_block))

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

    #TEST BLOCK TO HTML CONVERSIO
    def test_block_to_html(self):
        pass

if __name__ == "__main__":
    unittest.main()