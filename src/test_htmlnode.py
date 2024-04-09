import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = create_html_node(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        expected_props_html = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(transform_props_to_html(node), expected_props_html)

        node2 = create_html_node(tag="p")
        self.assertEqual(transform_props_to_html(node2), "")


class TestLeafNode(unittest.TestCase):
    def test_render_no_tag(self):
        node = create_leaf_node(value="This is a paragraph of text.")
        self.assertEqual(transform_leaf_node_to_html(node), "This is a paragraph of text.")

    def test_render_with_tag(self):
        node = create_leaf_node(tag="p", value="This is a paragraph of text.")
        self.assertEqual(transform_leaf_node_to_html(node), "<p>This is a paragraph of text.</p>")

    def test_render_with_tag_and_props(self):
        node = create_leaf_node(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(transform_leaf_node_to_html(node), '<a href="https://www.google.com">Click me!</a>')

    def test_value_required(self):
        with self.assertRaises(ValueError):
            create_leaf_node()


class TestParentNode(unittest.TestCase):
    def test_render(self):
        children = [
            create_leaf_node("b", "Bold text"),
            create_leaf_node(None, "Normal text"),
            create_leaf_node("i", "italic text"),
            create_leaf_node(None, "Normal text"),
        ]
        node = create_parent_node("p", children)
        expected_html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(transform_parent_node_to_html(node), expected_html)

    def test_tag_required(self):
        with self.assertRaises(ValueError):
            create_parent_node()

    def test_children_required(self):
        with self.assertRaises(ValueError):
            create_parent_node("div")

if __name__ == "__main__":
    unittest.main()