#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This script will demo how to generate a collection one object
# at a time using a generator function
"""

    Docstring
"""
def get_numbers():
    """ Return an entire list of numbers """
    print("Executing get_numbers")
    numbers = []
    for x in range(0, 10000000000):
        numbers.append(x)
    return numbers

def generate_numbers():
    """ Yield one object at a time from a collection of numbers """
    print("Executing generate_numbers...")
    for x in range(0, 10):
        yield x

#for z in get_numbers():
#for z in generate_numbers():
#    print(z)

# Alternatively we could use a while loop and the built-in
# next() function to get the NEXT YIELDED value
gen = generate_numbers()
while True:
    num = next(gen, -1)
    if num != -1:
        print(num)
    else:
        break

# Alternatively we could just get NEXT yielded value manually
gen = generate_numbers()
num1 = next(gen)
num2 = next(gen)
num3 = next(gen)
print(num1)
print(num2)
print(num3)