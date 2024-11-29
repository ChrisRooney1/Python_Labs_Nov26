#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This module defines advanced functions for a calculator app
"""
    Advanced functions for calculator app includin modulus, power and sqrt
"""
import sys

def mod(x, z):
    """ Return the remainder of x modulus z """
    return x % z

def power(x, z):
    """ Return the power of x to z as a float """
    return float(x**z)

def sqrt(x):
    """ Return square root of x to 2 decimal places """
    return round(x**0.5, 2)

sys.exit(0)