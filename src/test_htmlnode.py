import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    
    TAG = "p"
    VALUE = "this is a text inside a paragraph"
    CHILDREN = [HTMLNode("a"), HTMLNode("h1")]
    PROPS = {"href": "https://www.google.com", "target": "_blank"}

    def test_eq_tag(self):
        node = HTMLNode(self.TAG)
        expected = self.TAG
        result = node.tag
        self.assertEqual(expected, result)

    def test_eq_props_to_html(self):
        node = HTMLNode(self.TAG, self.VALUE, self.CHILDREN, self.PROPS)
        expected = ' href="https://www.google.com" target="_blank"'
        result = node.props_to_html()
        self.assertEqual(expected, result)

    def test_not_eq_props_to_html(self):
        node = HTMLNode(self.TAG, self.VALUE, self.CHILDREN, self.PROPS)
        failure = 'href="https://www.google.com" target="_blank"'
        result = node.props_to_html()
        self.assertNotEqual(failure, result)
    
    def test_eq_repr(self):
        node = HTMLNode(self.TAG)
        expected = f"HTMLNode({self.TAG}, None, None, None)"
        result = str(node)
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()