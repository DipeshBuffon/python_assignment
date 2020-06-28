#even number of list

l=[1,4,3,9,80,77,50,2]

def check(l):
    print("Even numbers are:- ")
    for i in l:
        if i%2==0:
            print(i)

check(l)
