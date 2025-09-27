import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_grandchildren(self):
        grandchild = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild])
        parent = ParentNode("div", [child_node])
        self.assertEqual(parent.to_html(),  "<div><span><b>grandchild</b></span></div>")
    
    def test_no_tag(self):
        parent = ParentNode(None, [LeafNode("b", "this is very bold")])
        with self.assertRaises(ValueError) as context:
            parent.to_html()
        self.assertEqual(str(context.exception), "Parent node should have a tag value")

    def test_no_children(self):
        node = ParentNode("div", [])
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "Parent node should have a children")

    def test_no_children(self):
        node = ParentNode("div", "")
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "Parent node should have a children")

        
    def test_with_props(self):
        leaf = LeafNode("a", "text", {"href": "google.com", "target": "blank"})
        node = ParentNode("p", [leaf])
        self.assertEqual(node.to_html(), '<p><a href="google.com" target="blank">text</a></p>')


    def test_repr(self):
        node = ParentNode("div", [LeafNode("b", "text")], {"href": "google.com", "tab": "notab"})
        self.assertEqual(node.__repr__(), "ParentNode(div, children: [LeafNode(b, text, None)], {'href': 'google.com', 'tab': 'notab'})")
        