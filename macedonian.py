import sys

#Firstly, I will separate sentencs from one another. We assume that we have a text. 
# I want each sentence to begin from a new line. 
# So we can write a changed version right after the original sentence.
line = sys.stdin.readline()
while line: 
	line=line.strip()
	if line != '':
		line = line.replace ('. ', '.\n')
		line = line.replace ('?', '?\n')
		line = line.replace ('!', '!\n')
		print('Original sentence = %s' % (line)) # Printed the original sentence. 
		# Now we will work with the changed sentence
		# which will be printed after this original one.

		# I am replacing punctuation with space + punctuation 
		# because I will simetimes replace some words from macedonuian to Russian (like a dictionary)
		# that's why I need to work with words without punctuation. 
		# Afterwars we will remove this space between the word and punctuation mark
		line = line.replace ('.', ' .')
		line = line.replace (',', ' ,')
		line = line.replace ('?', ' ?')
		line = line.replace ('!', ' !')
		line = line.replace (':', ' :')
		line = line.replace (')', ' )')
		line = line.replace ('(', '( ')
		line = line.replace ('„', '„ ')
		line = line.replace ('“', ' “')
		line = line.replace ('"', ' " ')


# Transliteration first
# Then changing of the words (prononouns + aux verbs)
# Check whether changibg part of the word is a good idea
# Do the separate file which explains what is the program + example of output
	
		# We are returning the punctuational marks to the original position
		line = line.replace (' .', '.')
		line = line.replace (' ,', ',')
		line = line.replace (' ?', '?')
		line = line.replace (' !', '!')
		line = line.replace (' :', ':')
		line = line.replace (' )', ')')
		line = line.replace ('( ', '(')
		line = line.replace ('„ ', '„')
		line = line.replace (' “', '“')
		line = line.replace (' " ', '"')

#For what we need this line?
		line = sys.stdin.readline() #Thisline should be in the end of this while line


# ------------------------------------------------------------------- above is made, below is in process (actually it is the middle part)
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
	


