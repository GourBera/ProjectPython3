'''
Created on Jun 1, 2018

@author: berag
'''

if __name__ == '__main__':
    pass
'''
# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    with open(datafile, "r") as f:
        for line in f:
            print line

    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline

    
test()
'''
import csv
from csv import DictReader
import os
import pprint

DataDIR = ""
file = "./beatles-diskography.csv"

with open(file) as csvfile:
    read = csv.reader(csvfile, delimiter = ',')
    for row in read:
        print(row)


def parse_csv(file):
    data = []
    n=0
    
    with open(file, 'rb') as sd:
        r = sd.DictReader()
        for line in r:
            data.append(line)
    return data


def parse_csv1(file):
    lst = []
    
    with open(file, 'rb') as f:        
        data = str(f.readline()).replace("b'", "").split(",")
        for i in range(10):
            dta =  str(f.readline()).replace("b'", "").split(",")
            dct = {}
            for x, y in zip(data, dta):
                dct[x] = y
            lst.append(dct)
                
    return lst 
        
'''
df = parse_csv(file)
#print(df[0])
print(df)

for d in df:
    print(d)

'''





































