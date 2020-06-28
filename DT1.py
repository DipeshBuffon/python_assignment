#To count total numbers of character in a string

string= input("Enter a string:- ")

count={}
for i in string:
    if i in count.keys():
        count[i]+=1
    else:
        count[i]=1
print(count)
