import nltk
from nltk.tag import *
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords 
import os
import string
from nltk.text import Text
import sys
dest = '/home/amisha/Desktop/sourcedata/'
def bag_of_words(path):
	import string
	f="foodhotel.txt"

	fo = open(path + f, "rw+")
	review=fo.read()

	sentence=word_tokenize(review)
	tokens = pos_tag(Text(sentence))
	customStopWords=set(stopwords.words('english')+list(string.punctuation))
	useful_words= [words for words in tokens if words not in customStopWords]
	nouns = [word for word,pos in useful_words if pos == 'JJ' or pos=='VBG' or pos=='NN' or pos == 'RB' or pos == 'VB']
	freq_nouns=nltk.FreqDist(nouns)
	adj_tags=str(freq_nouns.most_common(100000))
	check = adj_tags.split('),')
	string_list = ''
	for word in check: 
	   string_list = string_list+'\n'+ str(word)
        print string_list
        output = open("/home/amisha/Desktop/sourcedata/output_food.txt", "w")
	output.write(string_list)
	output.close() 

bag_of_words(dest)




