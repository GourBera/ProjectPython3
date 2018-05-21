'''
Created on May 11, 2018

@author: berag
'''
import numpy
if __name__ == '__main__':
    pass


a = [1,2,3,4,5]
b = [1,2,3,4,5]

print(numpy.dot(a,b))   #(1*1)+(2*2)+......


a = [1,2]
b = [[2,4,6],
     [3,5,7]]

print(numpy.dot(a,b))

a = [[2,4,6],
     [3,5,7]]
b = [[8],
     [9],
     [10]]

print(numpy.dot(a,b))






