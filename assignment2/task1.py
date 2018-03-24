import sys
from pyspark import SparkContext
from csv import reader

def combineRecord(x, y):
    # Sum up the flag values, paid will have value 1, unpaid will have value (1 - 1) = 0
    status = x[0] + y[0]

    # Pass on the field values of parking data (with flag 1)
    if x[0] == 1:
	    return (status, x[1], x[2], x[3], x[4])
    else:
	    return (status, y[1], y[2], y[3], y[4])

def flagPositive(x):
    # Check if the flag value (first field of the values) is positive
    return x[1][0] > 0

def formatOutput(x):
    return x[0] + "\t" + x[1][1] + ", " + x[1][2] + ", " + x[1][3] + ", " + x[1][4]

def main():
    sc = SparkContext()
    
    # Load parking data and extract required fields, flag as 1
    parkings = sc.textFile(sys.argv[1], 1)
    parkings = parkings.mapPartitions(lambda x : reader(x))
    parkings = parkings.map(lambda x: (x[0], (1, x[14], x[6], x[2], x[1])))

    # Load open data, flag as -1
    opens = sc.textFile(sys.argv[2], 1)
    opens = opens.mapPartitions(lambda x : reader(x))
    opens = opens.map(lambda x : (x[0], (-1, "x", "x", "x", "x")))

    alls = parkings.union(opens)

    res = alls.reduceByKey(combineRecord).filter(flagPositive).map(formatOutput)
    res.saveAsTextFile("task1.out")

if __name__ == "__main__":
    main()
