#regular expression to extract date from a given string

import re 
pattern_to_found=r"\d{2}/\d{2}/\d{4}"
string_to_match="Today is 01/09/2024 Tomorrow is Pawan Klayan's birthday that is 02/09/2024"
def extract_data(pattern,string):
    iterator_object=re.finditer(pattern,string)
    
    list_of_matches=[]
    for match in iterator_object:
        list_of_matches.append(match)
    return list_of_matches
     





result=extract_data(pattern_to_found,string_to_match)
print(result)
for match in result:
# print(result[0].group())
# print(result[1].group())
   print(match.group())
   print(type(match.group()))
   print(match.group(0))