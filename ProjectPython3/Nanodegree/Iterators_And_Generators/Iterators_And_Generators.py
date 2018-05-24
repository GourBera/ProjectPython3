'''
Created on May 24, 2018

@author: berag
'''

if __name__ == '__main__':
    pass

'''
x = [1,2,3,4]
b = list(enumerate(x))


def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1
        
for x in my_range(5):
    print(x)
'''
'''
# https://softwareengineering.stackexchange.com/questions/290231/when-should-i-use-a-generator-and-when-a-list-in-python/290235

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    count = start
    for element in iterable:
        yield count, element
        count += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
'''    
'''
If you have an iterable that is too large to fit in memory in full (e.g., when dealing with large files), being able to take and use chunks of it at a time can be very valuable.

Implement a generator function, chunker, that takes in an iterable and yields a chunk of a specified size at a time.

Calling the function like this:

for chunk in chunker(range(25), 4):
    print(list(chunk))
should output:

[0, 1, 2, 3]
[4, 5, 6, 7]
[8, 9, 10, 11]
[12, 13, 14, 15]
[16, 17, 18, 19]
[20, 21, 22, 23]
[24]
'''
# https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks

def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 5):
    print(list(chunk))    
    
'''
Generator Expressions
Here's a cool concept that combines generators and list comprehensions! You can actually create a generator in the same way 
you'd normally write a list comprehension, except with parentheses instead of square brackets. For example:
'''
sq_list = [x**2 for x in range(10)]  # this produces a list of squares

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares
print(sq_list)
print(sq_iterator)








































