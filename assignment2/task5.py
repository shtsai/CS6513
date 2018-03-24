import sys
from pyspark import SparkContext
from csv import reader

def createMapping(x):
    # plate_id, registration_state
    return ((x[14], x[16]), 1)

def computeMax(x, y):
    if x[1] > y[1]:
        return x
    else:
        return y

def formatOutput(x):
    return "{0:s}, {1:s}\t{2:d}".format(x[0][0], x[0][1], x[1])

def main():
    sc = SparkContext()
    
    # Load parking data and extract required fields, flag as 1
    parkings = sc.textFile(sys.argv[1], 1)
    parkings = parkings.mapPartitions(lambda x : reader(x))
    parkings = parkings.map(createMapping)

    maxViolation = parkings.reduceByKey(lambda x, y: x + y).reduce(computeMax)
    res = sc.parallelize([maxViolation]).map(formatOutput)
    res.saveAsTextFile("task5.out")

if __name__ == "__main__":
    main()
