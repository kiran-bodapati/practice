#regular expression to get the last word  of  a sentence in the paragraph
 
import re
pattern=r"\b\w+\."
#pattern=r"\b[0-9a-zA-Z]\b"
string_to_match="""This is a string.This program tries to get the last word.It means the last \n word of every sentence"""
def word_at_theend_of_sentence(pattern,string):
    iterator_object=re.finditer(pattern,string)
    list_of_matches=[]
    for match in iterator_object:
        list_of_matches.append(match)
    return list_of_matches
results=word_at_theend_of_sentence(pattern,string_to_match)
print(results)
for result in results:
    Word_before_sentenceend=result.group()
    print(Word_before_sentenceend[0:-1])