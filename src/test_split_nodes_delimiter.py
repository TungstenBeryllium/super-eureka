import unittest

from textnode import TextType, TextNode, text_node_to_html_node
from split_nodes_delimiter import split_nodes_delimiter



class TestSplitNodesDelimiter(unittest.TestCase):

    def test_split_nodes_code(self):
        markdownnode = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([markdownnode], "`", TextType.CODE)
        self.assertEqual([
    TextNode("This is text with a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" word", TextType.TEXT),
], new_nodes)

    def test_split_nodes_italic(self):
        markdownnode2 = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes2 = split_nodes_delimiter([markdownnode2], "_", TextType.ITALIC)
        self.assertEqual([
    TextNode("This is text with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word", TextType.TEXT),
], new_nodes2)

    def test_split_nodes_bold(self):
        markdownnode3 = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes3 = split_nodes_delimiter([markdownnode3], "**", TextType.BOLD)
        self.assertEqual([
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ], new_nodes3)





    def test_compare_bold(self):
        markdownnode4 = [TextNode("This is text with a **bold** word", TextType.TEXT), TextNode("This is text with a **bold** word", TextType.TEXT)]
        newnodes4 = split_nodes_delimiter(markdownnode4, "**", TextType.BOLD)

        self.assertEqual([TextNode("This is text with a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" word", TextType.TEXT),
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT)], newnodes4)

        self.assertNotEqual([TextNode("This is text with a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" word", TextType.TEXT),
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT)], newnodes4)




    def test_compare_italic(self):
        markdownnode5 = [TextNode("This is text with an _italic_ word", TextType.TEXT), TextNode("This is text with an _italic_ word", TextType.TEXT)]
        newnodes5 = split_nodes_delimiter(markdownnode5, "_", TextType.ITALIC)

        self.assertEqual([TextNode("This is text with an ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word", TextType.TEXT), TextNode("This is text with an ", TextType.TEXT),
                          TextNode("italic", TextType.ITALIC), TextNode(" word", TextType.TEXT),], newnodes5)

        self.assertNotEqual([TextNode("This is text with an ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" word", TextType.TEXT), TextNode("This is text with an ", TextType.TEXT),
                          TextNode("italic", TextType.ITALIC), TextNode(" word", TextType.TEXT),], newnodes5)







    def test_compare_code(self):
        markdownnode6 = [TextNode("This is text with a `code block` word", TextType.TEXT), TextNode("This is text with a `code block` word", TextType.TEXT)]
        newnodes6 = split_nodes_delimiter(markdownnode6, "`", TextType.CODE)
        self.assertEqual([TextNode("This is text with a ", TextType.TEXT),
                          TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT), TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE),
                          TextNode(" word", TextType.TEXT)], newnodes6)

        self.assertNotEqual([TextNode("This is text with a ", TextType.TEXT),
                          TextNode("italic", TextType.ITALIC), TextNode(" word", TextType.TEXT), TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE),
                          TextNode(" word", TextType.TEXT)], newnodes6)




if __name__ == "__main__":
    unittest.main(verbosity=2)
