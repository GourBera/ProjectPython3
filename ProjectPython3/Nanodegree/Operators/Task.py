'''
Created on May 22, 2018

@author: berag
'''

if __name__ == '__main__':
    pass

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6
# decrease the rainfall variable by 10% to account for runoff ==> (1 - (10/100))
rainfall *= .9      
# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall
# increase reservoir_volume by 5% to account for stormwater that flows    ==> (1 + (5/100))
# into the reservoir in the days following the storm
reservoir_volume *= 1.05
# decrease reservoir_volume by 5% to account for evaporation  ==> (1 - (5/100))
reservoir_volume *= 0.95
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5
# print the new value of the reservoir_volume variable
print(reservoir_volume)











































