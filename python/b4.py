import sys
#in_file = open(sys.argv[1],"r")
#out_file = open(sys.argv[2],"w")

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
