#regiular expression to find all case-insensitive occurances of the word 'data' in a string

import re
patter=re.compile(r"\bdata\b",re.IGNORECASE)
string="This is string to find all the occurences of the word 'dATa' from this given string data"
def occurrence_of_data(pattern,string):
    All_occurences=re.findall(pattern,string)
    return All_occurences
result=occurrence_of_data(patter,string)
print(result)