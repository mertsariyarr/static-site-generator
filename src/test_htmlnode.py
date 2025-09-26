import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode("div", "hello, world!", None, {"class": "greeting", "href": "boot.dev"})
        self.assertEqual(node.props_to_html(), ' class="greeting" href="boot.dev"')
    def test_values(self):
        node = HTMLNode("div", "hello", None,  {"class": "greeting", "href": "boot.dev"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "hello")
        self.assertEqual(node.children, None)
    def test_repr(self):
        node = HTMLNode("div", "hello", None,  {"class": "greeting", "href": "boot.dev"})
        self.assertEqual(node.__repr__(), "HTMLNode(div, hello, children: None, {'class': 'greeting', 'href': 'boot.dev'})")
 


if __name__ == "__main__":
    unittest.main()