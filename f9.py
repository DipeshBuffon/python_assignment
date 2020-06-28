#Prime or not

n=int(input("Enter a number to be checked:- "))

def check(n):
    for i in range(2,n):
        if n%i==0:
            print("Not prime")
            break
    else:
        print("prime")

check(n)
