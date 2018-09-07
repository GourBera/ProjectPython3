'''
Created on 07-Sep-2018

@author: Titan
'''

if __name__ == '__main__':
    pass


import threading
import time


def mul(lst=[]):
    for i in lst:
        print(i*i)
        
def cube(lst=[]):
    for i in lst:
        print(i*i*i)
        
lst = [2,3,4,5,6]

t = time.time()

t1 = threading.Thread(target=mul, args=(lst,))
t2 = threading.Thread(target=cube, args=(lst,))

t1.start()
t2.start()

t1.join()
t2.join()

print("time taen: ", time.time() - t)