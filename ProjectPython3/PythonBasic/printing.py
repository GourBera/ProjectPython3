'''
Created on Apr 2, 2018

@author: berag
'''

Value = 20
# For details, refer "printf style formatting" [https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting ]
print("Printing Variables: %d" %Value)  # integer
print("Printing Variables: %s" %Value)  # string
print("Printing Variables: %f" %Value)  # float
print("Printing Variables: %.3f" %Value)# float with decimal digits set by user

print("\n Concatenation of string and var:", Value)


print(type(10.25))
print(type('string'))

integer = int(Value)
string = str(Value)
float = float(Value)

print()

print(integer)
print(string)
print(float)

print()

print(type(integer))
print(type(string))
print(type(float))


formatter = ("%d.%d.%d.%d")
print ("\n IP address is:" + formatter %(192, 168.11, 0, 100))
print ('\n From {} to {}'.format(10.58, 20))












