'''
Created on 12-Apr-2018

@author: Titan
'''

if __name__ == '__main__':
    pass

'''
spam = "7"
spam = spam + "0"
print(spam)
eggs = int(spam) + 3
print(eggs)
print(float(eggs))

word = input("Enter a word: ")
print(word + ' shop')

print(17%3)

x = 5
y = x + 3
y = int(str(y) + "2")
print(y)

print(7>7.0) #False
print(8.7 <= 8.70) #True

spam = 7
if spam > 5:
   print("five")
if spam > 8:
   print("eight")
   
num = 7
if num > 3:
   print("3")
   if num < 5:
      print("5")
      if num ==7:
         print("7")
        
if not True: #By default its True
   print("1")
elif not (1 + 1 == 3):
   print("2")
else:
   print("3")
   
print(1 + 1 * 3) #4
   
if 1 + 1 * 3 == 6:
   print("Yes:")
   
else:
   print("No")

i = 3
while i>=0:
   print(i)
   i = i - 1
   
i = 5
while True:
  print(i)
  i = i - 1
  if i <= 2:
    break

nums = [5, 4, 3, 2, 1]
print(nums[1])

words = ["hello"]
words.append("world")
print(words[1])

nums = [9, 8, 7, 6, 5]
nums.append(4)
nums.insert(2, 11)
print(nums)
print(len(nums))

nums = list(range(5, 8))
print(len(nums))
print(nums)

nums = list(range(3, 15, 2))
print(nums[2])
print(nums)

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])

for i in range(10):
  if not i % 2 == 0:
    print(i+1)

while False:
  print("Looping...")

def print_numbers():
  print(1)
  print(2)
  return
  print(4)
  print(6)

print_numbers()

def print_nums(x):
  for i in range(x):
    print(i)
    return
print_nums(10)

def func(x):
  res = 0
  for i in range(x):
     res += i
  return res

print(func(4))

print("7" + 4)

try:
  variable = 10
  print (10 / 2)
except ZeroDivisionError:
  print("Error")
print("Finished")

try:
  meaning = 42
  print(meaning / 0)
  print("the meaning of life")
except (ValueError, TypeError):
  print("ValueError or TypeError occurred")
except ZeroDivisionError:
  print("Divided by zero")

print(0)
assert "h" != "w"
print (1)
assert False
print(2)
assert True
print(3)

try:
  print(1)
  assert 2 + 2 == 5
except AssertionError:
  print(3)
except:
  print(4)

primes = {1: 2, 2: 3, 4: 7, 7:17}
print(primes[primes[4]])

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))

tuple = (1, (1, 2, 3))
print(tuple[1])

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64]
print(sqs[4:7])

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[1::4])

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])

print("{0}{1}{0}".format("abra", "cad"))

str="{c}, {b}, {a}".format(a=5, b=9, c=7)
print(str)

a=min([sum([11, 22]), max(abs(-30), 2)])
print(a)
''' 
nums = [-1, 2, -3, 4, -5]
if all([abs(i) < 3 for i in nums]):
  print(1)
else:
  print(2)

nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))

def test(func, arg):
  return func(func(arg))

def mult(x):
  return x * x

print(test(mult, 2))


























































































