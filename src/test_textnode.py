import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from split_nodes_delimiter import split_nodes_delimiter

class TestTextNodeToHTMLNode(unittest.TestCase):


    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")




    def test_text2(self):
        node2 = TextNode("This is a text node", TextType.TEXT)
        html_node2 = text_node_to_html_node(node2)
        self.assertEqual(html_node2.tag, None)
        self.assertEqual(html_node2.value, "This is a text node")


    def test_bold(self):
        node3 = TextNode("This is a text node", TextType.BOLD)
        html_node3 = text_node_to_html_node(node3)
        self.assertEqual(html_node3.tag, "b")
        self.assertEqual(html_node3.value, "This is a text node")


    def test_italic(self):
        node4 = TextNode("This is a text node", TextType.ITALIC)
        html_node4 = text_node_to_html_node(node4)
        self.assertEqual(html_node4.tag, "i")
        self.assertEqual(html_node4.value, "This is a text node")

    def test_code(self):
        node5 = TextNode("This is a text node", TextType.CODE)
        html_node5 = text_node_to_html_node(node5)
        self.assertEqual(html_node5.tag, "code")
        self.assertEqual(html_node5.value, "This is a text node")

    def test_link(self):
        node6 = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        html_node6 = text_node_to_html_node(node6)
        self.assertEqual(html_node6.tag, "a")
        self.assertEqual(html_node6.value, "This is a text node")
        self.assertEqual(html_node6.props, {"href": "https://www.google.com"})

    def test_image(self):
        node7 = TextNode("https://example.com/cat.png", TextType.IMAGE, "A very wise cat")
        html_node7 = text_node_to_html_node(node7)
        self.assertEqual(html_node7.tag, "img")
        self.assertEqual(html_node7.value, "")
        self.assertEqual(html_node7.props, {"src": "https://example.com/cat.png", "alt": "A very wise cat"})


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

    def test_compare_italic(self):
        markdownnode5 = [TextNode("This is text with an _italic_ word", TextType.TEXT), TextNode("This is text with an _italic_ word", TextType.TEXT)]
        newnodes5 = split_nodes_delimiter(markdownnode5, "_", TextType.ITALIC)

        self.assertEqual([TextNode("This is text with an ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word", TextType.TEXT), TextNode("This is text with an ", TextType.TEXT),
                          TextNode("italic", TextType.ITALIC), TextNode(" word", TextType.TEXT),], newnodes5)
    def test_compare_code(self):
        markdownnode6 = [TextNode("This is text with a `code block` word", TextType.TEXT), TextNode("This is text with a `code block` word", TextType.TEXT)]
        newnodes6 = split_nodes_delimiter(markdownnode6, "`", TextType.CODE)
        self.assertEqual([TextNode("This is text with a ", TextType.TEXT),
                          TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT), TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE),
                          TextNode(" word", TextType.TEXT)], newnodes6) 
if __name__ == "__main__":
    unittest.main(verbosity=2)
