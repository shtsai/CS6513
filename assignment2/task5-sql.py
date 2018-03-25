import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

def main():
    spark = SparkSession.builder.appName("Task 5").config("spark.some.config.option", "some-value").getOrCreate()
    
    # Load parking and open data
    parkings = spark.read.format('csv').options(header='true', inferschema='true').load(sys.argv[1])
    parkings.createOrReplaceTempView("parkings")

    result = spark.sql('''SELECT plate_id, registration_state, COUNT(*) AS numbers
                          FROM parkings
                          GROUP BY plate_id, registration_state
                          HAVING numbers = (SELECT MAX(numbers2)
                                            FROM (SELECT plate_id, registration_state, COUNT(*) AS numbers2
                                                  FROM parkings
                                                  GROUP BY plate_id, registration_state))''')

    result.select(format_string('%s, %s\t%d', result.plate_id, result.registration_state, result.numbers)).write.save("task5-sql.out", format="text")

if __name__ == "__main__":
    main()
