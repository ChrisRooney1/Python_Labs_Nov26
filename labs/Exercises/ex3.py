import sys

var = input("Please enter an integer: ")

if var.isdecimal():
    for num in range(int(var), -1, -2):
        print(num)
else:
    print("Input is not an integer. Exiting program")
    sys.exit(1)

year = int(input("Please enter a year: "))

if var.isdecimal():
    if year % 400 == 0:
        print(str(year) + " is a leap year")
    elif year % 4 == 0 and year % 100 != 0:
        print(str(year) + " is a leap year")
    else:
        print(str(year) + " is not a leap year")
else:
    print("Input is not an valid year. Exiting program")
    sys.exit(1)