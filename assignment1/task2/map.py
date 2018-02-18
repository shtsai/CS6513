#!/usr/bin/env python
# map function for task 1

import sys
import string
#import numpy


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    entry = line.split(",")

    violationCode = entry[2]
    print('{0:s}\t{1:d}'.format(violationCode, 1))


