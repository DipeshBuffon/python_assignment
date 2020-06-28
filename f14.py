#Write a Python program to sort a list of dictionaries using Lambda.

list=[{'name':'Dipesh','age':18},{'name':"Ayush",'age':22},{'name':"Bobby",'age':10}]

sort_list=sorted(list,key=lambda l:l['name'])
print(sort_list)
