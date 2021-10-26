#!/usr/bin/env python3
import math # Imports the math module
# everything = dir(math) # Sets everything to a list of things from math
# print (everything) # Prints 'em all!

print (type(42))
print (type(4.2))
print (type('spam'))

def is_numeric(num):
  return type(num) == int or type(num) == float

print(is_numeric(5))

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
  print (original)
else:
  print ('empty')


