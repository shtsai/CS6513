#!/usr/bin/env python
# map function for task 1

import sys
import string
#import numpy

'''
    Try parse input string.
'''
def tryParseInt(input):
    try:
        intValue = int(input)
        return True, intValue
    except ValueError:
        return False, -1


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    entry = line.split(",")

    violationCodeStatus, violationCode = tryParseInt(entry[2])
    if violationCodeStatus:
        print('{0:d}\t{1:d}'.format(violationCode, 1))


