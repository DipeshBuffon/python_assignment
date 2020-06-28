#Write a Python program to remove the nth index character from a nonempty string.
str=input("Enter a string:- ")
n=int(input("Enter the index to be removed:- "))
if(len(str)==0 or n+1>len(str)):
    print("Invalid input")
else:
    print(str[0:n]+str[n+1:])
