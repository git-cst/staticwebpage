import os; import shutil

def copy_files(source, destination):
    current_filetree = os.listdir(source)

    if not os.path.exists(destination):
        os.mkdir(destination)

    for node in current_filetree:
        full_path = os.path.join(source, node)
        
        if os.path.isdir(full_path):
            copy_files(full_path, destination + "/" + node)

        if os.path.isfile(full_path):
            shutil.copy(full_path, destination)