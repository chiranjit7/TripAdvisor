corpusfilepath = "/home/amisha/Desktop/sourcedata/food/"
corpusfile ="foodcorpus"
reviewfilepath="/home/amisha/Desktop/sourcedata/food/"

from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from nltk.corpus import stopwords 
import os
import string
from nltk.text import Text
import pickle
import sys
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation
from heapq import nlargest
import pandas as pd

with open(reviewfilepath+"Review","r") as fine:
    array = []
    for line in fine:
        array.append(line)
        sent = [f for f in array]
    for i in range (0,len(sent)-1):
    	print i, sent[i]
	sents = sent_tokenize(sent[i])
