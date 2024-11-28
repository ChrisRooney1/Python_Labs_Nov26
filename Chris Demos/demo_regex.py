#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This script will demo how to match text data using str testing
#and Regular Expressions/Regex and the re module
"""

    Docstring
"""
import re

# Open file handle for READING in TEXT mode
fh_in = open(r"C:\Project\Python_Labs_Nov26\labs\words", mode="rt")



# Iterate through the file handle one line at a time
for line in fh_in:
    # Example of str testing
    #if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
    #m = re.search(r"town", line) # Match lines with "town" in the string
    #m = re.search(r"^town", line) # Match lines starting with "town" in the string
    #m = re.search(r"town$", line) # Match lines ending with "town" in the string
    #m = re.search(r"^[A-Z]", line) # Match lines starting with CAPITALS
    #m = re.search(r"^.ing$", line) # Match lines with only one character followed by ing
    #m = re.search(r"^[adpr]ing$", line) # Match lines with ONLY either [adpr] one character followed by ing
    #m = re.search(r"^...................$", line) # Match lines with only exactly 19 characters
    #m = re.search(r"^.{19}", line) # Match lines with exactly 19 characters
    #m = re.search(r"[aeiou][aeiou][aeiou]", line) # Match lines with 3 consecutive vowels
    #m = re.search(r"[aeiou]{5,}", line) # Match lines with at least 5 consecutive vowels
    #m = re.search(r"[0-9][0-9]", line) # Match lines with only two consecutive digits
    #m = re.search(r"\.", line) # Match lines that contain a dot
    #m = re.search(r"[.]", line) # Match lines that contain a dot
    #m = re.search(r"^[A-Z].*[A-Z]$", line) # Match lines starting and ending with CAPITALS
    #m = re.search(r"^[A-Z].{3}[A-Z]$", line) # Match lines of 5 characters starting and ending with CAPITALS
    m = re.search(r"^(.)(.).\2\1$", line, flags=re.IGNORECASE) # Match 5 character palindromes
    #m = re.search(r"^([A-Z]).*\1$", line) # Match lines that start and end with the same capital
    #m = re.match(r"([A-Z]).*\1$", line) # Match automatically lines STARTING with pattern
    #m = re.fullmatch(r"([A-Z]).*\1\n$", line) # Match entire lines including HIDDEN characters like newline
    if m:
        print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()},", f"Groupings={m.groups()}, Group 1={m.group(1)}")

fh_in.close()