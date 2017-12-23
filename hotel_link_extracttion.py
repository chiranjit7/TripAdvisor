import urllib
from bs4 import BeautifulSoup
import os
import string
import sys
import pandas as pd
'''
This program intends to extract all the review pages for the hotels in Bali from Trip Advisor.
Even if your connection fails, dont worry it will take care of that.
Only pain part it is it will start from the begining. At the end it will only give you the distinct 
hotel names.

You just have to give the first page in the URL.
It is fine if your internet connection dies in between.
It will not impact the code.

Also you dont need to worry about the total pages out there for your location.


'''
orig_stdout = sys.stdout
f = file('input_file.txt', 'w')
sys.stdout = f

main_url = 'https://www.tripadvisor.com.sg/Hotels-g60763-New_York_City_New_York-Hotels.html' ## Give the first page of the hotel list. Here this is the page which comes when you search with BALI + Hotels


def hotellinst(url,k=0):
	
		thepage = urllib.urlopen(url).read().decode('utf8') 
		soup = BeautifulSoup(thepage, "html.parser")

		link = soup.find_all(attrs={"class": "pageNum last taLnk "})
		max_len= max_len = int(str(str(link[0])[43:49].split(' ')[0])[1:len(str(str(link[0])[43:49].split(' ')[0]))-1])/30 +1
		       
		for j in range(2,max_len+1):
			thepage = urllib.urlopen(url).read().decode('utf8') 
			soup = BeautifulSoup(thepage, "html.parser")
			link_new = soup.find_all(attrs={"class":"prw_rup prw_meta_hsx_responsive_listing bottom-sep"})
					
			for i in range(0, len(link_new)):

				soup = BeautifulSoup(urllib.urlopen("http://www.tripadvisor.com" + link_new[i].find('a')['href']),"html.parser")
                
				checker = link_new[i].find('a')['href']

				urlhotel = "http://www.tripadvisor.com" + checker 
				
				print urlhotel
				#print url
				
			url= main_url[:len('-'.join([s for s in main_url.split('-')[:2]]))]+'-oa'+str((j-1)*30)+'-'+main_url[(len('-'.join([s for s in main_url.split('-')[:2]])))+1:len(main_url)]
			
try:
    import httplib
except:
    import http.client as httplib

def have_internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=1)
    try:
        conn.request("HEAD", "/")
        
        return hotellinst(main_url)
		#conn.close()
    except:
        #conn.close()
        return False

have_internet()

sys.stdout = orig_stdout
f.close()
	
def remove_duplicate_lines(input_path, output_path):

    if os.path.isfile(output_path):
        raise OSError('File at {} (output file location) exists.'.format(output_path))

    with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
        seen_lines = set()

        def add_line(line):
            seen_lines.add(hash(line))
            return line

        output_file.writelines((add_line(line) for line in input_file
                                if hash(line) not in seen_lines))

				
remove_duplicate_lines('input_file.txt','output_file_all.txt')
