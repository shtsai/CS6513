#!/bin/bash

HADOOP_EXE='/usr/bin/hadoop'
HADOOP_LIBPATH='/opt/cloudera/parcels/CDH/lib'
HADOOP_STREAMING='hadoop-mapreduce/hadoop-streaming.jar'

hfs="$HADOOP_EXE fs"
hjs="$HADOOP_EXE jar $HADOOP_LIBPATH/$HADOOP_STREAMING"


if [ "$1" = "local" ]; then
	OPERATION=$2
	TASK=$3
	echo $OPERATION
	if [ $OPERATION = "both" ]; then
		cat small-open-violations.csv small-parking-violations.csv |
		python $TASK/map.py |
		sort -n |
		python $TASK/reduce.py
	elif [ $OPERATION = "all" ]; then
		cat small-parking-violations.csv |
		python $TASK/map.py |
		sort -n |
		python $TASK/reduce.py
	elif [ $OPERATION = "open" ]; then
		cat small-open-violations.csv |
		python $TASK/map.py |
		sort -n |
		python $TASK/reduce.py
	fi	
elif [ $# -eq 3 ]; then
	TASK=$1
	REDUCER=$2
	OPERATION=$3

	# remove previous output
	$hfs -rm -r $TASK.out

	if [ $OPERATION = "both" ]; then
		$hjs \
		-D mapreduce.job.reduces=$REDUCER \
		-files /home/st3127/assignment1/$TASK \
		-mapper $TASK/map.py \
		-reducer $TASK/reduce.py \
		-input /user/ecc290/HW1data/parking-violations.csv \
		-input /user/ecc290/HW1data/open-violations.csv \
		-output /user/st3127/$TASK.out 
	elif [ $OPERATION = "all" ]; then
		$hjs \
		-D mapreduce.job.reduces=$REDUCER \
		-files /home/st3127/assignment1/$TASK \
		-mapper $TASK/map.py \
		-reducer $TASK/reduce.py \
		-input /user/ecc290/HW1data/parking-violations.csv \
		-output /user/st3127/$TASK.out 
	elif [ $OPERATION = "open" ]; then
		$hjs \
		-D mapreduce.job.reduces=$REDUCER \
		-files /home/st3127/assignment1/$TASK \
		-mapper $TASK/map.py \
		-reducer $TASK/reduce.py \
		-input /user/ecc290/HW1data/open-violations.csv \
		-output /user/st3127/$TASK.out 
	fi	
	
else
	echo "INVALID arguments"
fi
