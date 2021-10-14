
import re

PUNCTS = [".", "?", "!"]
LIMIT = 13

def is_valid_sentence(s):
	numbers_found = find_numbers(s)

	# if no nums found, or, if nums found are < 13
	if(not numbers_found) or (numbers_found and not nums_under_limit(numbers_found)):
		if(begins_capitalized(s)):
			if(ends_with_valid_punctuation(s)):
				if(period_is_at_end(s)):
					if(even_quotes_count(s)):
						return True
	return False

def find_numbers(s):
	# strip string of everything but whitespace, numbers, letters & underscore
	# return a list of numbers found
    s = re.sub(r'[^\w\s]', '', s)
    return [int(s) for s in s.split() if s.isdigit()]
    
def nums_under_limit(nums):
    return any(num<LIMIT for num in nums)

def begins_capitalized(s):
	# s begins w/ capital
	return s[0].isupper()

def ends_with_valid_punctuation(s):
	# ensure last char is valid punctuation
	return s[-1] in PUNCTS

def period_is_at_end(s):
	# if a period occurs, it must be @ end
	return '.' not in s or (('.') in s and s.index('.')==len(s)-1)

def even_quotes_count(s):
	# number of inverted commas must be an even number, suggesting opened & closed 
	return '"' not in s or (('"') in s and s.count('"')%2==0)