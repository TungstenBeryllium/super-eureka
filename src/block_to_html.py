from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_to_blocks import *
from blocktype import *
import re
from textnode import text_node_to_html_node
from text_to_textnodes import text_to_textnodes


def text_extractor(typeblock, text):
    if typeblock == BlockType.HEADING:

        heading = []
        split_heading_text = text.split("\n")
        heading_text = re.match(r"^(#{1,6} (.*))", split_heading_text[0])
        stripped_title_heading = heading_text.group(2).strip()
        heading.append(stripped_title_heading)
        for item_heading in split_heading_text[1:]:
            if item_heading.strip() == "":
                continue
            stripped_heading = item_heading.strip()
            heading.append(stripped_heading)
        combined_heading = " ".join(heading)
        return combined_heading

    elif typeblock == BlockType.QUOTE:
        quoted = []
        split_quote_text = text.split("\n")
        for itemquote in split_quote_text:
            if itemquote.strip() == "":
                continue
            if itemquote.startswith(">"):
                strippeditemquote = itemquote.lstrip(">")
                strippedquote = strippeditemquote.strip()
                quoted.append(strippedquote)
        combined_quoted = " ".join(quoted)
        return combined_quoted

    elif typeblock == BlockType.UNORDERED_LIST:
        unordered = []
        split_unordered_list = text.split("\n")
        for item in split_unordered_list:
            if item.strip() == "":
                continue
            unordered_list_text = re.match(r"^- (.*)", item)
            if not unordered_list_text:
                continue
            stripped_unordered = unordered_list_text.group(1).strip()
            unordered.append(stripped_unordered)
        return unordered

    elif typeblock == BlockType.ORDERED_LIST:
        ordered_list = []
        split_ordered_list = text.split("\n")
        for item2 in split_ordered_list:
            if item2.strip() == "":
                continue
            ordered_list_text = re.match(r"^\d+\. (.*)", item2)
            if not ordered_list_text:
                continue
            stripped_ordered = ordered_list_text.group(1).strip()
            ordered_list.append(stripped_ordered)
        return ordered_list

    elif typeblock == BlockType.PARAGRAPH:
        paragraph_list = []
        split_paragraph_text = text.split("\n")
        for item_par in split_paragraph_text:
            if item_par.strip() == "":
                continue
            stripped_paragraph = item_par.strip()
            paragraph_list.append(stripped_paragraph)
        combined_par = " ".join(paragraph_list)
        return combined_par


def code_extractor(typeblock, text):
    if typeblock == BlockType.CODE:
        
        split_code_text = text.split("\n")
        innercode_text = split_code_text[1:-1]
        joined_code_text = "\n".join(innercode_text)
        joined_code_plus_newline = joined_code_text + "\n"


        return joined_code_plus_newline


def text_to_children(text):
    list_of_textnodes = text_to_textnodes(text)
    htmlnodes = []
    for textnode in list_of_textnodes:
        nodes = text_node_to_html_node(textnode)
        htmlnodes.append(nodes)
    return htmlnodes


def markdown_to_html_node(markdown):
    
    



    blocks = markdown_to_blocks(markdown)
    html_blocks = []
    for block in blocks:



        type_of_block = block_to_block_type(block)
        if type_of_block == BlockType.PARAGRAPH:
            clean_paragraph = text_extractor(type_of_block, block)
            children_of_paragraph = text_to_children(clean_paragraph)
            paragraph_object = ParentNode("p", children_of_paragraph)
            html_blocks.append(paragraph_object)

        elif type_of_block == BlockType.QUOTE:
            clean_quote = text_extractor(type_of_block, block)
            children_of_quote = text_to_children(clean_quote)
            quote_object = ParentNode("blockquote", children_of_quote)
            html_blocks.append(quote_object)

        elif type_of_block == BlockType.UNORDERED_LIST:
            clean_unordered_list = text_extractor(type_of_block, block)
            unordered_list_nodes = []
            for item in clean_unordered_list:
                children_of_unordered = text_to_children(item)
                unordered_list_nodes.append(ParentNode("li",children_of_unordered))
            unordered_list_object = ParentNode("ul", unordered_list_nodes)
            html_blocks.append(unordered_list_object)

        elif type_of_block == BlockType.HEADING:
            heading = block.split(" ")
            heading_counter = heading[0].count("#")
            clean_heading = text_extractor(type_of_block, block)
            tag = f"h{heading_counter}"
            children_of_heading = text_to_children(clean_heading)
            heading_object = ParentNode(tag, children_of_heading)
            html_blocks.append(heading_object)

        elif type_of_block == BlockType.ORDERED_LIST:
            clean_ordered_list = text_extractor(type_of_block, block)
            ordered_list_nodes = []
            for item in clean_ordered_list:
                children_of_ordered = text_to_children(item)
                ordered_list_nodes.append(ParentNode("li",children_of_ordered))
            ordered_list_object = ParentNode("ol", ordered_list_nodes)
            html_blocks.append(ordered_list_object)

        elif type_of_block == BlockType.CODE:
            clean_code = code_extractor(type_of_block, block)
            leafcode_object = LeafNode(None, clean_code)
            node_of_leafcode_object = ParentNode("code", [leafcode_object])
            pre_node_of_leafcode_object = ParentNode("pre", [node_of_leafcode_object])
            html_blocks.append(pre_node_of_leafcode_object)

    total = ParentNode("div", html_blocks)
    return total
