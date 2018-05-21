'''
Created on May 4, 2018

@author: berag
'''

if __name__ == '__main__':
    pass
import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    runtime = time.clock() - start
    return result, runtime


print(time_execution("2 + 8 * 9"))

def add(a,b):
    return a +b

print(time_execution("add(5,6)"))


