#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This script will demo how to preserve one Python object
# to a pickle file using the pickle module
"""

    Docstring
"""
import pickle
import pprint
import gzip 
import re

all_ports = set(range(1, 201))
used_ports = set()

with open(r"C:\Project\Python_Labs_Nov26\Chris Demos\services", mode="rt") as fh_in:
    for line in fh_in:
        if line.startswith("#"): continue
        if re.search(r"^\s+$", line) : continue
        
        m = re.search(r"(\d+)/(tcp|udp)", line)
        if m and int(m.group(1)) <= 200:
            print(line, end="")
            used_ports.add(int(m.group(1)))

    unused_ports = all_ports - used_ports
#    for port in unused_ports:
#        print(port)
    print(f"Unused ports = {unused_ports}")
        