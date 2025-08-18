import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    
    def test_eq_tag(self):
        node = HTMLNode("p")
        expected = "p"
        result = node.tag
        self.assertEqual(expected, result)

    def test_eq_props_to_html(self):
        node = HTMLNode(
            "p", "this is a text inside a paragraph", 
            [HTMLNode("a"), HTMLNode("h1")], 
            {"href": "https://www.google.com", "target": "_blank"}
        )
        expected = ' href="https://www.google.com" target="_blank"'
        result = node.props_to_html()
        self.assertEqual(expected, result)

    def test_eq_repr(self):
        node = HTMLNode("p")
        expected = f"HTMLNode(p, None, None, None)"
        result = str(node)
        self.assertEqual(expected, result)

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        result = LeafNode("p", "Hello, world!").to_html()
        expected = "<p>Hello, world!</p>"
        self.assertEqual(result, expected)
    
    def test_leaf_to_html_a(self):
        result = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(result, expected)

    def test_leaf_to_html_no_value(self):
        # no code ;(
        # Here it is important to just insert the method 
        # via .to_html and not call it (i.e., .to_html()).

        # with the context manager i can also evaluate the message.
        # While doing this i have to call the method directly.
        with self.assertRaises(ValueError) as e:
            LeafNode("code", None).to_html()
        self.assertEqual(str(e.exception), "invalid HTML: no value")

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_parents(self):
        grandchild_of_frist_node = LeafNode("b", "grandchild of first node")
        first_child_node = ParentNode("span", [grandchild_of_frist_node])
        grandchild_of_second_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        second_child_node = ParentNode("p", [grandchild_of_second_node])
        parent_node = ParentNode("div", [first_child_node, second_child_node])
        repr_fir_child = '<span><b>grandchild of first node</b></span>'
        repr_sec_child = '<p><a href="https://www.google.com">Click me!</a></p>'
        expected = f'<div>{repr_fir_child}{repr_sec_child}</div>'
        self.assertEqual(
            parent_node.to_html(),
            expected
        )

if __name__ == "__main__":
    unittest.main()