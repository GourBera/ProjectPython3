'''
Created on May 24, 2018

@author: berag
'''

if __name__ == '__main__':
    pass

'''
cast = ["barney stinson", "robin scherbatsky", "ted mosby", "lily aldrin", "marshall eriksen"]

capitalized_cast = [cst.title() for cst in cast]
print(capitalized_cast)

# Conditionals in List Comprehensions
squares = [x**2 for x in range(9) if x % 2 == 0]
print(squares)

squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
print(squares)
'''


# Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# write your list comprehension here
first_names = [name.split()[0].lower() for name in names]
print(first_names)

# Use a list comprehension to create a list multiples_3 containing the first 20 multiples of 3.
multiples_3 = [x * 3 for x in range(1, 21)]
print(multiples_3)
print(len(multiples_3))

# Use a list comprehension to create a list of names passed that only include those that scored at least 65.

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [x for x in scores if scores[x] > 65]
print(passed)





































