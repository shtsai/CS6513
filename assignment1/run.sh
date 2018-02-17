#!/bin/bash

HADOOP_EXE='/usr/bin/hadoop'
HADOOP_LIBPATH='/opt/cloudera/parcels/CDH/lib'
HADOOP_STREAMING='hadoop-mapreduce/hadoop-streaming.jar'

hfs="$HADOOP_EXE fs"
hjs="$HADOOP_EXE jar $HADOOP_LIBPATH/$HADOOP_STREAMING"


if [ $# -eq 1 ]; then
	TASK=$1

	# remove previous output
	$hfs -rm -r $TASK.out

	$hjs \
	-D mapreduce.job.reduces=2 \
	-files /home/st3127/assignment1/$TASK \
	-mapper $TASK/map.py \
	-reducer $TASK/reduce.py \
	-input /user/ecc290/HW1data/parking-violations.csv \
	-input /user/ecc290/HW1data/open-violations.csv \
	-output /user/st3127/$TASK.out 

elif [ $# -eq 2 ]; then
	TASK=$1
	OPERATION=$2
	echo $OPERATION
	if [ $OPERATION = "small" ]; then
		cat small-open-violations.csv small-parking-violations.csv |
		python $TASK/map.py |
		sort -n |
		python $TASK/reduce.py
	fi
else
	echo "too many arguments"
fi
