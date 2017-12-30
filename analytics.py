#Analytics
import csv
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.text import Text 
import pickle
import sys
import os
import string
from nltk.corpus import stopwords
from nltk.tag import *
from string import punctuation
from collections import defaultdict

class FrequencySummarizer:
 #ranking = 0
 def __init__(self, min_cut=0.1, max_cut=0.9):
        self._min_cut = min_cut
        self._max_cut = max_cut 
        self._stopwords = set(stopwords.words('english') + list(punctuation))

 def _words(self,path):
    with open(path, 'rb') as f:
     reader = csv.reader(f)
     test= [row for row in reader]
     freq = defaultdict(int)
     #return test
     for i in range (0, len(test)) :
     	try:
        	first = str(test[i]).split(',')[0] 
                second = str(test[i]).split(',')[1] 
                freq[first]= second
                #print freq
        except ValueError:
        	print("Error Value.")
     return freq 
     #print freq
 
 def summarize(self,lines,path):
	#ranking = defaultdict(int)
        ranking =0
        self._freq = self._words(path)
        #print self._freq
        #print self._freq.values()
        #for k, v in self._freq.items():
        #    print k
    	#    if k == "['amisha'":
    	#	new_name =v 
       # 	print k, v, new_name.strip("]")
        #    else:
        #        print "no need"
        for i,sent in enumerate(word_tokenize(lines)):
            for w in sent.split():
                 allwords= "["+w, self._freq.get("["+"'"+w+"'")
                 print allwords
                 if w in allwords.split(','):
                    print w
		    #FrequencySummarizer.ranking += self._freq.get("["+"'"+w+"'")
        	    #print ranking

path='/home/amisha/Desktop/sourcedata/dictionary.csv'
#words(path)
fs = FrequencySummarizer()
summary = fs.summarize('amisha bycycle original english.',path)
#summary = fs._words(path)
#print summary
#print "Hello World"

