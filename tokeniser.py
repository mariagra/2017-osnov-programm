import sys

tokens = []
index = 1

# read in one line
line = sys.stdin.readline()
# while we have not read the whole file
while line: 
	# print out the sentence id
	print('# sent_id = %d' % (index))
	# print out the original text of the line, after stripping whitespace
	line = line.strip()
	print ('# text = %s' % (line))
	# replace punctuation with space + punctuation
	line = line.replace (',', ' ,')
	line = line.replace (':', ' :')
	line = line.replace (')', ' )')
	line = line.replace ('(', ' (')
	# split the line into tokens with the ' ' character
	line=line.split(' ')
	tokens.append(line)
	# start counting of tokens in the line
	token_id = 1
	# for each of the tokens in the line
	for token in line:
	# print out the token id, the token itself and 8 empty columns
		print ('%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_\t_' % (token_id, token))
		# increase counting index of tokens in the line
		token_id += 1
	# increase counting index of lines
	index += 1
	print ()
	line = sys.stdin.readline()
	


