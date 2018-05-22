'''
Created on Mar 7, 2018

@author: berag
'''
from abc import abstractclassmethod


'''
def define a function
__init__ -define a constructor
self - object reference that is going to be call

'''


class Car():
    #pass
    def __init__(self, model, price, release):
        self.model = model
        self.price = price
        self.release = release
        
    #price will increase 10% automatically
    def price_increase(self):
        self.price = (self.price * 1.10)
        
#
'''1        
honda = Car()
volvo = Car()

honda.model = 'honda city'
honda.price = 900000
honda.release = 2017


volvo.model = 'volvo'
volvo.price = 1900000
volvo.release = 2018

print(honda.price)
#
'''
'''2
honda = Car('honda city', 100000, 2017)
volvo = Car('volvo', 100000, 2018)

print(honda.price)

honda.cc = 1500

print(honda.__dict__)
print(volvo.__dict__)

print(honda.price)
honda.price_increase()
print(honda.price)
'''
'''3
#Inheretence
class SuperCar(Car):
    #pass
    def __init__(self, model, price, release, cc):
        super.__init__(model, price, release)
        self.cc = cc

honda = SuperCar('honda city', 100000, 2017)
volvo = SuperCar('volvo', 100000, 2018)

print(honda.model)
#print(help(honda))
print(honda.price_increase())
'''

#Encapsulation - bind code and hiding data , getter/setter and atproject
from abc import ABC, abstractmethod

class SuperCar(ABC):
    @abstractmethod
    def price_increase(self, price):
        pass
      
      
class CheckPrice(Car):
    def price_increase(self, price):
        finalprice = (price * 1.10)
        return finalprice
    
    
    
honda = CheckPrice()
print(honda.price_increase(1000))    


  


#Abstruction - hide implementation details, provide only the functionality
#can not have a object of its own, it has to be inherated from parent



















































