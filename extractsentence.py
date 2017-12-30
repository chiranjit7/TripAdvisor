import sys
import re
import nltk

path = '/home/amisha/Desktop/sourcedata/'
f="output_concatFile.txt"

fo = open(path + f, "rw+")
review=fo.read()
word = 'food'
sentence= [sent+ '.' for sent in review.split('.') if word in sent] 
sentence =str(sentence)

output = open("/home/amisha/Desktop/sourcedata/foodhotel.txt", "w")
output.write(sentence)
output.close()

