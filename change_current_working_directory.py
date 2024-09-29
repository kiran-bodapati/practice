#change the current working directory to the directory specified by the user

import os
def change_the_workdir(working_dir,directory_to_get_into):
    
    return os.chdir(directory_to_get_into)

current_directory=os.getcwd()
print(f"current_directory is {current_directory}")
directory_to_get_into="/home/bsl025/Downloads/Downloads/my_Practice"
change_the_workdir(current_directory,directory_to_get_into)
print(f"changed directory is {os.getcwd()}")