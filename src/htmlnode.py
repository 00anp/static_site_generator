def create_html_node(tag=None, value=None, children=None, props=None):
    html_node = {
        'tag':tag,
        'value':value,
        'children':children,
        'props':props
    }
    return html_node


def transform_to_html():
    raise NotImplementedError("transform_to_html not implemented")


def transform_props_to_html(html_node):
    if html_node['props'] is None:
            return ""
    props = ""
    for k,v in html_node['props'].items():
        props += f' {k}="{v}"'
    return props


def represent_html_node(html_node):
    return f"HTMLNode({html_node['tag']}, {html_node['value']}, {html_node['children']}, {html_node['props']})"


def create_leaf_node(tag=None, value=None, props=None):
    if value is None:
        raise ValueError("LeafNode must have a value.")
    leaf_node = {
        'tag':tag,
        'value':value,
        'props':props
    }
    return leaf_node


def transform_leaf_node_to_html(leaf_node):
    if leaf_node['value'] is None:
        raise ValueError("Invalid HTML: no value")
    if leaf_node['tag'] is None:
        return leaf_node['value']
    return f"<{leaf_node['tag']}{transform_props_to_html(leaf_node)}>{leaf_node['value']}</{leaf_node['tag']}>"


def create_parent_node(tag=None, children=None, props=None):
    if tag is None:
        raise ValueError("ParentNode must have a tag.")
    if children is None or len(children) == 0:
        raise ValueError("ParentNode must have children.")
    parent_node = {
        'tag':tag,
        'children':children,
        'props':props
    }
    return parent_node


def transform_parent_node_to_html(parent_node):
    children = parent_node['children']
    children_html = "".join(transform_leaf_node_to_html(child) for child in children)
    return f"<{parent_node['tag']}{transform_props_to_html(parent_node)}>{children_html}</{parent_node['tag']}>"