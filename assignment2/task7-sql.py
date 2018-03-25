import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

def main():
    spark = SparkSession.builder.appName("Task 7").config("spark.some.config.option", "some-value").getOrCreate()
    
    # Load parking and open data
    parkings = spark.read.format('csv').options(header='true', inferschema='true').load(sys.argv[1])
    parkings.createOrReplaceTempView("parkings")

    # compute frequency for weekend days
    weekend = spark.sql('''SELECT violation_code, COUNT(*) AS wend_count
                           FROM parkings
                           WHERE day(issue_date) IN (5, 6, 12, 13, 19, 20, 26, 27)
                           GROUP BY violation_code
                        ''')
    # compute frequency for week days
    week = spark.sql('''   SELECT violation_code, COUNT(*) AS w_count
                           FROM parkings
                           WHERE day(issue_date) NOT IN (5, 6, 12, 13, 19, 20, 26, 27)
                           GROUP BY violation_code
                    ''')
    weekend.createOrReplaceTempView("weekend")
    week.createOrReplaceTempView("week")
    
    result = spark.sql('''SELECT IFNULL(week.violation_code, weekend.violation_code) AS vcode, 
                                 (IFNULL(wend_count,0) / 8) AS wend_avg, 
                                 (IFNULL(w_count,0) / 23) AS w_avg
                          FROM weekend FULL OUTER JOIN week ON weekend.violation_code = week.violation_code
                       ''')

    result.select(format_string('%s\t%.2f, %.2f', result.vcode, result.wend_avg, result.w_avg)).write.save("task7-sql.out", format="text")

if __name__ == "__main__":
    main()
