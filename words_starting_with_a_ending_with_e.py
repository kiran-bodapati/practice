#regular expresssion to get aal words that start with 'a' and end with 'e'

import re 
pattern=re.compile(r"\ba\w+e\b")
string_to_match="""apples caanot be made to oranges and oranges cannot be made into apples an apple
an apple is an apple and an orange is an orange """

def words_startringwith_a_endingwith_e(pattern,string_to_match):
    iterator_object=re.finditer(pattern,string_to_match)
    list_of_objects=[]
    for object in iterator_object:
        list_of_objects.append(object)
    list_of_such_words=[]
    for objcet in list_of_objects:
        list_of_such_words.append(objcet.group())
    return list_of_such_words

words_list=words_startringwith_a_endingwith_e(pattern,string_to_match)
print(words_list)