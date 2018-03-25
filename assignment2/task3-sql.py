import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

def main():
    spark = SparkSession.builder.appName("Task 3").config("spark.some.config.option", "some-value").getOrCreate()
    
    # Load parking and open data
    opens = spark.read.format('csv').options(header='true', inferschema='true').load(sys.argv[1])
    opens.createOrReplaceTempView("opens")

    result = spark.sql('''SELECT license_type, SUM(amount_due) AS total_amount, AVG(amount_due) AS avg_amount
                          FROM opens
                          GROUP BY license_type''')

    result.select(format_string('%s\t%.2f, %.2f', result.license_type, result.total_amount, result.avg_amount)).write.save("task3-sql.out", format="text")

if __name__ == "__main__":
    main()
