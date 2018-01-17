# Spark part
These are the solutions for the spark training

## task 1
```python
def make_plural(word):
	return word + 's'
make_plural('cat')
```

## task 2
```python
from pyspark import SparkContext,SparkConf
sc=SparkContext()
def plural(x):
	return x + 's'
animal_list = ['dog','cat','rabbit','hare','deer','gull','woodpecker','mole']
animal_rdd = sc.parallelize(animal_list)
plural_rdd = animal_rdd.map(plural)
print(plural_rdd.collect())
```

## task 3
```python
from pyspark import SparkContext,SparkConf
sc = SparkContext()
animal_list = ['dog','cat','rabbit','hare','deer','gull','woodpecker','mole']
plural = lambda x: x+'s'
lambda_plural_rdd = sc.parallelize(plural(animal_list),2)
print(lambda_plural_rdd.collect())
```

## task 4
```python
from pyspark import SparkContext,SparkConf
sc = SparkContext()
animal_list = ['dog','cat','rabbit','hare','deer','gull','woodpecker','mole']
length = lambda x: list(map(len,x))
animal_rdd = sc.parallelize(animal_list,2)
word_lengths = animal_rdd.map(word_length)
print(word_lengths.collect())
```

## task 5
```python
from pyspark import SparkContext,SparkConf
sc=SparkContext()
pride_rdd = sc.textFile('LINK')
pride_words_try = pride_rdd.flatMap(lambda line: line.split())
pride_pairs = pride_words_try.take(lambda x: (x,1))
print(pride_pairs.take(10))

```

## task 6
```python
from pyspark import SparkContext,SparkConf
sc=SparkContext()
pride_rdd = sc.textFile('LINK')
pride_words_try = pride_rdd.flatMap(lambda line: line.split()
pride_pairs = pride_words_try.take(lambda x: (x,1))
word_count = pride_pairs.reduceByKey(lambda a,b: a+b)

top10_words = word_counts.takeOrdered(10, key=lambda p: -p[1])
print(top10_words)
```

