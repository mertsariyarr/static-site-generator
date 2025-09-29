from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    final = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            final.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            final.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                final.append(TextNode(sections[0], TextType.TEXT))
            final.append(
                TextNode(
                    image[0],
                    TextType.IMAGES,
                    image[1]
                )
            )
            original_text = sections[1]
        if original_text != "":
            final.append(TextNode(original_text, TextType.TEXT))
    return final


def split_nodes_link(old_nodes):
    final = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            final.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            final.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})")
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                final.append(TextNode(sections[0], TextType.TEXT))
            final.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            final.append(TextNode(original_text, TextType.TEXT))
    return final


node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT)

print(split_nodes_link([node]))