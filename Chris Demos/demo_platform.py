#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This script will demo how to test which platform you are running on
#and will get the HOME path of the user

import sys
import os
import platform

if sys.platform == "win32":
    home = os.environ["HOMEPATH"]
else:
    home = os.environ["HOME"]

print("My home directory is", home)    

print(platform.system())
print(platform.platform())
print(platform.machine())
print(platform.architecture())
print(platform.node())
print(platform.python_implementation())

try:
    sys.exit(0)
except SystemError:
    print("Quitting program...")
    sys.exit(0)