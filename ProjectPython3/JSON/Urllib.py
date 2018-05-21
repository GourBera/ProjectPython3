'''
Created on May 21, 2018

@author: berag
'''

if __name__ == '__main__':
    pass


import json
from urllib.request import *

with urlopen("http://google.com") as resp:
    source = resp.read()
    print(source)
    
data = json.loads(source)
print(json.dumps(data, indent = 2))