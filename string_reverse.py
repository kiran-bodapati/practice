string="kiran"
def string_reverse(string):
    l1=[]
    
    for i in string:
        l1.append(i)
    print(l1)
    string2=""
    for i in range (len(l1)-1, -1,-1):
        # print(l1[i])
        string2+=l1[i]
        # print(l1[i])


    # result="".join(l1)
    # return result
    return string2





reversed_string=string_reverse(string)
print(f"final string is {reversed_string} {string}")
print("final result is", reversed_string,string)