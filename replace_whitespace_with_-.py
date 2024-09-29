#regular expression to replace whitespace characters with '-'


import re
pattern=re.compile("\s")
print(pattern)
character_to_replace='-'
string_to_match="This is the 6th program in \n re module \s "
def replace_whitespace_hyphen(pattern,string_to_match):
    modified_string=re.sub(pattern,character_to_replace,string_to_match)
    return modified_string
result=replace_whitespace_hyphen(pattern,string_to_match)
print(result)