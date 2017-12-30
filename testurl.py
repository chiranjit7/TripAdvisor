
import urllib
from bs4 import BeautifulSoup
import re

def get_only_text_washington_post_url(url):
    page = urllib.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(page, "html.parser")
    text = ' '.join(map(lambda p: p.text, soup.find_all('div',attrs={"class" : "entry"})))
    user = ' '.join(map(lambda p: p.text, soup.find_all('div',attrs={"class" : "username mo"})))
    soup2 = BeautifulSoup(text)
    text = ' '.join(map(lambda p: p.text, soup2.find_all('p')))
    pageno1 = soup.find_all("span",{"class" : "pageNum current"})
    print user,text, pageno1,
    

someUrl = "https://www.tripadvisor.com.sg/ShowUserReviews-g562690-d1197076-r389951029-Holiday_Inn_Resort_Baruna_Bali-Tuban_Bali.html"
textOfUrl = get_only_text_washington_post_url(someUrl)

#[<span class="pageNum current" data-offset="40" data-page-number="5" onclick="ta.trackEventOnPage('STANDARD_PAGINATION', 'curpage', '5', 0)">5</span>]

   
