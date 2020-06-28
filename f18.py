#Write a Python program to check whether a given string is number or not
#using Lambda.
a=10
b='Dipesh'

f=lambda x:"{} is number".format(x) if type(x)==int else "{} is a string".format(x)

print(f(a))
print(f(b))
