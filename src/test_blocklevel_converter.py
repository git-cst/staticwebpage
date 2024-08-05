import unittest

from blocklevel_converter import *

class TestHTMLNode(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()