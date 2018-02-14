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

    #Remove leading and trailing whitespace
    line = line.strip()

    #Get key/value
    key, value = line.split('\t')
    success, intValue = tryParseInt(value)
    if not success:
        continue

    #If we are still on the same key...
    if key == currentKey:
        currentCount += intValue

    #Otherwise, if this is a new key...
    else:
        #If this is a new key and not the first key we've seen
        if currentKey:
            print('{0:s}\t{1:d}'.format(currentKey, currentCount))

        currentKey = key
        currentCount = intValue


# Compute/output result for the last key (your code goes here)
if currentKey:
    print('{0:s}\t{1:d}'.format(currentKey, currentCount))


