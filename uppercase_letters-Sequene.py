#regular expression for a sequence of uppercase letters

import re 
pattern=re.compile(r"[A-Z]+",re.M)
string="""HI, THIS iS a 5th pROGram
 on re MODULE"""
def sequence_of_uppercase(pattern,string):
       matches=re.findall(pattern,string)
       if matches:
              return matches
       else:
              return None
result=sequence_of_uppercase(pattern,string)
print(result)