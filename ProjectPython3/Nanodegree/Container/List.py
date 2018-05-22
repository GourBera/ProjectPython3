'''
Created on May 22, 2018

@author: berag

#Operation or method
in
not in

len()
min()
max()
sorted()

mutable - its value can be changed
ordered - 


'''

if __name__ == '__main__':
    pass

lst = [1,5,4,9,2]
lst1 = ['a','b','c','d']
lst2 = ['a', 2, 'c', 4]
#print(lst[9])       #IndexError: list index out of range
print(lst[len(lst)-1]) # Last element
print(max(lst))
print(max(lst1))
#print(max(lst2))        #TypeError: '>' not supported between instances of 'int' and 'str'

print(' '.join(lst1))   

print('\n'.join(lst1))


a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))


a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == b)       #True
print(a is b)       #True
print(a == c)       #True
print(a is c)       #False

animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4], 'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}

print(animals['dogs'][3])   #15
#print(animals[3])           #KeyError: 3
print(animals['fish'])















