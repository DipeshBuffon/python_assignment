#Swap 1st two letters

str1=input("Enter 1st string:- ")
str2=input("Enter 2nd string:- ")

if len(str1)<2 or len(str2)<2:
    print("Invalid input")
else:
    print(str2[0:2]+str1[2:]+' '+str1[0:2]+str2[2:])
