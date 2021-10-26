#
# Read and write files using the built-in Python file methods
#

# my_list = [i ** 2 for i in range(1, 20)]
# Generates a list of squares of the numbers 1 - 19

# Open a file for writing and "+" means create it if it doesn't exist
f = open("/Users/firoz/desktop/PythonTest/IOExp/output.txt", "w+")
# Open the file for appending text to the end
# f = open("textfile.txt","a+")

# for item in my_list:
 #  f.write(str(item) + "\n")

# write some lines of data to the file
for i in range(10):
  f.write("This is line %d\r\n" % (i+1))

# close the file when done
f.close()

# Open the file back up and read the contents
my_file = open("/Users/firoz/desktop/PythonTest/IOExp/output.txt", "r")

if my_file.mode == 'r': # check to make sure that the file was opened
  # use the read() function to read the entire file
  # contents = f.read()
  
  fl = my_file.readlines() # readlines reads the individual lines into a list
  for x in fl:
    print (x)

# print (my_file.read())









  

