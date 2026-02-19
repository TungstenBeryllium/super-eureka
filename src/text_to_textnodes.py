from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_other import split_nodes_image, split_nodes_link


def text_to_textnodes(text):

    if text == "":
        return []
    else:
        text_list = [TextNode(text, TextType.TEXT)]
        no_bold = split_nodes_delimiter(text_list, "**", TextType.BOLD)
        no_italic = split_nodes_delimiter(no_bold, "_", TextType.ITALIC)
        no_code = split_nodes_delimiter(no_italic, "`", TextType.CODE)
        no_link = split_nodes_link(no_code)
        no_images = split_nodes_image(no_link)

        return no_images
