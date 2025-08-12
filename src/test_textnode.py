import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        url = "http://boot.dev"
        node = TextNode("This is a text node", TextType.BOLD, url)
        node2 = TextNode("This is a text node", TextType.BOLD, url)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        url1 = "https://www.geeksforgeeks.org"
        url2 = "https://www.w3schools.com/"
        node = TextNode("This is a text node with a link", TextType.LINK, url1)
        node2 = TextNode("This is a text node with a link", TextType.LINK, url2)
        self.assertNotEqual(node, node2)

    def test_textnode_to_htmlnode_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node") 

    def test_textnode_to_htmlnode_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<b>This is a text node</b>") 

    def test_textnode_to_htmlnode_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<i>This is a text node</i>") 
    
    def test_textnode_to_htmlnode_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<code>This is a text node</code>") 

    def test_textnode_to_htmlnode_link(self):
        href = "https://boot.dev"
        node = TextNode("This is a text node", TextType.LINK, href)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), f'<a href="{href}">This is a text node</a>') 

    def test_textnode_to_htmlnode_image(self):
        src = "https://en.wikipedia.org/wiki/de:Rembrandt_van_Rijn"
        alt = "Rembrandt van Rijn"
        node = TextNode(alt, TextType.IMAGE, src)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), f'<img src="{src}" alt="{alt}"></img>')

    def test_textnode_to_htmlnode_value_error(self):
        node = TextNode("This is a text node", "plain")
        with self.assertRaises(ValueError) as e:
            text_node_to_html_node(node)
        self.assertEqual(str(e.exception), f"invalid text node: {node.text_type}")

if __name__ == "__main__":
    unittest.main()