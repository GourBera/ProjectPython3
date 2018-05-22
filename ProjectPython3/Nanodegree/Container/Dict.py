'''
Created on May 22, 2018

@author: berag

Dictionary keys must be immutable

mutable
ordered

in
not in

get('')


'''

if __name__ == '__main__':
    pass

dct = dict(a = 1, b = 2)
dct['c'] = 3
print(dct)
#print(dct['d'])     # KeyError: 'd'


#dct1 = dict(a = 1, b = 2, 3 = c)     # Key has to be of same type

elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}

helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
print(helium)
print(hydrogen_weight)



elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't
elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True

print(elements['hydrogen']['is_noble_gas'])
print(elements['helium']['is_noble_gas'])



