import sys

# At the very beginning I will do all the preparatpry steps. 
# They includes all the dictionaries of replacements that will be done in the sentences.

#  Firstly, we will do transliteration from Macedonian letters to Russian
# We will start this stage from creating a dictionary with letters. Left - Macedonian, Right - Russian.
table1 = {'а':'а',
'б':'б',
'в':'в',
'г':'г',
'д':'д',
'ѓ':'дж',
'е':'е',
'ж':'ж',
'з':'з',
'ѕ':'дз',
'и':'и',
'ј':'й',
'к':'к',
'л':'л',
'љ':'ль',
'м':'м',
'н':'н',
'њ':'нь',
'о':'о',
'п':'п',
'р':'р',
'с':'с',
'т':'т',
'ќ':'ч',
'у':'у',
'ф':'ф',
'х':'х',
'ц':'ц',
'ч':'ч',
'џ':'дж',
'ш':'ш'}

# Then will be the second doctionary where we have some replacements 
# to make our transliterion better.

table2 = {'джа':'джя',
'джо':'джё',
'джу':'джю',
'льа':'ля',
'лье':'ле',
'льи':'ли',
'льо':'лё',
'льу':'лю',
'ньа':'ня',
'нье':'не',
'ньи':'ни',
'ньо':'нё',
'ньу':'ню'}

# We also want to replace some of the words = translate them. 
#We also will do the same with  the some parts of the words.
# We will make all these changes in the whole line later while working with the line.
# We can't do all the words in this projects but we wil put pronouns in the needed forms.


# Now we stert our work with the text

#Firstly, working with text I will separate sentencs from one another. We assume that we have a text. 
# I want each sentence to begin from a new line. 
# So we can write a changed version right after the original sentence.
line = sys.stdin.readline()
while line: 
	line=line.strip()
	if line != '':
		line = line.replace ('. ', '.\n')
		line = line.replace ('?', '?\n')
		line = line.replace ('!', '!\n')
		if line == '': #if the line is blank (sentence boundary)
				print()
				continue
		if line[0] == '#': #if the line is a comment
				print (line)
				continue
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

		for word in line




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


		# We are  translating some of the words and some of the words'parts
		# We will use spaces in the beginning or/and in the end of the word
		# to identify that we work with the word or that we work only with the end of the word
		line = line.replace (' йас ', ' я ')
		line = line.replace (' ти ', ' ты ')
		line = line.replace (' ?', '?')
		line = line.replace (' !', '!')
		line = line.replace (' :', ':')
		line = line.replace (' )', ')')
		line = line.replace ('( ', '(')
		line = line.replace ('„ ', '„')
		line = line.replace (' “', '“')
		line = line.replace (' " ', '"')

# I will increase the number later, now want to fix programming problems
	
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
# Do the separate file which explains what is the program + example of output
#For what we need this line?
		line = sys.stdin.readline() #Thisline should be in the end of this whole line


# ------------------------------------------------------------------- above is made, below is in process (actually it is the middle part)
# Copied from transliterator and will be changed afterwars



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
	


