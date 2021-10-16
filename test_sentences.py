import unittest
from SentenceValidator import SentenceValidator

VALIDS = [
	'The quick brown fox said “hello Mr lazy dog”.',
	'The quick brown fox said hello Mr lazy dog.',
	'One lazy dog is too few, 13 is too many.',
	'One lazy dog is too few, thirteen is too many.',
	'How many "lazy dogs" are there?'
]

INVALIDS = [
	'The quick brown fox said "hello Mr. lazy dog".',
	'the quick brown fox said “hello Mr lazy dog".',
	'"The quick brown fox said “hello Mr lazy dog."',
	'One lazy dog is too few, 12 is too many.',
	'Are there 11, 12, or 13 lazy dogs?',
	'There is no punctuation in this sentence'
]

class TestSentenceValidityChecker(unittest.TestCase):

	def test_find_numbers(self):
		sv = SentenceValidator()

		# each tuple has a string, and a count of nums in that string
		sentences = [
			('one hundred 300 & 66', 2),
			('238947, 32476, and 34', 3),
			('fifty 5', 1),
			('one two three four five six', 0)
		]

		for s in sentences:
			nums = sv.find_numbers(s[0])
		self.assertEqual(len(nums), s[1])

	def test_ending_punctuation_invalid(self):
		sv = SentenceValidator()
		
		sentences = [
			'The big bad wolf&',
			'The big bad wolf',
			'The big bad wolf^'
		]
		for s in sentences:
			self.assertEqual(sv.ends_with_valid_punctuation(s), False)

	def test_ending_punctuation_invalid(self):
		sv = SentenceValidator()
		
		sentences = [
			'The big bad wolf.',
			'The big bad wolf?',
			'The big bad wolf!'
		]
		for s in sentences:
			self.assertEqual(sv.ends_with_valid_punctuation(s), True)

	def test_quote_count_valid(self):
		sv = SentenceValidator()
		
		sentences = [
			'"Hello", said Jim', 
			'"Hi", he said. "Goodbye!" she replied', 
			'"""this one has 6"""'
		]
		for s in sentences:
			self.assertEqual(sv.even_quotes_count(s), True)

	def test_quote_count_invalid(self):
		sv = SentenceValidator()
		
		sentences = [
			'"Hello, said Jim', 
			'"Hi", he said. "Goodbye! she replied', 
			'"""this one has 7""""'
		]
		for s in sentences:
			self.assertEqual(sv.even_quotes_count(s), False)

	def test_period_only_at_end_invalid(self):
		sv = SentenceValidator()

		sentences = [
			'This. period is not at the end.', 
			'This has ellipsis...', 
			'One. Two. Three.'
		]
		for s in sentences:
			self.assertEqual(sv.period_is_at_end(s), False)

	def test_valids(self):
		sv = SentenceValidator()

		for sentence in VALIDS:
			print(f'{sentence}')
			self.assertEqual(sv.is_valid_sentence(sentence), True)

	def test_invalids(self):
		sv = SentenceValidator()

		for sentence in INVALIDS:
			print(f'{sentence}')
			self.assertEqual(sv.is_valid_sentence(sentence), False)