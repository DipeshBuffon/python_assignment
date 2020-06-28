#Write a Python function to insert a string in the middle of a string.
str=input("Enter a string:- ")
sym=input("Enter the symbol in which string is to be inserted:- ")\

def insert_string_middle(sym,str):
    print(sym[:2]+str+sym[2:])

insert_string_middle(sym,str)
