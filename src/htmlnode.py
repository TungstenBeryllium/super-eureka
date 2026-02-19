class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props =  props


    def to_html(self):
        raise Exception(NotImplementedError)


    def props_to_html(self):
        return "".join(f" {i}=\"{self.props[i]}\"" for i in self.props)

    def __eq__(self, other):
        if self.tag == other.tag and self.value==other.value and self.children == other.children and self.props == other.props:
            return True           

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)


    def to_html(self):

        if self.value == None:
            raise ValueError
        if self.tag == None:
            return str(self.value)
        
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        elif self.props != None:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)


    def to_html(self):

        result =""

        if self.tag == None:
            raise ValueError ("tags are missing")
        if self.children == None:
            raise ValueError ("children node is missing")

        for child in self.children:
            result += child.to_html()

        if self.props == None:
            
            return f"<{self.tag}>{result}</{self.tag}>"



        
        return f'<{self.tag}{self.props_to_html()}>{result}</{self.tag}>'



        
