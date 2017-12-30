import urllib
from bs4 import BeautifulSoup
import re
import os
import csv
import sys
import numpy as np

def extracting_review_data (hotelname,url,maxint):

	outpufileR = hotelname+"review.txt"
	pathR= "C:\\Users\\chira\\OneDrive\\Desktop\\Code_dump\\"+outpufileR
  
	orig_stdout = sys.stdout
	f = file(pathR, 'w')
	sys.stdout = f

	for i in range(1, maxint):
		   #print url
		   thepage = urllib.urlopen(url).read().decode('utf8')
		   
		   soup = BeautifulSoup(thepage, "html.parser")
		   text = ' '.join(map(lambda p: p.text, soup.find_all('div',attrs={"class" : "entry"})))
		   soup2 = BeautifulSoup(text,"lxml")
		   text = ' '.join(map(lambda p: p.text, soup2.find_all('p')))
		   soup2 = BeautifulSoup(text, "html.parser")
		   user = ' '.join(map(lambda p: p.text, soup.find_all('div',attrs={"class" : "username mo"})))
           
		   test = text.encode('ascii', 'ignore').decode('ascii')
		   Review = text.replace('\n\n\n', '||').replace('See more room tips', '')
		   recordR = Review
		   recordU = user
		   #if Checker == "REVIEWS":=
		   print(bytes(recordR.encode('ascii', 'ignore').decode('ascii'))+"|"+recordU.encode('ascii', 'ignore').decode('ascii')+ "|" )
		   
		   link = soup.find_all(attrs={"class": "pageNum taLnk "})
		   
		   try:
				linkmax=link[1].get('href')
				#print linkmax +  'Link-1' + str(i)
				url = "http://www.tripadvisor.com" + linkmax
				
				#fileR.write(inkmax +  'Link-0'+ str(i))
		   except:
				linkmax=link[0].get('href')
				#print linkmax +  'Link-0'+ str(i)
				url = "http://www.tripadvisor.com" + linkmax
				

	sys.stdout = orig_stdout
	f.close()
	
try:
    import httplib
except:
    import http.client as httplib

def have_internet(hotelname,urlgiven,maxint=3):
    conn = httplib.HTTPConnection("www.google.com", timeout=1)
    try:
        conn.request("HEAD", "/")
        return extracting_review_data(hotelname,urlgiven,maxint)

    except:
        #conn.close()
        return False


		
have_internet('Hotel53','https://www.tripadvisor.com.sg/ShowUserReviews-g60763-d93421-r359836237-Hotel_Carter-New_York_City_New_York.html',20)

