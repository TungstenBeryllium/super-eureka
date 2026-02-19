from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH  = "paragraph"
    HEADING  = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown_text):


    heading_match = re.match(r"^(#{1,6} .*)", markdown_text)
    convert_from_line = markdown_text.split("\n")
    unordered_check = all(line.lstrip().startswith("- ") for line in convert_from_line if line.strip() != "")
    quote_check = all(line.lstrip().startswith(">") for line in convert_from_line if line.strip() != "")


    def multiline():
        lines = markdown_text.split("\n")
        while lines and lines[0].strip() == "":
            lines.pop(0)
        while lines and lines[-1].strip() == "":
            lines.pop()
        if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
            return True
        else:
            return False

    def is_ordered():
        lines = [l for l in convert_from_line if l.strip() != ""]
        if len(lines) < 2:
            return False
        expected_number = 1
        for line in lines:
            stripped = line.lstrip()
            ordered_var = re.match(r"^(\d+)\.\ .+", stripped)
            if ordered_var == None:
                return False
            if expected_number != int(ordered_var.group(1)):
                return False
            expected_number += 1
        return True

    if heading_match:
        return BlockType.HEADING
    elif multiline():
        return BlockType.CODE
    elif quote_check:
        return BlockType.QUOTE
    elif unordered_check:
        return BlockType.UNORDERED_LIST
    elif is_ordered():
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
