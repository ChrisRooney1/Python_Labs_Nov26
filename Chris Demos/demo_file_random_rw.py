#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This script will demo hwo to open, close, read and write
# randomly to a file using the seek() and tell() methods
"""

    Docstring
"""
import sys

SOF = 0 # Start of file
CUR = 1 # Current file position
EOF = 2 # End of file

# Open file handle for READING in text mode
with open(r"C:\Project\Python_Labs_Nov26\Chris Demos\movies.txt", mode="rt") as fh_in:
    fh_in.seek(90, SOF)
    text = fh_in.read(30)
    print(f"Text at position {fh_in.tell() - len(text)} = {text}")

    fh_in.seek(135, SOF)
    text = fh_in.read(30)
    print(f"Text at position {fh_in.tell() - len(text)} = {text}")

print("-" * 60)

# Open file handle for READING in text mode
with open(r"C:\Project\Python_Labs_Nov26\Chris Demos\movies.txt", mode="rb") as fh_data:
    fh_data.seek(-90, EOF) # Seek backwards 90 bytes from EOF
    text = fh_data.read(30)
    print(f"Text at position {fh_data.tell() - len(text)} = {text}")

    fh_data.seek(-60, CUR) # Seek backwards 60 bytes from the current position
    text = fh_data.read(30)
    print(f"Text at position {fh_data.tell() - len(text)} = {text}")
