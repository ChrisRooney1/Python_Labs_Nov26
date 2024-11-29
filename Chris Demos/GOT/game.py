#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This script will demo
"""

    Docstring
"""
import sys
import tank

def main():
    # Instantiate 3 new tank objects
    thomas_tank = tank.Tank("German", "Tiger")
    chris_tank = tank.Tank("American", "Sherman")
    naoki_tank = tank.Tank("British", "Churchill")

    # And the game begins
    thomas_tank.accel(64)
    chris_tank.accel(31)

    naoki_tank.rotate_left(289)
    naoki_tank.accel(27)
    naoki_tank.shoot()

    # ...and success
    thomas_tank.take_damage(59)
    chris_tank.take_damage(39)

    # And now for some game visuals - well at least some print statements!
    # print(f"Health of Thomas the tank is {thomas_tank._health}") # POOR CODE!

    # This is an example of operator overloading
    print(f"The health of Thomas and Chris' tanks = {thomas_tank + chris_tank}")

    # Thomas has received a health boost
    #thomas_tank._health = 100 # DO NOT ACCESS PRIVATE VARIABLES

    # Better to use SETTER and GETTER methods
    thomas_tank.set_health(101)
    print(f"The new health of Thomas' tank is {thomas_tank.get_health()}")

    thomas_tank.tank_health = 102
    print(f"The new health of Thomas' tank is {thomas_tank.tank_health}")

    print(f"Status of Thomas' tank = {thomas_tank}")

    return None

# Namespace truck
if __name__ == "__main__":
    main()
    sys.exit(0)