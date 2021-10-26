
print ("**** is prime ******")
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

print (is_prime(131))
print (is_prime(10))

print ("**** reverse ******")
def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word
  
print (reverse("Hello World"))

print ("**** Scrabble ******")
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
  word = word.lower()
  total = 0
  for letter in word:
    for leter in score:
      if letter == leter:
        total = total + score[leter]
  return total

print (scrabble_score("pizza"))

""" Define a function called count that has two arguments called sequence and item. 
    Return the number of times the item occurs in the list. For example: 
    count([1, 2, 1, 1], 1) should return 3 (because 1 appears 3 times in the list)."""

def count(sequence, item):
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    return count
  
print (count([1, 2, 1, 1], 1))

""" Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, 
    and returns the result. For example, purify([1,2,3]) should return [2]."""

def purify(lst):
    res = []
    for ele in lst:
        if ele % 2 == 0:
            res.append(ele)
    return res
  
print (purify([1, 2, 3, 4]))

""" Define a function called product that takes a list of integers as input and returns the product of all of 
the elements in the list. For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100)."""

def product(list):
  total = 1
  for num in list:
    total = total * num
  return total

print (product([4, 5, 5]))

""" Write a function remove_duplicates that takes in a list and removes elements of the list that are the same. 
    For example: remove_duplicates([1, 1, 2, 2]) should return [1, 2]. """

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
  
print (remove_duplicates([1, 1, 2, 2]))


""" Write a function called median that takes a list as an input and returns the median value of the list. For example: median([1, 1, 2]) should return 1. """

def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)/2
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2
        return mean
   
print (median([2, 4, 5, 9]))