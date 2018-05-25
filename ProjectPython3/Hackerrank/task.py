'''
Created on 22-May-2018

@author: Titan
'''

if __name__ == '__main__':
    pass

'''
from statistics import mean
n = int(input(""))
student_marks = {}
for _ in range(n):
    name, *line = input('').split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input('')
result = student_marks[query_name]
print(mean(result))
'''
'''
for i in range(int(input('enter'))):
    a, b = input('prompt').split(" ")
    try:
        print(int(a) / int(b))
    except Exception as e:
        print(e)
'''
'''
number = int(input('input'))
while number > 0:
    a, b = input('input').split(" ")
    try:
        print(int(a) // int(b))
    except Exception as e:
        print("Error Code: {}".format(e))
    number -= 1 
'''
        
  
'''  
1, 4
'''
'''
number, output = map(int, input('enter').split())
#print(number**3 + number**2 + number + 1 == output)

f = lambda x:eval("x**3 + x**2 + x + 1")
print(f(number) == output)
'''
'''
input, output = map(int, input('enter').split())
print(output == eval("input**3 + input**2 + input + 1"))
'''
'''
5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5
''' 
'''
subject, student = map(int, input('enter').split()) 

marks = []
for _ in range(student):
    marks.append( map(float, input('enter').split()) ) 

for i in zip(*marks): 
    print( sum(i)/len(i) )  
'''   
'''
distinct_country = set()   
for i in range(int(input('prompt'))):
    country = input('prompt')
    if country not in distinct_country:
        distinct_country.add(country)
        
print(len(distinct_country))
'''
    
if __name__ == '__main__':
    from statistics import mean
    
    nofstud = int(input('enter'))
    student_marks = {}
    
    for _ in range(nofstud):
        line = input('neter').split()
        name, scores = line[0], line[1:]
        scores = list(map(float, scores))
        student_marks[name] = scores
        
    query_name = input('enter')
    query_scores = student_marks[query_name]
    print("{0:.2f}".format(mean(query_scores)))
    #print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))    
    
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    
    
    
    

    
    
    
    
    
    






















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    