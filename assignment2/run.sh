#!/bin/bash

HADOOP_EXE='/usr/bin/hadoop'
HADOOP_LIBPATH='/opt/cloudera/parcels/CDH/lib'
HADOOP_STREAMING='hadoop-mapreduce/hadoop-streaming.jar'

hfs="$HADOOP_EXE fs"
hjs="$HADOOP_EXE jar $HADOOP_LIBPATH/$HADOOP_STREAMING"

TASK=$1
TASKFILE=$TASK

if [ "$2" = "sql" ]; then
	TASKFILE=$TASK-sql
	PARKINGS="/user/ecc290/HW1data/parking-violations-header.csv"
	OPENS="/user/ecc290/HW1data/open-violations-header.csv"
elif [ "$3" = "small" ]; then
	PARKINGS="/user/st3127/small-parking-violations.csv"
	OPENS="/user/st3127/small-open-violations.csv"
else
	PARKINGS="/user/ecc290/HW1data/parking-violations.csv"
	OPENS="/user/ecc290/HW1data/open-violations.csv"
fi

$hfs -rm -r $TASKFILE.out

TASKFILE=$TASKFILE.py

if [ "$TASK" = "task1" ]; then
	spark-submit --conf spark.pyspark.python=/share/apps/python/3.4.4/bin/python $TASKFILE $PARKINGS $OPENS
elif [ "$TASK" = "task3" ]; then
	spark-submit --conf spark.pyspark.python=/share/apps/python/3.4.4/bin/python $TASKFILE $OPENS
else
	spark-submit --conf spark.pyspark.python=/share/apps/python/3.4.4/bin/python $TASKFILE $PARKINGS
fi
