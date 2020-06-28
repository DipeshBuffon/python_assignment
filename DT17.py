#Write a Python program to multiply all the items in a list.

n=int(input("Enter length of list:- "))
list=[]
for i in range(n):
    a=int(input("Enter numeric value for list:- "))
    list.append(a)
product=1
for i in range(len(list)):
    product*=list[i]

print(product)
