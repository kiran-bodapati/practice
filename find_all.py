# import re

# #Return a list containing every occurrence of "ai":

# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)


# import re
# string_to_search="re"
# string1="Hello , Welcome to re module , this is my first practic eprogram on re module"
# re_occurences=re.findall(string_to_search,string1)
# print(re_occurences)


import re 
string1="Python has been introduced in 1990s.REcently it has been booming in terms of its usage beacause of the easy syntax and shortness.Python has many in-built packages as well"
string_to_match="Python"
python_occurrence=re.findall(string_to_match,string1)
print(python_occurrence)