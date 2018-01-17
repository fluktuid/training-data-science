#!/usr/bin/env python3.2
import sys
def fump():
	print(sys.argv[1][int(sys.argv[2]):int(sys.argv[3])] + ' ' + sys.argv[1][int(sys.argv[4]):int(sys.argv[5])])

fump()
