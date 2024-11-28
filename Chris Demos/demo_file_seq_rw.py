#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This script will demo how to open, and read, write and append, and close
# a TEXT file.
"""

    Docstring
"""
import sys

movies = {'chris': ['die hard', 'trainspotting', 'barbie'],
          'tom': ['12 strong','forest gump', 'gladiator'],
          'andrius': ['gladiator', 'the boondock saints', 'con air'],
          'winson': ['top gun', 'terminator', 'pretty woman']}

# Open file handle for writing in text mode
fh_out = open(r"C:\Project\Python_Labs_Nov26\Chris Demos\movies.txt", mode="wt")

# Iterate through the movies dictionary and write movie info to file handle
for name in movies.keys():
    print(f"{name}: {movies[name]}", file=sys.stdout) # To Terminal
    print(f"{name}: {movies[name]}", file=fh_out) # To file
    #fh_out.write(f"{name}: {movies[name]}\n")

fh_out.close() # Flush buffers and close file

print("-" * 60)

# Open file handle for reading in text mode
fh_in = open(r"C:\Project\Python_Labs_Nov26\Chris Demos\movies.txt", mode="rt")

#text = fh_in.read() # Read ENTIRE file into one string object. Be careful of huge files
#text = fh_in.read(30) # Read next 30 characters into one string object
#text = fh_in.readline() # Read next line into one string object
#lines = fh_in.readlines() # Read entire file into list object. Be careful of huge files
#print(lines[0]) # Can INDEX list to get specific lines

# ITERATE through the file ONE line at a time
# Using an ITERATOR loop plus an ITERATOR object (iter/next method built-in)
for line in fh_in:
    print(line, end="")

fh_in.close()