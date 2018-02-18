#!/usr/bin/env python
# map function for task 1

import sys
import string
#import numpy

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    entry = line.split(",")

    plateId = entry[14]
    state = entry[16]

    print('{0:s}, {1:s}\t{2:d}'.format(plateId, state, 1))


