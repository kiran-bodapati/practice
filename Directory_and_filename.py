#print directory and filename from  a given path

import os



def directory_and_filename(file_path):
#
  filename=os.path.basename(file_path)
  dir_name=os.path.dirname(file_path)
  print(os.path.dirname(dir_name))
  directory_name=os.path.basename(dir_name)
  return filename,directory_name



file_path="/home/bsl025/Downloads/Downloads/my_Practice/os_module/renaming_files.py"
print(directory_and_filename(file_path))
