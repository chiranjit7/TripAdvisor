from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from nltk.corpus import stopwords 
import os
import string
from nltk.text import Text
import pickle
import sys

class keepusefulchar:
        def  __init__(self,text):
             self.text =text

	def specialchar(self):
    		return self.text.replace('\\', r'').replace('`', r'').replace('*', r'').replace('_', r'').replace('{', r'').replace('}', r'').replace('[', r'').replace(']', r'').replace('(', 		
                r'').replace(')', '').replace('>', r'').replace('#', r'').replace('+', r'').replace('-', r'').replace('$', r'').replace("'", r'').replace("\n", r'')
        
        def removechar(text):
            return keepusefulchar(text)

def get_all_phases_containing_tar_wrd(target_word, sourcefile, hotelname,width):
 #f=open(os.path.expanduser(r"~/Desktop/log_r.txt","wb"), "wb")
 path= '/home/amisha/Desktop/sourcedata/'+sourcefile
 outpufile = target_word+'review'
 f=open(path,'rU')
 saveout = sys.stdout
 SavedConcordance = open(os.path.expanduser(r"~/Desktop/sourcedata/food/"+outpufile+hotelname), "w")     
 sys.stdout = SavedConcordance                                       
 review=f.read()
 tokens = word_tokenize(review)
 #sents = sent_tokenize(review)
 #tokensclean=Text(keepusefulchar(tokens))
 newline=Text(tokens).concordance(target_word,width=width, lines = 80000)
 sys.stdout = saveout                                     
 SavedConcordance.close() 

items = ['food'] #outdoor,'chef'#'kids','food','breakfast','lunch','dinner','snack','poisoning','Indian','cuisine','bar' ,'happy hour','restaurant','room service','drinks']
for f in items:
  get_all_phases_containing_tar_wrd(f, "output_concatFile.txt",f+'_concatFile',200),



