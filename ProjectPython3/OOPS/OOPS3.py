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
        self.marks = int(self.marks * self.per_rise)
        
    @classmethod
    def set_percentage_rise(cls, per_rise):
        cls.per_rise(per_rise)
        
    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday == 6:
            return False
        return True
    #debugging and logging purpose (useful when we get un-ambigious result)
    def __repr__(self):
        return "Student('{}', '{}', '{}')".format(self.first, self.last, self.marks)
    
    #redable representation of an object. For end users
    def __str__(self):
        return '{}', '{}', '{}'.format(self.first, self.last, self.marks)
        
        
        
Std1 = Student('Gour', 'Bera', 80)
Std2 = Student('Tulsi', 'raman', 60)
Std3 = Student('Tulsi', 'raman', 60)


print(Std1.email)
print(Std1.marks)
Std1.apply_percentage_rise()
print(Std1.marks)  
print(Student.no_of_Std)


'''
class method
'''
Std1.set_percentage_rise(5)
Std1.apply_percentage_rise()
print(Std1.marks)

'''
Static method
'''

import datetime
mydate = datetime.date(2018, 7, 3)

print(Student.is_workday(mydate))


print(repr(Std1))
print(repr(Std2))
print(Std1.__repr__())
print(Std1.__str__())