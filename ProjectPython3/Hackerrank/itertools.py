'''
Created on 26-May-2018

@author: Titan
'''

if __name__ == '__main__':
    pass

from itertools import combinations_with_replacement
from itertools import combinations

'''
print(list(combinations_with_replacement('12345',2)))

A = [1,1,3,3,3]
print(list(combinations(A,2)))  
'''

s, no = input('prompt').split()
lst = []
for i in s:
    lst.append(i)
for i in combinations_with_replacement(lst, int(no)):
    print(''.join(i))





































