def markdown_to_blocks(markdown):



    blocks_list = []
    blocks = markdown.split("\n\n")

    for block in blocks:
        stripped = block.strip()
        if stripped == "":
            continue
        blocks_list.append(stripped)

    return blocks_list
