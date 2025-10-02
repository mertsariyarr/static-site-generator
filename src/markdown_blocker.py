def markdown_to_blocks(markdown):
    mydown = markdown.split("\n\n")
    final = []

    for block in mydown:
        if block == '':
            continue
        final.append(block.strip())
    
    return final
    

md = """
This is **bolded** paragraph            

This is another paragraph with _italic_ text and `code` here   
This is the same paragraph on a new line


- This is a list
- with items
"""


print(markdown_to_blocks(md))

