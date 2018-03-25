import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

def main():
    spark = SparkSession.builder.appName("Task 4").config("spark.some.config.option", "some-value").getOrCreate()
    
    # Load parking and open data
    parkings = spark.read.format('csv').options(header='true', inferschema='true').load(sys.argv[1])
    parkings.createOrReplaceTempView("parkings")

    ny = spark.sql('''SELECT COUNT(*) AS numbers
                      FROM parkings
                      WHERE registration_state = "NY" ''')
    other = spark.sql('''SELECT COUNT(*) AS numbers
                      FROM parkings
                      WHERE NOT registration_state = "NY" ''')

    ny.select(format_string('NY\t%d', ny.numbers)).write.save("task4-sql.out", format="text")
    other.select(format_string('Other\t%d', other.numbers)).write.save("task4-sql.out", format="text", mode="append")

if __name__ == "__main__":
    main()
