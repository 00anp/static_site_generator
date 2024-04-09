import re
from textnode import *


def represent_as_text_node(nodes):
    new_nodes = []
    for node in nodes:
        new_nodes.append(represent_text_node(node))
    return new_nodes


def text_to_textnodes(text):
    nodes = [create_text_node(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_images(nodes)
    nodes = split_nodes_links(nodes)
    nodes = represent_as_text_node(nodes)
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node['text_type'] != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node['text'].split(delimiter)
        if len(sections)%2 == 0:
            raise ValueError("Invalid markdown, formatted sections not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                text_node = create_text_node((sections[i]), text_type_text)
                split_nodes.append(text_node)
            else:
                text_node = create_text_node((sections[i]), text_type)
                split_nodes.append(text_node)
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_images(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node['text_type'] != text_type_text:
            new_nodes.append(old_node)
            continue
        old_node_text = old_node['text']
        images = extract_markdown_images(old_node_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = old_node_text.split(f"![{image[0]}]({image[1]})",1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(create_text_node(sections[0], text_type_text))
            new_nodes.append(create_text_node(image[0], text_type_image, image[1]))
            old_node_text = sections[1]
        if old_node_text != "":
            new_nodes.append(create_text_node(old_node_text, text_type_text))
    return new_nodes


def split_nodes_links(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node['text_type'] != text_type_text:
            new_nodes.append(old_node)
            continue
        old_node_text = old_node['text']
        links = extract_markdown_links(old_node_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = old_node_text.split(f"[{link[0]}]({link[1]})",1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(create_text_node(sections[0], text_type_text))
            new_nodes.append(create_text_node(link[0], text_type_link, link[1]))
            old_node_text = sections[1]
        if old_node_text != "":
            new_nodes.append(create_text_node(old_node_text, text_type_text))
    return new_nodes



def extract_markdown_images(text):
    images = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return images


def extract_markdown_links(text):
    links = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return links





# node = create_text_node("This is text with a `code block` word", text_type_text)
# new_nodes = split_nodes_delimiter([node], "`", text_type_code)
# print(new_nodes)
# text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
# print("#"*30)
# print("Text nodes")
# print(new_nodes)
# print("#"*30)
# print("image nodes")
# print(extract_markdown_images(text))
# text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
# print("#"*30)
# print("link nodes")
# print(extract_markdown_links(text))
# print("#"*30)
# print("split images nodes")
# node = create_text_node("This is text with an [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
#     text_type_text)
# print(node)
# links = split_nodes_links([node])
# print(links)
print("#"*30)
print("text to textnodes")
text =  "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
t_text =  text_to_textnodes(text)
print(t_text)
