'''
Created on May 9, 2018
@author: berag

\ -> Excape char
. -> Any char except newLine
-? -> - and rest
^ -> not 
*
+
\n -> New Line



'''

if __name__ == '__main__':
    pass

import re
'''
a1 = re.findall(r"[0-9]", "Her bday was 8-june-1993")
print(a1)

a2 = re.findall(r"[A-Z]", "Her bday was 8-june-1993")
print(a2)

a3 = re.findall(r"[a-z][1-9]", "a1 2b cc4 dd4")
print(a3)

print(re.findall(r"[a]+", "a aa aaa aaaa aaaaaa.... ")) # + takes only the bigger numbers
print(re.findall(r"[0-9]+", "13 from 1 in 1992"))   #['13', '1', '1992']
print(re.findall(r"[0-7]+", "13 from 1 in 1992")) #['13', '1', '1', '2']

print(re.findall(r"[0-9][ ][0-9]+", "a1 2b cc3 44d")) #['1 2', '3 44']
print(re.findall(r"[0-9]+%", "1% 5896% 96520% % cbc% 1ac%")) #['1%', '5896%', '96520%']
print(re.findall(r"[0-9]+:", "1: 5896: 96520: : cbc: 1ac:")) #['1:', '5896:', '96520:']
print(re.findall(r"[0-9]+:%", "1:% 5896:% 96520:% : cbc:% 1ac:%")) #['1:%', '5896:%', '96520:%']

print(re.findall(r"[a-z]+| [0-9]+", "Gour 1992")) #['our', '1992']
print(re.findall(r"[a-z A-Z]+|[0-9]+", "Gour 1992")) #['Gour', '1992']
'''
'''
# Assign to the variable regexp a regular expression that matches either the
# exact string ab or one or more digits.

regexp = r"ab|[0-9]+"

# regexp matches:

print(re.findall(regexp,"ab") == ["ab"])
#>>> True
print(re.findall(regexp,"1") == ["1"])
#>>> True
print(re.findall(regexp,"123") == ["123"])
#>>> True

# regexp does not match:
print(re.findall(regexp,"a") != ["a"])
#>>> True
print(re.findall(regexp,"abc") != ["abc"])
#>>> True
print(re.findall(regexp,"abc123") != ["abc123"])
#>>> True 

print(re.findall(r"-?[0-9]+", "1861-1941 R. Tagore"))   #['1861', '-1941']
'''
'''
# Escape Sequence

a = 'I said "Hello."'
b = "I said \"Hello.\""

print(a)
print(b)
print(a == b)

regexp = r"\+\+" # To find ++
print(re.findall(regexp,"ab++ bc+* cd+-"))
'''
'''
# Assign to the variable regexp a Python regular expression that matches
# lowercase words (a-z) or singly-hyphenated lowercase words.

# Hint: It may not be possible to get correctly - do your best!

regexp = r"[a-z]+-?[a-z]+"

# regexp matches:

print(re.findall(regexp,"well-liked") == ["well-liked"])
#>>> True
print(re.findall(regexp,"html") == ["html"])
#>>> True

# regexp does not match:
print(re.findall(regexp,"a-b-c") != ["a-b-c"])
#>>> True
print(re.findall(regexp,"a--b") != ["a--b"])
#>>> True
'''
'''
regexp = r"[a-z]+\( *[0-9]+ *\)"     # \ escape

# regexp matches:

print(re.findall(regexp,"cos(0)") == ["cos(0)"])
#>>> True
print(re.findall(regexp,"sqrt(   2     )") == ["sqrt(   2     )"])
#>>> True

# regexp does not match:
print(re.findall(regexp,"cos     (0)") != ["cos     (0)"])
#>>> True
print(re.findall(regexp,"sqrt(x)") != ["sqrt(x)"])
#>>> True
'''
'''
regexp = r"[0-9].[0-9]" # . any single value
print(re.findall(regexp,"1a1 2z2 cc3(1aa1 aa2.8")) # ['1a1', '2z2', '3(1', '2.8']

regexp = r"[0-9][^ab]" 
print(re.findall(regexp,"1a1 2z2 cc3(1aa1 aa2.8")) # ['1 ', '2z', '2 ', '3(', '1 ', '2.']

regexp = r"(?:mi|re|do)+"  #
print(re.findall(regexp,"mimi rere midore doo-wop"))    #['mimi', 'rere', 'midore', 'do']
'''
'''
# Tricky REs with ^ and \

# Assign to regexp a regular expression for double-quoted string literals that
# allows for escaped double quotes.

# Hint: Escape " and \
# Hint: (?: (?: ) )

import re

regexp = r'"(?:[^\)]|?:\\.) )*"'

# regexp matches:
print(re.findall(regexp,'"I say, \\"hello.\\""') == ['"I say, \\"hello.\\""'])
#>>> True
# regexp does not match:
print(re.findall(regexp,'"\\"') != ['"\\"'])
#>>> True
'''
'''
# FSM Simulation

edges = {(1, 'a') : 2,
         (2, 'a') : 2,
         (2, '1') : 3,
         (3, '1') : 3}

accepting = [3]

def fsmsim(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        if (current, letter) in edges:
            destination = edges[(current, letter)]
            remaining_str = string[1:]
            return fsmsim(remaining_str, destination, edges, accepting)
        # QUIZ: You fill this out!
        # Is there a valid edge?
        # If so, take it.
        # If not, return False.
        # Hint: recursion.

print(fsmsim("aaa111",1,edges,accepting))
# >>> True
'''
'''
regexp = r"[0-9]+" 
b = re.findall(regexp,"""The Act of Independence of Lithuania was signed 
on February 16, 1918, by 20 council members.""")
sum = 0
for i in b:
    sum += int(i)

print(sum)
'''
'''
regexp = r'(?:[a-z]+-[a-z]+)|(?:[a-z]+)'

# This problem includes an example test case to help you tell if you are on
# the right track. You may want to make your own additional tests as well.

test_case_input = """the wide-field infrared survey explorer is a nasa
infrared-wavelength space telescope in an earth-orbiting satellite which
performed an all-sky astronomical survey. be careful of -tricky tricky-
hyphens --- be precise."""

test_case_output = ['the', 'wide-field', 'infrared', 'survey', 'explorer',
'is', 'a', 'nasa', 'infrared-wavelength', 'space', 'telescope', 'in', 'an',
'earth-orbiting', 'satellite', 'which', 'performed', 'an', 'all-sky',
'astronomical', 'survey', 'be', 'careful', 'of', 'tricky', 'tricky',
'hyphens', 'be', 'precise']

if re.findall(regexp, test_case_input) == test_case_output:
  print("Test case passed.")
else:
  print("Test case failed:" )
  print(re.findall(regexp, test_case_input))
'''


# Email Addresses & Spam
#
# In this assignment you will write Python code to to extract email
# addresses from a string of text. To avoid unsolicited commercial email
# (commonly known as "spam"), users sometimes add the text NOSPAM to an
# other-wise legal email address, trusting that humans will be smart enough
# to remove it but that machines will not. As we shall see, this provides
# only relatively weak protection. 
#
# For the purposes of this exercise, an email address consists of a
# word, an '@', and a domain name. A word is a non-empty sequence
# of upper- or lower-case letters. A domain name is a sequence of two or
# more words, separated by periods. 
#
# Example: wes@udacity.com
# Example: username@domain.name
# Example: me@this.is.a.very.long.domain.name
#
# If an email address has the text NOSPAM (uppercase only) anywhere in it,
# you should remove all such text. Example: 
# 'wes@NOSPAMudacity.com' -> 'wes@udacity.com' 
# 'wesNOSPAM@udacity.com' -> 'wes@udacity.com' 
#
# You should write a procedure addresses() that accepts as input a string.
# Your procedure should return a list of valid email addresses found within
# that string -- each of which should have NOSPAM removed, if applicable. 
#
# Hint 1: Just as we can FIND a regular expression in a string using
# re.findall(), we can also REPLACE or SUBSTITUTE a regular expression in a
# string using re.sub(regexp, new_text, haystack). Example: 
# 
# print re.sub(r"[0-9]+", "NUMBER", "22 + 33 = 55") 
# "NUMBER + NUMBER = NUMBER" 
#
# Hint 2: Don't forget to escape special characters. 
#
# Hint 3: You don't have to write very much code to complete this exercise:
# you just have to put together a few concepts. It is possible to complete
# this exercise without using a lexer at all. You may use any approach that
# works. 


import ply.lex as lex
import re 


tokens = ('EMAIL',)
def t_EMAIL(token):
    r'[a-zA-Z]+@(?:[a-zA-Z]+\.)+[a-zA-Z]+'
    token.value = re.sub(r"NOSPAM", "", token.value)
    return token

def t_error(t):
    t.lexer.skip(1)
# Fill in your answer here. 

def addresses(haystack): 
    lexer = lex.lex()
    lexer.input(haystack)
    result = []
    while True:
        tok = lexer.token()
        if not tok: break
        result = result + [(tok.value)]
    return result
    
# We have provided a single test case for you. You will probably want to
# write your own. 
input1 = """louiseNOSPAMaston@germany.de (1814-1871) was an advocate for
democracy. irmgardNOSPAMkeun@NOSPAMweimar.NOSPAMde (1905-1982) wrote about
the early nazi era. rahelNOSPAMvarnhagen@berlin.de was honored with a 1994
deutsche bundespost stamp. seti@home is not actually an email address."""

output1 = ['louiseaston@germany.de', 'irmgardkeun@weimar.de', 'rahelvarnhagen@berlin.de']

print(addresses(input1) == output1)



    

















