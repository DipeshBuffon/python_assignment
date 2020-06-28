#Write a Python program to insert a given string at the beginning of all items in
#a list.

s=[1,2,3,4]
x='emp'
new=[]
for i in s:
    new.append(x+str(i))

print(new)
