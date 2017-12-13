import sys
# mapping between form + tag -> frequency
m = {} # m['house']['NOUN'] = 0
m_freq = {} # dictionary for calculating frequency of tags
c = 0
# read through each of the lines
for line in sys.stdin.readlines():
	# if the line is a comment, skip it
	if line[0] == '#':
		continue
	#if the line doesn't contain a tab, skip it
	if '\t' not in line:
		continue
	# make a list of columns
	row = line.split('\t')

	tag = row[3]
	form = row[1]

	if form not in m: # if we haven't seen the form before
		m[form] = {} # make a new map to hold tag -> frequency
	if tag not in m[form]: # if we haven't seen the tag for this form before
		m[form][tag] = 0

	m[form][tag] = m[form][tag] + 1 #increment the count by 1
	c = c + 1

	# the same with m_freq (frequency of the tag)
	if tag not in m_freq:
		m_freq[tag] = 0
	m_freq[tag] = m_freq[tag] + 1

print ('# P \t count \t tag \t form')

for line in m_freq:
	a = m_freq[line]
	b = a/c
	print (b,'\t',m_freq[line],'\t',line,'\t', '-')

for line in m:
	for tag in m[line]:
		a = m[line][tag]
		b = a/c
		print (b,'\t',m[line][tag],'\t',tag,'\t',line)
	

