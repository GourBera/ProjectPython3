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
