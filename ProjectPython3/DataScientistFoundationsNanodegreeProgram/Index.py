'''
Created on May 22, 2018

@author: berag
'''

if __name__ == '__main__':
    pass
'''
Data-Structure    Ordered    Mutable    Constructor                 Example
int                  NA          NA          int()                      5
float                NA          NA          float()                    6.5
string               Yes         No          ' ' or " " or str()        "this is a string"
bool                 NA          NA          NA                         True or False
list                 Yes         Yes         [ ] or list()              [5, 'yes', 5.7]
tuple                Yes         No          ( ) or tuple()             (5, 'yes', 5.7)
set                  No          Yes         { } or set()               {5, 'yes', 5.7}
dictionary           No          Keys: No    { } or dict()              {'Jun':75, 'Jul':89}
'''

'''
for i in range(5, 35, 5):
    print(i)    
    

'''

import time
start_time = time.time()
#main()
print("--- %s seconds ---" % (time.time() - start_time))

'''
csv: very convenient for reading and writing csv files
collections: useful extensions of the usual data types including OrderedDict, defaultdict and namedtuple
random: generates pseudo-random numbers, shuffles sequences randomly and chooses random items
string: more functions on strings. This module also contains useful collections of letters like 
        string.digits (a string containing all characters which are valid digits).
re: pattern-matching in strings via regular expressions
math: some standard mathematical functions
os: interacting with operating systems
os.path: submodule of os for manipulating path names
sys: work directly with the Python interpreter
json: good for reading and writing json files (good for web work)
'''

from datetime import datetime
import pytz

utc = pytz.utc
ist = pytz.timezone('Asia/Kolkata')

now = datetime.time(tz = utc)
ist_now = now.astimezone(ist)

print(now)
print(ist_now)




















