
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from nltk.corpus import stopwords 
import os
import string
from nltk.text import Text
import pickle
import sys
#from  sys.stdout import sys 


def n_concordance_tokenised(text,phrase,left_margin=5,right_margin=5):
    #concordance replication via https://simplypython.wordpress.com/2014/03/14/saving-output-of-nltk-text-concordance/
    #phraseList=phrase.split(' ')
    phraseList ="Chiru is a nice guy"
    c = nltk.ConcordanceIndex(text.tokens, key = lambda s: s.lower())
     
    #Find the offset for each token in the phrase
    offsets=[c.offsets(x) for x in phraseList]
    offsets_norm=[]
    #For each token in the phraselist, find the offsets and rebase them to the start of the phrase
    for i in range(len(phraseList)):
        offsets_norm.append([x-i for x in offsets[i]])
    #We have found the offset of a phrase if the rebased values intersect
    #--
    # http://stackoverflow.com/a/3852792/454773
    #the intersection method takes an arbitrary amount of arguments
    #result = set(d[0]).intersection(*d[1:])
    #--
    intersects=set(offsets_norm[0]).intersection(*offsets_norm[1:])
     
    concordance_txt = ([text.tokens[map(lambda x: x-left_margin if (x-left_margin)>0 else 0,[offset])[0]:offset+len(phraseList)+right_margin]
                        for offset in intersects])
                          
    outputs=[''.join([x+' ' for x in con_sub]) for con_sub in concordance_txt]
    return outputs
 
def n_concordance(txt,phrase,left_margin=5,right_margin=5):
    tokens = nltk.word_tokenize(txt)
    text = nltk.Text(tokens)
  
    return n_concordance_tokenised(text,phrase,left_margin=left_margin,right_margin=right_margin)

