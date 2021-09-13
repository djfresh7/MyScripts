import operator
import random

ops = {'+': operator.add, '-': operator.sub, 'x': operator.mul}

g = [3, 2, 5]

r = random.randrange(1, 10)
print(r)

# function that says if weekday is false and vacation is true then return True.
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

# function that returns a string for a set number of times.
def string_times(str, num):
  return str * num
# lets test it
t = string_times("might", 2)
print(t)

def hello_name(name):
  return "Hello! " + name

# lets test it
l = hello_name("bob")
print(l)

# function to see if the beginning & end of a list is 6, then return true and if not then return false.
r = 6
def first_last(list):
  if list[0] == 6 or list[-1] == 6:
    return True
  else:
    return False
# lets test it
y = first_last([6, 3, 5])
print(y)

# how to add something to a variable without it being there before.
d = "yo"
d = d + "yes"
d += "no"
print(d)

# for loop that prints each letter in d twice.
f = ""
for letter in d:
  f += letter*2 # or f = f + letter*2
print(f)

# function that returns each letter in the given str twice.
def double_char(str):
  t = ""
  for letter in str:
    t += letter*2
  return t
# lets test it
j = double_char("yo")
print(j)

def str_int(txt):
  return int(txt)

print(str_int("1"))

def calculator(num1, operator, num2):
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*" or operator == "x":
    return num1 * num2
  elif operator == "/":
    return num1 / num2
  elif operator == "/" and num2 == 0:
    return "Can't divide by 0!"
  else:
    pass

r = calculator(4, "/", 2)
print(r)

def stutter(word):
  return word[0:2] + "... " + word[0:2] + "... " + word + "?"

print(stutter("interesting"))

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif not a_smile and not b_smile:
    return True
  elif not a_smile and b_smile:
    return False
  elif b_smile and not a_smile:
    return True
  elif a_smile and not b_smile:
    return False
  else:
    return False

print(monkey_trouble(True, True))

del str_int
del calculator
del stutter
del monkey_trouble
del r 

def alarm_clock(day, vacation):
  weekdays = [1, 2, 3, 4, 5]
  weekends = [6, 0]
  for day in weekdays:
    if day and vacation:
      return "10:00"
    elif day and not vacation:
      return "7:00"
    else:
      break
      for dayoff in weekends:
        if dayoff and not vacation:
          return "10:00"
        elif dayoff and vacation:
          return "off"
        else:
          break

del alarm_clock

def non_start(a, b):
  y = a[1:]
  t = b[1:]
  return y + t

print(non_start("you", "no"))

del non_start

def make_abba(a, b):
  return a + b + b + a

def extra_end(word):
  e = word[-2] + word[-1]
  return e*3

del extra_end

def without_end(str):
  r = str[1:-1]
  return r

print(without_end("whatthe"))

def reverse3(nums):
    return nums[::-1]

def middle_way(a, b):
    return a[1:-1] + b[1:-1]

def same_first_last(nums):
    if nums > 1 and nums[0] == nums[-1] or nums[-1] == nums[0]:
        return True
    else:
        return False

def sum2(nums):
    return sum(nums[0:2])

def has23(nums):
    if 2 in nums or 3 in nums:
        return True
    else:
        return False

def make_ends(nums):
    return [nums[0], nums[-1]]

def max_end3(nums):
    if nums[0] > nums[-1]:
        return nums[0], nums[0], nums[0]
    elif nums[-1] > nums[0]:
        return nums[-1], nums[-1], nums[-1]
    elif nums[0] == nums[-1]:
        return [nums[0], nums[0], nums[0]] or [nums[-1], nums[-1], nums[-1]]
    else:
        pass

def first_last6(nums):
    if 6 in nums[0] or 6 in nums[-1]:
        return True
    else:
        return False

def common_end(a, b):
    if [a[0]] in [b[0]] or [a[-1]] in [b[0]]:
        return True
    elif [a[0]] in [b[-1]] or [a[-1]] in [b[-1]]:
        return True
    elif [b[0]] in [a[0]] or [b[-1]] in [a[0]]:
        return True
    elif [b[0]] in [a[-1]] or [b[-1]] in [a[-1]]:
        return True
    elif [b[:]] in a or [a[:]] in b:
        return True
    else:
        return False