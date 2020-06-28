#WAP to calculate total nuber of upper and lower case in string:-

str=input("Enter a string:- ")

def cal(str):
    ucase=0
    lcase=0
    for i in str:
        if i.isupper():
            ucase+=1
        else:
            lcase+=1

    print("Upper case is :- {a} and lower case is {b}".format(a=ucase,b=lcase))

cal(str)
