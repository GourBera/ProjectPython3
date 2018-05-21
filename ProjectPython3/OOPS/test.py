'''
Created on Mar 6, 2018

@author: berag
'''
from pip._vendor.requests.packages.urllib3.connectionpool import xrange
from ctypes.test.test_pickling import name

if __name__ == '__main__':
    pass

'''

import os
print(dir(os))


'print til 9'
for i in range(0,10):   
    print(i) 
    
print('Second Progran')       

i = 0
while i<10:
    print(i)
    i=i+1

a=10
b=20

if a<b:
    print("{} is less then {}".format(a, b))
elif a==20:
    print("{} is equal then {}".format(a, b))
else:
    print("{} is greater then {}".format(a, b))
        

'list of all files inside particular folder'
import os, glob

os.chdir("C:/Users/berag/Desktop/")

for file in glob.glob("*.txt"):
    print(file)    


'Fizz Buzz'
for num in range(1,101):
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 ==0:
        print("Buzz")
    else:
        print(num)


'Fibonacci Sequence - 0,1,1,2,3,5,8,13,21,34'
a, b=0, 1
for i in xrange(0, 10):
    print(a)
    a, b=b, a+b
    
'Fibonacci Generator'

def fib(num):
    a,b = 0,1
    for i in xrange(0, num):
        yield "{}: {}".format(i+1, a)
        a, b = b, a+b
        
for item in fib(10):
    print(item)

'DataType'
'List'
Mlist = [10,20,30,40,50]
for i in Mlist:
    print(i)
    
print("Dict")
Mdict = {'name': 'Gour', 'age': '24', 'occupation': 'SE'}
for key,val in Mdict.items():
    print("My {} is {}".format(key, val))
    
print("Tuples")
Mtup = (1,2,3,4,5,6,7,8,9,10)
for i in Mtup:
    print(i) 
    
print("Set will print unique value")
Mset = {1,1,2,1,5,2,7,9,9,10}
for i in Mset:
    print(i) 


mylist = [1,2,3,4,5,6,7,8,9,10]
squares = [num*num for num in mylist]
print(squares)


class Person(object):
    def __init__ (self, name):
        self.name = name
        
    def reveal_identity(self):
        print("My name is {}".format(self.name))
        
class SeperHero(Person):
    def __init__ (self, name, hero_name):
        super(SeperHero, self).__init__(name)
        self.hero_name = hero_name
        
    def reveal_identity(self):        
        super(SeperHero, self).reveal_identity()
        print("... And I am {}".format(self.hero_name))
        

corey = Person('Corey')
corey.reveal_identity()

wade = SeperHero('ShaktiMan', 'Deadpool')
wade.reveal_identity()



l1 = [1,2,3,4]
l2 = l1
l2.append(5)
print(l1)
print(l2)


'Shallow copy - do not copy everything, create a separate memory location'
'Deepcopy - copy all reference, takes long time'
import copy

l1 = [1,2,3,4]
l3 = copy.copy(l1)
l2 = l1
l3.append(11)

print(l1)
print(l2)
print(l3)
'''
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4, 11]
'''

print(id(l1))
print(id(l2))
print(id(l3))
''' 
59749576
59749576
59749448
'''
    
l4 = copy.deepcopy(l2)
print(l4) 
'''
[1, 2, 3, 4]
'''
print(id(l4)) 
'''
59448968
'''



import multiprocessing
import threading





a, b = 10, 10
big = a if a > b else b
print(big)



class Myclass(object):
    def f(self):
        print("f()")
        

def monkey_f(self):
        print("monkey_f()")
        
x = Myclass()
x.f()

print("------------")

Myclass.f = monkey_f
obj = Myclass()
obj.f()

'it will print monkey_f()'



from random import shuffle
x = ['keep', 'the', 'blue', 'flag']
shuffle(x)
print(x)



'Integer String Short'

l1 = ['1','4','2','10','5']

import copy
l2 = copy.copy(l1)
l2.sort()
print(l2)

'Correct '
list = ['1','4','2','10','5']

l1 = [int(i) for i in list]
l1.sort()
print(l1)


list1 = ['1','4','2','10','5']
l3 = map(int, list1)
l3.sort()
print(l3)

from test import support

result = zip()
tuple1 = ['a','b','c','d','e','f','g','h']
tuple2 = ['1','2','3','4','5','6','7','8']
x =zip(tuple1, tuple2)

print(set(x))





numberList = [1, 2, 3]
strList = ['one', 'two', 'three']

result = zip(numberList, strList)


resultList = list(result)
print(resultList)
resultDict = dict(result)
print(resultList)
resultSet = set(result)
print(resultSet)

'# UnZip'
coordinate = ['x', 'y', 'z']
value = [3, 4, 5, 0, 9]

result = zip(coordinate, value)
resultList = list(result)
print(resultList)

c, v =  zip(*resultList)
print('c =', c)
print('v =', v)

'''


print('find length'.__len__())













