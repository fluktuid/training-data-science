# Bash (Grid) part
These are the solutions for the python part of the Bash / Grid training

## task 1
```bash
sleep 60
```

## task 2
```
$cat <file>
$less <file>
$head <file>
$tail <file>
$vi <file>
$vim <file>
```

## task 3
```bash
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
```

## task 4
```bash
FILE="~/output.txt"
for i in `seq 10`;
do
bash a2.sh 10000 >> FILE
done
```

## task 5
```bash
perc=$(bc -l <<< "scale=2; $num*100/$cnt")
echo "AVG: $perc%"
```

## task 6
```bash
qsub -q all.q script.sh
```

## task 7
```bash
FILE=$1
cat $FILE | tr .:, \s | tr '[:upper:]' '[:lower:]' | sed -e 's/\s/\n/g' | sort | uniq -c | sort -nr | head
```


