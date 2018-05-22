'''
Created on 22-May-2018

@author: Titan
'''

from audioop import minmax


'''
    N = int(input('Enter'))
    lst = []
    for i in range(N):
        op = str(input('Enter')).split()
        if op[0]=='insert':
            lst.insert(int(op[1]), int(op[2]))
        if op[0]=='print':
            print(lst)
        if op[0]=='remove':
            lst.remove(int(op[1]))
        if op[0]=='append':
            lst.append(int(op[1]))
        if op[0]=='sort':
            lst.sort()
        if op[0]=='pop':
            lst.pop()
        if op[0]=='reverse':
            lst.reverse()
'''

'''
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird


if __name__ == '__main__':
    n = int(input("Enter one no: "))
    if n >=1 and n <=100:
        if n % 2 != 0:
            print("Weird")
        elif n % 2 == 0 and n in range(2,5):
            print("Not Weird")
        elif n % 2 == 0 and n in range(6, 20):
            print("Weird")
        elif n % 2 == 0 and n > 20:
            print("Not Weird")        
    else:
        print("No is <1 or >100")
'''
'''
Which year you will become 100 years old

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
Extras:
Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

def addressed_message():
    name = input("Give me your name: ")
    age = input("Enter your age: ") 
    copy = input("How many coppies you want: ")   
    
    year = 2018 + (100 - int(age))
    msg = "Hello ", name, " in year ", year, " you will become 100 years old"
    
    for i in range(int(copy)):
        print(msg)
    
addressed_message()

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_a = []
for i in a:
    if i <=5:
        print(i, end=' ')
        new_a.append(i)
print('new_a: ', new_a)
'''               
'''
write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 21]

result = [i for i in set(a) if i in b]
print(result)
'''
'''
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)


def Palindrom():
    inp = input("Enter Str to test Palindrome: ")
    reverse = inp[::-1]
    if inp == reverse:
        print("Given string is palindrom")
    else:
        print("Given string is NOT a palindrom")

Palindrom()
'''
'''
Fibonacci

def fibonacci():
    num = int(input("How many numbers that generates?:"))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib
print(fibonacci())
'''
'''
# Write a function that takes a list and returns a new list that contains 
# all the elements of the first list minus duplicates.

# this one uses a for loop
def dedupe_v1(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y

#this one uses sets
def dedupe_v2(x):
    return list(set(x))

a = [1,2,3,4,3,2,1]
print a
print dedupe_v1(a)
print dedupe_v2(a)
'''
'''
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
My name is Gour -  Gour is name My  and ruoG si eman yM 


inp = input("Enter some String: ")

split = inp.split()
for i in split[::-1]:
    print(i, end=" ")
print()
for i in split[::-1]:
    print(i[::-1], end=" ")
'''
'''
Password Generator

import random

str1 = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
count = 8
p =  "".join(random.sample(str1, count))
print(p)

import string
import random

def pw_gen():
    size = int(input("How many characters in your password?"))
    chars = string.ascii_letters + string.digits + string.punctuation
    print("".join(random.sample(chars, size)))

pw_gen()
'''
'''
import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)

for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())
'''

'''
from hashlib import *
n = int(input('Enter'))
integer_list = map(int, input('Enter').split())
print(hash(tuple(integer_list)))
'''


'''
abracadabra
5 k
abrackdabra
'''

def print_formatted(number):
    # your code goes here
    for i in range(number):
        print(i,oct(i),hex(i),bin(i))
        

print_formatted(10)


def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

string = "CDCCDCCDC" 
# counts the number of times substring occurs in 
# the given string and returns an integer
print(string.count("CDC"))



a = 10
print("this is {}".format(a))       
        
str = "this is str".split()
print('-'.join(str))        

# Find Second Largest
el = [20,67,3,2.6,7,74,2.8,90.8,52.8,4,3,2,5,7]
import heapq
b = heapq.nlargest(2, el)
#print(b)

lst = [2, 3, 6, 6, 5]

print(max(lst))


arr = map(int, input('enter').split())
arr.sort()


print(arr)

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    if len(arr) == 0:
        print(0)
    elif len(arr) == 1:
        print(len)
    else:
        first, second = 0, 0
        for i in arr:
            if i > first:
                first, second = i, first
            elif first > i > second:
                second = i
        print(second)











