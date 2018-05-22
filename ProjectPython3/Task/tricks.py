'''
Created on May 22, 2018

@author: berag
'''

if __name__ == '__main__':
    pass


import statistics as st

print(st.mean([1,2,5,9,4,3]))   #4
print(st.median([1,2,5,4]))     #3.0

print( 11//2)                   #5
print( 11.0//2)                 #5.0

print(.1 + .1 + .1)             # Not .3 its 0.30000000000000004
# https://docs.python.org/3/tutorial/floatingpoint.html
print(1/10)                     #0.1

print("I think you\'re Super Hero")
#print("String" / 2)             #TypeError: unsupported operand type(s) for /: 'str' and 'int'

import os
print (os.path.expanduser('~'))

import re
print(re.search(r"[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$","micheal.pages@mp.com"))

list = ['a', 'b', 'c', 'd', 'e']
print (list[10:])

'''
Here are a few PDB commands to start debugging Python code.

Add breakpoint – <b>
Resume execution – <c>
Step by step debugging – <s>
Move to next line – <n>
List source code – <l>
Print an expression – <p>

$ python -m pdb python-script.py
'''

'''
my_list = [1,2,3,4,5,6,7,8,10] # List of numbers 1 - 10

# Add your code below!
print(my_list[::2])
print(my_list[::3])

#Print Backward
print(my_list[::-2])
print(my_list[::-3])
#odd from the list
odds = my_list[::2]
print(odds)
#
middle_third = my_list[3:8]
print(middle_third)
'''
'''
allowed to pass functions around just as if they were variables or values.

lambda x: x % 3 == 0

def by_three(x):
  return x % 3 == 0

'''
'''
my_list = range(16)
b = filter(lambda x: x % 3 == 0, my_list)
for i in b:
    print(i)


languages = ["HTML", "JavaScript", "Python", "Ruby"]
# Add arguments to the filter()
b = filter(lambda x: x == "Python", languages)
for i in b:
    print(i)
    
'''
'''
Create a list, squares, between 1 to 10. 
Use filter() and a lambda expression to print out 
only the squares that are between 30 and 70 (inclusive).

'''
'''
squares = [x ** 2 for x in range(1, 11)]
b = filter(lambda x: x >= 30 and x <= 70, squares)
for i in b:
    print(i)
    
    
'''
'''
a list, threes_and_fives, 
that consists only of the numbers between 1 and 15 (inclusive) 
that are evenly divisible by 3 or 5.

'''
'''

threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]

for i in threes_and_fives:
    print(i)
    
'''
'''
str = "ABCDEFGHIJ"
start, end, stride = 1, 6, 2
print(str[start:end:stride])

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print(message)

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
b = filter(lambda x: x != "X", garbled)
for i in b:
    print(i)
    
print(5 >> 4)  # Right Shift
print(5 << 1)  # Left Shift
print(8 & 5)   # Bitwise AND
print(9 | 4)   # Bitwise OR
print(12 ^ 42) # Bitwise XOR
print(~88)     # Bitwise NOT

print(0b1)    #1
print(0b10)   #2
print(0b11)   #3
print(0b100)  #4
print(0b101)  #5
print(0b110)  #6
print(0b111)  #7
print("******")
print(0b1 + 0b11)
print(0b11 * 0b11)


print(bin(1))
print(bin(2))
print(bin(3))
print(bin(4))


print(int("1",2))
print(int("10",2))
print(int("111",2))
print(int("0b100",2))
print(int(bin(5),2))
# Print out the decimal equivalent of the binary 11001001.
print(int("11001001", 2))

shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right = shift_right >> 2
shift_left = shift_left << 2

print(bin(shift_right))
print(bin(shift_left))

'''
'''

In order to print a number in its binary representation, you can use the bin() function. bin() takes an integer as input and returns the binary representation of that integer in a string.
You can also represent numbers in base 8 and base 16 using the oct() and hex()
'''
