#
# Example file for working with os.path module
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

# Print the name of the OS
print (os.name)

my_file = "/Users/firoz/desktop/PythonTest/IOExp/output.txt"

# Check for item existence and type
print ("Item exists: " + str(path.exists(my_file)))
print ("Item exists: " + str(path.exists("/Users/firoz/desktop/PythonTest/output.txt")))
print ("Item is a file: " + str(path.isfile(my_file)))
print ("Item is a directory: " + str(path.isdir("/Users/firoz/desktop/PythonTest/IOExp")))

# Work with file paths
print ("Item's path: " + str(path.realpath(my_file)))
print ("Item's path and name: " + str(path.split(path.realpath(my_file))))

# Get the modification time
t = time.ctime(path.getmtime(my_file))
print (t)
print (datetime.datetime.fromtimestamp(path.getmtime(my_file)))

# Calculate how long ago the item was modified
td= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime(my_file))
print ("It has been " + str(td) + "since the file was modified")
print ("Or, " + str(td.total_seconds()) + " seconds")
  
