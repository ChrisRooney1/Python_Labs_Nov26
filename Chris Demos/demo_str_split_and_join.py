#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This script will demo how to split and rejoin a string
"""

    Docstring
"""
import sys

# Sample line from /rtx/passwd on Linux for the root user account
line = r"root:x:0:0:The Super User:/root:/bin/ksh"

# and I want to modify parts of the string! IMMUTABLE
fields = line.split(":") # Returns a list which is MUTABLE
print(fields)
fields[4] = "The Administrator"
fields[6] = "/bin/bash"

line = ":".join(fields) # Return a new STR
print(line)

sys.exit(0)