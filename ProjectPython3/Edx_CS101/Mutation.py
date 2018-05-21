'''
Created on May 2, 2018

@author: berag

List is mutable

'''

if __name__ == '__main__':
    pass

'''
a = "Hello"
a[0] = 'Y'
print(a)
# TypeError: 'str' object does not support item assignment
'''


b = ['a', 'b', 'c', 'd', 'e']
print(b)
c = b
print(c)
b[1] = 'f'

print(b, ' ', c)








