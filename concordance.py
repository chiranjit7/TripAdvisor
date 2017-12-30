
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from nltk.corpus import stopwords 
import os
import string
from nltk.text import Text
import pickle
import sys
#from  sys.stdout import sys 

#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import nltk, os, sys 
print "\n\n CONCORDANCES SEARCH ENGINE \n" 
#print "These are the files in your current directory \n" 
print os.listdir('.') 
print "\n\n Insert the text filename you want to work with\n" 
#thefile=raw_input() 
f=open('/home/amisha/Desktop/log_r.txt', 'rU') 
text=f.read().decode('utf8','ignore') 
textD=text.split() 
textDS=nltk.Text(textD) 
print "\n Introduce the word you want to find \n" 
theword=raw_input() 
print "\n Concordances with \"" + theword + "\"\n" 
results=textDS.concordance(theword) 
print "\n"


saveout = sys.stdout                                     
SavedConcordance = open('output.txt', 'w')                             
sys.stdout = SavedConcordance                                       
textDS.concordance(theword, width=100, lines=50000)
sys.stdout = saveout                                     
SavedConcordance.close()                                           

print "Succesfuly saved to outfile.txt\n"
