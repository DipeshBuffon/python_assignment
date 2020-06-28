#Write a Python program to find intersection of two given arrays using
#Lambda.

a=[1,5,6,4,9]
b=[2,0,9,44,1]

f = list(filter(lambda x: x in a, b))
print(f)
