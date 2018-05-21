'''
Created on May 10, 2018

@author: berag
'''

if __name__ == '__main__':
    pass

from pandas import DataFrame, read_csv
# General syntax to import a library but no functions: 
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

# Enable inline plotting
#%matplotlib inline

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]
title = ['Mr','Ms','Ms','Mr','Mr']

BabyDataSet = list(zip(names,births,title))
print(BabyDataSet)

df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births','title'])
print(df)
print(df.dtypes)
print(df.Births.dtype)

# Add 2 Col
df['FullName'] = df['title']+' '+df['Names']
print(df)

#df.to_csv('births1880.csv',index=False,header=False, columns=['Names', 'Births', 'FullName'])

Location = r'C:\Users\berag\My Documents\LiClipse Workspace\SampleProject\DataScience\births1880.csv'
dataset = pd.read_csv(Location)
print(dataset)

dataset = pd.read_csv(Location, header=None)
print(dataset)


df = pd.read_csv(Location, names=['Names','Births'])
print(df)

print(df.describe())

'''
import os
os.remove(Location)    # Deleting File
'''

# Method 1:
Sorted = df.sort_values(['Births'], ascending=False)

# Method 2:
print(df['Births'].max())

df.to_csv('newData.csv',index=False, header=False, columns=['Names', 'Births'])
































