import unittest
from split_nodes_other import split_nodes_image, split_nodes_link
from textnode import TextType, TextNode


class TestSplitNodesImages(unittest.TestCase):
    def test_split_nodes_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

        node3 = TextNode("hello", TextType.TEXT)
        new_nodes33 = split_nodes_image([node3])
        self.assertListEqual([TextNode("hello", TextType.TEXT)], new_nodes33)

        node4 = TextNode("", TextType.TEXT)
        new_nodes44 = split_nodes_image([node4])
        self.assertListEqual([], new_nodes44)

        node5 = [TextNode("uwowo", TextType.TEXT), TextNode("[to boot dev](https://www.boot.dev)", TextType.LINK),
                 TextNode("![second image](https://i.imgur.com/3elNhQu.png)", TextType.IMAGE)]
        new_nodes55 = split_nodes_image(node5)
        self.assertListEqual([TextNode("uwowo", TextType.TEXT), TextNode("[to boot dev](https://www.boot.dev)", TextType.LINK), TextNode("![second image](https://i.imgur.com/3elNhQu.png)", TextType.IMAGE)], new_nodes55)





class TestSplitNodesLinks(unittest.TestCase):
    def test_split_nodes_links(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("This is text with a link ", TextType.TEXT),
     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
    TextNode(" and ", TextType.TEXT),
    TextNode(
        "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")], new_nodes)

        node3 = TextNode("hello", TextType.TEXT)
        new_nodes3 = split_nodes_link([node3])
        self.assertListEqual([TextNode("hello", TextType.TEXT)], new_nodes3)

        node4 = TextNode("", TextType.TEXT)
        new_nodes4 = split_nodes_link([node4])
        self.assertListEqual([], new_nodes4)

        node5 = [TextNode("uwowo", TextType.TEXT), TextNode("[to boot dev](https://www.boot.dev)", TextType.LINK), TextNode("![second image](https://i.imgur.com/3elNhQu.png)", TextType.IMAGE)]
        new_nodes5 = split_nodes_link(node5)
        self.assertListEqual([TextNode("uwowo", TextType.TEXT), TextNode("[to boot dev](https://www.boot.dev)", TextType.LINK), TextNode("![second image](https://i.imgur.com/3elNhQu.png)", TextType.IMAGE)], new_nodes5)






















if __name__ == "__main__":
    unittest.main(verbosity=2)
