from htmlnode import HTMLNode



class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node should have a tag value")
        if self.children is None or len(self.children) == 0 or self.children == "":
            raise ValueError("Parent node should have a children")
        mystr = ""
        for child in self.children:
            mystr += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{mystr}</{self.tag}>"
            
        
            
        
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
        