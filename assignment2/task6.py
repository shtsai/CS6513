import sys
from pyspark import SparkContext
from csv import reader

def createMapping(x):
    # plate_id, registration_state
    return ((x[14], x[16]), 1)

def reverseKeyValue(x):
    return (x[1], x[0])

def computeMax(x, y):
    if x[1] > y[1]:
        return x
    else:
        return y

def formatOutput(x):
    return "{0:s}, {1:s}\t{2:d}".format(x[1][0], x[1][1], x[0])

def main():
    sc = SparkContext()
    
    # Load parking data and extract required fields, flag as 1
    parkings = sc.textFile(sys.argv[1], 1)
    parkings = parkings.mapPartitions(lambda x : reader(x))
    parkings = parkings.map(createMapping)

    top30 = parkings.reduceByKey(lambda x, y: x + y).map(reverseKeyValue).sortByKey(ascending=False).take(30)
    # Sort in decreasing order of count. If there is a tie, sort by plate id in accending order
    top20 = sorted(top30, key=lambda x: (-x[0], x[1][0]))[:20]
    res = sc.parallelize(top20).map(formatOutput)
    res.saveAsTextFile("task6.out")

if __name__ == "__main__":
    main()
