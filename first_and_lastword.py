#regular expression to get the first  and last word  in a  given string

import re
pattern=r"\w+"
string="Hello, THis is the  10th practice program on re  module"     #example string 
def first_and_lastword(pattern,string):
    iterator_object=re.finditer(pattern,string)
    list_of_matches=[]
    for match in iterator_object:
        list_of_matches.append(match)
    return list_of_matches                                              #returns the list of matches 


    


result=first_and_lastword(pattern,string)
print(result)
print(result[0].group())
length_of_list_of_matches=len(result)
print(result[-1].group())