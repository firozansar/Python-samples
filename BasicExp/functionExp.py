#!/usr/bin/env python3
from math import sqrt

# define a function
def func1():
  print ("I am a function")

# function that takes arguments
def func2(arg1, arg2):
  print ("{0} {1}".format(arg1, arg2))

# function that returns a value
def cube(x):
  return x*x*x

# function with default value for an argument
def power(num, x=1):
  result = 1
  for i in range(x):
    result = result * num  
  return result

#function with variable number of arguments
def multi_add(*args):
  result = 0
  for x in args:
    result = result + x
  return result

# func1()
# print func1()
# print func1
# func2(10,20)
print (func2(10,20))
print (cube(3))
print (power(2))
print (power(2,3))
print (power(x=3, num=2))
print (multi_add(4,5,10,4))


print ("**** Math ********")

# print(sqrt(16))

def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print ("{0} squared is {1}.".format(n, squared))
  return squared

# print(square(4))

def biggest_number(*args):
  print (max(args))
  return max(args)
    
def smallest_number(*args):
  print (min(args))
  return min(args)

def distance_from_zero(arg):
  print (abs(arg))
  return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

print ("**** Tax and Tip Calculator ********")

def tax(bill):
  """Adds 8% tax to a restaurant bill."""
  bill *= 1.08
  print ("With tax: {0}".format(bill))
  return bill

def tip(bill):
  """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print ("With tip: {0}".format(bill))
  return bill
  
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

print ("**** Grades Calculator ********")
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print (grade)

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

# print_grades(grades)
# print(grades_sum(grades))
# print(grades_average(grades))

print ("**** Lambda ********")

# lambda x: x % 3 == 0

# Is the same as

# def by_three(x):
#   return x % 3 == 0

my_list = range(16)
filterted = filter(lambda x: x % 3 == 0, my_list)
for f in filterted:
    print (f)

languages = ["HTML", "JavaScript", "Python", "Ruby"]

filtLang = filter(lambda x: x == "Python", languages)
for f in filtLang:
    print (f)

numbers = [x ** 3 for x in range(1, 11)]
cubes = filter(lambda x: x % 3 == 0, numbers)
for n in cubes:
    print (n)




