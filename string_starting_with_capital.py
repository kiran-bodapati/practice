#regukar expression to check if a string starts with a Capital letter

import re
pattern="^[A-Z]"
string_to_match="""THIS STRing is to check if THis starts with  a capital letter \n
It is a ,multiline string   \n
this line does not start with a capital letter \n"""
def check_string_starts_with_cap_letter(pattern,string_to_match):
   matches_iterator= re.finditer(pattern,string_to_match,re.MULTILINE)
   list_of_objects=[]
   for match in matches_iterator:
      list_of_objects.append(match)
   final_list=[]
   for object in list_of_objects:
      final_list.append(object.group())
   return final_list
      
      
   #return matches_iterator
    
result=check_string_starts_with_cap_letter(pattern,string_to_match)
print(result)