#
# 1) write a test that fails
# 2) write simplest code that will pass test
# 3) refactor
# #

'''
testing a convert_to_word_list() function:
    simplest test: empty string
    think about:
        - requirements: 
            > does it split on required delimiters?
        - edge cases: 
            > several delimiters following each other
'''
import unittest
import word_processing as wp

# test fixture: class that inherits from class "TestCase" 
# contains test methods 
class WordProcessingTest(unittest.TestCase):
    # will need to test what happens when i pass an empty string to convert_to_word_list()
    # unittest method names format: test_functionName_testDescription
    def test_convertToWordList_emptyStringParameter(self):
        # capture results of function
        words = wp.convert_to_word_list("") # doesn't exist yet. this test will be broken.
        expected_output = []
        # check for expected output
        self.assertEqual(expected_output, words)
    
    def test_convertToWordList_splitsOnDelimiters(self):
        words = wp.convert_to_word_list('These are indeed interesting, an obvious understatement, times. What say you?')
        expected = ['these','are','indeed','interesting','an','obvious','understatement','times','what','say','you']
        self.assertCountEqual(expected, words)
    
    def test_convertToWordList_convertsToLowerCase(self):
        words = wp.convert_to_word_list("ASDF, teSt, Wods; things? welL")
        expected = ["asdf", "test", "wods", "things", "well"]
        self.assertCountEqual(expected, words)

    def test_wordsLongerThan_emptyStringParameter(self):
        words = wp.words_longer_than(1, "")
        expected = []
        self.assertEqual(expected, words)

    def test_wordsLongerThan_withDelimiters(self):
        words = wp.words_longer_than(1, "string with spaces,and commas;notToMentionSemiColons?qMarks.and full stops")
        expected = ["string", "with", "spaces", "and", "commas", "nottomentionsemicolons", "qmarks", "and", "full", "stops"]
        self.assertCountEqual(expected, words)

# run test in global scope
if __name__ == '__main__':
    unittest.main()
# it will fail. now make it not fail.