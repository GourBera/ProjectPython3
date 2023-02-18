lst = []
items = [1, "val1", "val2", 1]
items.insert(3, "val2.5")
print(items.count("val1"))
# find the index of the first occurrence of a specified item | list.index(item, start, end)
print(items.index("val1", 1, len(items)))

# pop() ==> removes and returns the element at the specified index
# remove() ==> removes the first occurrence of the specified value in the list.
value_removed = items.pop(0)    # 1
items.remove(1)
items.reverse()
items.clear()





