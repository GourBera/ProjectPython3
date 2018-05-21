'''
Created on May 9, 2018

@author: berag
'''

if __name__ == '__main__':
    pass

# Crafting Input

# Define a variable called webpage that holds a string that causes our lexical
# analyzer to produce the exact output below

# LexToken(WORD,'This',1,0)
# LexToken(WORD,'is',1,5)
# LexToken(LANGLE,'<',2,11)
# LexToken(WORD,'b',2,12)
# LexToken(RANGLE,'>',2,13)
# LexToken(WORD,'webpage!',2,14)


webpage = """This is   
<b>webpage!"""



import ply.lex as lex

tokens = ('LANGLE', # <
          'LANGLESLASH', # </
          'RANGLE', # >
          'EQUAL', # =
          'STRING', # "hello"
          'WORD', # Welcome!
          )

t_ignore = ' ' # shortcut for whitespace

def t_newline(token):
    r'\n'
    token.lexer.lineno += 1
    pass

def t_LANGLESLASH(token):
    r'</'
    return token

def t_LANGLE(token):
    r'<'
    return token

def t_RANGLE(token):
    r'>'
    return token

def t_EQUAL(token):
    r'='
    return token

def t_STRING(token):
    r'"[^"]*"'
    token.value = token.value[1:-1]
    return token

def t_WORD(token):
    r'[^ <>\n]+'
    return token


htmllexer = lex.lex()
htmllexer.input(webpage)
while True:
    tok = htmllexer.token()
    if not tok: break
    print(tok)
    
    
def t_NUM_decimal(token):
  r'[0-9]+'
  token.value = int(token.value) # won't work on hex numbers!
  token.type = 'NUM'
  return token

t_ignore = ' \t\v\r'

def t_error(t):
  print("Lexer: unexpected character " + t.value[0])
  t.lexer.skip(1) 

# We have included some testing code to help you check your work. You will
# probably want to add your own additional tests. 
lexer = lex.lex() 

def test_lexer(input_string):
  lexer.input(input_string)
  result = [ ] 
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [(tok.type, tok.value)]
  return result    
    
    
    
