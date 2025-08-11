class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    def props_to_html(self):
        if self.props is None:
            return ""
        return "".join(
            map(lambda item: "=".join((f" {item[0]}", f"\"{item[1]}\"")), self.props.items())
        )
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("invalid HTML: no value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    
    def __init__(self, tag, children, props = None):    
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("invalid HTML: no tag")
        if self.children == None:
            raise ValueError("invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{super().props_to_html()}>{children_html}</{self.tag}>"
            

def main():
    node = HTMLNode("a")
    print(str(node))
    print(node.__repr__())
    props = {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    print(
        "".join(
            map(lambda item: "=".join((f" {item[0]}", f"\"{item[1]}\"")), props.items())
        )
    )

if __name__ == "__main__":
    main()