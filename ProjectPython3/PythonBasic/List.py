'''
Created on Apr 2, 2018

@author: berag
'''

if __name__ == '__main__':
    pass

lst = []
print(lst)

items = [1, "val1", "val2", 1]
print(items)
print(type(items))

items.append("val3")
print(items)

items.insert(3, "val2.5")
print(items)

print(items.count("val1"))

print(items.index("val1", 1, len(items))) #Find


try:
    print(items.index("val1", 3, len(items)))
except:
    print("Not Found")    
finally:
    print("Not Found")

print(items[2])

for i in items:
    print(i)


items.pop(4)
print(items)

items.remove(1)
print(items)

items.reverse()
print(items)

#empty list
items.clear()
print(items)




