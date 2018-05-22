'''
Created on May 22, 2018

@author: berag


Immutable
Ordered


'''

if __name__ == '__main__':
    pass



tuple_a = 1, 2
tuple_b = (1, 2)

print(tuple_a == tuple_b)   # True
print(tuple_a[1])       #
print(type(tuple_a))    #Tuple



a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop()     #remove the first item

print(a, '\n', b)