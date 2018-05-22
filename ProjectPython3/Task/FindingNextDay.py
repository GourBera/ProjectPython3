'''
Created on 29-Apr-2018

@author: Titan
'''

if __name__ == '__main__':
    pass


def daysInMonth1(year, month):
    return 30


def isLeapyear():
    pass
    

def daysInMonth(year, month):
    
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 2:
        return 28
    else:
        return 30
    

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # if day < 30:
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1


print(nextDay(1999, 12, 30))
print(nextDay(2013, 1, 30))
print(nextDay(2012, 12, 30))


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
       
    return False,


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    
    # YOUR CODE HERE!
    
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1    
    return days


print(daysBetweenDates(2011, 6, 30, 2012, 6, 30))
assert(daysBetweenDates(2011, 6, 30, 2012, 6, 30) == 360)


def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 57),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 360),
                  ((2011, 1, 1, 2012, 8, 8), 577),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")


test()

