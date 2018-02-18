#!/usr/bin/env python
# map function for task 1

import sys
import string
#import numpy


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    entry = line.split(",")

    color = entry[19]
    make = entry[20]
    # 0:make,  1: color
    print('{0:s}, {1:s}\t{2:d}'.format("0", make, 1))
    print('{0:s}, {1:s}\t{2:d}'.format("1", color, 1))



