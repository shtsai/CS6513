#!/usr/bin/env python
# map function for task 1

import sys
import string
#import numpy

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    entry = line.split(",")

    licenceType = entry[2]
    amount = entry[13]
    print('{0:s}\t{1:s}'.format(licenceType, amount))


