#!/usr/bin/env python
# map function for task 1

import os
import sys
import csv
import string
#import numpy


# input comes from STDIN (stream data that goes to the program)
data = csv.reader(sys.stdin)
for entry in data:
    # If this is an entry from parking-violations.csv
    #if (len(entry) == 22):
    if "parking" in os.environ.get("mapreduce_map_input_file"):
        summonsNumber = entry[0]
        plateId = entry[14]
        violationPrecinct = entry[6]
        violationCode = entry[2]
        issueDate = entry[1]
        status = "All"


        print('{0:s}\t{1:s}, {2:s}, {3:s}, {4:s}, {5:s}'.format(summonsNumber, status, plateId, violationPrecinct, violationCode, issueDate))


    # Otherwise, if this is an entry from open-violations.csv
    #else:
    elif "open" in os.environ.get("mapreduce_map_input_file"):
        summonsNumber = entry[0]
        status = "Open"


        print('{0:s}\t{1:s}, {2:s}, {3:s}, {4:s}, {5:s}'.format(summonsNumber, status, "x", "x", "x", "x"))


