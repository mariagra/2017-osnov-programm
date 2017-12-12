import sys
from pprint import pprint

rus = ['бы', 'вас', 'видит', 'всего', 'вы']
eng = ['a', 'absorbed', 'all', 'and', 'another']

m = {}

# We first loop through the Russian list and make a new sub
# dict for each item in the list
for w1 in rus: 
	if w1 not in m: 
		m[w1] = {}
	# After that we loop through the English list and set every
	# pair in the matrix to 0
	for w2 in eng:
		m[w1][w2] = 0

pprint(m)