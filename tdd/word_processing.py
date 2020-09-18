import re

def split(delimiters, text):
    regexStr = str(['|'.join(delimiters)])
    return list(filter(lambda word: len(word)>0, re.split(regexStr, text)))

def convert_to_word_list(text):
    words = []
    if (len(text) > 0):
        words = list(map(lambda word: word.lower(), split([' ',',',';','.','?'], text.strip(" ,;.?"))))
    return words

def words_longer_than(length, text):
    words = []
    words = convert_to_word_list(text)
    return words