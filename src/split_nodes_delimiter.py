from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):

	new_nodes = []

	for old_node in old_nodes:
		if old_node.text_type != TextType.TEXT:
			new_nodes.append(old_node)
			continue
		elif delimiter not in old_node.text:
			new_nodes.append(old_node)
			continue
		splitnodes = []
		splitdelimiter = old_node.text.split(delimiter)
		if len(splitdelimiter) % 2 == 0:
			raise Exception("incorrect Markdown syntax")
		for i in range(len(splitdelimiter)):
			if splitdelimiter[i] == "":
				continue
			if i % 2 == 0:
				splitnodes.append(TextNode(splitdelimiter[i], TextType.TEXT))
			else:
				splitnodes.append(TextNode(splitdelimiter[i], text_type))
		new_nodes.extend(splitnodes)
	return new_nodes

