#!/bin/bash/
FILE=$1
cat $FILE | tr .:, \s | tr '[:upper:]' '[:lower:]' | sed -e 's/\s/\n/g' | sort | uniq -c | sort -nr | head

