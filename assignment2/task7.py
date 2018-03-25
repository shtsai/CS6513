import sys
from pyspark import SparkContext
from csv import reader

def createMapping(x):
    # mapping: (violation code, (weekendCount, weekCount))
    date = x[1]
    day = date.split("-")[2]
    if day in ["05", "06", "12", "13", "19", "20", "26", "27"]:
        return (x[2], (1, 0))
    else:
        return (x[2], (0, 1))

def computeSum(x, y):
    # sum up weekend and week value
    return (x[0] + y[0], x[1] + y[1])

def computeAverage(x):
    return (x[0], (round(x[1][0] / 8, 2), round(x[1][1] / 23, 2)))

def formatOutput(x):
    return "{0:s}\t{1:.2f}, {2:.2f}".format(x[0], x[1][0], x[1][1])

def main():
    sc = SparkContext()
    
    # Load parking data and extract required fields, flag as 1
    parkings = sc.textFile(sys.argv[1], 1)
    parkings = parkings.mapPartitions(lambda x : reader(x))

    res = parkings.map(createMapping).reduceByKey(computeSum).map(computeAverage).map(formatOutput)
    res.saveAsTextFile("task7.out")

if __name__ == "__main__":
    main()
