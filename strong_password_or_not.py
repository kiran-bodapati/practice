#regular expreesiion to check if the given password is strong or not

import re
pattern=r"^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*[#$@^&*]).{8,}$"                                 #must conatin one uppercase character,one lowercase character, one digit,one special character
string="Gw9abcD&"
def vaild_password_or_not(pattern,string):
    if re.match(pattern,string):
        return f"The entered string  is  a strong password"
    else:
        return f"The given string is not a strong password"
    
print(vaild_password_or_not(pattern,string))