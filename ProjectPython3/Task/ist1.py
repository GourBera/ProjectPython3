'''
Created on 20-Apr-2018

@author: Titan
'''


a = [1, 3, 4, 2] 
print(a)
B = [[1, 2, 3], [4, 5, 7]] 
print(B)
C = [1 + 2, "a" * 5, 3]
print(C)

x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]

print(x[2][0])
print(x[2][:2])

x = ["a", "b", "c", "d"]
x[1] = "r"
x[2:] = ["s", "t"]
print(x)

# Deep Copy
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Create areas_copy
areas_copy = areas[:]
# Change areas_copy
areas_copy[0] = 5.0
# Print areas
print(areas)

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
# Paste together first and second: full
full = first + second
# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)
# Print out full_sorted
print(full_sorted)

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50, 20.0, 20.0]
# Print out the index of the element 20.0
print(areas.index(20.0))
# Print out how often 14.5 appears in areas
print(areas.count(14.5))
areas.reverse()
print(areas)


