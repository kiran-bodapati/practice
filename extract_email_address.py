#regular expression to extract all email addresses in a string


import re
pattern=re.compile(r"\w+@\w+\.\w+")
string=" fisrt mail is kirankumarbodpato@gmail.com   and the second one is \n   third and the 4th are  bodapatikiran06@gmail+com,xyz@yahoo.org"
def extract_emails(pattern,string):
    emails=re.findall(pattern,string)
    return emails
results=extract_emails(pattern,string)
for result  in results:
    print(result)