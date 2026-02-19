from textnode import TextType, TextNode
from extract_markdown import *
import re


def split_nodes_image(old_nodes):

    new_nodes_image = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes_image.append(node)
            continue
        check_image = extract_markdown_images(node.text)
        if not check_image:
            if node.text != "":
                new_nodes_image.append(node)
            continue
        splitimage = []
        text = node.text
        for (image_tag, image_link) in check_image:
            before, after = text.split(f"![{image_tag}]({image_link})", 1)
            if before != "":
                splitimage.append(TextNode(before, TextType.TEXT))
            splitimage.append(TextNode(image_tag, TextType.IMAGE, image_link))
            text = after
        if text != "":
            splitimage.append(TextNode(text, TextType.TEXT))
        new_nodes_image.extend(splitimage)
    return new_nodes_image


def split_nodes_link(old_nodes):
    new_nodes_link = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes_link.append(node)
            continue
        check_link = extract_markdown_links(node.text)
        if not check_link:
            if node.text != "":
                new_nodes_link.append(node)
            continue
        splitlink = []
        text = node.text
        for (link_tag, link_link) in check_link:
            before, after = text.split(f"[{link_tag}]({link_link})", 1)
            if before != "":
                splitlink.append(TextNode(before, TextType.TEXT))
            splitlink.append(TextNode(link_tag, TextType.LINK, link_link))
            text = after
        if text != "":
            splitlink.append(TextNode(text, TextType.TEXT))
        new_nodes_link.extend(splitlink)
    return new_nodes_link
