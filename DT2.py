#To get strings made up of first and last two character of a string

string=input("Enter  a string:- ")

x=len(string)
if x<2:
    print('Empty String')
elif x==2:
    print (string*2)
else:
    print(string[0:2]+string[-2:])
