#To count total numbers of words in a sentence

string= input("Enter a sentence:- ")
list=string.split(' ')
count={}
for i in list:
    if i in count.keys():
        count[i]+=1
    else:
        count[i]=1
print(count)
