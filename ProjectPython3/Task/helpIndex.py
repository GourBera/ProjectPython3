'''
Created on 04-May-2018

@author: Titan

sys.__doc__


glob
For filename expansion
socket
For network connections and Inter-Process Communication (IPC)
threading , _thread , queue
For running and synchronizing concurrent threads
time , timeit
For accessing system time details
subprocess , multiprocessing
For launching and controlling parallel processes
signal , select , shutil , tempfile , and others
For various other system-related tasks
'''

import os
os.environ['foo'] = 'bar'
print(os.environ['foo'])



c = dict(name='Tom', age=50, job=None, pay=0)
import this as t
print(t)

print(help(max))
# in Shell - ?max

    

'''
len([])
c.copy()
round(number)
map()
hash(obj)
max(iterable, *)
enumerate
'''
'''------STRING --------
str = "This is String"
str.capitalize()
str.split(sep, maxsplit)
str.splitlines(keepends)
str.startswith(prefix)
str.swapcase()
str.title()
str.zfill(width)
str.translate(table)
str.count(sub)
str.find(sub)
str.rfind(sub)
str.join(iterable)
str.lower()
str.upper()
str.index(sub)
str.rindex(sub)
str.replace(old, new, count)
str.lstrip(chars)
str.rstrip(chars)
str.isalnum()
str.isalpha()
str.isdecimal()
str.isdigit()
str.isidentifier()
str.isnumeric()
str.islower()
str.isupper()
str.isprintable()
str.isspace()
str.maketrans(x, y, z)
str.partition(sep)
str.strip(chars)
'''

''' --------LIST-------------
lst = []
l = list(1,2,3)
lst.insert(index, object)
lst.append(object)
lst.count(value)
lst.index(value, start, stop)
lst.reverse()
lst.sort()
lst.pop(index)
lst.remove(value)
lst.clear()

'-'.join(list)

'''
'''-----------DICTIONARY-----------
dct = {}
dct = dict()

dct.get(key, default)
dct.items()
dct.keys()
dct.values()
dct.pop(k)
dct.popitem()
dct.update()
dct.fromkeys(type, iterable, value)

len(dct)
'''
'''-----TUPLE--------------------
tup = ()
tup.count(value)
tup.index(value, start, stop)
'''
'''---------------SET-----------
st = set()
st.add()
st.clear()
st.difference()
st.intersection()
st.pop()
st.remove()
st.symmetric_difference()
st.union()
st.isdisjoint()
st.issubset()
st.issuperset()
st.update()
'''





















