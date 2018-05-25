'''
Created on May 24, 2018

@author: berag
'''

if __name__ == '__main__':
    pass

'''
# Default mode r
f = open('my_path/my_file.txt', 'r')
file_data = f.read()
f.close()

# Everything in file will be deleted in 'w' mode we should append
f = open('my_path/my_file.txt', 'w')
f.write("Hello there!")
f.close()

# with autoclose the file after processing
with open('my_path/my_file.txt', 'r') as f:
    file_data = f.read()
    
camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)

print(__name__)

'''
'''
import math
print(pow(math.e, 3))
print(math.exp(3))

'''
# Use an import statement at the top

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces

def generate_password():
    import random
    
    return ''.join(random.sample(word_list,3))


def generate_password1():
    import random 
    
    password = ""
    for i in range(3):
        word = random.choice(word_list)
        password += word
    return password
# test your function
print(generate_password())













