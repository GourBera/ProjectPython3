'''
Created on May 24, 2018

@author: berag
'''
from pip._vendor import retrying
from pip._internal.cmdoptions import retries


if __name__ == '__main__':
    pass
'''
how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""


print(snake_string * how_many_snakes)
'''

'''
def test(retries = 3):
    raise ArithmeticError
    print('error')
        
test()


def call_api():
    if bad_things():
        raise RuntimeError("Error")

'''
print(int("Dog"))


names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
    
    






























