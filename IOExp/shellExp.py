#
# Example file for working with filesystem shell methods
#
import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive

my_file = "/Users/firoz/desktop/PythonTest/IOExp/output.txt"
# make a duplicate of an existing file
if path.exists(my_file):
  # get the path to the file in the current directory
  src = path.realpath(my_file)
  
  # separate the path part from the filename
  head, tail = path.split(src)
  print ("path: {0}".format(head))
  print ("file: {0}".format(tail))
  
  # let's make a backup copy by appending "bak" to the name
  dst = src + ".bak"
  # now use the shell to make a copy of the file
  # shutil.copy(src, dst)
  
  # copy over the permissions, modification times, and other info
  # shutil.copystat(src, dst)
  
  # rename the original file
  # os.rename(my_file, "/Users/firoz/desktop/PythonTest/IOExp/newfile.txt")
  
  # now put things into a ZIP archive
#     root_dir,tail = path.split(src)
#     shutil.make_archive("archive", "zip", root_dir)

  # more fine-grained control over ZIP files
  # with ZipFile("testzip.zip","w") as newzip:
   #  newzip.write("newfile.txt")
    # newzip.write("textfile.txt.bak")
    
