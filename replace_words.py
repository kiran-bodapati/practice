#tregiular expression to replace all occurences of apple with orange

import re
pattern=r"apple"
word_to_replace_with="orange"
string_to_match="A shopkeeper has 10 oranges and 50 apples , but he wants to make his stock eevn by getting 50 more oranges and 10 more apples"
def replace_apple_with_orange(pattern,word_to_replace_with,string_to_match):
    final_string=re.sub(pattern,word_to_replace_with,string_to_match)
    return final_string
    
final_string=replace_apple_with_orange(pattern,word_to_replace_with,string_to_match)
print(final_string)