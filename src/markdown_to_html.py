from block_types import BlockType, block_to_block_type
from markdown_blocker import markdown_to_blocks
from text_and_nodes import text_to_textnodes
from parentnode import ParentNode
from textnode import text_node_to_html_node, TextNode, TextType

md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
    

#Create all above under div
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


# block type getter
def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return ordered_list(block)
    if block_type == BlockType.UNORDERED_LIST:
        return uordered_to_html(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    raise ValueError("invalid block type")

#Create textnodes from text_to_textnodes function and use text_node_html to create a list of LeafNodes
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


#for headers
def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)



## For paragraphs
def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

## for codes
def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

## for quotes
def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

    
## unordered_list
def uordered_to_html(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        new_lines.append(ParentNode("li", children))
    return ParentNode("ul", new_lines)


## ordered_list
def ordered_list(block):
    lines = block.split("\n")
    html_items = []
    for line in lines:
        text = line[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


        

