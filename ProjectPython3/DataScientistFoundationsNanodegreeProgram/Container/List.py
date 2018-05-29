'''
Created on May 22, 2018

@author: berag

#Operation or method
in
not in

len()
min()
max()
sorted()

mutable - its value can be changed
ordered - 


'''

if __name__ == '__main__':
    pass
'''
lst = [1,5,4,9,2]
lst1 = ['a','b','c','d']
lst2 = ['a', 2, 'c', 4]
#print(lst[9])       #IndexError: list index out of range
print(lst[len(lst)-1]) # Last element
print(max(lst))
print(max(lst1))
#print(max(lst2))        #TypeError: '>' not supported between instances of 'int' and 'str'

print(' '.join(lst1))   

print('\n'.join(lst1))


a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))


a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == b)       #True
print(a is b)       #True
print(a == c)       #True
print(a is c)       #False

animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4], 'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}

print(animals['dogs'][3])   #15
#print(animals[3])           #KeyError: 3
print(animals['fish'])


# Creating a new list
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())
    
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for index in range(len(cities)):
    cities[index] = cities[index].title()
'''
'''
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append(name.replace(" ", "_").lower())
    
print(usernames)

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in names:
    name = name.lower().replace(" ", "_")

print(names)

'''
'''
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for i in range(len(usernames)):
    usernames.replace(usernames[i].replace(" ", "_").lower())    
print(usernames)

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)

'''
'''
items = ['first string', 'second string']
html_str = "<ul>\n"          # The "\n" here is the end-of-line char, causing
                             # chars after this in html_str to be on next line

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)
'''
'''
print(list(range(4)))
print(list(range(4,8)))
print(list(range(4,10,2)))
print(list(range(0,-5)))

colors = ['Red', 'Blue', 'Green', 'Purple']
lower_colors = [ ]

for color in colors:
    lower_colors.append(object)
    
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

print("Iterating through keys:")
for key in cast:
    print(key)

print("\nIterating through keys and values:")
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))
'''
'''
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for fruit in basket_items:
    if fruit in fruits:
        fruit_count += basket_items[fruit]
    else:
        not_fruit_count += basket_items[fruit]

print(fruit_count, not_fruit_count)
'''
'''
# Start with a sample number for first test - change this when testing your code more!
number = 6    
# We'll always start with our product equal to the number
product = number

# TODO: Write while loop header line - how will you tell it when to stop looping?
while number > 1:
    # TODO: Each time through the loop, what do we want to do to our number?
    number -= 1
    # TODO: Each time, what do we want to multiply the current product by?
    product *= number
#    print(number) 
# TODO: Print out final product (how do we indicate this should happen after loop ends?)
print(product)


# This is the number we'll find the factorial of - change it to test your code!
number = 6
# We'll start with the product equal to the number
product = number
# TODO: Write a for loop that calculates the factorial of our number 
for i in range(1, number):
    product *= i
# TODO: print the factorial of your number
print(product)
'''
'''
start_num = 1#provide some start number
end_num = 10#provide some end number that you stop when you hit
count_by = 6#provide some number to count by 

# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
break_num = 4
while start_num > end_num:
    if  start_num >= count_by:
        print(start_num)
    start_num += 1

print(break_num)
'''
'''
start_num = 5
end_num = 100
count_by = 2

if start_num > end_num:
    result = "Oops!  Looks like your start value is greater than the end value.  Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by

    result = break_num

print(result)
'''
''''
Input:
start_num = 300
end_num = 548
count_by = 23
Output:
553
'''
'''
# Nearest Square

limit = 40
num = 0

while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)
'''
'''
limit = 52
num = 0
n = 0
for i in range(0, limit):
    num = i ** 2
    #print(i)
    if num < limit:
        n = i
print(n, '**', n ** 2)
'''     
























