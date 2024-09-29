#regular expression to match a string that contains three or more consecutive vowels 


import re 
pattern=r"[aeiou]{3,}"
string_to_match="HI, this program is to check if this striiing contains thtree or more consecutive vowels"

def three_or_more_vowels(pattern,string):
    match=re.search(pattern,string)
    if match:
        return f"the string contains three or more vowels"
    else:
        return f"the string  does not contaian three or more vowels"
print(three_or_more_vowels(pattern,string_to_match))