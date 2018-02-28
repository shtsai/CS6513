#!/usr/bin/env python

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

def addToHeap(id, count, top):
    currentVehicleTop = (count, id)
    if len(top) < 20:
        heapq.heappush(top, currentVehicleTop)
    elif top[0] < currentVehicleTop:
        heapq.heappop(top)
        heapq.heappush(top, currentVehicleTop)

currentKey = None
currentCount = 0
top = []
heapq.heapify(top)

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
            addToHeap(currentKey, currentCount, top)

        currentKey = key
        currentCount = intValue

# process last key
if currentKey:
    addToHeap(currentKey, currentCount, top)

# Output results
topVehicles = []
while len(top) != 0:
    topVehicles.append(heapq.heappop(top))

topVehicles = sorted(topVehicles, key = lambda x : (-x[0], x[1]))
for v in topVehicles:
    print('{0:s}\t{1:d}'.format(v[1], v[0]))

#for v in reversed(topVehicles):
#    print('{0:s}\t{1:d}'.format(v[1], v[0]))

