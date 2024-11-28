#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This script will demo a safer way of managing file handles
# using a Context Resource Manager (with statement). Simulating BLOCK scope
"""

    Docstring
"""
import sys

movies = {'chris': ['die hard', 'trainspotting', 'barbie'],
          'tom': ['12 strong','forest gump', 'gladiator'],
          'andrius': ['gladiator', 'the boondock saints', 'con air'],
          'winson': ['top gun', 'terminator', 'pretty woman']}

# Open file handle for writing in text mode
with open(r"C:\Project\Python_Labs_Nov26\Chris Demos\movies.txt", mode="wt") as fh_out:
    # Iterate through the movies dictionary and write movie info to file handle
    for name in movies.keys():
        print(f"{name}: {movies[name]}", file=sys.stdout) # To Terminal
        print(f"{name}: {movies[name]}", file=fh_out) # To file
        # End of block, fh_out is closed and deleted automatically

print("-" * 60)

# Open file handle for reading in text mode
with open(r"C:\Project\Python_Labs_Nov26\Chris Demos\movies.txt", mode="rt") as fh_in:
    # ITERATE through the file ONE line at a time
    # Using an ITERATOR loop plus an ITERATOR object (iter/next method built-in)
    for line in fh_in:
        print(line, end="")

