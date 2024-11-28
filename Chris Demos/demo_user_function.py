#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This script will demo how to define, name, call and optionally pass
# parameters in and optionally return data from a user function
"""

    Docstring
"""
#Example of an user function with parameter passing
# and optional default values. And annotations (embedded
# comment specifying preferred datatype)
def say_hello(greeting:str="ciao", recipient:str="amici")->None:
    message = f"{greeting} {recipient}"
    print(message)
    return None

say_hello("hello", "my friends") #Example of Positional Parameter passing
say_hello(greeting="konichiwa", recipient="tomodachi") # Named Parameter Passing
say_hello(recipient="mes amis",greeting="bonjour") # Named Parameter Passing (different order)
say_hello("ciao",recipient="amici") # Mixed Parameter Passing (position then named)
say_hello("ciao")
say_hello()

print(f"Annotations for say_hello {say_hello.__annotations__}")