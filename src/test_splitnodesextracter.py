import unittest
from split_nodes_extracter import split_nodes_link, split_nodes_image
from textnode import TextNode, TextType


class SplitNodesExtracter(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGES, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGES, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_image_single(self):
        node = TextNode("![image](https://www.example.COM/IMAGE.PNG)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([
            TextNode("image", TextType.IMAGES, "https://www.example.COM/IMAGE.PNG")
        ],
          new_nodes)
    
    def test_split_one_link(self):
        node = TextNode("This is a text with a [this is link](and this is the explain) link out.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a text with a ", TextType.TEXT),
                TextNode("this is link", TextType.LINK, "and this is the explain"),
                TextNode(" link out.", TextType.TEXT),
                ],new_nodes
        )

    def test_split_more_link(self):
        node = TextNode("This is a text with a [this is link](and this is the explain) and [this is another link](another explain) links.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a text with a ", TextType.TEXT),
                TextNode("this is link", TextType.LINK, "and this is the explain"),
                TextNode(" and ", TextType.TEXT),
                TextNode("this is another link", TextType.LINK, "another explain"),
                TextNode(" links.", TextType.TEXT)
            ],
            new_nodes
        )



if __name__ == "__main__":
    unittest.main()