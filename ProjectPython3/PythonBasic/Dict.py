dict = {}
dict.setdefault('key', 0)
dict = {'key1': 10, 'key2': 20, 'key3': 30, 'key4': 40, 'key5': 50}
print(dict)

value = dict.pop('key1')
print(value)

key, value = dict.popitem()
print(key, value)

dict['key6'] = 60
print(dict.values())

b = dict.copy()
# creates a new dictionary with keys from a sequence (such as a list, tuple, or range) and
# values set to a specified default value, which defaults to None if not specified.
print(dict.fromkeys('key1'))

print(dict.get('key1'))
print(dict.items())
print(dict.keys())

dict.clear()
print(dict)







