#!/usr/bin/env python3
import random

if 8 > 9:
  print ("I don't get printed!")
else:
  print ("I get printed!")



def clinic():
    print ("You've just entered the clinic!")
    print ("Do you take the door on the left or the right?")
    answer = input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print ("This is the Verbal Abuse Room, you heap of parrot droppings!")
    elif answer == "right" or answer == "r":
        print ("Of course this is the Argument Room, I've told you that already!")
    else:
        print ("You didn't pick left or right! Try again.")
        clinic()

# clinic()

print ("******************")

print ("Lucky Numbers! 3 numbers will be generated.")
print ("If one of them is a '5', you lose!")

count = 0
while count < 3:
  num = random.randint(1, 6)
  print (num)
  if num == 5:
    print ("Sorry, you lose!")
    break
  count += 1
else:
  print ("You win!")

print ("******************")

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print ('You have...')
for f in fruits:
  if f == 'tomato':
    print ('A tomato is not a fruit!') # (It actually is.)
    break
  print ('A', f)
else:
  print ('A fine selection of fruits!')

print ("******************")

x, y = 10, 100

# conditional flow uses if, elif, else  
if(x < y):
  st= "x is less than y"
elif (x == y):
  st= "x is same as y"
else:
  st= "x is greater than y"
print (st)

# conditional statements let you use "a if C else b"
st = "x is less than y" if (x < y) else "x is greater than or equal to y"
print (st)

# Python does not have support for higher-order conditionals
# like "switch-case" in other languages
