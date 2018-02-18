#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string
#import numpy


currentCode = None
weekCount = 0
weekendCount = 0
weekDays = 23.0
weekendDays = 8.0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    line = line.strip()
    code, type = line.split('\t')

    if code == currentCode:
        if type == "Week":
            weekCount += 1
        elif type == "Weekend":
            weekendCount += 1
    else:
        if currentCode:
            weekendAverage = round(weekendCount / weekendDays, 2)
            weekAverage = round(weekCount / weekDays, 2)
            print('{0:s}\t{1:.2f}, {2:.2f}'.format(currentCode, weekendAverage, weekAverage))
            weekCount = 0
            weekendCount = 0

        currentCode = code
        if type == "Week":
            weekCount += 1
        elif type == "Weekend":
            weekendCount += 1


# Compute/output result for the last key
if currentCode:
    weekendAverage = round(weekendCount / weekendDays, 2)
    weekAverage = round(weekCount / weekDays, 2)
    print('{0:s}\t{1:.2f}, {2:.2f}'.format(currentCode, weekendAverage, weekAverage))

