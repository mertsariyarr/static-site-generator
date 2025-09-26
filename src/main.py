from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():
    node = TextNode("some_text", TextType.BOLD, "http:sssss")
    node2 = HTMLNode("div", "hello", None,  {"class": "greeting", "href": "boot.dev"})
    node3 = LeafNode("p", "wowww")
    node4 = LeafNode("a", "Hello World!", {"href":"google.com", "target": "_blank"})
    node5 = LeafNode(None, "None", None)



main()