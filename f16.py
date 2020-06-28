#Write a Python program to square and cube every number in a given list of
#integers using Lambda.

lst=[1,2,4,6,10]

f=list(map(lambda x:(x*x,x**3),lst))
print(f)
