#Write a Python program to sum all the items in a list.

list=[]
n=int(input("Enter length of list:- "))
for i in range(n):
    a=int(input("Enter numeric value for list:- "))
    list.append(a)
sum=0
for i in range(len(list)):
    sum+=list[i]

print(sum)
