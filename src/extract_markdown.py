import re

def extract_markdown_images(text):

    images_regex = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    return images_regex


def extract_markdown_links(text):

    links_regex = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    return links_regex
