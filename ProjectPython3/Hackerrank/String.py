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

'''
Sample Input

AABCAAADA
3   
Sample Output

AB
CA
AD
'''

def merge_the_tools(string, k):
    out = string[0]
    for str in string[1:]:
        if out != str:
            print(out + str)
            out = str
            continue
        
            
#merge_the_tools("AABCAAADA", 3)   

string, k = input('enter'), int(input('enter')) 
for part in zip(*[iter(string)] * k):
    print()
        
    
    
    
'''
    out = part[0]
    for p in part[1:]:
        for i in range(1, k-1):
            if out != p:
                print(out + p)
                out = p
'''            
'''
S, N = input('enter'), int(input('enter')) 
for part in zip(*[iter(S)] * N):
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))           
'''        
'''
4
1 4 3 2
'''
n = int(input())

arr = map(int, input().rstrip().split())
print(" ".join(map(str, arr[::-1])))













































