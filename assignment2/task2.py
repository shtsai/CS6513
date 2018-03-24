import sys
from pyspark import SparkContext
from csv import reader

def formatOutput(x):
    return str(x[0]) + "\t" + str(x[1])

def main():
    sc = SparkContext()
    
    # Load parking data and extract required fields, flag as 1
    parkings = sc.textFile(sys.argv[1], 1)
    parkings = parkings.mapPartitions(lambda x : reader(x))
    parkings = parkings.map(lambda x: (x[2], 1))

    res = parkings.reduceByKey(lambda x, y: x + y).map(formatOutput)
    res.saveAsTextFile("task2.out")

if __name__ == "__main__":
    main()
