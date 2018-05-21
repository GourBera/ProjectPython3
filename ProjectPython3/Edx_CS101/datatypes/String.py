'''
Created on Apr 18, 2018

@author: berag


.split()
.join()
.title()
.isdigit()
.isalpha()
.upper()
.lower()
.strip()
.startswith()

sorted(obj)

end=' ' # to print loop in same line


'''

if __name__ == '__main__':
    pass


'''
str = "Hello_World"

print(str[0])
print(str[-1])

#Slicing
print(str[:5]) #Hello : is start from 0 [same as 0:5]
print(str[6:]) #same as 6:11
print(str[4:7]) #3 letter o_w

#Step Size
str = 'ABCDEFGHIJKLMN'

print(str[:])
print(str[::2]) #Start from 0
print(str[1::2]) #Start from 1
print(str[1:10:2]) #Start from 1 to 10 step 2

#Negative Step size

str = "Hello world"
print(str[::-1]) 
print(str[4::-1]) #olleH
print(str[4::-2]) #olH

# [ ] print the first 4 letters of long_word
# [ ] print the first 4 letters of long_word in reverse
# [ ] print the last 4 letters of long_word in reverse
# [ ] print the letters spanning indexes 3 to 6 of long_word in Reverse

long_word = "timeline"

print(long_word[:4])
print(long_word[3::-1])
print(long_word[:3:-1]) or print(long_word[8:3:-1])
print(long_word[5:1:-1]) #ilem


for loop in range(0,3):
    
    str = input('Enter your name: ')
    newstr = ""

    for i in str:
    
        if not i.lower() == "Y":
            newstr += i.upper()
        else:
            newstr += i        
    
    print('Upper case of name- ' + str + ' is: ' + newstr + '\n')

    
# [ ] create & print a variable, other_word, made of every other letter in long_word
long_word = "juxtaposition"
# Mirror Color
# [ ] get user input, fav_color
# [ ] print fav_color backwards + fav_color
# example: "Red" prints "deRRed"

other_word = ""
for i in long_word:
    other_word += i
    
print('long_word is: ' + long_word + ' other_word is: '+ other_word)

fav_color = input('Enter your fav_color: ')

rev1 = fav_color[::-1]
rev2 = rev1[::-1] 

print(rev1 + rev2)
'''
'''
len() - returns a strings length
count() - returns number of times a character or sub-string occur
find() - returns index of first character or sub-string match returns -1 if no match found
'''
'''
str1 = "Enter your fav_color"

ln = len(str1)
prt = int(ln/2)

print(str1[:prt])
print(str1[prt:])

print('no.of n in first pert: ' + str(str1[:prt].count('n')))
print("no.of o in second pert: " + str(str1[prt:].count('o')))

# find the index of "u" searching a slice work_tip[3:6]
print(str1.find("y",0,15), "\n")

str1 = "abcdefabcdefabcdef"
location = str1.find('a')

while location >= 0:
    print("'a' at index: ", location)
    
    location = str1.find('a', location + 1)
print('No more a found')    
    
# [ ] use len() to find the midpoint of the string 
# [ ] print the halves on separate lines
random_tip = "wear a hat when it rains"

mid = int(len(random_tip) / 2)
print(random_tip[:mid]) or print(random_tip[mid:])  

# for letters: "e" and "a" in random_tip
# [ ] print letter counts 
# [ ] BONUS: print which letter is most frequent
random_tip = "wear a hat when it rains eeeeeeeeeee"

mf = 0
for i in random_tip:    
    print("The count of letter ", i, " is: ", random_tip.count(i), " times..")
   
    if random_tip.count(i) >= mf:
        mf = random_tip.count(i)
        
print('most frequent letter is: ', i, ' total count is: ', mf)

# [ ] Print each word in the quote on a new line
quote = "they stumble who run fast"

start = 0
space_index = quote.find(" ")

while space_index != -1:
    print(quote[start:space_index])
    start = space_index + 1
    space_index = quote.find(" ", space_index + 1)
print(quote[start:])
'''
'''
Create a program inputs a phrase (like a famous quotation) and prints all of the words that start with h-z
Sample input: enter a 1 sentence quote, non-alpha separate words: Wheresoever you go, go with all your heart

Sample output:
WHERESOEVER
YOU
WITH
YOUR
HEART
'''
'''
words = "Wheresoever you go, go with all your heart"
 
upper = words.upper()
print(upper)

splt = upper.split(" ")
print(splt)

for i in splt:
    if i[0] > 'G' and i[0] < 'Z':
        print(i)

        
words = "Wheresoever you go, go with all your heart"

word = ''

for letter in words:
    
    if letter.isalpha():
        word += letter
    elif word.lower() >= 'h':
        print(word.upper())
        word = ''
    else:
        word = ''
        
if word.lower() >= 'h':
    print(word.upper())

st = "abcdabcdabcdabcdabcd"

c = 0
for i in st:
    c +=1
    if i == 'a':
        print('a at position: ', c)

str1 = "abc def ghi jkl m"
print(str1.split())

str1 = "abcdefghijklm"
print(str1.split())

str1 = "abc-def-ghi-jkl-m"
print(str1.split('-'))

str1 = """line1
lene2
line3
line4"""
b = str1.split('\n')
print(b)

for i in b[::-1]:
    print(i)
   
    
dash = "-"
space = " "
word = "Iteration"
ellipises = "..."

dash_join = dash.join(word)
print(dash_join)
print(space.join(word))
print(ellipises.join(word))


for letter in "Concatenation":
    print(letter, end=' ')  
    
for letter in "Concatenation":
    print(letter, end='-')     

for letter in "Concatenation":
    print(letter, end='.\n') 

str1 = "Helloworld"
print(list(str1))

wisdom_list = ["mistakes", "are", "a", "part", "of", "learning"]
wisdom_string = "()".join(wisdom_list)
print(wisdom_string)

code_tip = "-PythonO-usesO-spacesO-forO-indentation"
tip_words = code_tip.split('O')
print(tip_words)

''' 

lst = []
print(len(lst))

lst = ['cat']
print(len(lst))









