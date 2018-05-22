'''
Created on May 21, 2018

@author: berag
'''

str = "This is sample string"
print(str.count("is",0,len(str)))   

print("-----------------")

for i in range(0,10,2):
    print(i)
    
lst = ["fisrt", "middle", "last"]
ptrn = ", "
print(ptrn.join(lst))


'''
Created on Mar 19, 2018

@author: berag
'''
from pydoc_data.topics import topics
from pip._vendor.requests import packages
import keyword
import os
import sys
from timeit import Timer


'''
import os
print(os.system("pwd"))


print(topics)
print(packages)
print(keyword)
print(dir())
print(dir(__builtins__))
print(help())



x=10
y="test"
print(x,y)

print(os.system("cls"))


if os.name == 'nt':
    os.system("cls")
else:
    os.system("clear")
    
    


print("this is output")
sys.stderr.write("error msg \n")
data = input("enter data")
print(data)


#0-stdin
#2-stderr

tuple = (1,5,8,4,6,4,2,4)
print(tuple.count(4))


def add(a,b):    
    return a+b

dir(Timer)
print(Timer('a,b=b,a',"a=10;b=20").timeit())
print(Timer('add(a,b)','a=10;b=20').timeit())


import pprint

nest =['roo1',['gour','bera'],['560093','krishnappa garden']]

print(nest)
pprint.pprint(nest, width=50)


a,b,c,d=10,20,30,40

def A():
    a,b,c=100,200,300
    print("In A ", a,b,c,d)
    def B():
        a,b=1000,2000
        print("In B ", a,b,c,d)
        def C():
            a=10000
            print("In C ", a,b,c,d)
            
            C()
    B()
A()


print("In__main__",a,b,c,d)


#default argument
def sum(a=0,b=0,c=0,d=0,e=0):
    print(a+b+c+d+e)
    
sum()
sum(10)
sum(10,20)
sum(10,20,30)
sum(10,20,30,40)
sum(10,20,30,40,50)


def callByValue(a,b):
    a,b=b,a
    print("a is: ", a)
    print("b is: ", b)
    
a=10
b=20
callByValue(a, b)



def Fact(n):
    if n==0:
        return 1
    return n*Fact(n-1)

print(Fact(7))



x=100
def fun(a,b):
    global x
    print(a+b+x)
    x=150
    
#fun(10,20)
#print(x)



lst = [10,20]
fun(lst)
print(fun)
'''

class date():
    "Example class of + operator ==> __add__"
    def __init__(self):
        self.dd=22
        self.mm=3
        self.yy=2018
        
    def display(self):
        print(self.dd,self.mm,self.yy)
        
    def __add__(self,days):
        self.dd+=days
        return(self)
    
    def __sub__(self,day):
        self.dd-=day
        return(self)
    
    
today=date()
today.display()
print(dir(today))
tomorrow=today+1
tomorrow.display()
yesterday = today-1
yesterday.display()
        
        
'''
Created on Apr 12, 2018

@author: berag
'''


'''
triple = lambda x: x * 3
add = lambda x, y: x + y
print(add(triple(3), 4))

def countdown():
  i=5
  while i > 0:
    yield i
    i -= 1
    
for i in countdown():
  print(i)

def make_word():
    word = ""
    for ch in "spam":
        word +=ch
        yield word

print(list(make_word()))

def sum_to(x):
    return x + sum_to(x-1)
print(sum_to(5))

def fib(x):
  if x == 0 or x == 1:
    return 1
  else: 
    return fib(x-1) + fib(x-2)
print(fib(4))

a = {1, 2, 3}
b = {0, 3, 4, 5}
print(a & b)

from itertools import product
a={1, 2}
print(len(list(product(range(3), a))))

nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x: x > 1, nums)
print(len(list(nums)))

def power(x, y):
    
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)

print(power(2, 3))

a, b, c, d, *e, f, g = range(20)
print(len(e))

for i in range(10):
   if i > 5:
      print(i)
      break
else:
   print("7")

try:
  print(1)
  print(1 + "1" == 2)
  print(2)
except TypeError:
  print(3)
else:
  print(4)

def func(**kwargs):
    print(kwargs["zero"])

func(a = 0, zero = 8)

for i in range(10):
    try:
        if 10 / i == 2.0:
            break
    except ZeroDivisionError:
        print(1)
    else:
        print(2)
'''


str = '2018-04-15T13:42:20+0000'

print(str[0:10] + ' ' + str[11:19])
        

'''
list = ['a', 'b', 'c', 'd', 'e']
print(list[10:]) #Empty list
print(list[:10]) 
'''
list = [['0'],['1'],['2'],['3']] *5
print(list)
list[0].append(10)
list[1].append(20)
list[2].append(30)
list[3].append(40)
list[4].append(70)
list[5].append(80)
list.append(50)
list.append(60)
print(list)


d = { 
  "name": "Eric",
  "age": 26
}

for key in d:
  print(key, d[key])

for letter in "Eric":
  print(letter) 












        
        
        
        
        
        
        
        
        
        
        
        
        
        













