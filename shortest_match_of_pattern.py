#regular expression to find shortest match of a pattern

import re 
pattern=r"<.?>"
string="<div><span><a><div>"
def shortest_match_of_pattern(pattern,string):
    match=re.search(pattern,string)
    return match
result=shortest_match_of_pattern(pattern,string)
print(result)