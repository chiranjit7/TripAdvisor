import urllib
from bs4 import BeautifulSoup
import re
import os
import csv
import sys
import numpy as np
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from nltk.corpus import stopwords 

url = "https://www.tripadvisor.com.sg/ShowUserReviews-g562690-d1197076-r389951029-Holiday_Inn_Resort_Baruna_Bali-Tuban_Bali.html"
fileR = open(os.path.expanduser(r"~/Desktop/log_r.txt"), "wb")
fileU = open(os.path.expanduser(r"~/Desktop/log_u.txt"), "wb")

Checker = "REVIEWS"

for i in range(1, 263):
   thepage = urllib.urlopen(url).read().decode('utf8') 
   soup = BeautifulSoup(thepage, "html.parser")
   text = ' '.join(map(lambda p: p.text, soup.find_all('div',attrs={"class" : "entry"})))
   soup2 = BeautifulSoup(text,"lxml")
   text = ' '.join(map(lambda p: p.text, soup2.find_all('p')))
   soup2 = BeautifulSoup(text, "html.parser")
   user = ' '.join(map(lambda p: p.text, soup.find_all('div',attrs={"class" : "username mo"})))
       
   user = user
   test = text.encode('ascii', 'ignore').decode('ascii')
   Review = text.replace('\n\n\n', '||').replace('See more room tips', '')
   recordR = Review
   recordU = user
   if Checker == "REVIEWS":
                fileR.write(bytes(str(i) + recordR.encode('ascii', 'ignore').decode('ascii')))
                fileU.write(bytes(str(i) + recordU.encode('ascii', 'ignore').decode('ascii')))
     
   link = soup.find_all(attrs={"class": "pageNum taLnk "})
   #print link[1].get('href')
   if len(link) == 0:
      break
   else:
      soup = BeautifulSoup(urllib.urlopen("http://www.tripadvisor.com" + link[1].get('href')),"html.parser")
      Checker = link[1].get('href')[-7:]
   url = "http://www.tripadvisor.com" + link[1].get('href')
   
fileR.close()
fileU.close()


