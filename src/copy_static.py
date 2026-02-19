import os
import shutil

def setup_docs(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)

def copy_static(src, dest):

    list_of_source = os.listdir(src)
    for item in list_of_source:
        child_source_path = os.path.join(src, item)
        print(child_source_path)
        child_destination_path = os.path.join(dest, item)
        print(child_destination_path)

        if os.path.isfile(child_source_path):
            shutil.copy(child_source_path, child_destination_path)
        else:
            os.mkdir(child_destination_path)
            copy_static(child_source_path, child_destination_path)

