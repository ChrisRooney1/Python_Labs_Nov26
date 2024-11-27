#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This script will demo how to iterate through files
# and the file system using an ITERATOR for loop plus the glob module

import glob
import sys
import os

if sys.platform == "win32":
    if os.environ["USERPROFILE"]:
        home = os.environ["USERPROFILE"]
    else:
        home = r"c:\users\crooney"
    pattern = home + r"\*"
else:
    home = os.environ["HOME"]
    pattern = home + "/*"

print(home)
print(pattern)
for file in glob.glob(pattern):
    if os.path.getsize(file) != 0:
        print(os.path.basename(file), os.path.getsize(file))
