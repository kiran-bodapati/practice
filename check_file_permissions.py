#check if the user has read, write and executable permission for the file

import os


def check_file_permissions(file_name):
# print(os.access("absolute_or_relative_path.py",os.F_OK))
# print(os.access("absolute_or_relative_path.py",os.R_OK))
# print(os.access("absolute_or_relative_path.py",os.W_OK))
# print(os.access("absolute_or_relative_path.py",os.EX_OK))
#print(os.access("chcek_file_permissions",os.F_OK))
 if os.access("absolute_or_relative_path.py",os.F_OK):
     print(f"The file '{file_name}'  exits ")
 if os.access("absolute_or_relative_path.py",os.R_OK):
     print(f"The current user had the read permission for the '{file_name} file ")
 if os.access("absolute_or_relative_path.py",os.W_OK):
     print(f"The current user had the write permission for the '{file_name} file ")
 if os.access("absolute_or_relative_path.py",os.EX_OK):
    print(f"The current user had the excutable permission for the '{file_name} file ")


file="absolute_or_relative_path"
check_file_permissions(file)
