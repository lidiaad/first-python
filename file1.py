#!/usr/bin/env python3

import sys

input_file = sys.argv[1]

with open(input_file,'r', newline = '') as filereader:
#filereader = open(input_file, 'r')
	for row in filereader:
    		print(row.strip())
#filereader.close()

l1 = [1, 2, 3, 4]
print(l1)
l2 = {'kk' : 'horse'}
print(l2)
print(l2.keys())
