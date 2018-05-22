'''
Created on May 22, 2018

@author: berag
'''

if __name__ == '__main__':
    pass


def print_formatted(number):
    for i in range(1, number+1):
        print("{} {} {} {}".format(i, oct(i)[2:], hex(i)[2:], bin(i)[2:]))


print_formatted(2)

str = "sdfjgkjhlksnfdhfoieryfsdbnfbf"

for i in str:
    for j in range(0, 3):
        print(i, end='')
