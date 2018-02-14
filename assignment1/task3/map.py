#!/usr/bin/env python
# map function for task 1

import sys
import string
#import numpy

'''
    Try parse input string to float.
'''
def tryParseFloat(input):
    try:
        floatValue = float(input)
        return True, floatValue
    except ValueError:
        return False, -1


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    entry = line.split(",")

    licenceType = entry[2]
    success, amount = tryParseFloat(entry[13])

    if success:
        print('{0:s}\t{1:f}'.format(licenceType, amount))


