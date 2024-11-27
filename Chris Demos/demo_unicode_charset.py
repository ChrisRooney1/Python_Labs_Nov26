#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This script will demo how to display the entire 
#unicode character set
"""

    Docstring
"""
import sys

# Iterate through all the character positions in Unicode charset
for pos in range(0, 65536):
    try:
        print(chr(pos),end=" ")
        if pos % 16 == 0:
            print()
    except UnicodeEncodeError:
        print("")

sys.exit(0)