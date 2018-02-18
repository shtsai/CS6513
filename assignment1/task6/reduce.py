#!/usr/bin/env python
# Reduce function for computing matrix multiply A*B

# Input arguments:
# variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string
import heapq


# import numpy


'''
    Try parse input string to integer.
'''
def tryParseInt(input):
    try:
        intValue = int(input)
        return True, intValue
    except ValueError:
        return False, -1

def addToHeap(id, count, top, bottom):
    currentVehicleTop = (count, id)
    if len(top) < 10:
        heapq.heappush(top, currentVehicleTop)
    elif top[0] < currentVehicleTop:
        heapq.heappop(top)
        heapq.heappush(top, currentVehicleTop)

    currentVehicleButtom = (-count, id)
    if len(bottom) < 10:
        heapq.heappush(bottom, currentVehicleButtom)
    elif bottom[0] < currentVehicleButtom:
        heapq.heappop(bottom)
        heapq.heappush(bottom, currentVehicleButtom)


currentKey = None
currentCount = 0
top = []
bottom = []

heapq.heapify(top)
heapq.heapify(bottom)

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
            addToHeap(currentKey, currentCount, top, bottom)

        currentKey = key
        currentCount = intValue

# process last key
if currentKey:
    addToHeap(currentKey, currentCount, top, bottom)

# Output results
topVehicles = []
while len(top) != 0:
    topVehicles.append(heapq.heappop(top))
for v in reversed(topVehicles):
    print('{0:s}\t{1:d}'.format(v[1], v[0]))

while len(bottom) != 0:
    v = heapq.heappop(bottom)
    print('{0:s}\t{1:d}'.format(v[1], -v[0]))

