'''
Created on 24-May-2018

@author: Titan
'''
from calendar import firstweekday

if __name__ == '__main__':
    pass

import calendar

print(calendar.TextCalendar(firstweekday=7).formatyear(2018))

print(calendar.weekday(int('2018'), int('05'), int('25')))
#thrusday = 3




