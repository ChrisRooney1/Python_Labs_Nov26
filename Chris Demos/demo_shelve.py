#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This script will demo
"""

    Docstring
"""
import shelve

movies = {'chris': ['die hard', 'trainspotting', 'barbie'],
          'tom': ['12 strong','forest gump', 'the matrix'],
          'andrius': ['gladiator', 'the boondock saints', 'con air'],
          'winson': ['top gun', 'terminator', 'pretty woman']}

tv_series = { 'chris' : ['walking dead', 'yellowstone'],
               'tom': ['breaking bad', 'the boys'],
               'andrius': ['outlander', 'dads army']}

books = {'andrius': 'dummys guide to python',
         'winson': 'extreme ironing'}

with shelve.open(r"C:\Project\Python_Labs_Nov26\Chris Demos\media") as db:
    db['movies'] = movies
    db['tv_series'] = tv_series
    db['books'] = books

with shelve.open(r"C:\Project\Python_Labs_Nov26\Chris Demos\media") as db:
    print(f"Chris' favourite movies are {db['movies']['chris']}")
    print(f"Tom's favourite tv series is {db['tv_series']['tom'][0]}")
    print(f"Winson's favourite book is {db['books']['winson']}")