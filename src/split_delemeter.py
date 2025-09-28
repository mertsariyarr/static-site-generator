from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    final = []
    for nodes in old_nodes:
        if nodes.text_type != TextType.TEXT:
            final.append(nodes)
        else:
            if delimiter not in nodes.text:
                final.append(nodes)
                continue
            else:
                splited = nodes.text.split(delimiter)
                if len(splited) % 2 == 0:
                    raise Exception("No allowed inner markdowns")
                else:
                    for i in range(len(splited)):
                        if i % 2 == 0:
                            final.append(TextNode(splited[i], TextType.TEXT))
                        else:
                            final.append(TextNode(splited[i], text_type))
    return final

        
        

            
    
    
node = [TextNode("This is a *bold* and *verybold* text. and -this", TextType.TEXT)]





print(split_nodes_delimiter(node, "*", TextType.BOLD))