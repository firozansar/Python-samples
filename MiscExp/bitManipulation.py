# print (5 >> 4)  # Right Shift
# print (5 << 1)  # Left Shift
# print (8 & 5)   # Bitwise AND
# print (9 | 4)   # Bitwise OR
# print (12 ^ 42) # Bitwise XOR
# print (~88)     # Bitwise NOT

# numbers in binary format by starting the number with 0b
# print (0b1)    #1
# print (0b10)   #2
# print (0b11)   #3
# print (0b100)  #4
# print (0b101)  #5
# print (0b110)  #6
# print (0b111)  #7
# print (0b1 + 0b11) # 1 + 3 = 4
# print (0b11 * 0b11) # 3 * 3 = 9

# bin() takes an integer as input and returns the binary representation of that integer in a string
# print (bin(3)) # 0b11

# the int function actually has an optional second parameter. When given a string containing a number 
# and the base that number is in, the function will return the value of that number converted to base ten.
print (int("1",2))
print (int("10",2))
print (int("111",2))
print (int("0b100",2))
print (int(bin(5),2))

print (~42)
print (~123)

def check_bit4(input):
  mask = 0b1000
  desired = input & mask
  if desired > 0:
    return "on"
  else:
    return "off"

a = 0b10111011

mask = 0b100
desired = a | mask
print (bin(desired))

a = 0b110 # 6
mask = 0b111 # 7
desired =  a ^ mask # 0b1

# You can also use the left shift (<<) and right shift (>>) operators to slide masks into place.

a = 0b101 
# Tenth bit mask
mask = (0b1 << 9)  # One less than ten 
desired = a ^ mask


