import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        result = LeafNode("p", "Hello, world!").to_html()
        expected = "<p>Hello, world!</p>"
        self.assertEqual(result, expected)
    
    def test_leaf_to_html_a(self):
        result = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(result, expected)

    # to-do: debug 
    def test_leaf_to_html_no_value(self):
        # no code ;(
        self.assertRaises(ValueError, LeafNode("code", None).to_html())

if __name__ == "__main__":
    unittest.main()