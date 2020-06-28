#check if string ends with 'ing' or not..and if not add 'ing' ant the end

string=input("Enter a string:- ")

if len(string)<3:
    print(string)
elif string.endswith('ing',-3):
    print(string+'ly')
else:
    print(string+'ing')
