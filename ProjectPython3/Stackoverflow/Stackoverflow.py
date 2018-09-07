'''
Created on 18-Jul-2018

@author: Titan
'''

if __name__ == '__main__':
    pass

import copy

meteo = open('meteo.txt', 'r+')
meteo.seek(0, 0)
ar = []
a=True
x=0

#print(meteo.read())



for i in meteo.read():
    print(i)

'''

while a:
    com=[meteo.readline(), meteo.readline(), meteo.readline()]
    ar.append(com)
    
    print(id(ar))
    print(id(com))
    
    #ar = copy.deepcopy(com)
    print(ar[x], '___', com)
    com.clear()
    print('--------------------')
    print(ar[x][:])
    if ar[x][:] == '':
        a=False
    x=x+1
    
'''    

'''
#print(meteo.readline())

com=[meteo.readline(), meteo.readline(), meteo.readline()]
ar = copy.deepcopy(com)
print(ar)
print(ar[x], '___', com)
com.clear()
print(ar[x][:], '___', com)
'''