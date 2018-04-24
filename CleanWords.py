
# cleans at the word-level

import re
import nltk
from nltk.corpus import stopwords
from nltk.corpus import words
import string
from string import punctuation
from stop_words import get_stop_words

#stop_words = get_stop_words('en')

rwords = set(words.words())

mystopwords = [set(stopwords.words('english')),get_stop_words('english'),
               "you","interview", "questions", "and", "the", "answers", "that", "not", "would", "for"
              ,"forbidden", "support", "are", "will", "can", "all", "list", "canada", "represent", "forget", "skip"]

def CleanWords(raw):
    clean_text=str.lower(str(raw)) # forces lower case
    clean_text =nltk.word_tokenize (clean_text) # tokenises by word
    clean_text =[word for word in clean_text if len(word)>2] # keeps only words with more than 2 letters
    clean_words =[word for word in clean_text if word in rwords and word not in mystopwords] #removes defined list of stopwords
    return clean_words
