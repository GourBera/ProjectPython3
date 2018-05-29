'''
Created on May 24, 2018

@author: berag
'''

if __name__ == '__main__':
    pass

'''
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

print(cylinder_volume(10, 3))

def cylinder_volume_defaultValue(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2



print(cylinder_volume_defaultValue(10))



# write your function here
def population_density(population, land_area):
    return population / land_area

# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))
'''

# write your function here
def readable_timedelta(days):
    w = days // 7
    d = days % 7 # days - (w * 7)
    return "{} week(s) and {} day(s).".format(w, d)

# test your function
print(readable_timedelta(20))

egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

# buy_eggs() # UnboundLocalError: local variable 'egg_count' referenced before assignment


















