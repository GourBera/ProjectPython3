'''
Created on Apr 19, 2018

@author: berag

Mutation - List is Mutable / String is Immutable - when we update any string actually it create a 
new updated string and make a reference to it. each time it actually create a new string not updated the same 

Empty list returns 0
Start from 0

del 
pop()
remove()

append()
count()

extend() # +
reverse()
sort()
sorted(listname)

index()
in 
not in

.rotate(0)

def is_list(p):
    return isinstance(p, list)

'''

if __name__ == '__main__':
    pass
'''
list can be collection of string or integer or both
we can perform string/integer operation with list like - title(), sum() 


lst = [1, 'str1', 2, 'str2', 3, 'str3']

print(lst[0])
print(lst[5])
print(lst[1].title())

lst = [1, 'Gour', 'gour@gmail.com', 2, 'user2', 'user2@gmail.com', 3, 'user3', 'user3@gmail.com']
print('User no.', lst[0], ' is: ', lst[1].title(), ' and pwd is: ', lst[2])

#print(lst[0]+lst[2]) # integer operation can not be performed in mixed list 

lst = [1,2,3,4]
print('Sum of all the list element is: ', lst[0] + lst[1]+ lst[2] + lst[3])


# List Append

lst.append(.5) 
print(lst)
lst.append("") 
print(lst)
lst.append(5) 
print(lst)
lst.append(True) 
print(lst)


lst = []
c = input('If want to continue type q:')
while c == 'q':
    inp = input('Enter BDay: ')
    lst.append(inp)
    print(lst)
    c = input('If want to continue type q:')
    

lst = ['Gour', 'sandeep', 'swadesh']
print(lst)
lst[0] = lst[0]+" Bera"
print(lst)
'''
'''
replace items in a list
    create a list, three_num, containing 3 single digit integers
    print three_num
    check if index 0 value is < 5
        if < 5 , replace index 0 with a string: "small"
        else, replace index 0 with a string: "large"
    print three_num

# [ ] complete "replace items in a list" task


lst = [1,6,3]

lenth = len(lst)
no = 0

for i in lst:
    print(lst[no])
    if i < 5:
        print('small')
        lst[no] = 'small'
    else:
        print('big')
        lst[no] = 'big'
    no+=1
    
print(lst)

lst = [1,6,3]

lenth = len(lst)

while lenth > 0:
    print(lst[lenth-1])
    lenth = lenth - 1


lst = ['ABC', 'DEF', 'GHI']    

lenth = len(lst[0])
let = ""
while lenth > 0:
    l = lst[0][lenth-1]
    let = let + l
    lenth = lenth - 1
    
print(let) #CAB
  

lst = [1,2,3,4,5]
lst.insert(0, 0)    
print(lst)
lst.insert(10, 10)    
print(lst)
lst.insert(1, 10)    
print(lst) # it does not replace index value
 

# delete, pop() & remove()

lst = [1,2,3,4,5]

del lst[0]
print(lst)
del lst[-1]
print(lst)
#del lst[10]

lst = [1,2,3,4,5]

lst.pop()
print(lst)
lst.pop(-1)
print(lst)

lst = [1,2,3,4,5,6,7,8,9]
print('List value: ', lst)
n1 = lst.pop()
n2 = lst.pop()

print('After popped: ', lst)
print('Sum of popped value: ', n1, ' + ', n2, ' = ', n1+n2)


dog_types = ["Lab", "Pug", "Poodle"]

while dog_types: 
    print(dog_types.pop(), ' popped from the list.. List now: ', dog_types)
'''
'''
create a empty list purchase_amounts
populate the list with user input for the price of items
continue adding to list with while until "done" is entered

    can use while True: with break

print purchase_amounts
''' 
'''
purchase_amounts = []
t = True

while True:
    price = input('Enter the price: ')
    
    if price == 'done':
        break
    else:
        purchase_amounts.append(price)  
        print(purchase_amounts)  
     
while t == True:
    price = input('Enter the price: ')
    
    if price == 'done':
        t = False
    else:
        purchase_amounts.append(price)  
        print(purchase_amounts)

lst = [10.10, 20.20, 30.30, 40.40]

n1 = lst.pop()
n2 = lst.pop()

print(n1+n2)


dog_types = ["Lab", "Pug", "Poodle"]

if "Pug" in dog_types:
    dog_types.remove("Pug")
else:
    print("no Pug found")
print(dog_types)

dogs = ["Lab", "Pug", "Poodle", "Poodle", "Pug", "Poodle"]

print(dogs)
while "Poodle" in dogs:
    dogs.remove("Poodle")
    print(dogs)
 
numbers = [2, 3, 2]
total = 0
while numbers:
    total += numbers.pop()
    print(total)
    print(numbers)
    
days = [12, 9, "Monday",  1]
#days.remove("Friday") # Error


days_of_week = [1,2,3,4,5,6,7]

for i in days_of_week:
    if not i % 2 == 0:
        print(i)
        
for i in phone_letters:
    print(index,'\n', i)
    index +=1
        
phone_letters = [1, 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ', '*', ' ', '#']
index = 0


for i in phone_letters:
    print(i)

last = len(phone_letters)
print(last)

for i in phone_letters:
    print(phone_letters[last-1])
    last = last - 1 


 

def ListOmatic():  
    #while len(list1) == 0:
    list1 = lst  
    inp1 = input('Enter some Animal name: ')
    
    def list_o_matic_Function():        
        inp = inp1      
        if inp == "":
            item = list1.pop()
            print(list1)
            print('Last item', item, ' removed from the list')
        elif inp in list1:
            list1.remove(inp)
            print(list1)
            print(inp, ' removed from the list')
        else:
            list1.append(inp)
            print(list1)
            print(inp, ' added to the list')
        #ListOmatic()
        
    if not inp1 == 'q':
        list_o_matic_Function()
        
    else:
        print('Goodby')
        
        
    
lst = ['cat', 'dog', 'a', 'b'] 
    
ListOmatic()  



lst = [1,2,3,4,5,6,7,8,9]

tot = 0

for i in lst:
    tot +=i
    print( i * 2)
    
print('Total is: ', tot)

lst = ['a','b','c','d','e']
conct = ''
for i in lst:
    conct +=i  
print(conct)


def city_search(search_item, cities = ["New York", "Shanghai", "Munich", "Tokyo"] ):
    for city in cities:
        if city.lower() == search_item.lower():
            return True
        else:
            # go to the next item
            pass
    # no more items in list
    return False

# a list of cities
visited_cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
search = input("enter a city visited: ")
# Search the default city list
print(search, "in default cities is", city_search(search))
# search the list visited_cities using 2nd argument
print(search, "in visited_cites list is", city_search(search,visited_cities))


students = ["Alton", "Hiroto", "Skye", "Tobias"]
for student in students:
    print("Hello", student)

cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]

for city in cities:
    if city.startswith("P"):
        print(city)
    elif city.startswith("D"):
        print(city)

sub_total = 0
temp = 0
for item in range(25,46,5):
    temp = sub_total
    sub_total += item
    print("sub_total:", temp, "+", item, "=",sub_total)
print("Total =", sub_total)

spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

for index in range(0,len(spell_list),2):
    print(spell_list[index])

seq=range(0,5)
for x in seq:
    print(x)
    
numbers = ""
for x in range(7):
    numbers += str(x)
print(numbers)

numbers = ""
for x in range(2,8,2):
    numbers += str(x)
print(numbers)

numbers = ""
for x in range(2,8,2):
    numbers += str(x)
print(numbers)


visited_cities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
wish_cities = ["Reykjavík", "Moscow", "Beijing", "Lamu"]

# .extend() 
visited_cities.extend(wish_cities)
print("ALL CITIES",visited_cities)

visited_cities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
wish_cities = ["Reykjavík", "Moscow", "Beijing", "Lamu"]

print('ALL CITIES',visited_cities + wish_cities)


quiz_scores = [20, 19, 20, 15, 20, 20, 20, 18, 18, 18, 19]

# use .sort()
quiz_scores.sort()
print("quiz_scores:", quiz_scores)

game_points = [20, 19, 20, 15, 20, 20, 20, 18, 18, 18, 19]
# use sorted()
sorted_points = sorted(game_points)

print("game_points:", game_points)
print("sorted_points:", sorted_points)

cities_1 = ["Dubai", "Mexico City", "São Paulo", "Hyderabad"]

print("Unsorted", cities_1)
cities_1.sort()
print("Sorted", cities_1)

cities_2 = ["Dubai", "Mexico City", "São Paulo", "Hyderabad"]
print(sorted(cities_2))


scores = [ 0, 5, 2, 11, 1, 9, 7]

scores.reverse()  
print(scores) 
'''
'''
Rotate

import collections

d = collections.deque([1,2,3,4,5])
d.rotate(3)

print(d)
'''

def rotate(l, x):
  return l[-x:] + l[:-x]

print(rotate([1,2,3,4,5,6], 3))
print(rotate("abcdef", 13))









