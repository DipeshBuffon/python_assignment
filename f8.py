#Write a Python function that takes a list and returns a new list with unique
#elements of the first list.

list=[1,2,3,1,1,2,4,4,4,4,4,5,3,2,5]

def change(l):
    return(set(l))

new_list=[*change(list)]
print(new_list)
