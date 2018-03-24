import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

def main():
    spark = SparkSession.builder.appName("Task 2").config("spark.some.config.option", "some-value").getOrCreate()
    
    # Load parking and open data
    parkings = spark.read.format('csv').options(header='true', inferschema='true').load(sys.argv[1])
    parkings.createOrReplaceTempView("parkings")

    result = spark.sql('''SELECT violation_code, COUNT(*) AS numbers
                          FROM parkings
                          GROUP BY violation_code''')

    result.select(format_string('%d\t%d', result.violation_code, result.numbers)).write.save("task2-sql.out", format="text")

if __name__ == "__main__":
    main()
