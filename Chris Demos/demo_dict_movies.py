#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This script will demo how to create, grow and shrink and access
#keys and values in a dictionary (Unordered collection with unique keys)
#Python 3.6 onwards, keys are INSERTION order
"""

    Docstring
"""
import pprint

#Create a multi-dimensional dict of lists
movies = {'chris': ['die hard', 'trainspotting', 'barbie'],
          'tom': ['12 strong','forest gump', 'gladiator'],
          'andrius': ['gladiator', 'the boondock saints', 'con air'],
          'winson': ['top gun', 'terminator', 'pretty woman']}
#Grow a dict
movies['naoki'] = ['titanic','star wars','spiderman']
movies['donald'] = ['seven samurai', 'battle royale', 'the last samurai']

#Access a dictionary
print(f"Chris's favourite movies are {movies['chris']}")
print(f"Tom's ultimate movie is {movies['tom'][0]}")
print(f"Andrius's best films are {movies.get('andrius')}")

#Shrink a dictionary
films = movies.copy() # Shallow copy dictionary
films.clear() # Empty dictionary
movies.pop('winson') # Pop/remove Winson key and value
movies.popitem() # Removes last inserted key value pair
pprint.pprint(movies) #Display sorted keys plus values in human pretty form, key value pairs on separate lines

print('-' * 60)
# Accessing a dictionary and it's keys and values
# 1. Using an iterator loop plus the keys() method
for name in movies.keys():
    print(f"{name} likes {movies[name]}")

print('-' * 60)
# 2. Using an iterator loop plus the values() method
for films in movies.values():
    print(f"Good films = {films}")

print('-' * 60)
# 3. Using an iterator keys and values using items() method
for name, films in movies.items():
    print(f"{name} loves the films {films}")