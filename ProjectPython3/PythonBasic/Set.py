'''
Created on Apr 9, 2018

@author: berag
'''

'''
Different Python Set Methods

add()     Add an element to a set
clear()     Remove all elements form a set
copy()     Return a shallow copy of a set
difference()     Return the difference of two or more sets as a new set
difference_update()     Remove all elements of another set from this set
discard()     Remove an element from set if it is a member. (Do nothing if the element is not in set)
intersection()     Return the intersection of two sets as a new set
intersection_update()     Update the set with the intersection of itself and another
isdisjoint()     Return True if two sets have a null intersection
issubset()     Return True if another set contains this set
issuperset()     Return True if this set contains another set
pop()     Remove and return an arbitary set element. Raise KeyError if the set is empty
remove()     Remove an element from a set. If the element is not a member, raise a KeyError
symmetric_difference()     Return the symmetric difference of two sets as a new set
symmetric_difference_update()     Update a set with the symmetric difference of itself and another
union()     Return the union of sets in a new set
update()     Update a set with the union of itself and others
'''
'''
Other Set Operations

# initialize my_set
my_set = set("apple")

# check if 'a' is present
# Output: True
print('a' in my_set)

# check if 'p' is present
# Output: False
print('p' not in my_set)

for letter in set("apple"):
    print(letter)

'''
'''
Built-in Functions with Set

all()     Return True if all elements of the set are true (or if the set is empty).
any()     Return True if any element of the set is true. If the set is empty, return False.
enumerate()     Return an enumerate object. It contains the index and value of all the items of set as a pair.
len()     Return the length (the number of items) in the set.
max()     Return the largest item in the set.
min()     Return the smallest item in the set.
sorted()     Return a new sorted list from elements in the set(does not sort the set itself).
sum()     Retrun the sum of all elements in the set.

'''
'''
Python Frozenset

Frozensets can be created using the function frozenset().

This datatype supports methods like copy(), difference(), intersection(), isdisjoint(), issubset(), issuperset(), symmetric_difference() and union(). Being immutable it does not have method that add or remove elements.
'''

# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

A.isdisjoint(B)
False
A.difference(B)
frozenset({1, 2})
A | B
frozenset({1, 2, 3, 4, 5, 6})
A.add(3)



setvar = {1, 2, 3, 4, 5, 6, 7, 7, 7}
print(setvar)

# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

my_set.add(2)
print(my_set)

# add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2, 3, 4])
print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4, 5], {1, 6, 8})
print(my_set)

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element
# not present in my_set
# If you uncomment line 27,
# you will get an error.
# Output: KeyError: 2

# my_set.remove(2)
# initialize my_set
# Output: set of unique elements
my_set = set("HelloWorld")
print(my_set)

# pop an element
# Output: random element
print(my_set.pop())

# pop another element
# Output: random element
my_set.pop()
print(my_set)

# clear my_set
# Output: set()
my_set.clear()
print(my_set)

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)

# use union function
A.union(B)
{1, 2, 3, 4, 5, 6, 7, 8}

# use union function on B
B.union(A)
{1, 2, 3, 4, 5, 6, 7, 8}

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use & operator
# Output: {4, 5}
print(A & B)

# use intersection function on A
A.intersection(B)
{4, 5}

# use intersection function on B
B.intersection(A)
{4, 5}

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A
# Output: {1, 2, 3}
print(A - B)

# use difference function on A
A.difference(B)
{1, 2, 3}

# use - operator on B
B - A
{8, 6, 7}

# use difference function on B
B.difference(A)
{8, 6, 7}

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)

# use symmetric_difference function on A
A.symmetric_difference(B)
{1, 2, 3, 6, 7, 8}

# use symmetric_difference function on B
B.symmetric_difference(A)
{1, 2, 3, 6, 7, 8}

