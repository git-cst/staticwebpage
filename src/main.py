from textnode import *
from htmlnode import *
from inline_markdown import *
import os

def copy_to_public(destination_folder):
    #CLEAN UP DESTINATION FOLDER
    files_in_destination = os.listdir(destination_folder)
    if len(files_in_destination) > 0:
        for file in files_in_destination:
            os.remove(rf'{destination_folder}/{file}')

def get_files_to_copy(directory):
    list_of_files = []

    files_in_destination = os.listdir(directory)

def main():
    copy_to_public('./public')

main()
