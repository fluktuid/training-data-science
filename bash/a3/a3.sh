#!/bin/bash/
WORD=$2
FILE=$1
cnt=$(cat $FILE | wc -l)
echo "$WORD"
num=$(cat $FILE | grep $WORD | wc -l)

#echo "ABDECKUNG: $((num*100/cnt)).$((num*100%cnt))%"
perc=$(bc -l <<< "scale=2; $num*100/$cnt")
echo "SAUBER: $perc%"
