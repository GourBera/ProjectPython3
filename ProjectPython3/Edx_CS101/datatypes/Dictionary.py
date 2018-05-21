'''
Created on May 16, 2018

@author: berag
'''

if __name__ == '__main__':
    pass
import string
import sys

str = """Cache Size 
The Cache Size field displays the cache in the database, and allows the user to determine how many table rows are cached.  
caching makes the calculation faster as the old values are 
stores so future requests for that data can be served faster"""
'''
strplt = str.strip().split()

dct = {}

for w in strplt:
    if w not in dct:
        dct[w.lower()]=1
    else:
        dct[w] = dct[w] + 1
        
for d in dct:
    print(d, '-', dct[d])

'''


def word_count():
    import string
    import sys
    
    word_count = {}
    
    for line in sys.stdin:
        data = line.strip().split(" ")
        print(data)
        
        
        
word_count()


def mapper():
    import string
    import sys
    
    word_count = {}
    
    for line in sys.stdin:
        data = line.strip().split(" ")
    
        for i in data:
            
            #cleaned_data = i.translate(string.maketrans(" ", ""), string.punctuation().lower())
            cleaned_data = i.translate(string.punctuation().lower())
            print("{0}\t{1}".format(cleaned_data, 1))
            
    


str = """Cache Size 
The Cache Size field displays the cache in the database, and allows the user to determine how many table rows are cached.  
caching makes the calculation faster as the old values are 
stores so future requests for that data can be served faster"""

print(mapper(str))



def reducer():
    import sys
    
    word_count = 0
    old_key = None
    
    for line in sys.stdin:
        data = line.strip().split(" ")
        
        if len(data) != 2:
            continue
        
        this_key, count = data
        
        if old_key and old_key != this_key:
            print("{0}\t{1}".format(old_key, word_count))
            word_count = 0
        
        old_key = this_key
        word_count += float(count)    
        
    if old_key != None:
        print("{0}\t{1}".format(old_key, word_count))
            
    
    

































