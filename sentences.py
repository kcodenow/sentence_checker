NUMS = [str(n) for n in list(range(13))]
PUNCTS = [".", "?", "!"]

def is_valid_sentence(s):
	words = tokenize_sentence(s)

	# TODO - check nums appearing.  use any() in list

	# begins w/ capital
	if(s[0].isupper()):
		# ensure last char is valid punctuation
		if(s[-1] in PUNCTS):
			# if a period occurs, it must be @ end
			if(((('.') in s) and s.index('.')==len(s)-1) or '.' not in s):
				# do we have an even qty of inverted comma?
				if((('"') in words and words['"']%2==0)) or ('"') not in words:
					return True
	return False

def tokenize_sentence(s):
	# dict from words in s
	# keys=words, values=no. times word appears 
	d={}
	for x in s.split(' '):
		if x in d:
			d[x]+=1
		else:
			d[x]=1
	return d