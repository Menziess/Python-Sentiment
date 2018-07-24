import os
import sys
import csv
import glob
import nltk
import string
import pandas as pd
import numpy as np

nltk.download('punkt')
nltk.download('stopwords')

from many_stop_words import get_stop_words
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from collections import Counter

class Tokenizer:
	"""Cleans and tokenizes text body"""

	def tokenize(body):
		tokens = word_tokenize(body)
		tokens = [w.lower() for w in tokens]
		tokens = [w for w in tokens if len(w) > 2]
		table = str.maketrans('', '', string.punctuation)
		stripped = [w.translate(table) for w in tokens]
		words = [word for word in stripped if word.isalpha()]
		stop_words = list(get_stop_words('nl'))
		nltk_words = list(stopwords.words('dutch'))
		stop_words.extend(nltk_words)
		words = [w for w in words if not w in stop_words]
		stemmer = SnowballStemmer("dutch")
		words = [stemmer.stem(word) for word in words]
		return words

if __name__ == '__main__':
	Tokenizer.tokenize(sys.argv[1])
