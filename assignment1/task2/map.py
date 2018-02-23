#!/usr/bin/env python
# map function for task 1

import sys
import string
import csv
#import numpy


# input comes from STDIN (stream data that goes to the program)
data = csv.reader(sys.stdin)
for entry in data:
    violationCode = entry[2]
    print('{0:s}\t{1:d}'.format(violationCode, 1))


