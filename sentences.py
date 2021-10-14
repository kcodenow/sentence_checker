
import pdb

def is_valid_sentence(s):
	words = tokenize_sentence(s)

	# begins w/ capital
	if(s[0].isupper()):
		return True
	return False

def tokenize_sentence(s):
	d={}
	for x in s.split(' '):
		if x in d:
			d[x]+=1
		else:
			d[x]=1
	return d