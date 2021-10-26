
numbers = [1, 2, 3, 4]
my_list = range(51) # a list of the numbers from 0 to 50 (inclusive).

def first_item(items):
  print (items[0])
 
# print(first_item(numbers))
numbers.append(5)
# print(numbers)

def double_first(n):
  n[0] = n[0] * 2

def double_all(n):
    for i in range(0, len(n)):
        n[i] = n[i] * 2

double_all(numbers)
print(numbers)

print ("******************")

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

lists = [list_a, list_b]
 
def flatten(list_of_lists):
    for lst in list_of_lists:
        for item in lst:
            print (item)

print ("Flatten:")     
print(flatten(lists))

def zippen(list1, list2):
    for a, b in zip(list1, list2):
        print ("Pair {0} - {1}".format(a, b))

print ("Zip :")  
print(zippen(list_a, list_b))

print ("*** List Comprehension *****")
# This will create a new_list populated by the numbers one to five. 

new_list = [x for x in range(1, 6)] 
print(new_list) # => [1, 2, 3, 4, 5]

# If you want those numbers doubled, you could use:

doubles = [x * 2 for x in range(1, 6)] 
print(doubles) # => [2, 4, 6, 8, 10]

# And if you only wanted the doubled numbers that are evenly divisible by three:

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0] 
print(doubles_by_3) # => [6]

# prints out a list containing ['C', 'C', 'C'].
c = ['C' for x in range(5) if x < 3]
print (c)


print ("*** List Slicing *****")
# [start:end:stride]
# if you don’t pass a particular index to the list slice, Python will pick a default.
# The default starting index is 0.
# The default ending index is the end of the list.
# The default stride is 1.

to_five = ['A', 'B', 'C', 'D', 'E']
 
print (to_five[3:])
# prints ['D', 'E'] 
 
print (to_five[:2])
# prints ['A', 'B']
 
print (to_five[::2])
# print ['A', 'C', 'E']

print (to_five[::-1]) # negative strive will reverse the list. 
# print ['E', 'D', 'C', 'B', 'A']

to_21 = range(1, 22)

odds = to_21[::2]

middle_third = to_21[7:14]