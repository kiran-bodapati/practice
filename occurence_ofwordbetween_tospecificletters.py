#regular expression to match all occurenecs of  a word between 2 specific characters

import re
pattern=r"\ba\w*s\b"
string_to_match="dpplesoranges mangoes mangoes dappleed fppleg efxrappleskygcu apples"
def match_word_between2specificcharacters(pattern,string_to_match):
    matches=re.findall(pattern,string_to_match)
    if matches:
        return f"The string conatins the given pattern",matches
    else:
        return f"The string does not conatin the given pattern"
    
result=match_word_between2specificcharacters(pattern,string_to_match)
print(result)
# print(len(result))
# print(result[1])
# a=result[1]
# if len(result)>1:
#     for match in a:
#         print(match)