#regular expression to replace multiple spaces with a single space

import re
pattern=r"\s+"
replacing_string=" "
string_to_match="""THis    is  a program to               replace multiple spaces with a single space,
THis is the      second line of           the string     """
def replace_multiple_sapace_with_single(pattern,replacing_string,string_to_match):
    final_string=re.sub(pattern,replacing_string,string_to_match)
    return final_string
final_string=replace_multiple_sapace_with_single(pattern,replacing_string,string_to_match)
print(final_string)