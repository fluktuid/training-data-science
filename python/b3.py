import sys

def printblub(x,y):
	sum = 0
	for i in range(x,y+1):
		if i%2==1 :
			sum+=i
	print(sum)

printblub(int(sys.argv[1]),int(sys.argv[2]))
