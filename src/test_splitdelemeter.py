import unittest
from split_delemeter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitDelemeter(unittest.TestCase):
    def test_bold(self):
        node = [TextNode("This is a *bold* text.", TextType.TEXT)]
        mysplit = split_nodes_delimiter(node, "*", TextType.BOLD)
        result = [TextNode("This is a ", TextType.TEXT, None), TextNode("bold", TextType.BOLD, None), TextNode(" text.", TextType.TEXT, None)]
        self.assertEqual(mysplit, result)

    def test_it(self):
        node = [TextNode("This is a -italic- text.", TextType.TEXT)]
        mysplit = split_nodes_delimiter(node, "-", TextType.ITALIC)
        result = [TextNode("This is a ", TextType.TEXT, None), TextNode("italic", TextType.ITALIC, None), TextNode(" text.", TextType.TEXT, None)]
        self.assertEqual(mysplit, result)

    def test_multiple(self):
        node = [TextNode("This is a -italic- text.", TextType.TEXT), TextNode("This is a *bold* text.", TextType.TEXT)]
        mysplit = split_nodes_delimiter(node, "*", TextType.BOLD)
        result = [TextNode("This is a -italic- text.", TextType.TEXT, None), TextNode("This is a ", TextType.TEXT, None), TextNode("bold", TextType.BOLD, None), TextNode(" text.", TextType.TEXT, None)]
        self.assertEqual(mysplit, result)

    def test_error(self):
        node = [TextNode("This is a *bold text, *like that*", TextType.TEXT)]
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(node, "*", TextType.BOLD)
        self.assertEqual(str(context.exception), "No allowed inner markdowns")

if __name__ == "__main__":
    unittest.main()