from textnode import *
from htmlnode import *

def main():
    # Create a new TextNode object
    node = create_text_node("This is a text node", "bold", "https://www.boot.dev")
    node1 = create_text_node("Hello", "heading", "example.com")
    node2 = create_text_node("Hello", "heading", "example.com")
    print("#"*30)
    print("TEXT NODES")
    print(node)
    print(node1)
    print(compare_text_node(node, node1))
    print(compare_text_node(node1, node2))
    print(represent_text_node(node))
    print(represent_text_node(node1))
    print("#"*30)
    print("HTML NODES")

    html_node = create_html_node(
        tag = 'a',
        value = 'google',
        children = None,
        props = {"href": "https://www.google.com", "target": "_blank"}
        )
    
    print(html_node)
    print(transform_props_to_html(html_node))
    print(represent_html_node(html_node))
    

    leaf_node = create_leaf_node(
        tag = "a", 
        value = "Click me!", 
        props = {"href": "https://www.google.com"}
    )
    leaf_node2 = create_leaf_node(
        tag = "p", 
        value = "This is a paragraph of text."
    )

    print("#"*30)
    print("LEAF NODES")
    print(leaf_node)
    print(leaf_node2)
    print(transform_leaf_node_to_html(leaf_node))
    print(transform_leaf_node_to_html(leaf_node2))
    print("#"*30)
    print("PARENT NODES")

    parent_node = create_parent_node(
        tag="p",
        children=[
            create_leaf_node("b", "Bold text"),
            create_leaf_node(None, "Normal text"),
            create_leaf_node("i", "italic text"),
            create_leaf_node(None, "Normal text"),
        ])
    print(parent_node)
    print(transform_parent_node_to_html(parent_node))
    print("#"*30)
    print("TEXT NODES TO HTML NODES")
    text_2_html = text_node_to_html_node(node)
    print(text_2_html)
    

# Call the main function
if __name__ == "__main__":
    main()
