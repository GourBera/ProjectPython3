'''
Created on May 22, 2018

@author: berag
'''

if __name__ == '__main__':
    pass

'''
def print_formatted(number):
    for i in range(1, number+1):
        print("{} {} {} {}".format(i, oct(i)[2:], hex(i)[2:], bin(i)[2:]))


print_formatted(2)

       
import string
word = "word!"
print(word.strip(string.punctuation))
'''
'''

if __name__ == '__main__':
    N = int(input('enter')) 
    reminder = N % 2 

    if reminder == 0 and (2<= N <=5): 
        print('Not Weird')
    elif reminder == 0 and (6<= N <=20): 
        print('Weird')
    elif reminder == 0 and N > 20: 
        print("Not Weird")
    elif N % 2 != 0: 
        print('Weird')
'''        
        
import calendar

print(calendar.isleap(1990))




















