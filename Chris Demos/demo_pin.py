#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This script will simulate a high street bank PIN machine

import getpass

master_pin = "0123"
pin  = None
attempts = 0
max_attempts = 3

while pin != master_pin and attempts < 3:
    pin = getpass.getpass("Enter PIN: ")
    if pin == master_pin:
        print("Valid PIN")
        break
    else:
        attempts += 1
        print("Invalid PIN. You have used " + str(attempts) + " out of " + str(max_attempts) + " attempts available.") 
else:
    # Executes only once when while condition becomes false
    print("Too many attempts")
    print("Your card has been retained. Have a nice day \N{grinning face}")

print("Done.")