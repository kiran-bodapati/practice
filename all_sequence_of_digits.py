#regular expression to find out all sequences of digits


import re
pattern_to_search=r"\d+"
string="""bodapatikiran06@gmail.com ,
THsi is my 4th program on re  module"""
def find_digits_sequence(pattern,string):
    # if re.finditer(pattern,string):
    #     iter_object
     List_of_pattern_occurrence=[]
     iter_object=re.finditer(pattern,string,re.MULTILINE)
     for object in iter_object:
          number=object.start()
          List_of_pattern_occurrence.append(number)
     return List_of_pattern_occurrence
          

result=find_digits_sequence(pattern_to_search,string)
print(result)



#another way
import re
pattern=r"[0-9]+"
string="THis is another way to solve the same problem, Iam taking an exaple numbers for this problem 42,4267,27,48"
def  second_way(pattern,string):
     match=re.finditer(pattern,string)
     #return match.start()
     #return match.span()
     list_of_matches=[]
     match_iter=re.finditer(pattern,string)
     for match in match_iter:
          list_of_matches.append(match.span())
     return list_of_matches


result=second_way(pattern,string)
print(result)
        
     

