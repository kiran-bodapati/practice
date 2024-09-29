#regular expression to get all the hashtags from  a social media post

import re
pattern=r"#\w+"
pattern=r"\b#.+\b"
string="Why #OrvillePeck is the unconventional Best New Artist pick the #Grammys need  http://blbrd.cm/cStCkmr"
def hashtags(pattern,string):
    matches_object=re.search(pattern,string)
    return matches_object
print(hashtags(pattern,string))