#check if the given path is absolute or relative path
import os


def absolute_or_relative_path(working_directory):
    if os.path.isabs(working_directory):
        return "absolutepath"
    else:
        return "realpath"
    




current_directory=os.getcwd()
result=absolute_or_relative_path(current_directory)
print(result)





