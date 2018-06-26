'''
Created on Apr 2, 2018

@author: berag
'''

dict = {}
print(dict)

dict.setdefault('key', 0)
print(dict)

dict = {'key1': 10, 'key2':20, 'key3':30, 'key4':40, 'key5':50}
print(dict)

dict['key6'] = 60

print(dict)

print(dict.values())

b = dict.copy()
print(b)

print(dict.fromkeys('key1'))

print(dict.get('key1'))

print(dict.items())

print(dict.keys())

dict.pop('key1')
print(dict)

dict.popitem()
print(dict)

dict.clear()
print(dict)







