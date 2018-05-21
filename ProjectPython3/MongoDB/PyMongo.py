'''
Created on May 21, 2018

@author: berag
'''
from pymongo import *

if __name__ == '__main__':
    pass

    
cli = mongo_client
db = cli["Library"]
    
coll = db["Books"]
    
book = {}
    
book["Title"] = "MongoDB Practical"
book["Author"] = "Unknown"
book["Year"] = 2018
    
    
coll.insert(book)
    
print(book)
    