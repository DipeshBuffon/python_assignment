#Write a Python function to create the HTML string with tags around the word(s).
str=input("Enter a string:-  ")
tag=input("Enter the  tag to be implemented:- ")

def add_tags(a,b):
    print('<'+a+'>'+b+'</'+a+'>')

add_tags(tag,str)
