#Write a Python program to get a list, sorted in increasing order by the last
#element in each tuple from a given list of non-empty tuples.

list= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def secondvalue(element):
    return element[1]
new_list=sorted(list,key=secondvalue)
print(new_list)
