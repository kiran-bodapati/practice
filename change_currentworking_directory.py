#change the current working directory

import os

current_directory=os.getcwd()              
print(current_directory)

new_directory=os.path.join(current_directory,"new_module_for_practicing.py")
print(new_directory)

os.makedirs("new_module_for_practicing.py",exist_ok=True)
#new_directory=os.path.join(current_directory,"new_module_for_practice")

os.chdir(new_directory)                 
changed_current_directory=os.getcwd()
print(changed_current_directory)

