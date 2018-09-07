'''
Created on 07-Sep-2018

@author: Titan
'''

if __name__ == '__main__':
    pass

import multiprocessing
import time

def mul(lst):
    for i in lst:
        print(i*i)
        
def cube(lst):
    for i in lst:
        print(i*i*i)
        
lst = [2,3,4,5,6]

t = time.time()

p1 = multiprocessing.Process(target=mul(lst))
#p2 = p(target=cube, args=(lst,))

p1.start()
#p2.start()

p1.join()
#p2.join()

print("time taen: ", time.time() - t)






