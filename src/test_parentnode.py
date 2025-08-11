import unittest

from htmlnode import *

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