import unittest
from markdown_to_html import *

class TestToMarkdownHtml(unittest.TestCase):
    #paragraphs test
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )
    #header test
    def test_header(self):
        md = """
# This is the header
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is the header</h1></div>"
        )
    #list test
    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, 
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",

        )
    #quote test
    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )
    #code test
    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

if __name__ == "__main__":
    unittest.main()