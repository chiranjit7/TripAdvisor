import urllib
from bs4 import BeautifulSoup
import re
import os
import csv
import sys
import numpy as np

def extracting_review_data (hotelname,url,maxint):
	#print url
    #Checker = "REVIEWS"
	outpufileR = hotelname+"review.txt"
	pathR= "C:\\Users\\chira\\OneDrive\\Desktop\\Code_dump\\"+outpufileR
	outpufile_distinct = hotelname+"outpufile_distinct.txt"
	output_path= "C:\\Users\\chira\\OneDrive\\Desktop\\Code_dump\\"+outpufile_distinct
  
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
				
				#fileU.write(inkmax +  'Link-0'+ str(i))
		   
		   #soup = BeautifulSoup(urllib.urlopen("http://www.tripadvisor.com" + linkmax),"html.parser")
				
	
	#print ("step done")
	sys.stdout = orig_stdout
	f.close()
	
	if os.path.isfile(output_path):
		raise OSError('File at {} (output file location) exists.'.format(output_path))

	with open(pathR, 'r') as input_file, open(output_path, 'w') as output_file:
		seen_lines = set()

	def add_line(line):
		seen_lines.add(hash(line))
		return line

	output_file.writelines((add_line(line) for line in input_file if hash(line) not in seen_lines))

				
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


		
have_internet('Hotel53','https://www.tripadvisor.com.sg/ShowUserReviews-g60763-d93421-r719289-Hotel_Carter-New_York_City_New_York.html',20)
'''
import threading
import time
t = threading.Thread(target=have_internet, args=('Hotel53','https://www.tripadvisor.com.sg/ShowUserReviews-g60763-d93421-r329147820-Hotel_Carter-New_York_City_New_York.html',3))
t.start()

while (t.is_alive()):
    time.sleep(2)  ## sleep so that we don't execute the print statement too often
    print "I'm alive!"



'''
	
#https://www.tripadvisor.in/ShowUserReviews-g60763-d93421-r427632854-Hotel_Carter-New_York_City_New_York.html#REVIEWS'
#	
#extracting_review_data('holidayin',urlgiven,300)

#extracting_review_data('Hotel50','https://www.tripadvisor.com.sg/ShowUserReviews-g562690-d588404-r423382034-Bakungs_Beach_Hotel-Tuban_Bali.html#REVIEWS',3000);

#extracting_review_data('Hotel51','https://www.tripadvisor.in/ShowUserReviews-g60763-d267183-r424582467-World_Hotel-New_York_City_New_York.html#REVIEWS',3000);
#extracting_review_data('Hotel52','https://www.tripadvisor.in/ShowUserReviews-g60763-d224229-r296235636-Hotel_Riverside_Studios-New_York_City_New_York.html#REVIEWS',3000);
#extracting_review_data('Hotel53','https://www.tripadvisor.in/ShowUserReviews-g60763-d93421-r427632854-Hotel_Carter-New_York_City_New_York.html#REVIEWS',3000);


#extracting_review_data('Hotel214','http://www.tripadvisor.com/ShowUserReviews-g1465999-d1581596-r410816252-The_Royal_Santrian_Luxury_Beach_Villas-Tanjung_Benoa_Nusa_Dua_Peninsula_Bali.html#review_410816252',3000);
#extracting_review_data('Hotel1','http://www.tripadvisor.com/ShowUserReviews-g297701-d1136203-r408201833-Gajah_Biru_Bungalows-Ubud_Bali.html#review_408201833',3000);
#extracting_review_data('Hotel2','http://www.tripadvisor.com/ShowUserReviews-g297701-d7022088-r412080002-The_Kayon_Resort-Ubud_Bali.html#review_412080002',3000);
#extracting_review_data('Hotel3','http://www.tripadvisor.com/ShowUserReviews-g297701-d1482678-r409090596-Amori_Villas-Ubud_Bali.html#review_409090596',3000);
#extracting_review_data('Hotel4','http://www.tripadvisor.com/ShowUserReviews-g297701-d603335-r411463313-Viceroy_Bali-Ubud_Bali.html#review_411463313',3000);
#extracting_review_data('Hotel5','http://www.tripadvisor.com/ShowUserReviews-g297701-d8293999-r411340990-Mandapa_A_Ritz_Carlton_Reserve-Ubud_Bali.html#review_411340990',3000);
#extracting_review_data('Hotel6','http://www.tripadvisor.com/ShowUserReviews-g469404-d627082-r411193058-The_Kunja_Villas_Spa-Seminyak_Bali.html#review_411193058',3000);
#extracting_review_data('Hotel7','http://www.tripadvisor.com/ShowUserReviews-g469404-d4549522-r405465938-Luna2_Studiotel-Seminyak_Bali.html#review_405465938',3000);
#extracting_review_data('Hotel8','http://www.tripadvisor.com/ShowUserReviews-g469404-d607687-r410938415-Dusun_Villas_Bali-Seminyak_Bali.html#review_410938415',3000);
#extracting_review_data('Hotel9','http://www.tripadvisor.com/ShowUserReviews-g297696-d609918-r404196493-Jamahal_Private_Resort_SPA-Jimbaran_Bali.html#review_404196493',3000);
#extracting_review_data('Hotel10','http://www.tripadvisor.com/ShowUserReviews-g297701-d1810099-r406161294-The_Samaya_Bali_Ubud-Ubud_Bali.html#review_406161294',3000);
#extracting_review_data('Hotel11','http://www.tripadvisor.com/ShowUserReviews-g297701-d307569-r411531124-Komaneka_at_Monkey_Forest-Ubud_Bali.html#review_411531124',3
#extracting_review_data('Hotel8','http://www.tripadvisor.com/ShowUserReviews-g469404-d607687-r410938415-Dusun_Villas_Bali-Seminyak_Bali.html#review_410938415',3000);
#extracting_review_data('Hotel9','http://www.tripadvisor.com/ShowUserReviews-g297696-d609918-r404196493-Jamahal_Private_Resort_SPA-Jimbaran_Bali.html#review_404196493',3000);
#extracting_review_data('Hotel10','http://www.tripadvisor.com/ShowUserReviews-g297701-d1810099-r406161294-The_Samaya_Bali_Ubud-Ubud_Bali.html#review_406161294',3000);
#extracting_review_data('Hotel12','http://www.tripadvisor.com/ShowUserReviews-g297701-d1168205-r411839925-Komaneka_at_Bisma-Ubud_Bali.html#review_411839925',3000);
#extracting_review_data('Hotel13','http://www.tripadvisor.com/ShowUserReviews-g297698-d572368-r409332818-Kayumanis_Nusa_Dua_Private_Villa_Spa-Nusa_Dua_Nusa_Dua_Peninsula_Bali.html#review_409332818',3000);
#extracting_review_data('Hotel14','http://www.tripadvisor.com/ShowUserReviews-g297701-d506292-r410423954-Uma_by_COMO_Ubud-Ubud_Bali.html#review_410423954',3000);
#extracting_review_data('Hotel15','http://www.tripadvisor.com/ShowUserReviews-g297701-d626311-r411641144-Komaneka_at_Tanggayuda-Ubud_Bali.html#review_411641144',3000);
#extracting_review_data('Hotel16','http://www.tripadvisor.com/ShowUserReviews-g2646686-d6478989-r408495141-Floating_Leaf_Eco_Luxury_Retreat-Sukawati_Bali.html#review_408495141',3000);
#extracting_review_data('Hotel17','http://www.tripadvisor.com/ShowUserReviews-g297696-d651426-r411667389-Kayumanis_Jimbaran_Private_Estate_Spa-Jimbaran_Bali.html#review_411667389',3000);
#extracting_review_data('Hotel18','http://www.tripadvisor.com/ShowUserReviews-g469404-d603376-r409315991-The_Samaya_Bali_Seminyak-Seminyak_Bali.html#review_409315991',3000);
#extracting_review_data('Hotel19','http://www.tripadvisor.com/ShowUserReviews-g297701-d609896-r404289302-Junjungan_Ubud_Hotel_and_Spa-Ubud_Bali.html#review_404289302',3000);
#extracting_review_data('Hotel20','http://www.tripadvisor.com/ShowUserReviews-g1599559-d309351-r407922928-The_Damai-Lovina_Beach_Bali.html#review_407922928',3000);
#extracting_review_data('Hotel21','http://www.tripadvisor.com/ShowUserReviews-g297696-d7311692-r409121746-The_Villas_at_AYANA_Resort-Jimbaran_Bali.html#review_409121746',3000);
#extracting_review_data('Hotel22','http://www.tripadvisor.com/ShowUserReviews-g297701-d2314151-r411243414-Komaneka_at_Rasa_Sayang-Ubud_Bali.html#review_411243414',3000);
#extracting_review_data('Hotel23','http://www.tripadvisor.com/ShowUserReviews-g608487-d7289453-r410335559-Seaside_Suites_Bali-Legian_Bali.html#review_410335559',3000);
#extracting_review_data('Hotel24','http://www.tripadvisor.com/ShowUserReviews-g297701-d309331-r412025519-Wapa_di_Ume_Resort_and_Spa-Ubud_Bali.html#review_412025519',3000);
#extracting_review_data('Hotel25','http://www.tripadvisor.com/ShowUserReviews-g469404-d594928-r412125123-The_Elysian-Seminyak_Bali.html#review_412125123',3000);
#extracting_review_data('Hotel26','http://www.tripadvisor.com/ShowUserReviews-g469404-d301649-r411750462-The_Legian_Bali-Seminyak_Bali.html#review_411750462',3000);
#extracting_review_data('Hotel27','http://www.tripadvisor.com/ShowUserReviews-g297701-d518441-r406856871-The_Chedi_Club_Tanah_Gajah_Ubud_Bali_a_GHM_hotel-Ubud_Bali.html#review_406856871',3000);
#extracting_review_data('Hotel29','http://www.tripadvisor.com/ShowUserReviews-g297698-d3633238-r410834574-Mulia_Villas-Nusa_Dua_Nusa_Dua_Peninsula_Bali.html#review_410834574',3000);
#extracting_review_data('Hotel30','http://www.tripadvisor.com/ShowUserReviews-g1629368-d1082544-r411689255-Zen_Resort_Bali-Seririt_Bali.html#review_411689255',3000);
#extracting_review_data('Hotel31','http://www.tripadvisor.com/ShowUserReviews-g469404-d302392-r412145833-The_Oberoi_Bali-Seminyak_Bali.html#review_412145833',3000);
#extracting_review_data('Hotel32','http://www.tripadvisor.com/ShowUserReviews-g297701-d5279694-r410119271-Sankara_Resort-Ubud_Bali.html#review_410119271',3000);
#extracting_review_data('Hotel33','http://www.tripadvisor.com/ShowUserReviews-g1137831-d7733886-r407333181-The_Ocean_Sunset_Villas_Ceningan-Nusa_Lembongan_Bali.html#review_407333181',3000);
#extracting_review_data('Hotel34','http://www.tripadvisor.com/ShowUserReviews-g469404-d3683062-r412308047-PING_Hotel_Seminyak_Bali-Seminyak_Bali.html#review_412308047',3000);
#extracting_review_data('Hotel35','http://www.tripadvisor.com/ShowUserReviews-g469404-d6635852-r412532984-Courtyard_Bali_Seminyak_Resort-Seminyak_Bali.html#review_412532984',3000);
#extracting_review_data('Hotel36','http://www.tripadvisor.com/ShowUserReviews-g1137831-d1234550-r387985129-Oka7_Bungalow-Nusa_Lembongan_Bali.html#review_387985129',3000);
#extracting_review_data('Hotel37','http://www.tripadvisor.com/ShowUserReviews-g297701-d6938623-r410491106-Puri_Sebali_Resort-Ubud_Bali.html#review_410491106',3000);
#extracting_review_data('Hotel38','http://www.tripadvisor.com/ShowUserReviews-g608487-d307581-r408992925-Legian_Beach_Hotel-Legian_Bali.html#review_408992925',3000);
#extracting_review_data('Hotel39','http://www.tripadvisor.com/ShowUserReviews-g469404-d7368654-r412570693-The_Trans_Resort_Bali-Seminyak_Bali.html#review_412570693',3000);
#extracting_review_data('Hotel40','http://www.tripadvisor.com/ShowUserReviews-g297697-d3947950-r408174578-The_Kuta_Beach_Heritage_Hotel_Bali_Managed_by_Accor-Kuta_Bali.html#review_408174578',3000);
#extracting_review_data('Hotel41','http://www.tripadvisor.com/ShowUserReviews-g297701-d2648944-r401570104-Sunset_Hill-Ubud_Bali.html#review_401570104',3000);
#extracting_review_data('Hotel42','http://www.tripadvisor.com/ShowUserReviews-g297696-d6476817-r408507298-The_Open_House-Jimbaran_Bali.html#review_408507298',3000);
#extracting_review_data('Hotel43','http://www.tripadvisor.com/ShowUserReviews-g297701-d639773-r391907358-Ketut_s_Place-Ubud_Bali.html#review_391907358',3000);
#extracting_review_data('Hotel44','http://www.tripadvisor.com/ShowUserReviews-g469404-d534638-r411024159-The_Royal_Beach_Seminyak_Bali_MGallery_Collection-Seminyak_Bali.html#review_411024159',3000);
#extracting_review_data('Hotel45','http://www.tripadvisor.com/ShowUserReviews-g297701-d309357-r404732982-Hotel_Tjampuhan_Spa-Ubud_Bali.html#review_404732982',3000);
#extracting_review_data('Hotel46','http://www.tripadvisor.com/ShowUserReviews-g469404-d2515034-r412046407-Centra_Taum_Seminyak_Bali-Seminyak_Bali.html#review_412046407',3000);
#extracting_review_data('Hotel47','http://www.tripadvisor.com/ShowUserReviews-g608487-d1391615-r412040315-Pullman_Bali_Legian_Nirwana-Legian_Bali.html#review_412040315',3000);
#extracting_review_data('Hotel48','http://www.tripadvisor.com/ShowUserReviews-g297697-d7931034-r412525350-Four_Points_by_Sheraton_Bali-Kuta_Bali.html#review_412525350',3000);

