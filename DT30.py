#Write a Python script to check whether a given key already exists in a dictionary.

d={1:1,2:4,3:9,4:16,5:25}

x=int(input("Enter the key to be checked:- "))

if x in d:
    print("Key is present in dictionary!!!")
else:
    print("Key is not present in dictionary!!!")
