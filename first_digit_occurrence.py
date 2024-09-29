#A regular expression that seraches for the first occurence of the digit and and prints its position

import re
#pattern=r"[0-9]"
pattern=r"\d"

string="kirankumar.bodapati06@gmail.com" 
def first_digit(pattern_to_find,given_string):
    #match=re.match(pattern_to_find,given_string)
    #print(type(iterator_object))
    # for match in iterator_object:
    #      print(match)
    #print(iterator_object.start)
    #match=re.search(pattern_to_find,given_string)
    match=re.search(pattern_to_find,given_string)
    #print(match.start())
    print(match)
    print(match.start())
    print(match.span())
    print(match.end())

first_digit(pattern,string)

