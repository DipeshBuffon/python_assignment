#Write a Python program to filter a list of integers using Lambda.

lst=[1,2.2,3,4.5,3.99,155]

x= list(filter(lambda l:int(l),lst))
print(x)
