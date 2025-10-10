import os
from markdown_to_html import  markdown_to_html_node


markdown_file_path = "/home/mert/static-site-generator/content/index.md"
template_file_path = "/home/mert/static-site-generator/template.html"
dest_path = "/home/mert/static-site-generator/public/index.html"

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:]
    raise Exception("there is no header!")




def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as r:
        md = r.read()  
    with open(template_path) as r:
        my_template = r.read()
    my_md = markdown_to_html_node(md).to_html()
    my_title = extract_title(md)
    new_content = my_template.replace("Content", my_md).replace("Title", my_title)
    with open(dest_path, "w") as f:
        f.write(new_content)
    
    


 
if __name__ == "__main__":
    generate_page(markdown_file_path, template_file_path, dest_path)