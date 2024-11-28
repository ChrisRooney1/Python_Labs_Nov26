#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This script will demo how to match and substitute regex patterns
# using the re.sub() and re.subn() functions
"""

    Docstring
"""
import re
# A sample line from /etc/passwd on Linux for the root user account
line = r"root:x:0:0:The Super User:/root:/bin/ksh"

# And I want to modify the line str object but strings are immutable
line = re.sub(r"[sS]uper [uU]ser", r"Administrator", line) # Returns modified string
line, num = re.subn(r"(ksh)$", r"\1bash", line) # Returns a tuple (modified str, number of changes)

print(f"Modified line = {line} with {num} changes")