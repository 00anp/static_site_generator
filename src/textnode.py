from htmlnode import *

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


def create_text_node(text, text_type, url=None):
    text_node = {
        'text': text,
        'text_type': text_type, 
        'url':url if url is not None else None
        }
    return text_node


def compare_text_node(node1, node2):
    return (node1['text'] == node2['text'] and 
            node1['text_type'] == node2['text_type'] and 
            node1['url'] == node2['url'])


def represent_text_node(node):
    return f"TextNode({node['text']}, {node['text_type']}, {node['url']})"


def text_node_to_html_node(text_node):
    if text_node['text_type'] == text_type_text:
        return transform_leaf_node_to_html(create_leaf_node(None, text_node['text']))
    if text_node['text_type'] == text_type_bold:
        return transform_leaf_node_to_html(create_leaf_node("b", text_node['text']))
    if text_node['text_type'] == text_type_italic:
        return transform_leaf_node_to_html(create_leaf_node("i", text_node['text']))
    if text_node['text_type'] == text_type_code:
        return transform_leaf_node_to_html(create_leaf_node("code", text_node['text']))
    if text_node['text_type'] == text_type_link:
        return transform_leaf_node_to_html(create_leaf_node("a", text_node['text'], {"href": text_node.url}))
    if text_node['text_type'] == text_type_image:
        return transform_leaf_node_to_html(create_leaf_node("img", "", {"src": text_node['url'], "alt": text_node['text']}))
    raise ValueError(f"Invalid text type: {text_node['text_type']}")
