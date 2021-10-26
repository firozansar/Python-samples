my_dict = {
  "fish": ["c", "a", "r", "p"],
  "cash": -4483,
  "luck": "good"
}
# print (my_dict["luck"][0])
# print (my_dict["luck"])

inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], 
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# print (inventory)

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# print (inventory)

choices = ['pizza', 'pasta', 'salad', 'nachos']

print ('Your choices are:')
for index, item in enumerate(choices):
  print (index, item)

print ("******************")

shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

for key in prices:
  print (key)
  print (("price: {0}").format(prices[key]))
  print (("stock: {0}").format(stock[key]))

print ("******************")

d = {
  "Name": "Firoz",
  "Age": 40,
  "BDFL": True
}
# print (d.items())
# print (d.keys())
# print (d.values())

for key in d:
  print (key, d[key])
 
for letter in "Firoz":
  print (letter) 

