# How to run a Python file = python3 or python (filename)
# How to run a Javascript file = node . or node (filename)
# How to stop any script file = CTRL + C

# All My Python Notes

# "hi" or 'get' = string in python.
# () = Parenthesis in python.
# (1) = agrument in python
# Variable: a = 2, this means that the value of a is 2.
# If, elif(else if) and else(if, elif & else clause)
# If can do something if something is different than the rest
# Use the website stackoverflow.com if you need help with coding.
# elif, else if = Can do something else if something is different
# def = define = Use this to create functions in python.
# * = times, / = divide, + & - = add & subtract
# Empty strings ("") will give a space in between things in python.
# "\n" Acts as an enter key in python, it creates new line spaces.

# import statement
# The import statement is used to import modules into your python script. You can also import methods from somewhere in a package or module and even rename it to whatever you like.
import time # import the time module
import random # import the random library
import os # The is library
# etc...

import time as t # imported the time module but renamed it to t
import random as r # imported the random module but renamed it to r
import os as opsys # imported the os module but renamed it to opsys
# etc...

from time import sleep # imported the sleep method from the time module
from random imoort randrange # imported the randrange method from the random module
from os import getcwd # imported the getcwd method from the os module
# etc...

# print statement
# The print statement prints out to the console whatever you put in the parenthesis.
# variables
t = 5
d = 8

t = d
d = t

# if statements
f = 5
g = 4

if g > f:
  print("g is greater than f")
elif f == g:
  print("they are both equal")
elif g < f + 5:
  print("f is greater than g by more than 5")
else:
  print("g isn't greater than f")

# functions
# return statement
# this statement can only be used in functions and excutes skmilar properties as the print statement.

def hello():
  print("hi")

hello()

def traits(x, y):
  print("this is the answer:")
  return x * y

l = traits(4, 8)
print(l)

# A nested function is a function inside a function.
# Example:
def func():
  pass
  def ok():
    pass

# lambda statement
# lambda is used to create an anonymous function (function with no name). It is an inline function that does not contain a return statement. It consists of an expression that is evaluated and returned.
# Anonymus Function
y = lambda g: g + t
print(y(1))
u = lambda txt: txt
print(u("My"))

# input & output
import time
name = input("Enter your name...")
print("Hi !", name, "Where ro you live?")
live = input("Enter your location...")
# you can use either + or , 
print("So you live in " + live, "? Well what's your hobby there?")
hobby = input("Enter your hobby...")
print("Ok, give me a sec...")
# using the time module
time.sleep(3)
print("Generating Data...")
time.sleep(2)
# split brackets
print(
  "Your Name: " + name,
  "Your location: " + live,
  "Your hobby: " + hobby,
)

# mappings
def mul(x):
  return x * 2

def adds(x, y):
  return x + y

m = adds(6, 8)
print(m)

def nicefunc(x, y):
  print(x)
  print("Loading...")
  return x - y

k = nicefunc(100000000, 49999999)
print(k)

# bmi calculator
name = "ME"
weight_kg = 90
height_m = 2

def bmi_cal(name, weight_kg, height_m):
  bmi = weight_kg / (height_m ** 2)
  print("bmi: ", bmi)
  if bmi < 25:
    print(name, "is overweight")
  else:
    print(name, "is not overweight")

result = bmi_cal(name, weight_kg, height_m)

# argument function
def ret(some_argument):
  print(some_argument)
  print("yay")

g = ret("what")

# lists
u = [5, 7, 2, 1]
print(u)
# append adds stuff to a list that wasn't there before
u.append(3)
print(u)
u.append("what")
print(u)
u.append([4, 3, 6, "yes"])
print(u)
# pop deletes the last item from the list
u.pop()
print(u)
# get back the first item from the list
print(u[0])
# extend extends a list by adding multiple items to it
u.extend("a", 4, 5)
print(u)
# 0 would be the first number in py, which in this list is 5.
# 1 would be second number, 2 would be the third, and 3 would be the fourth.
print(u[0]) # prints the first #
print(u[1]) # prints the second #
print(u[-1]) # prints the last #
# etc...
# Replaces a item with another item
u[0] = 300
print(u)
u[1] = 4
print(u)
# etc...
# We can access a range of items in a list by using the slicing operator :(colon).
my_list = ['p','r','o','g','r','a','m','i','z']
# elements 3rd to 5th
print(my_list[2:5])
# elements beginning to 4th
print(my_list[:-5])
# elements 6th to end
print(my_list[5:])
# elements beginning to end
print(my_list[:])

# Remove/Delete/Clear stuff from a list
my_list.remove('p')
# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)
# Output: 'o'
print(my_list.pop(1))
# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)
# Output: 'm'
print(my_list.pop())
# Output: ['r', 'b', 'l', 'e']
print(my_list)
my_list.clear()
# Output: []
print(my_list)

# Py List Methods
# append() - Add an element to the end of the list
# extend() - Add all elements of a list to the another list
# insert() - Insert an item at the defined index
# remove() - Removes an item from the list
# pop() - Removes and returns an element at the given index
# clear() - Removes all items from the list
# index() - Returns the index of the first matched item
# count() - Returns the count of the number of items passed as an argument
# sort() - Sort items in a list in ascending order
# reverse() - Reverse the order of items in the list
# copy() - Returns a shallow copy of the list

# sample code replacing banana with microsoft and microsoft with banana
# way #1
b = ["banana", "apple", "microsoft"]
temp = b[0]
b[0] = b[2]
b[2] = temp
print(b)
# way 2 (my way)
b[0] = "microsoft"
b[2] = "banana"
print(b)
# re-replacing all items to original
b[0], b[2] = b[2], b[0]
print(b)

# for loops
total2 = 0
o = ["bag", "trophy", "mug"]
# prints all the elements
for element in o:
  print(element)
# total amount for the elements
h = [7, 8, 2, 3]
total = 0
for e in h:
  print(h)
  total = total + e
print(total)
# range list from 3 to 10
# prints all numbers from 3-10 in the range
p = list(range(3, 10))
print(e)
# prints out all numbers from 4-8 in the range
v = list(range(4, 8))
print(v)
# prints all the elements in the current range vertically
for i in range(3, 10):
  print(i)
  total2 = total2 + i # this could also be total2 += i for shorter terms
print(total2)

total4 = 0
for i in range(4, 8):
  print(i)
  total4 = total4 + i
  # or
  # total2 += i
  # either way works
print(total4)

# +	Add two operands or unary plus	x + y+ 2
# -	Subtract right operand from the left or unary minus	x - y- 2
# *	Multiply two operands	x * y
# /	Divide left operand by the right one (always results into float)	x / y
# %	Modulus - remainder of the division of left operand by the right	x % y (remainder of x/y)
# // Floor division - division that results into whole number adjusted to the left in the number line	x // y
# ** Exponent - left operand raised to the power of right

# modulo operator
# divides the numbers then gives their remainder if they has it
print(6 % 4)
print(4 % 1)

print(list(range(1, 10)))
total5 = 0
for i in range(1, 10):
  if i % 3 == 0:
    total5 += i
    print(total5)

# text splits
test = "What is going on?"
test2 = test.split(" ")
print(test2)

# text joins
test3 = "_".join(test)
print(test3)

# for loop adding everything from 1-6
total = 0
for i in range(1, 6):
  total += i
print("yes", total)

# while loop adding everything from 1-6 in j
j = 1
total2 = 0

while j < 6:
  total2 += j
  j += 1
print(total2)
  
# this means that while j is less than 6
# add j to total2 which is 0
# so while j is less than 6 which means 1,2,3,4 and 5 which are all less than 6, add them to total2 which is 0 and you will get 15.

# adds everything in the variable reg_list that is greater than 0
# len = length
# i is the current index, but it could be anything
reg_list = [6, 5, 2, 1, -1, -2, -5, -6]
total3 = 0
i = 0
while i < len(reg_list) and reg_list[i] > 0:
  total3 += reg_list[i]
  i += 1
print(total3)

# for loop that adds everything in reg_list2 that isn't a negative #
reg_list2 = [7, 6, 5, 3, 1, -1, -3, -5, -6, -7]
total4 = 0
for element in reg_list2:
  if element <= 0:
    break
  total4 += element
print(total4)
# the break statement stops the while loop

total5 = 0
while True:
  total5 += reg_list2[k]
  i += 1
  if reg_list2[k] <= 0:
    break
print(total5)

# != is not equal
# == is equal
# += plus equal
# -= minus equal
# <= less than equal
# >= greater than equal

t = ["what", "no", "yes"]

# prints all numbers less than 5 that are positive
for i in range(3):
    print(t[i])

# i = index
# len = length
for i in range(len(t)):
  print(t[i])

for i in range(len(t)):
  for y in range(i + 1):
    print(t[i])

# the sum of all multiples of 3 and 5 that are less than 100
total = 0
for i in range(1, 100):
  if i % 3 == 0 or i % 5 == 0: 
    # instead of using the or statement, you could use elif.
    total += i
print(total)

thelist = [8, 7, 5, 5, 4, 3, 1, -1, -3, -5, -5, -7, -8]

total = 0
j = len(thelist) - 1

# finds the sum of all negative numbers in thelist
while thelist[j] < 0:
    total += thelist[j]
    j -= 1
print(total)

# Tuple in Py | Create a Tuple
at = ()
at = (4, 2, 3)
at = ("yo", 3, [3, 2, 5])
print(at)
# Tuple Unpacking
f = (3, 5, 1)
d, y, t = f
print(d, y, t)
# Nested Tuple
ntup = ("nah", [3, 1, 2], [5, 6, 2])
print(ntup[0][1])
print(ntup[1][2])
# However, item of mutable element can be changed
my_tuple = (4, 2, 3, [6, 5])
my_tuple[3][0] = 9    # Output: (4, 2, 3, [9, 5])
print(my_tuple)
# Tuples can be reassigned
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple)
print(my_tuple.count("r"))
print(my_tuple.index("p"))
# Membership Test
print("nah" in ntup)
print("no" in ntup)
print("p" in my_tuple)
for name in ("Yo" , "My"):
  print("Hello " + name)

# random library
import random
# random # between 1 and 10
t = random.randrange(1, 10)
print(t)
# random choice in the given list
m = [1, 5, 3, 4]
m = random.choice(m)
print(m)
# random shuffle in the above list
r = random.shuffle(m)
print(r)
# completely random item
print(random.random())

# # statement that detects a even or odd number
user_input = input("Enter a #: ")
if user_input % 2 != 0:
    print("That is odd")
else:
  print("That is even")

# Modulo Operator (%)
# The % symbol in Python is called the Modulo Operator. It returns the remainder of dividing the left hand operand by right hand operand. It's used to get the remainder of a division problem.
r = 5 % 4
print(r)
# this gives the remainder of 5 divided by 4.
v = [0, 4, 3, 7, 9]
for num in v:
  if num % 2 != 0:
    print(num)
# this prints out all the odd numbers in the list v.

# Keys & Values | Dictionaries in PY
g = {} # Creates a Dictionary called "g"

# Creating Keys with values
g["You"] = 6
g["Right"] = 4
g["Matthew"] = 1

# Printing out the values for the keys
print(g["You"])
print(g["Right"])
print(g["Matthew"])

# Changing a key's old values to a new value
g["Matthew"] = 4
print(g["Matthew"])

# keys are normally strings or numbers
# values can be any type

g[5] = 90
print(g[5])

# For loop that prints every key with their value in the g dictionary
for key, value in g.items():
  print("key", key, "", "value", value)

# pass statement
# pass is a null statement in Python. Nothing happens when it is executed. It is used as a placeholder.
# Here's a example function:

def good_func(number):
  if number != 5:
    pass
  else:
    print("# ", number)
# function that says if the number isn't 5, then do nothing.

# int = integer: 1, 3, -4, -7 (Numbers)
# float = decimals (1.3, 5.2, 8.4, 5.6)
# complex = comeplex numbers (1.5j, 5+3, 4.3k)
# str = string: "yo" "no", "entry" (Words)
# bool = boolean: True & False

# Another way to find out these values is:
print(type("smh")) # Output = str
print(type(1)) # Output = int
print(type(True)) # Output = bool

# Simple if clause statement
r = 1
t = 3

# Instead of saying if t > r:, you can say:
if True:
  print("t is greater than r")

# This statement is true so if you print it, then it will say True
bool_val = t > r
print(bool_val)

# Since bool_val is True, this is like saying above ^
if bool_val:
  print("t is greater than r")

# Function to find out if is_rainy is true and has_umbrella is false
def are_you_sad(is_rainy, has_umbrella):
  return is_rainy and not has_umbrella
# This works with the if & else clause below except the elif one though.

# if is_rainy and not has_umbrella: # same thing as saying: if is_rainy == True and has_umbrella == False:
#   return True
# elif has_umbrella and not is_rainy: # same thing as saying: elif is_rainy == False and has_umbrella == True:
#   return "imagine"
# else:
#   return False

# Lets test the function
print(are_you_sad(True, False))

# Function to return true if c is greater than d + e
def c_greater_than_d_plus_e(c, d, e):
  return c > d + e
  # if c > d + e:
  #   return True
  # else:
  #   return False

# either way is fine

# lets test it
print(c_greater_than_d_plus_e(4, 3, 5))
# and it works

# try, else, except & finally statements
# The try block lets you test a block of code for errors. The else block lets you excute a code if there aren't any exceptions. The except block lets you handle the error. The finally block lets you execute code, regardless of the result of the try and except blocks. This clause is executed no matter what, and is generally used to release external resources.

q = [
  4, 6, 1, 3,
]
for element in q:
  try:
    print(q[4])
  except IndexError:
    break
  else:
    pass
  finally:
    print("This was a try, except, else & finally clause.")
  
# yield statement

# with statement
# The with statement is used to wrap the execution of a block of code within methods defined by the context manager.
# Context manager is a class that implements __enter__ and __exit__ methods. Use of with statement ensures that the __exit__ method is called at the end of the nested block. This concept is similar to the use of try…finally block. Here, is an example.
fl = open("nothing.txt", "w")
with open("nothing.txt", "w") as fl:
  fl.write("Ok")

# global statement
# In Python, global keyword allows you to modify the variable outside of the current scope. It is used to create a global variable and make changes to the variable in a local context.
c = 30
def get():
  global c
  c += 1 # but c is already defined. How to fix that? Use global.
  return c

get()

# await statement

# assert statement
# assert is used for debugging purposes. 
# While programming, sometimes we wish to know the internal state or check if our assumptions are true. assert helps us do this and find bugs more conveniently. Assert is followed by a condition.
# If the condition is true, nothing happens. But if the condition is false, AssertionError is raised.
r = random.randrange(1, 10)
assert r # Checks if r is True and won't give any errors. In this case, r is True.
m = False
assert m # Checks if m is True and won't give errors. In this case m is False, which is the opposite of True, so it will give an error.
# This error is called AssertionError.
assert 50 > 60 # False, so AssertionError
t = "Rex"
assert t == "Mark" # False, so AssertionError
assert 9 == 9 # True, so no AssertionError
assert 4 - 1 == 3 # True, so no AssertionError
i = [False, False]
assert i # False, so AssertionError

# del statement
# The del statement is used to delete objects. This could be a variable, function, class and so much more.
v = 1
del v

# nonlocal statement
# The use of nonlocal keyword is very much similar to the global keyword. 
# The nonlocal statement is used to declare that a variable inside a nested function (function inside a function) is not local to it, meaning it lies in the outer inclosing function.
# The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.
# Use the keyword nonlocal to declare that the variable is not local.
def outer():
  t = 1
  def inner():
    nonlocal t
    t = 2
  inner()

# Here, the inner() is nested within the outer.
# The variable t is in the outer(). So, if we want to modify it in the inner(),
# we must declare it as nonlocal. Notice that a is not a global variable.
def new_function():
  r = 5
  def old_function():
    r = 10
    return "Old Function", r
  old_function()
  return "New Function", r
print(new_function())
# This is what happens when you don't use the nonlocal statement.
# Here, we do not declare that the variable a inside the nested function is nonlocal. 
# Hence, a new local variable with the same name is created, but the non-local a is not modified as seen in our output.
def myfunc1():
  f = "Yes"
  def myfunc2():
    nonlocal f
    f = "No"
  myfunc2()
  return f
print(myfunc1())

# raise statement
# The raise keyword is used to raise an exception. You can define what kind of error to raise, and the text to print to the user.
      
h = [
  "Yay", "Nah", "Meh"
]
if "Yay" in h:
  raise(NameError("Yay is there."))
else:
  print(h)

# continue statement
# The continue statement is used to skip the rest of the code inside a loop for the current iteration only. Loop does not terminate but continues on with the next iteration. The continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop. Can only be used within loops.
  
f = 1
while f < 8:
  for element in f:
    if element == 6:
      continue
  print(element)
print("Done!")

# To create a list it could be either:
# i = [] or i = list()

# simple y appended list
y = []
y.append(5)
y.append(1)
print(y)

# for loop that adds everything in y but times 2
t = []
for item in y:
  t.append(item * 2)
print(t)
# or it could be
u = [item * 2 for item in y]
print(u)

# for loop that creates a range from 1-7 without 7 (squared) and adds that to g
g = []
for x in range(1, 7):
  g.append(x ** 2)
print(g)
# and it also could be
f = [x ** 2 for x in range(1, 7)]
print(f)

# reversed numbered list
# this for loop generates the same numbers as above but reversed.
a = []
for t in range(6, 0, -1):
  a.append(t**2)
print(a)
# or it can also be
a2 = [t**2 for t in range(6, 0, -1)]
print(a2)

# another reversed list
t = [1, 2, 4, 6, 7, 10]
print(t[::-1])

# Sets in Py | Create a set
t = set()
print(t)

# add something in a set
t.add(3)
t.add(5)
print(t)

# Py rejects duplicates so if you add one thing already and you add it again, it will reject it.

# print all the items in a set
for item in t:
  print(item)

# adds all the items in alist to the s set.
s = set()
alist = [3, 3, 5, 1, 5]
for thing in alist:
  s.add(thing)
print(s)

# for loop that adds all of the set s's elements in f.
f = list()
for y in s:
  f.append(y)
print(f)

# you can add any int or str in a set:
h = set()
h.add("yo")
h.add("mo")
h.add(1)
print(h)

# sets are types of data that don't store the order in which things are added to it.

# for loop that adds all the items that don't repeat in the n set
anewlist = [1, 3, 4, 1, 4]
n = set()
for item in anewlist:
  n.add(item)
print(n)

# for loop that finds the sum of all the items in the n set.
total = 0
for item in n:
  total += item
print(total)

# or it could also be:
z = sum(n)
print(z)

# In Py, if you want to print the same str more than once, you can just add them.
w = "yes"
print(w + w)
# and etc...

# You can use the help() keyword if you need help with something in python.
help("assert") # prints information on the assert statement
# How to print the id of something
t = 5
print(id(t))

# Clesses & Objects in PY
# Self is used to represent the instance of the class in py
# __init__ is a constructor
class Bot:
  def __init__(self, name, color, weight):
    self.name = name
    self.color = color
    self.weight = weight
  
  def introduce_self(self):
    print("My name is: " + self.name)

# These objects are with the constructor called __init__
z = Bot("NotaBot", "black", 12)
m = Bot("Bot", "White", 50)

class Person:
  def __init__(self, n, p, i):
    self.name = n
    self.personality = p
    self.is_sitting = i
  def sit_down(self):
    self.is_sitting = True
  def stand_up(self):
    self.is_sitting = False

a1 = Person("Me", "cool", True)
a2 = Person("NotME", "idk", False)

a1.bot = z
a2.bot = m

a1.bot.introduce_self()

class HydroBot:
  def introduce_yself(self):
    print("Your name is ", self.name)

# Objects
# these only work with the old function called introduce_self
t1 = HydroBot()
t1.name = "Troy"
t1.color = "blue"
t1.weight = 10

me = HydroBot()
me.name = "ME"
me.color = "red"
me.weight = 5

# Run the objects
me.introduce_yself()
t1.introduce_yself()

# Arrays
t = ([3, 2, 4], [4, 6, 8])
print(t[0][0])
print([1, [4, 5, 9], 4][1][0])
print(["hi"][0])
print([True, False][0])
print([3.5, 8.9, 1.4][2])
u = lambda txt: txt
print([f"Hi: {u(1)}"])

# F strings are formatted strings.
print(f"Simple List {anewlist}")

# .format works exactly like f-strings but instead of using f"" you put the string first then put .format based on the amount of curly brackets in the string.
print("Yes: {}".format(t))

# Min() prints the smallest item in the given data.
# Max() prints the biggest item in the given data.
r = (1, 4, 5, 8)
print(min(r))
print(max(r))

h = 10
i = 1
smh = 0

while i <= h:
  smh += i
  i += 1
print(smh)
