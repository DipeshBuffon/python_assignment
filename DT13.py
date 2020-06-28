#comma seperated input and sorting them

w=input("Enter comma seperated words:- ").split(',')
l=[i for i in w]
l.sort()
print(','.join(l))
