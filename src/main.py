from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    node = TextNode("some_text", TextType.BOLD, "http:sssss")
    node2 = HTMLNode("div", "hello", None,  {"class": "greeting", "href": "boot.dev"})


    print(node2)


main()