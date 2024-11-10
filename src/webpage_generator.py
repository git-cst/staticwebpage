import os
from markdown_blocks import *

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    with open(from_path, 'r') as source_file:
        source_data = source_file.read()

    with open(template_path, 'r') as template_file:
        template_data = template_file.read()

    source_as_html = markdown_to_html_node(source_data).to_html()
    source_title = extract_title(source_data)

    destination_data = template_data.replace('{{ Title }}', source_title).replace('{{ Content }}', source_as_html)


    with open(dest_path, 'w+') as destination_file:
        for line in destination_data:
            destination_file.write(line)

def generate_page_recursively(from_path, template_path, dest_path):
    current_filetree = os.listdir(from_path)

    if not os.path.exists(dest_path):
        os.mkdir(dest_path)

    for node in current_filetree:
        full_path = os.path.join(from_path, node)

        if os.path.isfile(full_path):
            generate_page(full_path, template_path, dest_path + "/" + node.replace(".md", ".html"))
        
        if os.path.isdir(full_path):
           generate_page_recursively(full_path, template_path, dest_path + "/" + node)