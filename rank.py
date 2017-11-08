import sys

freq = []

fd = open('freq.txt', 'r')
for line in fd.readlines():
	line = line.strip('\n') #Remove extra newlines
	(f, w) = line.split('\t') #Split the line in two and put the result in a tuple
	freq.append((int(f), w))