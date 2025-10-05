import shutil
import os

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
static = "/home/mert/static-site-generator/static"
mypublic = "/home/mert/static-site-generator/public/"
from copystatic import copier, cleaner

def main():
    print("Deleting public directory...")
    cleaner(mypublic)

    print("Copying static files to pub dir.")
    copier(static, mypublic)


if __name__ == "__main__":
    main()