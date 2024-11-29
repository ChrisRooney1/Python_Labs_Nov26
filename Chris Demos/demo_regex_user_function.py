#! /usr/bin/env python3
#Author: Chris Rooney
#Version: 1.0
#Description: This script will demo how to define and call a user function
"""

    Docstring
"""
import sys
import re

""" def search_pattern(pattern=r"^.{19}$", file=r"C:\Project\Python_Labs_Nov26\labs\words"):
    lines = 0
    with open(file, mode="rt") as fh_in:
        for line in fh_in:
            m = re.search(pattern, line) # Match pattern

            if m:
                lines += 1
                print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")
    return lines """

def search_pattern(pattern=r"^.{19}$", file=r"C:\Project\Python_Labs_Nov26\labs\wrds"):
    lines = 0
    try:
        fh_in = open(file, mode="rt")
    except FileNotFoundError as err:
        print(f"Error={err.args[0]}, reason={err.args[1]}, file={err.filename}", file=sys.stderr)
        sys.exit(1)
    except PermissionError as err:
        print(f"Error={err.args[0]}, reason={err.args[1]}, file={err.filename}", file=sys.stderr)
        sys.exit(2)
    except BaseException as err:
        print("Some other error occured, Investigate")
        sys.exit(3)
    else:
        for line in fh_in:
            m = re.search(pattern, line) # Match pattern
            if m:
                lines += 1
                print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")
        fh_in.close()
    finally:
        print("And now for something completely different")           
    return lines

def main():
    num_lines = search_pattern()
    print(f"Matched {num_lines} lines")
    return None

if __name__ == "__main__":
     main()
     sys.exit()