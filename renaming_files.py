#renaming all files in a directory by adding '_backup' to their names

import os

def rename_files_folders(current_working_directory):
    tuples_of_files=[]
    list_of_file_names_without_extension=[]
    for file in os.listdir(current_working_directory):
        print(file)
        tuple=os.path.splitext(file)
        tuples_of_files.append(tuple)
    print(tuples_of_files)
    for tuple in tuples_of_files:
        list_of_file_names_without_extension.append(tuple[0])
    print(list_of_file_names_without_extension)
    for file in list_of_file_names_without_extension:
        os.rename(f"{file}.py",f"{file}_backup.py")

rename_files_folders(os.getcwd())