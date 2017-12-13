import sys

fd = open('model.tsv', 'r') # we are opening ofur model in the file

freq = 0
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

	row = line.split('\t')
	# take the wordform (column 2)
	wordform = row[1]

	for line in fd:
		if wordform in row[4]: # I am trying to find the word from the considered text in the model
			freq = row[0]

		
	
for line in fd:
	
# freq_tag - Noun
# freq_word_tag = {}
# freq_word_tag['book'] = 'NOUN'