import sys

def is_palindrome(s): 
	"""Return True if the given string is a palindrome."""
	return False

# Now let's load our frequency list from a file

freq = [] # List to store the frequencies in
fd = open('freq.txt', 'r')
for line in fd.readlines():
	line = line.strip() # Remove newline character
	(f,w) = line.split('\t') # Split the line into frequency and wordform
	freq.append((int(f), w))
fd.close()

for i in freq:
	palindrome = False
	rev = '' #String to store the reverse of the input string
	if len(i[1]) == 1:
		#String of length 1 can't be a palindrome
		continue
	#Now compute the reverse of the word
	#We do this by iterating backwards through the string
	for j in range(1, len(i[1]) + 1):
		rev = rev + i[1][-j]
	if i[1] == rev: #if the reverse is the same as the original
		palindrome = True 
	if palindrome:
		print('%d\t%s' % (i[0], i[1]))