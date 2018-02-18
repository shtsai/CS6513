#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string
#import numpy


'''
    Try parse input string to float.
'''
def tryParseFloat(input):
    try:
        floatValue = float(input.strip())
        return True, floatValue
    except ValueError:
        return False, -1


currentKey = None
currentValue = 0.0
currentCount = 0.0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    line = line.strip()
    key, value = line.split('\t')
    success, amount = tryParseFloat(value)

    if not success:
        continue

    if key == currentKey:
        currentValue += amount
        currentCount += 1.0

    else:
        if currentKey:
            total = round(currentValue, 2)
            average = round(currentValue / currentCount, 2)
            print('{0:s}\t{1:.2f}, {2:.2f}'.format(currentKey, total, average))

        currentKey = key
        currentValue = amount
        currentCount = 1.0


# Compute/output result for the last key
if currentKey:
    total = round(currentValue, 2)
    average = round(currentValue / currentCount, 2)
    print('{0:s}\t{1:.2f}, {2:.2f}'.format(currentKey, total, average))


