#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This script will demo how to create, grow, shrink and 
#combine sets using set operators
"""

    Docstring
"""
marvel_fans = {'donald','naoki','chris','isla','grace'}
dc_fans = set() # Create an empty set

# Grow a set
dc_fans.add('donald')
dc_fans.add('tom')
dc_fans.add('andrius')

# Change a set
#dc_fans.pop() # Randomly remove a value
comic_fans = dc_fans.copy() # Copy the set
comic_fans.clear() # Empty the set

print(f"Fans of Marvel = {marvel_fans}")
print(f"Fans of DC = {dc_fans}")

# Combine sets using set mthods 
print(f"Fans of EITHER Marvel or DC = {marvel_fans.union(dc_fans)}")
print(f"Fans of BOTH Marvel or DC = {marvel_fans.intersection(dc_fans)}")
print(f"Fans of ONLY Marvel = {marvel_fans.difference(dc_fans)}")
print(f"Fans of ONLY Marvel or DC but not both= {marvel_fans.symmetric_difference(dc_fans)}")

# Combine sets using set operators 
print(f"Fans of EITHER Marvel or DC = {marvel_fans | dc_fans}")
print(f"Fans of BOTH Marvel or DC = {marvel_fans & dc_fans}")
print(f"Fans of ONLY Marvel = {marvel_fans - dc_fans}")
print(f"Fans of ONLY Marvel or DC but not both= {marvel_fans ^ dc_fans}")