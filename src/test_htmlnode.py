import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        expected_props_html = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_props_html)

        node2 = HTMLNode(tag="p")
        self.assertEqual(node2.props_to_html(), "")


class TestLeafNode(unittest.TestCase):
    def test_render_no_tag(self):
        node = LeafNode(value="This is a paragraph of text.")
        self.assertEqual(node.to_html(), "This is a paragraph of text.")

    def test_render_with_tag(self):
        node = LeafNode(tag="p", value="This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_render_with_tag_and_props(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_value_required(self):
        with self.assertRaises(ValueError):
            LeafNode()


class TestParentNode(unittest.TestCase):
    def test_render(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]
        node = ParentNode("p", children)
        expected_html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_tag_required(self):
        with self.assertRaises(ValueError):
            ParentNode()

    def test_children_required(self):
        with self.assertRaises(ValueError):
            ParentNode("div")

if __name__ == "__main__":
    unittest.main()