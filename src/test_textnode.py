import unittest
from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = create_text_node("This is a text node", "bold")
        node2 = create_text_node("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq_different_text(self):
        node = create_text_node("This is a text node", "bold")
        node2 = create_text_node("This is another text node", "bold")
        self.assertNotEqual(node, node2)

    def test_not_eq_different_type(self):
        node = create_text_node("This is a text node", "bold")
        node2 = create_text_node("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_not_eq_different_url(self):
        node = create_text_node("This is a text node", "bold", "https://example.com")
        node2 = create_text_node("This is a text node", "bold", "https://another-example.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_url_none(self):
        node = create_text_node("This is a text node", "bold", "https://example.com")
        node2 = create_text_node("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_not_eq_url_none_reverse(self):
        node = create_text_node("This is a text node", "bold")
        node2 = create_text_node("This is a text node", "bold", "https://example.com")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = create_text_node("This is a text node", "bold", "https://example.com")
        self.assertEqual(represent_text_node(node), "TextNode(This is a text node, bold, https://example.com)")

if __name__ == "__main__":
    unittest.main()
