#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This script will demo how to format string in several ways
# using string concatenation and escape chars, str justification methods,
# the str() format method and f-strings!
"""

    Docstring
"""
planets = {'Mercury': 57.91, 'Venus': 108.2, 'Earth': 149.597870, "Mars": 227.94}

#Iterate through the keys in the planets dict and display planet infor
#Using str concatenation and escape chars UGLY

for planet in planets.keys():
    print("\t\t" + planet + ": " + str(planets[planet]) + "Gm\t" + str(hex(0xff)))

print("-" * 60)

# Using str justification methods.
for planet in planets.keys():
    print(planet.ljust(12) + ": " + str(planets[planet]).rjust(12) + "Gm\t" + str(hex(0xff).rjust(6)))

print("-" * 60)

# Using str.format() method
for planet in planets.keys():
    print("{0:>12s}: {1:.^12.3f}Gm {2:>#6x} ".format(planet, planets[planet], 0xff))

print("-" * 60)

# Using f-strings (Python 3.5 onwards)
for planet in planets.keys():
    print(f"{planet:>12s}: {planets[planet]:.^12.3f}Gm {0xff:>#6x} ")

first = "Chris"
last = "Rooney"

#Defaults to convert the parameters to strings
name = f"{first} {last}"

print(name)