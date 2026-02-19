import re

def extract_title(markdown):

    header_text = re.match(r"^(#{1} (.*))", markdown)
    if not header_text:
        raise Exception("Could not extract title")
    else:
        stripped_header_text = header_text.group(2).strip()
        return stripped_header_text
