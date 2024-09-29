#convert the relative_path to absolute_path

import os

def convert_realpth_to_abspath(path):
    absolute_path=os.path.abspath(path)
    return absolute_path


path="dummy_folder/file1.txt"
result=convert_realpth_to_abspath(path)
print(result)