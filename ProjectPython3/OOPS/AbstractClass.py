'''
Created on Mar 7, 2018

@author: berag
'''

if __name__ == '__main__':
    pass


class AbstractClass:
    
    def do_something(self):
        pass
    
    
class B(AbstractClass):
    pass
a = AbstractClass()
b = B()


from abc import ABC, abstractmethod
 
class AbstractClassExample(ABC):
 
    def __init__(self, value):
        self.value = value
        super().__init__()
    
    @abstractmethod
    def do_something(self):
        pass
'''    
class DoAdd42(AbstractClassExample):
    pass
x = DoAdd42(4)    
print(x)   
'''


class DoAdd42(AbstractClassExample):
    def do_something(self):
        return self.value + 42
    
class DoMul42(AbstractClassExample):
   
    def do_something(self):
        return self.value * 42
    
x = DoAdd42(10)
y = DoMul42(10)
print(x.do_something())
print(y.do_something()) 



'''

'''

from abc import ABC, abstractmethod
 
class AbstractDo(ABC):
    
    @abstractmethod
    def do_something(self):
        print("Some implementation!")
        
class AnotherDo(AbstractDo):
    def do_something(self):
        super().do_something()
        print("The enrichment from AnotherSubclass")
        
x = AnotherDo()
x.do_something()

'''
'''
from abc import ABC, abstractmethod 

class Employee(ABC):
    @abstractmethod
    def calculate_Sal(self, sal):
        pass
    def position(self, position):
        pass
    
    
class Developer(Employee):
    @abstractmethod
    def calculate_Sal(self, sal):
        totalsal = sal * 1.10
        return totalsal
    
    def position(self, position):
        self.position = position
        return position
    
    
    
emp1 = Developer()
#print(emp1.calculate_Sal(100))
print(emp1.position('Python devlp'))   






    
    
    
    
    
    
    
    
    
    
    
    
        