'''
Created on May 24, 2018

@author: berag
'''

if __name__ == '__main__':
    pass
'''
print(list(zip(['a', 'b', 'c'], [1, 2, 3])))

# You could unpack each tuple in a for loop like this.
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

# In addition to zipping two lists together, you can also unzip a list using an asterisk.
some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)
print(letters)
print(nums)


# enumerate is a built in function that returns an iterator of tuples containing indices and values of a list. You'll often use 
# this when you want the index along with each element of an iterable in a loop.

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
'''  
'''
# Zip Coordinates
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))

for point in points:
    print(point)

''' 
''' 
    
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = {} # replace with your code
cast_name_height = zip(cast_names, cast_heights)
for name, height in cast_name_height:
    #print(name, height)
    cast[name] = height

print(cast)
''' 
'''
# UnZIP
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here

names, heights = zip(*cast)

print(names)
print(heights)
'''
'''
# Zip Lists to a Dictionary

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)

# Transpose with Zip

data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)               #((0, 3, 6, 9), (1, 4, 7, 10), (2, 5, 8, 11))

# Enumerate

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])

print(cast)
'''












