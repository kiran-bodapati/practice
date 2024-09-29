#listing files and folders in a directory

import os

print(os.getcwd())
(os.chdir('../../'))


#print(os.listdir(path))
files_and_folders_list=(os.walk(os.getcwd()))
for item in files_and_folders_list:
     print(item)