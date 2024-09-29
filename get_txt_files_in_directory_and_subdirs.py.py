#get the '.txt' files in directory and subdirectories

import os

def get_txt_files_incl_subdirs(working_directory):
    generator_object=os.walk(working_directory)
    list1=[]
    for item in generator_object:
        print(item)
        for file in item[2]:
            if file.endswith("txt"):
                list1.append(file)


    #     if not os.path.isdir(item):
    #         if item.endswith(".txt"):
    #             list1.append(item)
    #     else:
    #         sub_directory=os.path.dirname(item)
    #         for file in sub_directory:
    #             if file.endswith('.txt'):
    #                 print(file)
    #                 list1.append(file)

    return  list1
        








current_directory=os.getcwd()
print(f"current_directory is {current_directory}")
print(get_txt_files_incl_subdirs(current_directory))