#!/usr/bin/env python
# map function for task 1

import sys
import string
#import numpy


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    entry = line.split(",")

    state = entry[16]

    if state == "NY":
        print('{0:s}\t{1:d}'.format(state, 1))
    else:
        print('{0:s}\t{1:d}'.format("Other", 1))



