import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

def main():
    spark = SparkSession.builder.appName("Task 6").config("spark.some.config.option", "some-value").getOrCreate()
    
    # Load parking and open data
    parkings = spark.read.format('csv').options(header='true', inferschema='true').load(sys.argv[1])
    parkings.createOrReplaceTempView("parkings")

    result = spark.sql('''SELECT plate_id, registration_state, COUNT(*) AS numbers
                          FROM parkings
                          GROUP BY plate_id, registration_state
                          ORDER BY numbers DESC, plate_id ASC
                          LIMIT 20''')

    result.select(format_string('%s, %s\t%d', result.plate_id, result.registration_state, result.numbers)).write.save("task6-sql.out", format="text")

if __name__ == "__main__":
    main()
