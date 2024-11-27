#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This script will iterate through a 
# sequence (str/tuple/list/dict/set) using and iterator for loop

heroes = ['iron man', 'deadpool', 'batman', 'hulk', 'wonder woman']

# ITERATE through the heroes LIST using an ITERATOR loop
for hero in heroes:
    print(hero, end='\N{grinning face}')

# ITERATE through the LIST and MODIFY the values using an
# ITERATOR loop plus an index counter
idx = 0
for hero in heroes:
    print(hero.upper())
    heroes[idx] = hero.upper()
    idx += 1

print("Heroes=", heroes)

# ITERATE through the LIST and MODIFY the values using an
# ITERATOR loop plus built-in enumerate() function
for (idx, hero) in enumerate(heroes):
    print(hero.title())
    heroes[idx] = hero.title()

print("Heroes=", heroes)    