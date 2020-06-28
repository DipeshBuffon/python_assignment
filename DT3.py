#change occurance of first character to $

string=input("Enter a string:- ")
i=0
x=string[0]
if x in string[1:]:
    print(x+string.replace(x,'$')[1:])
else:
    print(string)
