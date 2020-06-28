#WAP in python function to check whether the given number is in range or not.

n=int(input("Enter a number:- "))
r=int(input("enter the end of range:- "))

def check(n,r):
    if n in range(r+1):
        print('found')
    else:
        print("not found")

check(n,r)
