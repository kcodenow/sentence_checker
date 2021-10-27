#!/usr/bin/env python3
import unittest
import mock
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

	# end2end - ensure system labels valid sentences as such
	# def test_valids(self):
	# 	sv = SentenceValidator()

	# 	for sentence in VALIDS:
	# 		print(f'{sentence}')
	# 		self.assertEqual(sv.is_valid_sentence(sentence), True)

	# end2end - ensure system labels invalid sentences as such 
	def test_invalids(self):
		sv = SentenceValidator()

		for sentence in INVALIDS:
			print(f'{sentence}')
			self.assertEqual(sv.is_valid_sentence(sentence), False)

	def test_finding_of_numbers_in_string(self):
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

	# each tuple has a string, and bool of whether or not it contains nums under limit
	def test_finding_of_nums_under_limit(self):
		sv = SentenceValidator()

		# each tuple has a list of nums, and a boolean result informing if that list contains a num<limit
		nums = [
			([4, 14], True),
			([1, 2, 3.8], True),
			([13], False),
			([], False),
			([3013, 10000000000], False)
		]

		for numList in nums:
			self.assertEqual(sv.nums_under_limit(numList[0]), numList[1])


	# assert that sentences ending in ?!. results in bool True, otherwise bool False
	def test_starts_with_capital(self):
		sv = SentenceValidator()

		# each tuple has a string, and bool of whether or not it starts with cap
		sentences = [
			('Perfectly valid capitalisation', True),
			('ALL CAPS IN HERE', True),
			('eVERYTHING UPPERCASE BUT THE ONE THAT MATTERS', False),
			('no caps at all', False),
			('', False),
		]

		for s in sentences:
			res = sv.begins_capitalized(s[0])
			self.assertEqual(res, s[1])

	# assert that sentences ending in ?!. results in bool True, otherwise bool False
	def test_ending_punctuation_valid(self):
		sv = SentenceValidator()
		
		# each tuple has a string, and bool of whether or not that string ends in valid punctuation
		sentences = [
			('The big bad wolf.', True),
			('The big bad wolf?', True),
			('The big bad wolf!', True),
			('The big bad wolf&', False),
			('The big bad wolf', False),
			('The big bad wolf', False),
			('', False),
		]
		for s in sentences:
			self.assertEqual(sv.ends_with_valid_punctuation(s[0]), s[1])

	# assert that an even count of quotes results in bool True, otherwise bool False
	def test_quote_count_is_even(self):
		sv = SentenceValidator()
		
		# each tuple has a string, and bool of whether or not it contains en even count of quotes
		sentences = [
			('"Hello", said Jim', True),
			('"Hi", he said. "Goodbye!" she replied', True),
			('"""this one has 6"""', True),
			('"Hello, said Jim', False), 
			('"Hi", he said. "Goodbye! she replied', False), 
			('"""this one has 7""""', False),
		]
		for s in sentences:
			self.assertEqual(sv.even_quotes_count(s[0]), s[1])

	# assert that periods anywhere but the end result in boolean False
	def test_period_position_must_be_end_only(self):
		sv = SentenceValidator()

		# each tuple has a string, and bool of whether or not period exists only at end
		sentences = [
			('Ends with period.', True),
			('.', True),
			('This. period is not at the end', False),
			('This has ellipsis...', False),
			('One. Two. Three.', False),
		]
		for s in sentences:
			self.assertEqual(sv.period_is_at_end(s[0]), s[1])

	# asset system exits as planned, with exit code 1
	def test_application_exit_success(self):
		sv = SentenceValidator()

		# uses a context manager to perform system exit
		with self.assertRaises(SystemExit) as cm:
		    sv.exit()

		self.assertEqual(cm.exception.code, 1)