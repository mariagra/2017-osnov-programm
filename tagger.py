import sys

fd = open('model.tsv', 'r') # we are opening our model in the file


freq_tag = ''
freq_word_tag = {} # store the word -> tag
freq_word_max = {} # store highest tag frequency we have seen 


for line in fd:
	if line[0] == '#': 
		continue
	line = line.strip()
	# take the wordform (column 2)
	row = line.split('\t')
	tagfreq = int(row[1]) # convert row[1] to be an integer so we can compare it
	wordform = row[3].strip()
	tag = row[2].strip()
	if wordform not in freq_word_tag: # if we haven't seen this word before
		freq_word_max[wordform] = 0 # set the maximum count to 0
	if tagfreq > freq_word_max[wordform]: # if the frequency count of this tag given this word is higher than the maximum
		freq_word_max[wordform] = tagfreq # set the new maximum to be what we just saw
		freq_word_tag[wordform] = tag # set the tag for this word to be the one we just saw

#print(freq_word_tag)
#print(freq_word_max)

freq_tag = freq_word_tag['-'] 

#print(freq_tag)


# working with another file which will be given in a command line
#read through lines in a file
for line in sys.stdin.readlines():
	line = line.strip('\n') #remove all lines
	if line == '': #if the line is blank (sentence boundary)
		print()
		continue
	if line[0] == '#': #if the line is a comment
		print (line)
		continue


	
