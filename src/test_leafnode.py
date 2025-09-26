import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello World!")
        self.assertEqual(node.to_html(), "<p>Hello World!</p>")
        
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Hello World!", {"href":"google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="google.com" target="_blank">Hello World!</a>')


    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "hi")
        self.assertEqual(node.to_html(), "hi")


    def test_leaf_without_value(self):
        with self.assertRaises(ValueError) as context:
            node = LeafNode("a", None)
            node.to_html()
        self.assertEqual(str(context.exception), "all leaf nodes must have a value")
        
