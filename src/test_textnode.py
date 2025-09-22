import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

        
    def test_check_none(self):
        node = TextNode("this is a text node", TextType.CODE, None)
        self.assertIsNone(node.url)
    
    def test_check_not_none(self):
        node = TextNode("this is a text node", TextType.CODE, "https")
        self.assertIsNotNone(node.url)
        


    


if __name__ == "__main__":
    unittest.main()