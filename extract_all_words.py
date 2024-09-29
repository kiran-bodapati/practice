#regular expresiion to extract al words in a string

import re
pattern=r"\b\w+\b"
string_to_search="apples oranges apple banana watermelon lemon bananas lemons watermelons watermelon"
def extracat_all_words(pattern,string):
    words=re.findall(pattern,string,re.IGNORECASE)
    return words
result=(extracat_all_words(pattern,string_to_search))
print(result)
for word in result:
    count=result.count(word)
    print(f"{word} has occured {count} times in the string")
