'''
Created on Apr 24, 2018

@author: berag

'r'     read only mode
'w'     write - overwrites file with same name
'w+'     write and read mode - overwrites file with same name
'r+'     read and write mode (no overwrite)
'a'     opens for appending to end of file (no overwrite)
'a+'     opens for appending to end of file (no overwrite) plus read

'w+' - when we write into file pointer will be at the end / use seek(0) 

.open()
.read()
.write() 

sorted(obj)

.readlines()
.readline()
.strip()
.close()
.seek()
    file.seek(offset, whence)
    whence mode     description
        0                points to the beginning of the file
        1                points to the current location
        2                points to the end of the file & offset is always 0

'''

if __name__ == '__main__':
    pass


poem_file = open('poem1.txt', 'r') 
#content = poem_file.read()
#print(content)
'''
char5 = poem_file.read(10)
print(char5, '\n')
char5 = poem_file.read(10) #Print next 10 line
print(char5, '\n')

char5 = poem_file.read(10)
print(char5[2:5])

char5 = poem_file.read(10).title()
print(char5, '\n')

char5 = poem_file.read(10).upper()
print(char5, '\n')

char5 = poem_file.read(10).lower()
print(char5, '\n')

char5 = poem_file.read(10).isdigit()
print(char5, '\n')

char5 = poem_file.read(2).isalpha()
print(char5, '\n')
'''
'''
poem_lines = poem_file.readlines() #Store inside List
#print(poem_lines) #Type = List
i = 0
for line in poem_lines:
    poem_lines[i] = line[:-1]
    i +=1
    
for i in poem_lines:
    print(i) 
 
poem_file.close()
'''
'''
l1 = poem_file.readline()
print(l1)

l2 = poem_file.readline()
print(l2)

l3 = poem_file.readline()
print(l3)
'''
'''
line = poem_file.readline()

while line:
    print(line[:-1].upper())
    line = poem_file.readline()
'''
'''
poem_line = poem_file.readline().strip()

while poem_line:
    print(poem_line)
    poem_line = poem_file.readline().strip()
    
poem_file.close()
'''
'''
color = poem_file.readline().strip('*\n') #Strip any * and \n fron the str (begining and end)

while color:
    print(color)
    color = poem_file.readline().strip('*\n')

poem_file.close()
'''
'''
new_file = open('new_file.txt', 'w')
new_file.write("This is line #1 with 'w'\nThis is line #2 with 'w'\nThis is line #3 withn 'w'!\n")

new_file.close()

new_file = open('new_file.txt', 'r')

new_text = new_file.read()
print(new_text)

new_file.close()
'''
'''
new_file = open('file1.txt', 'w+')

new_text = new_file.read()
print(new_text)

new_file.write("This is line #4 with 'w+'\nThis is line #5 with 'w+'\n")

new_file.seek(0)
new_text = new_file.read()
print(new_text)
'''
'''
new_file = open('file1.txt', 'w+')
new_file.write("This is line #1 with 'w'\nThis is line #2 with 'w'\nThis is line #3 withn 'w'!\n")
read = new_file.read()
print(read)
new_file.seek(5) #5 character / new_file[5:]
read = new_file.read()
print(read)
'''
'''
tips_file = open('file2.text', 'w+')
# [ ] review and run example - setting pointer to end of file with whence value = 2
tips_file.seek(0,2)
tips_file.write("-use seek(0,2) to set read/write at end of file\n")

# read from beginning of file - .seek(0,0) is same as .seek(0)
tips_file.seek(0,0)
tips_text = tips_file.read()
print(tips_text)

# [ ] review and run example - point to file beginning and overwrite 1st line
tips_file.seek(0)
tips_file.write('-use simple function and variable names\n'.upper())

# [ ] review and run example - show new file contents
tips_file.seek(0,0)
tips_text = tips_file.read()
print(tips_text)
'''
'''
def logger(log):
    log_entry = input("enter log item (enter to quit): ")
    count = 0

    while log_entry:
        count += 1
        log.write(str(count) + ": " + log_entry + "\n")
        log_entry = input("enter log item (enter to quit): ")
        
    return count

log_file = open('log_file.txt', 'w+')
log_file.close()
log_file = open('log_file.txt', 'a+')
logger(log_file)    

log_file.seek(0)
log_text = log_file.read()

print()
print(log_text)
log_file.close()
'''
'''
count_file = open("count_file.txt", "w+")

count_file.write("Count is: 0")
count_file.seek(0)
print(count_file.readline().strip())
count_file.close()

count_file = open("count_file.txt", "r+")

count_file.seek(0)
count_line = count_file.readline().strip()
print("BEFORE\n" + count_line)

# get the int character(s) after the colon and space, cast and increment
count = int(count_line[10:])+1
count_file.seek(10)
count_file.write(str(count))

count_file.seek(0)
print("\nAFTER\n" + count_file.readline().strip())

count_file.close()

def inc_count(cnt_file):
    cnt_file.seek(0,0)
    cnt_line = cnt_file.readline().strip()
    cnt = int(cnt_line[10:])+1
    cnt_file.seek(10,0)
    cnt_file.write(str(cnt))
    return cnt

count_file = open("count_file.txt", "r+")

count_file.seek(0)
count_line = count_file.readline().strip()
print("BEFORE\n" + count_line)

for i in range(4):
    count = inc_count(count_file)
    count_file.seek(0)
    print("\nAFTER inc_count() call", i+1, "\n" + count_file.readline().strip())

count_file.close()
'''
















