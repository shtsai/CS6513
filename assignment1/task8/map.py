#!/usr/bin/env python
# map function for task 1

import sys
import string
import csv
#import numpy


# input comes from STDIN (stream data that goes to the program)
data = csv.reader(sys.stdin)
for entry in data:
    color = entry[19]
    make = entry[20]
    if color == "":
        color = "NONE"
    if make == "":
        make = "NONE"
    # 0:make,  1: color
    print('{0:s}, {1:s}\t{2:d}'.format("0", make, 1))
    print('{0:s}, {1:s}\t{2:d}'.format("1", color, 1))



