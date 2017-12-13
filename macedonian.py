import sys

#Firstly, I will separate sentencs from one another. We assume that we have a text. 
# I want each sentence to begin from a new line. 
# So we can write a changed version right after the original sentence.
line = sys.stdin.readline()
while line: 
	line = line.replace ('. ', '.\n')
	line = line.replace ('?', '?\n')
	line = line.replace ('!', '!\n')
	print('Original sentence = %s' % (line)) # Printed the original sentence. 
	# Now we will work with the changed sentence
	# which will be printed after this original one.
	print ('Changed sentence = %s' % (line))


	
	line = sys.stdin.readline() #Thisline should be in the end of this while line


# ------------------------------------------------------------------- above is made, below is in process
# Copied from transliterator and will be changed afterwars

table = {'а':'a',
'б':'b',
'в':'v',
'г':'g',
'д':'d',
'ѓ':"g'",
'е':'e',
'ж':'zh',
'з':'z',
'ѕ':'dz',
'и':'i',
'ј':'j',
'к':'k',
'л':'l',
'љ':'lj',
'м':'m',
'н':'n',
'њ':'nj',
'о':'o',
'п':'p',
'р':'r',
'с':'s',
'т':'t',
'ќ':"k'",
'у':'u',
'ф':'f',
'х':'h',
'ц':'c',
'ч':'ch',
'џ':'dzh',
'ш':'sh'}

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
		transliterated = row[1]

		# transliterate it
		for c in table:
				transliterated = transliterated.replace(c, table[c])
		# set the 10th column to the transliterted form
		row[9] = 'Translit=' + transliterated

		#print out line separated by tabs
		print('\t'.join(row))
	


