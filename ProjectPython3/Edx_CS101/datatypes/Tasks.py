'''
Created on Apr 24, 2018

@author: berag
'''


if __name__ == '__main__':
    pass

'''   
def list_O_matic(inp,animal):
    if inp == "":
        if len(animal) >= 1:
            animal.pop()
            return inp,"has been poped"        
    if inp in animal:
        animal.remove(inp)
        return (inp, "has been removed")
    else:
          animal.append(inp)
          return (inp, "has been added to your list")     
      

animalslist1 = ['cat']
animalslist2 = []

while animalslist1:
    print("Look at all of these",animalslist1)
    inp = input("Enter a name of an animal:")
    if inp == "Q".lower():
        break
    else:
        list_O_matic(inp,animalslist2)
    print (list_O_matic(inp,animalslist1))
'''
'''
def word_mixer(word_list) :
    new_words = []
    word_list.sort()
    while len(word_list) > 5 :
        new_words.append(word_list.pop(-5))
        new_words.append(word_list.pop(0))
        new_words.append(word_list.pop(-1))
        new_words.append("\n")
    return new_words
           
poem = input ("Enter poem: ") 
words_list = poem.split()

i=0

for word in words_list :
    if len(word) <= 3 :
        word = word.lower()
        words_list[i] = word
    elif len(word) >= 7 :
        word = word.upper()
        words_list[i] = word
    i+=1
     
for i in word_mixer(words_list):
    print(i, end=' ')  
'''
'''
name = ['a', 'b', 'c', 'd', 'e','a', 'b', 'c', 'd']
x = [1,2,3,4,5,6,7,8,9]

for x, y in zip(x, name):
    print(x, y)
    
dict = {}
name = ['a', 'b', 'c', 'd', 'e','a', 'b', 'c', 'd', 'e', 'f']
x = list(range(len(name)))

for x,y in zip(x, name):
    dict[x] = y
    
print(dict)
'''
'''
Find first and second string

'''
text = "all zip files are zipped and zip is that zip" 
'''

# first method
fz = text.find('zip')
print(fz) # First 'zip'
print(text.find('zip', fz + 1)) # second 'zip'

# Second method
print(text.find('zip', text.find('zip') + 1)) # second 'zip'

text = "all zip files are zipped and zip is that zip" 
n=0
for n in range(n, len(text)):
    loc = text.find('zip', n)
    print(loc)
    n = loc+1
'''
'''
x = 3.151548
y = 27.698542

inp = input("Enter some no: ")
n = inp.find('.') + 1

if n > 5:
   val = int(inp) + 0.5
   print(val[:n-1])
else:
    print(inp[:n-1])
'''
'''
str = "this is sample is is is is"
b = str.replace('is', 'are')
print(b)
b = str.replace('is', 'are', 3)
print(b)

    
Something = "Word Something"
Something = "Word"
Word = "Hey!"
Word = "Listen!"
print(Word)
''' 
'''
Factorial

from math import factorial
print(factorial(4))

def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fact = 1
        while n >= 1:
            fact = fact * n
            n = n-1
        return fact
print(factorial(4))
'''
'''
s = 5
t = 8

s, t = t, s
print(s, " ", t)
'''
'''
str = "this is is is is are is are is"
len = len(str)

f = str[:-1].find('is')
a = len-f
print(a)
print(str[:-1].find('is'))

'''
'''
Find last find

def find_last(str, lp):
    lps = -1
    while True:
        pos = str.find(lp, lps + 1)
        if pos == -1:
            return lps
        lps = pos
        
print(find_last('aaaa', 'a'))
#>>> 3
print(find_last('aaaaa', 'aa'))
#>>> 3
print(find_last('aaaa', 'b'))
#>>> -1
print(find_last("111111111", "1"))
#>>> 8
print(find_last("222222222", ""))
#>>> 9
print(find_last("", "3"))
#>>> -1
print(find_last("", ""))
#>>> 0
'''
'''
def nextDay1(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    day1 = day + 1
    month1 = month
    year1 = year
    
    # YOUR CODE HERE
    if day1 > 30:
        month1 += 1
        day1 = 1
        if month1 > 12:
            year1 += 1
            month1 = 1        
    
    return year1, month1, day1

def nextDay(year, month, day):
    if day < 30:
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1
    
print(nextDay(1999, 12, 30))
print(nextDay(2013, 1, 30))
print(nextDay(2012, 12, 30))

print(nextDay(2012, 1, 1))
print(nextDay(2012, 12, 1))


def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
'''
'''
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.

def how_many_days(month_number):
    days = days_in_month[month_number - 1]
    return days

print(how_many_days(1))
print(how_many_days(2))
print(how_many_days(3))
'''
'''
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# Write code to print out the capital of India
# by accessing the list
print(countries[1][1])
'''
'''
# Write a procedure, count_words, which takes as input a string
# and returns the number of words in the string. You may consider words
# as strings of characters separated by spaces.

def count_words(passage):
    output = passage.split()
    return len(output)

passage =("The number of orderings of the 52 cards in a deck of cards "
"is so great that if every one of the almost 7 billion people alive "
"today dealt one ordering of the cards per second, it would take "
"2.5 * 10**40 times the age of the universe to order the cards in every "
"possible way.")
print(count_words(passage))
#>>>56
'''
'''
# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(second):    
    
    if second >= 3600:
        h = second / 3600
        m1 = second % 3600
        m = m1 / 60
        s = m1 % 30
        
        
        return h, ' hours, ', m, ', minutes, ', s, ' second'   


print(convert_seconds(3661))
#>>> 1 hour, 1 minute, 1 second

print(convert_seconds(7325))
#>>> 2 hours, 2 minutes, 5 seconds

print(convert_seconds(7261.7))
#>>> 2 hours, 1 minute, 1.7 seconds
'''
'''
# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a' 
# following 'z'.

def shift(letter):
    b = ord(letter)
    if b == 122:
        return 'a'
    return chr(b + 1)

#print(shift('a'))
#>>> b
#print(shift('n'))
#>>> o
#print(shift('z'))
#>>> a

122
97
'''
'''
# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n = 0):
    b = ord(letter) + n
    if b == 96:
        return 'z'
    if b == 122:
        return 'a'
    if b > 122:
        return chr(97 + (b - 122) - 1)
    if b < 97:
        return chr(122 - (97 - b) + 1)
    return chr(b)

print(shift_n_letters('k', -12)) #y
print(shift_n_letters('s', 1))
#>>> t
print(shift_n_letters('s', 2))
#>>> u
print(shift_n_letters('z'))
print(shift_n_letters('a', -1))
print(shift_n_letters('a', 1))


# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

# Function to rotate string left and right by d length
 

    
def rotate(l, x):
    val = ""
    if len(l.split()) == 1:
        for i in l:
            b = shift_n_letters(i, x)
            val+=b
        return val
    else:
        return '???'
 
def rotate1(li, x):
    return li[-x % len(li):] + li[:-x % len(li)]

print(rotate('sarah', 13))
#>>> 'fnenu'
print(rotate('fnenu',13))
#>>> 'sarah'
print(rotate('dave',5))
#>>>'ifaj'
print(rotate('ifaj',-5))
#>>>'dave'
print(rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17))
#>>> ???
'''
'''
# Define a procedure, factorial, that takes a natural number as its input, and
# returns the number of ways to arrange the input number of items.

def factorial(n):
    count = 1
    if n == 0:
        return 1
    else:
        for i in range(n):
            count += count * i
    return count

print factorial(0)
#>>> 1

print factorial(5)
#>>> 120

print factorial(10)
#>>> 3628800
'''
'''
#Palendrom Recresive way

def is_Palindrom(s):
    if s == '':
        return True
    else:
        if s[0] == s[-1]:
            return is_Palindrom(s[1:-1])
        else:
            return False
    

print(is_Palindrom('a'))
print(is_Palindrom('ab'))


def is_Palindrom(s):
    for i in  range(0, int(len(s)/2)):
        if s[i] != s[-(i + 1)]:
            return False
    return True

print(is_Palindrom('ab'))
'''
'''
# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)

def fibonacci1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    
def fibonacci(n):
    current = 0
    after = 1    
    
    for i in range(n):      
        current, after = after, current + after      
         
    return current
        
 
print(fibonacci(0))
#>>> 0
print(fibonacci(1))
#>>> 1
print(fibonacci(15))
#>>> 610
print(fibonacci(36))
'''
'''
# Rabbits Multiplying

# A (slightly) more realistic model of rabbit multiplication than the Fibonacci
# model, would assume that rabbits eventually die. For this question, some
# rabbits die from month 6 onwards.
#
# Thus, we can model the number of rabbits as:
#
# rabbits(1) = 1 # There is one pair of immature rabbits in Month 1
# rabbits(2) = 1 # There is one pair of mature rabbits in Month 2
#
# For months 3-5:
# Same as Fibonacci model, no rabbits dying yet
# rabbits(n) = rabbits(n - 1) + rabbits(n - 2)
#
#
# For months > 5:
# All the rabbits that are over 5 months old die along with a few others
# so that the number that die is equal to the number alive 5 months ago.
# Before dying, the bunnies reproduce.
# rabbits(n) = rabbits(n - 1) + rabbits(n - 2) - rabbits(n - 5)
#
# This produces the rabbit sequence: 1, 1, 2, 3, 5, 7, 11, 16, 24, 35, 52, ...
#
# Define a procedure rabbits that takes as input a number n, and returns a
# number that is the value of the nth number in the rabbit sequence.
# For example, rabbits(10) -> 35. (It is okay if your procedure takes too
#                                long to run on inputs above 30.)

def rabbits(n):
    if n < 1:
        return 0
    else:
        if n == 1 or n == 2:
            return 1
        else:
            return rabbits(n-1) + rabbits(n-2) - rabbits(n - 5)


print(rabbits(10))
#>>> 35

s = ""
count = 0
for i in range(1,12):
    count+=1
    if count == 5:
        s = s + str(rabbits(i) - 1) + " "
    s = s + str(rabbits(i)) + " "
    
print(s)
#>>> 1 1 2 3 5 7 11 16 24 35 52
'''
'''
# Deep Count 

# The built-in len operator outputs the number of top-level elements in a List,
# but not the total number of elements. For this question, your goal is to count
# the total number of elements in a list, including all of the inner lists.

# Define a procedure, deep_count, that takes as input a list, and outputs the
# total number of elements in the list, including all elements in lists that it
# contains.


# For this procedure, you will need a way to test if a value is a list. We have
# provided a procedure, is_list(p) that does this:

def deep_count(p):
    sum = 0
    for i in p:
        sum = sum + 1
        if type(i) == list:
            sum = sum + deep_count(i)
    return sum

print(deep_count([[[[[[[[1, 2, 3]]]]]]]]))
print(deep_count([1, [1, 2, [3, 4]]]))
print(deep_count([1, 2, 3]))
print(deep_count([1, [], 3]))
'''

'''
# Single Gold Star

# Family Trees

# In the lecture, we showed a recursive definition for your ancestors. For this
# question, your goal is to define a procedure that finds someone's ancestors,
# given a Dictionary that provides the parent relationships.

# Here's an example of an input Dictionary:

ada_family = { 'Judith Blunt-Lytton': ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt'],
              'Ada King-Milbanke': ['Ralph King-Milbanke', 'Fanny Heriot'],
              'Ralph King-Milbanke': ['Augusta Ada King', 'William King-Noel'],
              'Anne Isabella Blunt': ['Augusta Ada King', 'William King-Noel'],
              'Byron King-Noel': ['Augusta Ada King', 'William King-Noel'],
              'Augusta Ada King': ['Anne Isabella Milbanke', 'George Gordon Byron'],
              'George Gordon Byron': ['Catherine Gordon', 'Captain John Byron'],
              'John Byron': ['Vice-Admiral John Byron', 'Sophia Trevannion'] }

# Define a procedure, ancestors(genealogy, person), that takes as its first input
# a Dictionary in the form given above, and as its second input the name of a
# person. It should return a list giving all the known ancestors of the input
# person (this should be the empty list if there are none). The order of the list
# does not matter and duplicates will be ignored.


def ancestor(genealogy, person):
    if person in genealogy:
        parents = genealogy[person]
        result = parents
        for p in parents:
            result = result + ancestor(genealogy, person)
        return result
    return []
    
    
# Here are some examples:

print ancestors(ada_family, 'Augusta Ada King')
#>>> ['Anne Isabella Milbanke', 'George Gordon Byron',
#    'Catherine Gordon','Captain John Byron']

print ancestors(ada_family, 'Judith Blunt-Lytton')
#>>> ['Anne Isabella Blunt', 'Wilfrid Scawen Blunt', 'Augusta Ada King',
#    'William King-Noel', 'Anne Isabella Milbanke', 'George Gordon Byron',
#    'Catherine Gordon', 'Captain John Byron']

print ancestors(ada_family, 'Dave')
#>>> []
'''
'''
# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.

def make_next_row(n):
    result = []
    prev = 0
    for i in n:
        result.append(i + prev)
        prev = i
    result.append(prev)
    return result

def triangle(n):
    result = []
    current = [1]
    for i in range(0, n):
        result.append(current)
        current = make_next_row(current)
    return result
        
#For example:

print(triangle(0))
#>>> []

print(triangle(1))
#>>> [[1]]

print(triangle(2))
#>> [[1], [1, 1]]

print(triangle(3))
#>>> [[1], [1, 1], [1, 2, 1]]

print(triangle(6))
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
'''
'''
# The triangular numbers are the numbers 1, 3, 6, 10, 15, 21, ...
# They are calculated as follows.

# 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 + 4 + 5 = 15

# Write a procedure, triangular, that takes as its input a positive 
# integer n and returns the nth triangular number.

def triangular(n):
    res = 0
    if n > 1:
        for i in range(n+1):
            res += i
        return res
    return 1


print triangular(1)
#>>>1

print triangular(3)
#>>> 6

print triangular(10)
#>>> 55
'''
'''
# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def remove_tags(tags):
    start = tags.find('<')
    while start != -1:
        end = tags.find('>', start)
        tags = tags[:start] + " " + tags[end + 1:]
        start = tags.find('<')
    return tags.split()


print(remove_tags("""<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>"""))
#>>> ['Title','This','is','a','link','.']
print(remove_tags("""<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>"""))
#>>> ['Hello','World!']
print(remove_tags("<hello><goodbye>"))
#>>> []
print(remove_tags("This is plain text."))
#>>> ['This', 'is', 'plain', 'text.']
'''
'''
# Question 5: Date Converter

# Write a procedure date_converter which takes two inputs. The first is 
# a dictionary and the second a string. The string is a valid date in 
# the format month/day/year. The procedure should return
# the date written in the form <day> <name of month> <year>.
# For example , if the
# dictionary is in English,

english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 
6:"June", 7:"July", 8:"August", 9:"September",10:"October", 
11:"November", 12:"December"}

# then  "5/11/2012" should be converted to "11 May 2012". 
# If the dictionary is in Swedish

swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj", 
6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober", 
11:"november", 12:"december"}


#print(english[5])

# then "5/11/2012" should be converted to "11 maj 2012".

# Hint: int('12') converts the string '12' to the integer 12.

def date_converter(language, date):
    m, d, y = date.split('/')
    return d+ ' '+ language[int(m)]+ ' '+ y


print(date_converter(english, '5/11/2012'))
#>>> 11 May 2012
print(date_converter(english, '5/11/12'))
#>>> 11 May 12
print(date_converter(swedish, '5/11/2012'))
#>>> 11 maj 2012
print(date_converter(swedish, '12/5/1791'))
#>>> 5 december 1791
'''
'''
# Question 7: Find and Replace

# For this question you need to define two procedures:
#  make_converter(match, replacement)
#     Takes as input two strings and returns a converter. It doesn't have
#     to make a specific type of thing. It can 
#     return anything you would find useful in apply_converter.
#  apply_converter(converter, string)
#     Takes as input a converter (produced by make_converter), and 
#     a string, and returns the result of applying the converter to the 
#     input string. This replaces all occurrences of the match used to 
#     build the converter, with the replacement.  It keeps doing 
#     replacements until there are no more opportunities for replacements.


def make_converter(match, replacement):
    return [match, replacement]

def apply_converter(converter, string):
    prev = None
    while prev != string:
        prev = string
        pos = string.find(converter[0])
        if pos != -1:
            string = string[:pos] + converter[1] + string[pos + len(converter[0]):]
    return string

# For example,

c1 = make_converter('aa', 'a')
print(apply_converter(c1, 'aaaa'))
#>>> a

c = make_converter('aba', 'b')
print(apply_converter(c, 'aaaaaabaaaaa'))
#>>> ab

# Note that this process is not guaranteed to terminate for all inputs
# (for example, apply_converter(make_converter('a', 'aa'), 'a') would 
# run forever).
'''
'''
# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(lst):
    best = None
    blen = 0
    current = None
    clen = 0
    for l in lst:
        if l != current:
            current = l
            clen = 1
        else:
            clen = clen + 1
        if clen > blen:
            best = current
            blen = clen
    return best
        

#For example,

print(longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1]))
# 3
print(longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']))
# b
print(longest_repetition([1,2,3,4,5]))
# 1
print(longest_repetition([]))
# None
'''
'''
# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list, 
# and returns a new list that is the deep reverse of the input list.  
# This means it reverses all the elements in the list, and if any 
# of those elements are lists themselves, reverses all the elements 
# in the inner list, all the way down. 

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if 
# p is a list and False if it is not.

def is_list(p):
    return isinstance(p, list)

def deep_reverse(p):
    if is_list(p):
        res = []
        for i in range(len(p) -1, -1, -1):
            res.append(deep_reverse(p[i]))
        return res
    else:
        return p


p = [1, [2, 3, [4, [5, 6]]]]
print(deep_reverse(p))
#>>> [[[[6, 5], 4], 3, 2], 1]
print(p)
#>>> [1, [2, 3, [4, [5, 6]]]]
q =  [1, [2,3], 4, [5,6]]
print(deep_reverse(q))
#>>> [ [6,5], 4, [3, 2], 1]
print(q)
#>>> [1, [2,3], 4, [5,6]]
'''
'''
# Two Gold Stars
# Question 2: Combatting Link Spam

# One of the problems with our page ranking system is pages can 
# collude with each other to improve their page ranks.  We consider 
# A->B a reciprocal link if there is a link path from B to A of length 
# equal to or below the collusion level, k.  The length of a link path 
# is the number of links which are taken to travel from one page to the 
# other.

# If k = 0, then a link from A to A is a reciprocal link for node A, 
# since no links needs to be taken to get from A to A.

# If k=1, B->A would count as a reciprocal link  if there is a link 
# A->B, which includes one link and so is of length 1. (it requires 
# two parties, A and B, to collude to increase each others page rank).

# If k=2, B->A would count as a reciprocal link for node A if there is
# a path A->C->B, for some page C, (link path of length 2),
# or a direct link A-> B (link path of length 1).

# Modify the compute_ranks code to 
#   - take an extra input k, which is a non-negative integer, and 
#   - exclude reciprocal links of length up to and including k from 
#     helping the page rank.

def is_reciprocal_link(graph, source, destination, k):
    if k == 0:
        if destination == source:
            return True
        return False
    if source in graph[destination]:
        if is_reciprocal_link(graph, source, destination, k-1):
            return True
        return False

def compute_ranks(graph, k):
    d = 0.8 # damping factor
    numloops = 10
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    if not is_reciprocal_link(graph, node, page, k):
                        newrank = newrank + d * (ranks[node]/len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks


# For example

g = {'a': ['a', 'b', 'c'], 'b':['a'], 'c':['d'], 'd':['a']}

print(compute_ranks(g, 0)) # the a->a link is reciprocal
#>>> {'a': 0.26676872354238684, 'c': 0.1216391112164609,
#     'b': 0.1216391112164609, 'd': 0.1476647842238683}

print(compute_ranks(g, 1)) # a->a, a->b, b->a links are reciprocal
#>>> {'a': 0.14761759762962962, 'c': 0.08936469270123457,
#     'b': 0.04999999999999999, 'd': 0.12202199703703702}

print(compute_ranks(g, 2))
# a->a, a->b, b->a, a->c, c->d, d->a links are reciprocal
# (so all pages end up with the same rank)
#>>> {'a': 0.04999999999999999, 'c': 0.04999999999999999,
#     'b': 0.04999999999999999, 'd': 0.04999999999999999}
'''

# THREE GOLD STARS
# Question 3-star: Elementary Cellular Automaton

# Please see the video for additional explanation.

# A one-dimensional cellular automata takes in a string, which in our 
# case, consists of the characters '.' and 'x', and changes it according 
# to some predetermined rules. The rules consider three characters, which 
# are a character at position k and its two neighbours, and determine 
# what the character at the corresponding position k will be in the new 
# string.

# For example, if the character at position k in the string  is '.' and 
# its neighbours are '.' and 'x', then the pattern is '..x'. We look up 
# '..x' in the table below. In the table, '..x' corresponds to 'x' which 
# means that in the new string, 'x' will be at position k.

# Rules:
#          pattern in         position k in        contribution to
# Value    current string     new string           pattern number
#                                                  is 0 if replaced by '.'
#                                                  and value if replaced
#                                                  by 'x'
#   1       '...'               '.'                        1 * 0
#   2       '..x'               'x'                        2 * 1
#   4       '.x.'               'x'                        4 * 1
#   8       '.xx'               'x'                        8 * 1
#  16       'x..'               '.'                       16 * 0
#  32       'x.x'               '.'                       32 * 0
#  64       'xx.'               '.'                       64 * 0
# 128       'xxx'               'x'                      128 * 1
#                                                      ----------
#                                                           142

# To calculate the patterns which will have the central character x, work 
# out the values required to sum to the pattern number. For example,
# 32 = 32 so only pattern 32 which is x.x changes the central position to
# an x. All the others have a . in the next line.

# 23 = 16 + 4 + 2 + 1 which means that 'x..', '.x.', '..x' and '...' all 
# lead to an 'x' in the next line and the rest have a '.'

# For pattern 142, and starting string
# ...........x...........
# the new strings created will be
# ..........xx...........  (generations = 1)
# .........xx............  (generations = 2)
# ........xx.............  (generations = 3)
# .......xx..............  (generations = 4)
# ......xx...............  (generations = 5)
# .....xx................  (generations = 6)
# ....xx.................  (generations = 7)
# ...xx..................  (generations = 8)
# ..xx...................  (generations = 9)
# .xx....................  (generations = 10)

# Note that the first position of the string is next to the last position 
# in the string.

# Define a procedure, cellular_automaton, that takes three inputs: 
#     a non-empty string, 
#     a pattern number which is an integer between 0 and 255 that
# represents a set of rules, and 
#     a positive integer, n, which is the number of generations. 
# The procedure should return a string which is the result of
# applying the rules generated by the pattern to the string n times.

def cellular_automaton(string, pattern_number, generations):
    patterns = {}
    pattern_list = ['...', '..x', '.x.', '.xx', 'x..', 'x.x', 'xx.', 'xxx']
    n = len(string)
    
    #build pattern dictionary
    for i in range(7, -1, -1):
        if pattern_number / (2**i) == 1:
            patterns[pattern_list[i]] = 'x'
            pattern_number = pattern_number - 2**i
        else:
            patterns[pattern_list[i]] = '.'
    # Make new string using the pattern
    #generation time
    for j in range(0, generations):
        new_string = ''
        for i in range(0, n):
            pattern = string[i -1] + string[i] + string[(i + 1) % n]
            new_string = new_string + patterns[pattern]
        string = new_string
    return new_string


print(cellular_automaton('.x.x.x.x.', 17, 2))
#>>> xxxxxxx..
print(cellular_automaton('.x.x.x.x.', 249, 3))
#>>> .x..x.x.x
print(cellular_automaton('...x....', 125, 1))
#>>> xx.xxxxx
print(cellular_automaton('...x....', 125, 2))
#>>> .xxx....
print(cellular_automaton('...x....', 125, 3))
#>>> .x.xxxxx
print(cellular_automaton('...x....', 125, 4))
#>>> xxxx...x
print(cellular_automaton('...x....', 125, 5))
#>>> ...xxx.x
print(cellular_automaton('...x....', 125, 6))
#>>> xx.x.xxx
print(cellular_automaton('...x....', 125, 7))
#>>> .xxxxx..
print(cellular_automaton('...x....', 125, 8))
#>>> .x...xxx
print(cellular_automaton('...x....', 125, 9))
#>>> xxxx.x.x
print(cellular_automaton('...x....', 125, 10))
#>>> ...xxxxx



























