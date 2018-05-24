'''
Created on May 21, 2018

@author: berag
'''

if __name__ == '__main__':
    pass

'''     Use a list comprehension to build a list called even_squares in the editor.
        Your even_squares list should include the squares of the even numbers between 1 to 11. Your list should start [4, 16, 36...] and go from there.
'''

doubles_by_3 = [x * 2 for x in range(1, 20) if (x * 2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x ** 2 for x in range(1, 20) if x % 2 == 0]

print(doubles_by_3)
print(even_squares)

c = ['C' for x in range(5) if x < 3]
print(c)

'''     Use a list comprehension to create a list, cubes_by_four.
        The comprehension should consist of the cubes of the numbers 1 through 10 only if the cube is evenly divisible by four.
        Finally, print that list to the console.
        Note that in this case, the cubed number should be evenly divisible by 4, not the original number.
'''
cubes_by_four = [x ** 3 for x in range(1, 11) if ((x ** 3) % 4) == 0]
print(cubes_by_four)



'''Remove_duplicates([1, 1, 2, 2]) should return [1, 2]'''

def remove_duplicates(inputlist):
    if inputlist == []:
        return []    
# Sort the input list from low to high    
    inputlist = sorted(inputlist)
# Initialize the output list, and give it the first value of the now-sorted input list
    outputlist = [inputlist[0]]
# Go through the values of the sorted list and append to the output list
# ...any values that are greater than the last value of the output list
    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)
        
    return outputlist

'''median([2, 4, 5, 9]) should return median 4.5'''

def median(lst):
    sorted_list = sorted(lst)
   
  
    if (len(sorted_list) % 2) != 0:
        #odd number of elements
        index = len(sorted_list) // 2 
        return sorted_list[index]
        #print(sorted_list[index])
    
    elif (len(sorted_list) % 2) == 0:
        #even no. of elements        
        index_1 = (len(sorted_list)//2) - 1
        index_2 = len(sorted_list)//2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean
    
print(median([2, 4, 5, 9]))






grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
  for i in grades:
    print(i)
    
#print_grades(grades)

def grades_sum(scores):
  total = 0
  for score in scores: 
    total = total + score
  return total

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

print(grades_average(grades))

def grades_variance(grades):
    variance = 0
    for number in grades:
        variance += (grades_average(grades) - number) ** 2
    return variance / len(grades)

#print(grades_variance(grades))

def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)

#print(grades_std_deviation(variance))

def Result(grades):
    print("all of the grades")
    print(print_grades(grades))
    print("sum of grades")
    print(grades_sum(grades))
    print("average grade")
    print(grades_average(grades))
    print("variance")
    print(grades_variance(grades))
    print("standard deviation")
    print(grades_std_deviation(variance))
    
    
Result(grades)
        






























