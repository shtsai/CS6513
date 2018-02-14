#!/usr/bin/env python
# map function for task 1

import sys
import string
#import numpy

'''
    Try parse input string.
'''
def tryParseInt(input):
    try:
        intValue = int(input)
        return True, intValue
    except ValueError:
        return False, -1


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
    # Remove leading and trailing whitespace
    line = line.strip()

    # Split line into array of entry data
    entry = line.split(",")

    # If this is an entry from parking-violations.csv
    if (len(entry) == 22):
        # Set row, column, and value for this entry
        summonsStatus, summonsNumber = tryParseInt(entry[0])
        plateId = entry[14]
        violationPrecinctStatus, violationPrecinct = tryParseInt(entry[6])
        violationCodeStatus, violationCode = tryParseInt(entry[2])
        issueDate = entry[1]
        status = "All"

        # Check if all fields are parsed successfully
        if not (summonsStatus and violationPrecinctStatus and violationCodeStatus):
            continue

        print('{0:d}\t{1:s}, {2:s}, {3:d}, {4:d}, {5:s}'.format(summonsNumber, status, plateId, violationPrecinct, violationCode, issueDate))


    # Otherwise, if this is an entry from open-violations.csv
    else:
        summonsStatus, summonsNumber = tryParseInt(entry[0])
        status = "Open"

        if not summonsStatus:
            continue

        print('{0:d}\t{1:s}, {2:s}, {3:d}, {4:d}, {5:s}'.format(summonsNumber, status, "tmp", -1, -1, "tmp"))

