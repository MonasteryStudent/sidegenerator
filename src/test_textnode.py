import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node with a link", TextType.BOLD, "http://boot.dev")
        node2 = TextNode("This is a text node with a link", TextType.BOLD, "http://boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is the last text node", TextType.PLAIN)
        node2 = TextNode("This is the last text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node with a link", TextType.LINK, "https://www.geeksforgeeks.org")
        node2 = TextNode("This is a text node with a link", TextType.LINK, "https://www.w3schools.com/")
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()