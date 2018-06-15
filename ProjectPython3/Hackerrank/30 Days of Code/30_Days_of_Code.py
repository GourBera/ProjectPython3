'''
Created on 11-Jun-2018

@author: Titan
'''

if __name__ == '__main__':
    pass

import array
from decimal import Decimal
from decimal import *


def fibSequence(n):
    """
    Generates a fibonacci sequence
    with the size of n
    """
    assert n > 0

    series = [1]

    while len(series) < n:
        if len(series) == 1:
            series.append(1)
        else:
            series.append(series[-1] + series[-2])

    for i in range(len(series)):  # Convert the numbers to strings
        series[i] = str(series[i])

    return(', '.join(series))  # Return the sequence seperated by commas


def main():  # Wrapper function

    print(fibSequence(int(input('How many numbers do you need? '))))

if __name__ == '__main__':
    main()


#Day 1
i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.
integer = None
double = None
string = None

# Read and save an integer, double, and String to your variables.
integer = int(input('enter'))
double = float(input('enter'))
string = str(input('enter'))

# Print the sum of both integer variables on a new line.
print(i + integer)

# Print the sum of the double variables on a new line.
print(d + double)

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + string)

#Day 3
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

if N % 2 != 0:
    print("Weird")
else:
    if N <= 5:
        print("Not Weird")
    elif N <= 20:
        print("Weird")
    else:
        print("Not Weird")

#Day 4
class Person:
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge > 0:
            self.age = initialAge
        else:
            print("Age is not valid, setting age to 0.")
            self.age = 0

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print("You are young.")
        elif self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1
        
t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")

#Day 5

#Day 6
N = int(input())

for i in range(0, N):

    string = input()

    for j in range(0, len(string)):
        if j % 2 == 0:
            print(string[j], end='')

    print(" ", end='')

    for j in range(0, len(string)):
        if j % 2 != 0:
            print(string[j], end='')

    print("")

#Day 7
input()

arr = str(input()).split(" ")
arr.reverse()

for num in arr:
    print(num + " ", end="")
    
#Day 8
num = int(input())

phone_book = {}

for i in range(0, num):
    entry = str(input()).split(" ")

    name = entry[0]
    phone = int(entry[1])
    phone_book[name] = phone

for j in range(0, num):
    name = str(input())

    if name in phone_book:
        phone = phone_book[name]
        print(name + "=" + str(phone))
    else:
        print("Not found")

#Day 9
import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    return 1 if n == 1 else factorial(n - 1) * n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#Day 10 
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

result = 0
maximum = 0

while n > 0:
    if n % 2 == 1:
        result += 1
        if result > maximum:
            maximum = result

    else:
        result = 0

    n //= 2

print(maximum)

#Day 11
arr = []

for _ in range(6):
    tmp = [int(x) for x in str(input()).split(" ")]
    arr.append(tmp)

maximum = -9 * 7

for i in range(6):
    for j in range(6):
        if j + 2 < 6 and i + 2 < 6:
            result = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            if result > maximum:
                maximum = result

print(maximum)
#Day 12

#Day 13

#Day 14

#Day 15

#Day 16
import sys

try:
    print(int(input()))
except ValueError:
    print("Bad String")

#Day 17
class Calculator:
    def power(self, n, p):
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        return pow(n, p)


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)

#Day 18


#Day 19


#Day 20


#Day 21


#Day 22


#Day 23


#Day 24


#Day 25
from math import sqrt

T = int(input())


def isPrime(n):
    for i in range(2, int(sqrt(n))):
        if n % i is 0:
            return False
    return True


for _ in range(T):
    n = int(input())
    
    if n >= 2 and isPrime(n):
        print("Prime")
    else:
        print("Not prime")


#Day 26


#Day 27


#Day 28


#Day 29


#Day 30



'''
1. Select * from CITY where POPULATION > 120000 and COUNTRYCODE = 'USA';
2. Select NAME from CITY where POPULATION > 120000 and COUNTRYCODE = 'USA';
3. select * from city;
4. select * from city where ID=1661;
5. select * from city where COUNTRYCODE='JPN';
6. Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.
Select distinct NAME from CITY where COUNTRYCODE = 'JPN';
7. Query a list of CITY and STATE from the STATION table.
select CITY, STATE from STATION;
8. Query a list of CITY names from STATION with even ID numbers only. You may print the results in any order, but must exclude duplicates from your answer.
select distinct CITY from STATION where MOD(ID,2) = 0;
9. 

'''



def arrays(arr):
    # complete this function
    # use numpy.array
    arr = list(map(float, arr))
    return numpy.array(arr[::-1])



