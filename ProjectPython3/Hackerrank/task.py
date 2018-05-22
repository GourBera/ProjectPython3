'''
Created on 22-May-2018

@author: Titan
'''

if __name__ == '__main__':
    pass


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
