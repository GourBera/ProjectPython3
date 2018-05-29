'''
Created on May 25, 2018

@author: berag
'''

if __name__ == '__main__':
    pass

import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)
    
#read_csv('./DataSource/titanic-data.csv')


import pandas as pd

x = pd.read_csv(r'C:\Users\berag\Desktop\DataScience\DataSource/titanic-data.csv')        

print(x.head(5))






































































































