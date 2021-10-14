import unittest
from sentences import is_valid_sentence

VALIDS = [
	'Capital letter should == valid.'
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
	def test_valids(self):
		for sentence in VALIDS:
			print(f'sentence')
			self.assertEqual(is_valid_sentence(sentence), True)