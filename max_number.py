print("enter the three numbers:")
a=input()
b=input()
c=input()

max=None
if a>b:
    max=a
else:
    max=b

if c>max:
    max=c


print(f"largest of the threee numbers is {max} ")
