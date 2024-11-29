#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This script will demo how to define and call a VARIADIC user function
"""
App to search for Regex patterns in text files
"""
import re


# Example of a VARIADIC function that allows variable number of parameters
def search_pattern(pattern=r"^.{19}$", *files):
    """ Search for Regex pattern in multiple files and return number of lines matched """
    lines = 0
    for file in files:
        with open(file, mode="rt") as fh_in:
            for line in fh_in:
                m = re.search(pattern, line) # Match pattern

                if m:
                    lines += 1
                    print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")
    return lines

num_lines = search_pattern(r"^.{20}$", r"C:\Project\Python_Labs_Nov26\Chris Demos\words", r"C:\Project\Python_Labs_Nov26\Chris Demos\words2", r"C:\Project\Python_Labs_Nov26\Chris Demos\words3")
print(f"Matched {num_lines} lines")