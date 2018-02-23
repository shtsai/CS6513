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
    date = entry[1]
    day = date.split("-")[2]
    if day in ["05", "06", "12", "13", "19", "20", "26", "27"]:
        print('{0:s}\t{1:s}'.format(violationCode, "Weekend"))
    else:
        print('{0:s}\t{1:s}'.format(violationCode, "Week"))



