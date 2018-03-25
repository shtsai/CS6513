import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from csv import reader

def main():
    spark = SparkSession.builder.appName("Task 1").config("spark.some.config.option", "some-value").getOrCreate()
    
    # Load parking and open data
    parkings = spark.read.format('csv').options(header='true', inferschema='true').load(sys.argv[1])
    opens = spark.read.format('csv').options(header='true', inferschema='true').load(sys.argv[2])

    parkings.createOrReplaceTempView("parkings")
    opens.createOrReplaceTempView("opens")

    result = spark.sql('''SELECT P.summons_number, P.plate_id, P.violation_precinct,
                                 P.violation_code, P.issue_date
                          FROM parkings AS P NATURAL JOIN (SELECT P1.summons_number
                                                           FROM parkings AS P1
                                                           MINUS
                                                           SELECT O.summons_number
                                                           FROM opens AS O)''')
                      
    result.select(format_string('%d\t%s, %d, %d, %s', result.summons_number, result.plate_id, result.violation_precinct, result.violation_code, date_format(result.issue_date, 'yyyy-MM-dd'))).write.save("task1-sql.out", format="text")

if __name__ == "__main__":
    main()
