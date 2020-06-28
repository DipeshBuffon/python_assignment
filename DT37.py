#Write a Python program to multiply all the items in a dictionary.

d={'A':5, 'B':11, 'C':3, 'D':8}

p=1
for i in d:
    p*=d[i]
print('Product is:- {}'.format(p))
