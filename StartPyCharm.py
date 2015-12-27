#!/usr/bin/python
import os

path = "/home/tony/Python/pycharm-community-5.0.2/bin/"

# Check current working directory.
retval = os.getcwd()
print("Current working directory %s" % retval)

# Now change the directory
os.chdir( path )

# Check current working directory.
retval = os.getcwd()

print("Directory changed successfully %s" % retval)

os.system("./pycharm.sh")