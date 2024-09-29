#regualar expression to find all multine commnets in  a code

import re
pattern=re.compile(r"#\w+",re.MULTILINE)
string="""#example_word_1         
example #example_word_2
 another example #example_word_3"""
"""This is a program to find the multiline commnets"""

def multiline_commnets(pattern,string):
    occurences=re.findall(pattern,string)
    return occurences
result=multiline_commnets(pattern,string)
print(result)