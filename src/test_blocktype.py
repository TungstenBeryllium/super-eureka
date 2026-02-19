import unittest
from blocktype import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):



    def test_block_type(self):

        string_for_text = "##### par"
        self.assertEqual(
            block_to_block_type(string_for_text), BlockType.HEADING)
    def test_code_type(self):
        string_for_text2 =  "```\ncode here\n```"
        self.assertEqual(block_to_block_type(string_for_text2), BlockType.CODE)
    def test_quote_type(self):
        string_for_text3 = """> quote 1
> quote 2
> quote 3"""
        self.assertEqual(block_to_block_type(string_for_text3), BlockType.QUOTE)
    def test_list_type_unordered(self):
        string_for_text4 = """- K-ON
- AZUSA"""
        self.assertEqual(block_to_block_type(string_for_text4), BlockType.UNORDERED_LIST)
    def test_list_type_ordered(self):

        string_for_text5 = """1. K-ON
2. AZUSA
3. YUI"""
        self.assertEqual(block_to_block_type(string_for_text5), BlockType.ORDERED_LIST)
    def test_list_type_paragraph(self):
        string_for_text6 = "hekas"
        self.assertEqual(block_to_block_type(string_for_text6), BlockType.PARAGRAPH)








if __name__ == "__main__":
    unittest.main(verbosity=2)
