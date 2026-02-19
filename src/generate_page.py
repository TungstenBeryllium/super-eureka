from block_to_html import markdown_to_html_node
from extract_title import extract_title
from htmlnode import HTMLNode, ParentNode, LeafNode
import os



def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown_origin = f.read()
    with open(template_path, "r") as g:
        template = g.read()

    HTMLblock = markdown_to_html_node(markdown_origin)
    HTMLstring = HTMLblock.to_html()
    title = extract_title(markdown_origin)

    template_with_content = template.replace("{{ Content }}", HTMLstring)
    template_with_title = template_with_content.replace("{{ Title }}", title)

    href_replace = template_with_title.replace('href="/',f'href="{basepath}')
    src_replace = href_replace.replace('src="/',f'src="{basepath}')

    destination_path = os.path.dirname(dest_path)
    if destination_path != "":
        os.makedirs(destination_path, exist_ok=True)

    with open(dest_path, "w") as h:
        h.write(src_replace)
