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

    def test_leaf_to_html_no_value(self):
        # no code ;(
        # Here it is important to just insert the method 
        # via .to_html and not call it (i.e., .to_html()).

        # with the context manager i can also evaluate the message.
        # While doing this i have to call the method directly.
        with self.assertRaises(ValueError) as e:
            LeafNode("code", None).to_html()
        self.assertEqual(str(e.exception), "invalid HTML: no value")

if __name__ == "__main__":
    unittest.main()