'''
Created on Mar 7, 2018

@author: berag
'''

if __name__ == '__main__':
    pass


class Student():
    
    no_of_Std = 0
    per_rise = 1.05
    
    
    def __init__(self, first, last, marks):
        self.first = first
        self.last = last
        self.marks = marks
        self.email = first + '.' +last + '@gmail.com'
        Student.no_of_Std += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_percentage_rise(self):
        self.marks = int(self.marks * 1.05)
        
        
        
Std1 = Student('Gour', 'Bera', 80)
Std2 = Student('Tulsi', 'raman', 60)
Std3 = Student('Tulsi', 'raman', 60)


print(Std1.email)
print(Std1.marks)
Std1.apply_percentage_rise()
print(Std1.marks)  
print(Student.no_of_Std)   


'''
Inheretance
'''   

class Dumb(Student):
    per_rise = 1.10
    #pass
    def __init__(self, first, last, marks, PLanguage):
        super().__init__(first, last, marks)        
        self.PLanguage = PLanguage



Std3 = Dumb('Dhanush', 'kumar', 70, 'Java')

print(Std3.PLanguage)




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        