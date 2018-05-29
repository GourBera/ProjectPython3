'''
Created on May 22, 2018

@author: berag

# Mathematical Operators
# Arithmetic operators
# Comparision and Logical operators in Python
# Logical operators
# Bitwise operators
# Assignment operators

######   Special operators #######

# Identity operators
# Membership operators

'''

if __name__ == '__main__':
    pass

'''
#Mathematical Operators
+
-
*
/
**
%
// - Intiger division




#Arithmetic operators

+    Add two operands or unary plus                         x + y+2
-    Subtract right operand from the left or unary minus    x - y-2
*    Multiply two operands                                  x * y
/    Divide left operand by the right one (always results into float)                                   x / y
%    Modulus - remainder of the division of left operand by the right                                   x % y (remainder of x/y)
//   Floor division - division that results into whole number adjusted to the left in the number line   x // y
**   Exponent - left operand raised to the power of right                                               x**y (x to the power y)
'''

x = 15
y = 4

# Output: x + y = 19
print('x + y =',x+y)
# Output: x - y = 11
print('x - y =',x-y)
# Output: x * y = 60
print('x * y =',x*y)
# Output: x / y = 3.75
print('x / y =',x/y)
# Output: x // y = 3
print('x // y =',x//y)
# Output: x ** y = 50625
print('x ** y =',x**y)

'''
# Comparision and Logical operators in Python

>    Greater that - True if left operand is greater than the right    x > y
<    Less that - True if left operand is less than the right    x < y
==    Equal to - True if both operands are equal    x == y
!=    Not equal to - True if operands are not equal    x != y
>=    Greater than or equal to - True if left operand is greater than or equal to the right    x >= y
<=    Less than or equal to - True if left operand is less than or equal to the right    x <= y
'''
# Output: x > y is False
print('x > y  is',x>y)
# Output: x < y is True
print('x < y  is',x<y)
# Output: x == y is False
print('x == y is',x==y)
# Output: x != y is True
print('x != y is',x!=y)
# Output: x >= y is False
print('x >= y is',x>=y)
# Output: x <= y is True
print('x <= y is',x<=y)


'''
# Logical operators

and    True if both the operands are true    x and y
or    True if either of the operands is true    x or y
not    True if operand is false (complements the operand)    not x
'''

x = True
y = False

# Output: x and y is False
print('x and y is',x and y)
# Output: x or y is True
print('x or y is',x or y)
# Output: not x is False
print('not x is',not x)

'''
# Bitwise operators

&    Bitwise AND    x& y = 0 (0000 0000)
|    Bitwise OR    x | y = 14 (0000 1110)
~    Bitwise NOT    ~x = -11 (1111 0101)
^    Bitwise XOR    x ^ y = 14 (0000 1110)
>>    Bitwise right shift    x>> 2 = 2 (0000 0010)
<<    Bitwise left shift    x<< 2 = 40 (0010 1000)


For example, 2 is 10 in binary and 7 is 111.
In the table below: Let x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)


# Assignment operators

=       x = 5       x = 5
+=      x += 5      x = x + 5
-=      x -= 5      x = x - 5
*=      x *= 5      x = x * 5
/=      x /= 5      x = x / 5
%=      x %= 5      x = x % 5
//=     x //= 5     x = x // 5
**=     x **= 5     x = x ** 5
&=      x &= 5      x = x & 5
|=      x |= 5      x = x | 5
^=      x ^= 5      x = x ^ 5
>>=     x >>= 5     x = x >> 5
<<=     x <<= 5     x = x << 5
'''

'''
######   Special operators #######

# Identity operators

is    True if the operands are identical (refer to the same object)    x is True
is not    True if the operands are not identical (do not refer to the same object)    x is not True
'''

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)
# Output: True
print(x2 is y2)
# Output: False
print(x3 is y3)


'''
# Membership operators
in    True if value/variable is found in the sequence    5 in x
not in    True if value/variable is not found in the sequence    5 not in x
'''


x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)
# Output: True
print('hello' not in x)
# Output: True
print(1 in y)
# Output: False
print('a' in y)













