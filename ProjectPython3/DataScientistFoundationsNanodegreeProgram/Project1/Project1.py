'''
Created on 03-Jun-2018

@author: Titan
'''

if __name__ == '__main__':
    pass

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

print(CITY_DATA)

x = lambda x: x in CITY_DATA.keys()
lst = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print("You can choose from {}".format(lst))


for _ in range(5):
    inp = input('Enter')
    print(inp.capitalize())


a = ['a','b','c','d','i']
b = ['e','f','g','h']

dct = {}
for x,y in zip(a,b):
    dct[x]=y
    
print(dct)


dct1={}
for x,y in enumerate(b):
    dct1[x]= y

print(dct1)


x,y,z = map(int, "1 2 3".split())
print(x,y,z)

x,y,z = map(float, "1 2 3".split())
print(x,y,z)

a = [1,1,2,2,3,3]
print(tuple(a))
print(set(a))


#print(tuple(a).__add__(4))  TypeError: can only concatenate tuple (not "int") to tuple
print(set(a).add(4))

months = ['january', 'february', 'march', 'april', 'may', 'june']
month = months.index('may') + 1

print(month)


import time
print(time.time())


