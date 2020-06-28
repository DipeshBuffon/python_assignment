#Write a Python program to find if a given string starts with a given character
#using Lambda.

str=input("Enter a string:- ")

x=input("ENter a character:- ")


f = lambda a:"Starts with {}".format(x) if str.startswith(x) else "Doesn't start"

print(f(str))
