class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        return "".join(
            map(lambda item: "=".join((f" {item[0]}", f"\"{item[1]}\"")), self.props.items())
        )
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

def main():
    node = HTMLNode("a")
    print(str(node))
    props = {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    print("".join(map(lambda item: "=".join((f" {item[0]}", f"\"{item[1]}\"")), props.items())))

if __name__ == "__main__":
    main()