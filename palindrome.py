import sys

def is_palindrome(s):
	"""Return True if the given string is a palindrome, otherwise False"""
	rev = ''
	if len(s) == 1:
		return False
	for j in range(1, len(s) + 1):
		rev = rev + s[-j]
	if s == rev:
		return True
	return False	



# Now let's load our frequency list from a file

freq = [] # List to store the frequencies in
fd = open('freq_1.txt', 'r')
for line in fd.readlines():
	line = line.strip() # Remove newline character
	(f,w) = line.split('\t') # Split the line into frequency and wordform
	freq.append((int(f), w))
fd.close()

for i in freq:
	if is_palindrome(i[1]):
		print('%d\t%s' % (i[0], i[1]))