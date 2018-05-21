'''
Created on May 11, 2018

@author: berag
'''

if __name__ == '__main__':
    pass
import pandas as pd
import numpy as np

#df = pd.read_csv('titanic-data.csv', header = None)
df = pd.read_csv('titanic-data.csv')
#df = pd.read_csv('titanic-data.csv', columns = ['Survived','Pclass','Age','Fare'])
#print(df)
dafr = pd.DataFrame(df, columns = ['Survived','Pclass','Age','Fare'])
'''
print(dafr)
print(dafr.info())
print(dafr.head())
print(dafr.tail())
print(dafr.describe())

b = dafr.describe()
print(b['Age']['mean'])
'''
'''
Prepare Data
'''
CLass = dafr['Pclass'].unique()
print(CLass)

ds = dafr['Fare'].describe()
print(ds)

summ = dafr['Fare'].sum()
print(summ)

mn = dafr['Fare'].mean()
print(mn)
















