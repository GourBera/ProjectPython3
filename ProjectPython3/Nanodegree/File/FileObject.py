'''
Created on May 24, 2018

@author: berag
'''

if __name__ == '__main__':
    pass

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
















