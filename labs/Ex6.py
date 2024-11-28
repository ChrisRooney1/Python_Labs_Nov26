#! /usr/bin/python
# Exercise 6, string formatting and regular expressions.
import re

infile = open(r'C:\Project\Python_Labs_Nov26\labs\projects\06 Regular Expressions\postcodes.txt', 'r')

# Variables for counting valid and invalid codes (part b)
valid = 0
invalid = 0

for postcode in infile:
    # The variable 'postcode' contain the line read from the file.
    
    # Ignore empty lines.
    if postcode.isspace(): continue
    
    # TODO (a): Remove newlines, tabs and spaces.
    postcode = re.sub(r"\s+", r"", postcode)
    
    # TODO (a): Convert to uppercase.
    postcode = postcode.upper()

    # TODO (a): Insert a space before the final digit and 2 letters.
    postcode = re.sub(r"(\d[A-Z]{2})$", r" \1", postcode)

    # Print the reformatted postcode.
    #print (postcode)

    # TODO (b) Validate the postcode, returning a match object 'm'.
    m = re.match(r"[A-Z]{1,2}\d{1,2}[A-Z]?\s\d[A-Z]{2}$", postcode)   # TODO (b) Replace this line with a call to re.match().
    
    if m:
        valid = valid + 1
        print(f"Valid postcode {postcode}")
    else:
        invalid = invalid + 1
        print(f"Invalid postcode {postcode}")

infile.close()

# TODO (b) Print the valid and invalid totals.
print(f"The number of valid postcodes is {valid}, the number of invalid postcodes is {invalid}")
