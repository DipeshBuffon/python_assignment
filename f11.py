#Write a Python program to create a lambda function that adds 15 to a given
#number passed in as an argument, also create a lambda function that multiplies
#argument x with argument y and print the result.

#add
a=int(input("Enter a number to be added:- "))

b=lambda a:a+15
print(b(a))


#multiply
x=int(input("Enter 1st number to be multiplied:- "))
y=int(input("Enter 2nd number to be multiplied:- "))
f=lambda x,y:x*y
print(f(x,y))
