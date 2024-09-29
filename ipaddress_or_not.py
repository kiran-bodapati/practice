#regular expression to find out if a given string is a valid IP address or not

import re
#pattern=r"^[\d+\.\d+\.\d+\.\d+]$"
pattern=r"^(\d{2,}\.)"r"(\d{2,}\.)"r"(\d{2,}\.)"r"(\d{2,})$"
string="7.4f.423.211"
def validating_ip_address(pattern,string):
 if re.match(pattern,string):
    return f"The given string is a valid IP address"
 else:
    return f"The given string is not  a valid IP address"
 
result=validating_ip_address(pattern,string)
print(result)