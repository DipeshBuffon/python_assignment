#Write a Python program to check whether all dictionaries in a list are empty or
#not.

list=[{},{},{}]

print(all(not a for a in list))
