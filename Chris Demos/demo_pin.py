#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This script will simulate a high street bank PIN machine

master_pin = "0123"
pin  = None
attempts = 0

while pin != master_pin and attempts < 3:
    pin = input("Enter PIN: ")
    if pin == master_pin:
        print("Valid PIN")
        break
    else:
        print("Invalid PIN")
        attempts += 1
else:
    # Executes only once when while condition becomes false
    print("Too many attempts")
    print("Your card has been retained. Have a nice day \N{grinning face}")

print("Done.")