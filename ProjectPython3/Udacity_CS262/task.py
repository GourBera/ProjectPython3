'''
Created on May 9, 2018

@author: berag
'''

if __name__ == '__main__':
    pass
'''
# Selecting Substrings : Writing a Python Procedure

# Let p and q each be strings containing two words separated by a space.

# Examples:
#    "bell hooks"
#    "grace hopper"
#    "alonzo church"

# Write a procedure called myfirst_yoursecond(p,q) that returns True if the
# first word in p equals the second word in q. Return False otherwise.

def myfirst_yoursecond1(p,q):
    psplit = p.split()
    qsplit = q.split()
    
    if psplit[0] == qsplit[-1]:
        return True
    return False

def myfirst_yoursecond(p,q):
    ps = p.find(" ")
    qs = q.find(" ")    
    return p[:ps] == q[qs+1:]

print(myfirst_yoursecond("bell hooks", "curer bell"))
#>>> True
'''

print("Python is fun".split())
print("July-August 1842".split())
print("6*9==42".split())





























































