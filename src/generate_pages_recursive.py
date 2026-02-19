from block_to_html import markdown_to_html_node
from extract_title import extract_title
from htmlnode import HTMLNode, ParentNode, LeafNode
import os
import shutil
from pathlib import Path
from generate_page import *


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):


    files_content_dir = os.listdir(dir_path_content)
    for file in files_content_dir:
        content_source_path = os.path.join(dir_path_content, file)
        directory_destination_path = os.path.join(dest_dir_path, file)

        if os.path.isfile(content_source_path):
            if content_source_path.endswith(".md"):
                file_path = Path(directory_destination_path)
                new_file_path = file_path.with_suffix(".html")
                generate_page(content_source_path, template_path, new_file_path, basepath)
            else:
                continue
        elif os.path.isdir(content_source_path):
            generate_pages_recursive(content_source_path, template_path, directory_destination_path, basepath)
