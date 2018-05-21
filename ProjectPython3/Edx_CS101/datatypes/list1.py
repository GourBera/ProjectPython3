'''
Created on May 3, 2018

@author: berag
'''

if __name__ == '__main__':
    pass


'''
lst1 = [1,2]
lst1.append(3)

lst2 = [5,6]
ad = lst1 + lst2

print(ad)
print(len(ad))

lst1.append(lst2)
print(lst1)
print(len(lst1))
'''
'''
lst = [1,2,3,4,5]

print(lst.index(1)) # Return 0
print(lst.index(5)) # Return 4
#print(lst.index(6)) # ValueError: 6 is not in list

print(5 in lst) # Return True
print(6 in lst) # Return False
'''

'''
def measure_udacity(lst):    
    c = 0
    for i in lst:
        if i[0] == "U":
            c+=1
    return c
        
print(measure_udacity(['Dave','Sebastian','mbrella']))
'''
'''
def find_element(lst, elm):
    
    for i in range(len(lst)):
        
        if lst[i] == elm:
            return i
    return -1  


print(find_element([1,2,3],3)) 
'''
'''
# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

def find_element(lst, elm):    
    if elm in lst:
        return lst.index(elm)
    return -1

print(find_element([1,2,3],3)) 
print(find_element(['alpha','beta'],'gamma'))
'''
'''
# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no 
# repeated elements.


def union(lst1, lst2):
    for i in lst2:
        if not i in lst1:
            lst1.append(i)



# To test, uncomment all lines 
# below except those beginning with >>>.

a = [1,2,3]
b = [2,4,6]
union(a,b)
print(a) 


#>>> [1,2,3,4,6]
print(b)
#>>> [2,4,6]
'''
'''
p = [1,0,1]

p[0] = p[0]+p[1]
p[1] = p[0]+p[2]
p[2] = p[0]+p[1]
print(p) # 123
'''
'''
# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(list_of_numbers):
    no = 1
    for i in list_of_numbers:
        no = no * i
    return no

print(product_list([9]))
#>>> 9
print(product_list([1,2,3,4]))
#>>> 24
print(product_list([]))
#>>> 1
'''
'''
# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest1(list_of_numbers):
    import math
    
    if len(list_of_numbers) == 0:
        return 0
    else:
        b = max(list_of_numbers)
        return b
        
def greatest(list_of_numbers):
    grt = 0    
    for i in list_of_numbers:
        if i > grt:
            grt = i
    return grt
        


print(greatest([4,23,1]))
#>>> 23
print(greatest([]))
#>>> 0
'''

# Suduku Game



