#To check if  a given string strats with Hello and ends with World


import re
#pattern=r"^\bHello\b.*\bworld\b$"
pattern=r"^\bHello\b.*\bworld\b$"
string="HelLo, this is a practice program on re module,WORLD"
def starts_ends_with(pattern,string):
  if re.findall(pattern,string,re.IGNORECASE):
     return f"The given string matches the crieteria "
  else:
     return f"The given string does not match  with the crieteria"
  

result=starts_ends_with(pattern,string)
print(result)