# python part
These are the solutions for the python part of the Data-Science training

## task 1
```python
#!/usr/bin/env python3.2
import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
print(pow(a,2)+pow(b,2))
```


## task 2
```
25
```

## task 3
```python
import sys
def fump():
	print(sys.argv[1][int(sys.argv[2]):int(sys.argv[3])] + ' ' + sys.argv[1][int(sys.argv[4]):int(sys.argv[5])])

fump()
```


## task 4
```python
import sys

def printblub(x,y):
	sum = 0
	for i in range(x,y+1):
		if i%2==1 :
			sum+=i
	print(sum)

printblub(int(sys.argv[1]),int(sys.argv[2]))
```

## task 5
```python
import sys

def read():
	out = ""
	with open(sys.argv[1],"r") as f:
		for line in f:
			line = line.replace(',',' ').split()
			for i in range(0,len(line)):
				if line[i].isdigit():
					if float(line[i]).is_integer():
						out+=line[i]+"\n"
	return out;

def write(out):
	with open(sys.argv[2],"w") as f:
		f.write(out)


write(read())
```

## task 6
```python
import sys

words = {}
for i in range(1,len(sys.argv)):
	word = sys.argv[i]
	word_in_list = 0
	if word in words:
		word_in_list = words[word]
	words.update({word:word_in_list+1})

print(words)
```
