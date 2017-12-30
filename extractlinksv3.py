import urllib
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from nltk.corpus import stopwords 
import os
import string
from nltk.text import Text
import sys

orig_stdout = sys.stdout
f = file('/home/amisha/Desktop/sourcedata/listofhotellinks.txt', 'w')
sys.stdout = f

url = 'https://www.tripadvisor.com.sg/Hotels-g294226-Bali-Hotels.html'

for j in range(0,45):
    thepage = urllib.urlopen(url).read().decode('utf8') 
    soup = BeautifulSoup(thepage, "html.parser")
    link = soup.find_all(attrs={"class": "cssTruncatedSnippet"})

    for i in range(0, len(link)):
        soup = BeautifulSoup(urllib.urlopen("http://www.tripadvisor.com" + link[i].find('a')['href']),"html.parser")
        checker = link[i].find('a')['href']
        urlhotel = "http://www.tripadvisor.com" + link[i].find('a')['href'] 
        print urlhotel
        
soup = BeautifulSoup(thepage, "html.parser")        
linkend = soup.find_all(attrs={"class": "nav next ui_button primary taLnk"})
if len(linkend) == 0:
    print len(linkend)
else:
    soup = BeautifulSoup(urllib.urlopen("http://www.tripadvisor.com" + linkend[0].get('href')),"html.parser")
    Checker = linkend[0].get('href')[-7:]
url = "http://www.tripadvisor.com" + linkend[0].get('href')

sys.stdout = orig_stdout
f.close()
