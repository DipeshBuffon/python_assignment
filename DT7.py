#Write a Python function that takes a list of words and returns the length of the longest one.

n=int(input("Enter a number:- "))
list=[]
for i in range(n):
    str=input("Enter string:- ")
    list.append(str)

list.sort(key=len)
print(list[-1])
