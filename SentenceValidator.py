
import re
import sys

class SentenceValidator(object):
	def __init__(self):
		self.CLOSING_PUNCTS = [".", "?", "!"]
		self.LIMIT = 13

	def __str__(self):
		return "The SentenceValidator is used to validate sentences based on rules."

	def print_rules(self):
		print(
			'Welcome to Sentence Validation\n\
			The following rules apply:\n\
			1\tSentence must start with a capital letter\n\
			2\tSentence must have an even no. quotation marks\n\
			3\tSentence must end with any of ?!.\n\
			4\tSentence may have no period other than the final char\n\
			5\tNumbers below 13 must be spelled\n\
			\ntype Q to quit!\n'
		)

	def begin_validate_sentences(self):
		# continually validate sentences, unless user quits
		while(True):
			sentence = input('Your sentence, please:\n')
			if(sentence.lower() == 'q'):
				self.exit()
			else:
				self.check_validity(sentence)


	def check_validity(self, s):
		msg = f'A valid sentence, indeed!\n' if self.is_valid_sentence(s)\
		 else f'That sentence is invalid\n'
		print(msg)

	def is_valid_sentence(self, s):
		numbers_found = self.find_numbers(s)

		# if no nums found, or, if nums found are < 13
		if(not numbers_found) or (numbers_found and not self.nums_under_limit(numbers_found)):
			if(self.begins_capitalized(s)):
				if(self.ends_with_valid_punctuation(s)):
					if(self.period_is_at_end(s)):
						if(self.even_quotes_count(s)):
							return True
		return False

	def find_numbers(self, s):
		# strip string of everything but whitespace, numbers, letters & underscore
		# return a list of numbers found
	    s = re.sub(r'[^\w\s]', '', s)
	    return [int(s) for s in s.split() if s.isdigit()]
	    
	def nums_under_limit(self, nums):
	    return any(num<self.LIMIT for num in nums)

	def begins_capitalized(self, s):
		# s begins w/ capital
		return s[0].isupper()

	def ends_with_valid_punctuation(self, s):
		# ensure last char is valid punctuation
		return s[-1] in self.CLOSING_PUNCTS

	def period_is_at_end(self, s):
		# if a period occurs, it must be @ end
		return '.' not in s or (('.') in s and s.index('.')==len(s)-1)

	def even_quotes_count(self, s):
		# number of inverted commas must be an even number, suggesting opened & closed 
		return '"' not in s or (('"') in s and s.count('"')%2==0)

	def exit(self):
		print('Goodbye!') # & terminate
		sys.exit()