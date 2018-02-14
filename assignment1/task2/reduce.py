#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

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


currentKey = None
currentCount = 0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    line = line.strip()
    key, value = line.split('\t')
    success, intValue = tryParseInt(value)
    if not success:
        continue

    if key == currentKey:
        currentCount += intValue
    else:
        if currentKey:
            print('{0:s}\t{1:d}'.format(currentKey, currentCount))

        currentKey = key
        currentCount = intValue


# Compute/output result for the last key
if currentKey:
    print('{0:s}\t{1:d}'.format(currentKey, currentCount))


