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
		print('Original text = %s' % (line)) # Printed the original text. 
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

		# Now we start working with the words 
		for c in table1: 
			line = line.replace(c, table1[c]) # First step of transliteration = change the letters according to the first dictionary

		for c in table2: 
			line = line.replace(c, table2[c]) # Second step of transliteration 


		# We are  translating some of the words and some of the words'parts
		# We will use spaces in the beginning or/and in the end of the word
		# to identify that we work with the word or that we work only with the end of the word
		line = line.replace (' йас ', ' я ')  # from here start pronouns (starting from NOM)
		line = line.replace (' ти ', ' ты ')
		line = line.replace (' ние ', ' мы ')
		line = line.replace (' вие ', ' вы ')
		line = line.replace (' той ', ' он ')
		line = line.replace (' тоа ', ' оно ')
		line = line.replace (' таа ', ' она ')
		line = line.replace (' тие ', ' они ')
		line = line.replace (' мене ', ' меня/мне ') # starting ACC (and DAT if they are the same)
		line = line.replace (' ме ', ' меня ')
		line = line.replace (' тебе ', ' тебя/тебе ')
		line = line.replace (' те ', ' тебя ')
		line = line.replace (' себе ', ' себя/себе ')
		line = line.replace (' се ', ' себя ')
		line = line.replace (' ве ', ' вас ') # some forms are the same in Russian and Macedonian
		# e.g. vas in Macedonian = вас in Russian. They won't be in this list of changes.
		line = line.replace (' него ', ' его ')
		line = line.replace (' го ', ' его ')		
		line = line.replace (' неа ', ' её ')
		line = line.replace (' йа ', ' её ')	
		line = line.replace (' нив ', ' их ')	
		line = line.replace (' ги ', ' их ')	
		line = line.replace (' ми ', ' мне ') # starting DAT (the rest)
		line = line.replace (' ти ', ' тебе ')
		line = line.replace (' си ', ' себе ')
		line = line.replace (' ни ', ' нам ')
		line = line.replace (' ви ', ' вам ')
		line = line.replace (' нему ', ' ему ')
		line = line.replace (' му ', ' ему ')
		line = line.replace (' нейзе ', ' ей ')
		line = line.replace (' ним ', ' им ')
		line = line.replace (' мойа ', ' моя ') # starting possessives
		line = line.replace (' мойот ', ' мой ')
		line = line.replace (' мойата ', ' моя ')
		line = line.replace (' моето ', ' моё ')
		line = line.replace (' моите ', ' мои ')
		line = line.replace (' твойа ', ' твоя ')
		line = line.replace (' твойот ', ' твой ')
		line = line.replace (' твойата ', ' твоя ')
		line = line.replace (' твоето ', ' твоё ')
		line = line.replace (' твоите ', ' твои ')
		line = line.replace (' свойа ', ' своя ')
		line = line.replace (' свойот ', ' свой ')
		line = line.replace (' свойата ', ' своя ')
		line = line.replace (' своето ', ' своё ')
		line = line.replace (' своите ', ' свои ')
		line = line.replace (' нашиот ', ' наш ')
		line = line.replace (' нашата ', ' наша ')
		line = line.replace (' нашето ', ' наше ')
		line = line.replace (' нашите ', ' наши ')
		line = line.replace (' вашиот ', ' ваш ')
		line = line.replace (' вашата ', ' ваша ')
		line = line.replace (' вашето ', ' ваше ')
		line = line.replace (' вашите ', ' ваши ')
		line = line.replace (' негов ', ' его ')
		line = line.replace (' негова ', '  его ')
		line = line.replace (' негово ', ' его ')
		line = line.replace (' негови ', ' его ')
		line = line.replace (' неговиот ', ' его ')
		line = line.replace (' неговата ', '  его ')
		line = line.replace (' неговото ', ' его ')
		line = line.replace (' неговите ', ' его ')
		line = line.replace (' нейзин ', ' её ')
		line = line.replace (' нейзина ', '  её ')
		line = line.replace (' нейзино ', ' её ')
		line = line.replace (' нейзини ', ' её ')
		line = line.replace (' нейзиниот ', ' её ')
		line = line.replace (' нейзината ', '  её ')
		line = line.replace (' нейзиното ', ' её ')
		line = line.replace (' нейзините ', ' её ')
		line = line.replace (' нивни ', ' их ')
		line = line.replace (' нивна ', '  их ')
		line = line.replace (' нивно ', ' их ')
		line = line.replace (' нивни ', ' их ')
		line = line.replace (' нивниот ', ' их ')
		line = line.replace (' нивниота ', '  их ')
		line = line.replace (' нивниото ', ' их ')
		line = line.replace (' нивниоти ', ' их ')

		line = line.replace ('ски ', 'ский ') # from here start endings
		line = line.replace ('ска ', 'ская ')
		line = line.replace ('ско', 'ское ')
	
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

		print('Changed text = %s' % (line)) # Printed the changed text. 

		line = sys.stdin.readline()








