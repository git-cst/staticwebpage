from textnode import *
from htmlnode import *
from inline_markdown import *
from provision_files import *
from webpage_generator import *
import os; import shutil

def extract_title(markdown):
    pass

def main():
    if os.path.exists('/home/csteenberg/projects/github.com/git-cst/static_web/public'):
        shutil.rmtree('/home/csteenberg/projects/github.com/git-cst/static_web/public')
    copy_files(source='/home/csteenberg/projects/github.com/git-cst/static_web/static', destination='/home/csteenberg/projects/github.com/git-cst/static_web/public')

    generate_page_recursively(from_path='/home/csteenberg/projects/github.com/git-cst/static_web/content', template_path='/home/csteenberg/projects/github.com/git-cst/static_web/template.html', dest_path='/home/csteenberg/projects/github.com/git-cst/static_web/public')

main()
