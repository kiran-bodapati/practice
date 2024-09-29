#regular expression to remove non-alphanumeric characters in a string

import re
pattern=r"[^0-9a-zA-Z]+"
replacing_character=""
string="""THIS program tries to remove non-alphanumeric characters from a 
this  string, this is 12_th-program that Iam practicing on the re module , _+%  """

def remove_alphanumeric_characters(pattern,replacing_character,string):
    final_string=re.sub(pattern,replacing_character,string)
    #list_of_matching_objects=[]
    # for match in iterator_object:
    #     list_of_matching_objects.append(match)
    # print(list_of_matching_objects)
    # if list_of_matching_objects:
    #     for object in list_of_matching_objects:
    #         final_string=string.replace(object.group(),"")
    #     return final_string
    # else:
    #     return string
    return final_string
        
final_string=remove_alphanumeric_characters(pattern,replacing_character,string)
print(final_string)