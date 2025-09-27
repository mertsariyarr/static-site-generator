from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
def main():
    node = TextNode("some_text", TextType.BOLD, "http:sssss")
    node2 = HTMLNode("div", "hello", None,  {"class": "greeting", "href": "boot.dev"})
    node3 = LeafNode("p", "wowww")
    node4 = LeafNode("a", "Hello World!", {"href":"google.com", "target": "_blank"})
    node5 = LeafNode(None, "None", None)
    leaf = LeafNode("a", "text", {"href": "google.com", "target": "blank"})
    node6 = ParentNode("p", [leaf])
    node7 = TextNode("this is a link", TextType.LINK, "google.com")
    node8 = TextNode("this is a image", TextType.IMAGES, "someimage/")
    myhtml = text_node_to_html_node(node8)
    print(myhtml.props)
    


main()