import sys

freq = []

#First open the file for reading
fd = open('freq.txt', 'r')

for line in fd.readlines():
	line = line.strip('\n') #Remove extra newlines
	(f, w) = line.split('\t') #Split the line in two and put the result in a tuple
	freq.append((int(f), w))

#We start at first rank
rank = 1
min = freq[0][0] #The current minimum is the first item in the frequency list
ranks = [] #List to store the ranked items
for i in range(0, len(freq)): 
	if freq[i][0] < min: #if the current frequency is lower than previous min, increase rank
		rank = rank + 1
		min = freq[i][0]
	ranks.append((rank, freq[i][0], freq[i][1]))

for w in ranks: 
	print('%d\t%d\t%s'%(w[0],w[1],w[2]))

