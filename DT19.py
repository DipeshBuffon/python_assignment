#Write a Python program to smalelst item in a list.

n=int(input("Enter length of list:- "))
list=[]
for i in range(n):
    a=int(input("Enter numeric value for list:- "))
    list.append(a)

list.sort()
print(list[0])
