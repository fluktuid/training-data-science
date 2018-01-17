#!/bin/bash

MAX=$1
sum=0
for i in `seq $MAX`;
do
	i=$RANDOM;
	echo $i;
	sum=$((sum+i));
done
echo "SUM: $sum"
echo "AVG: $((sum/MAX))"

