import sys
from pyspark import SparkContext
from csv import reader

def aggregateValue(x, y):
    # First value is the sum, second value is the count
    return (x[0] + y[0], x[1] + y[1])

def computeResult(x):
    # key is the license type, value is (total, average)
    return (x[0], (x[1][0], round(x[1][0] / x[1][1], 2)))

def formatOutput(x):
    return '{0:s}\t{1:.2f}, {2:.2f}'.format(x[0], x[1][0], x[1][1])

def main():
    sc = SparkContext()
    
    # Load parking data and extract required fields, flag as 1
    opens = sc.textFile(sys.argv[1], 1)
    opens = opens.mapPartitions(lambda x : reader(x))
    opens = opens.map(lambda x: (x[2], (float(x[12]), 1)))

    res = opens.reduceByKey(aggregateValue).map(computeResult).map(formatOutput)
    res.saveAsTextFile("task3.out")

if __name__ == "__main__":
    main()
