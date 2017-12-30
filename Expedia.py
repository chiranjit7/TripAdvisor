# tripadvisor Scrapper - use this one to scrape hotels

# importing libraries
from bs4 import BeautifulSoup
import urllib
import os
import urllib.request

# creating CSV file to be used

file = open(os.path.expanduser(r"~/Desktop/TripAdviser Reviews.csv"), "wb")
file.write(
    b"Organization,Address,Reviewer,Review Title,Review,Review Count,Help Count,Attraction Count,Restaurant Count,Hotel Count,Location,Rating Date,Rating" + b"\n")

# List the first page of the reviews (ends with "#REVIEWS") - separate the websites with ,
WebSites = [
    "http://www.tripadvisor.ca/Hotel_Review-g190479-d3587956-Reviews-The_Thief-Oslo_Eastern_Norway.html#REVIEWS"]
Checker = "REVIEWS"
# looping through each site until it hits a break
for theurl in WebSites:
    thepage = urllib.request.urlopen(theurl)
    soup = BeautifulSoup(thepage, "html.parser")
    while True:
        # extract the help count, restaurant review count, attraction review count and hotel review count
        a = b = 0
        helpcountarray = restaurantarray = attractionarray = hotelarray = ""

        for profile in soup.findAll(attrs={"class": "memberBadging g10n"}):
            image = profile.text.replace("\n", "|||||").strip()
            if image.find("helpful vote") > 0:
                counter = image.split("helpful vote", 1)[0].split("|", 1)[1][-4:].replace("|", "").strip()
                if len(helpcountarray) == 0:
                    helpcountarray = [counter]
                else:
                    helpcountarray.append(counter)
            elif image.find("helpful vote") < 0:
                if len(helpcountarray) == 0:
                    helpcountarray = ["0"]
                else:
                    helpcountarray.append("0")

            if image.find("attraction") > 0:
                counter = image.split("attraction", 1)[0].split("|", 1)[1][-4:].replace("|", "").strip()
                if len(attractionarray) == 0:
                    attractionarray = [counter]
                else:
                    attractionarray.append(counter)
            elif image.find("attraction") < 0:
                if len(attractionarray) == 0:
                    attractionarray = ["0"]
                else:
                    attractionarray.append("0")

            if image.find("restaurant") > 0:
                counter = image.split("restaurant", 1)[0].split("|", 1)[1][-4:].replace("|", "").strip()
                if len(restaurantarray) == 0:
                    restaurantarray = [counter]
                else:
                    restaurantarray.append(counter)
            elif image.find("restaurant") < 0:
                if len(restaurantarray) == 0:
                    restaurantarray = ["0"]
                else:
                    restaurantarray.append("0")

            if image.find("hotel") > 0:
                counter = image.split("hotel", 1)[0].split("|", 1)[1][-4:].replace("|", "").strip()
                if len(hotelarray) == 0:
                    hotelarray = [counter]
                else:
                    hotelarray.append(counter)
            elif image.find("hotel") < 0:
                if len(hotelarray) == 0:
                    hotelarray = ["0"]
                else:
                    hotelarray.append("0")

                # extract the rating count for each user review
        altarray = ""
        for rating in soup.findAll(attrs={"class": "rating reviewItemInline"}):
            alt = rating.find('img', alt=True)['alt']
            if alt[-5:] == 'stars':
                if len(altarray) == 0:
                    altarray = [alt]
                else:
                    altarray.append(alt)

        Organization = soup.find(attrs={"class": "heading_name"}).text.replace('"', ' ').replace('Review of',
                                                                                                 ' ').strip()
        Address = soup.findAll(attrs={"class": "format_address"})[0].text.replace(',', '').replace('\n', '').strip()

        # Loop through each review on the page
        for x in range(0, len(hotelarray)):
            try:
                Reviewer = soup.findAll(attrs={"class": "username mo"})[x].text
            except:
                Reviewer = "N/A"
                continue

            Reviewer = Reviewer.replace(',', ' ').replace('”', '').replace('“', '').replace('"', '').strip()
            ReviewCount = soup.findAll(attrs={"class": "reviewerBadge badge"})[x].text.split(' ', 1)[0].strip()
            Location = soup.findAll(attrs={"class": "location"})[x].text.replace(',', ' ').strip()
            ReviewTitle = soup.findAll(attrs={"class": "quote"})[x].text.replace(',', ' ').replace('”', '').replace('“','').replace('"', '').replace('é', 'e').strip()
            Review = soup.findAll(attrs={"class": "entry"})[x].text.replace(',', ' ').replace('\n', ' ').strip()
            RatingDate = soup.findAll(attrs={"class": "ratingDate"})[x].text.replace('Reviewed', ' ').replace('NEW',' ').replace(',', ' ').strip()
            Rating = altarray[x][:1]
            HelpCount = helpcountarray[x]
            AttractionCount = attractionarray[x]
            Restaurant = restaurantarray[x]
            Hotel = hotelarray[x]

            Record = Organization + "," + Address + "," + Reviewer + "," + ReviewTitle + "," + Review + "," + ReviewCount + "," + HelpCount + "," + AttractionCount + "," + Restaurant + "," + Hotel + "," + Location + "," + RatingDate + "," + Rating
            if Checker == "REVIEWS":
                file.write(bytes(Record, encoding="ascii", errors='ignore')  + b"\n")

        link = soup.find_all(attrs={"class": "nav next rndBtn ui_button primary taLnk"})
        print(Organization)
        if len(link) == 0:
            break
        else:
            soup = BeautifulSoup(urllib.request.urlopen("http://www.tripadvisor.com" + link[0].get('href')),"html.parser")
            print(link[0].get('href'))
            Checker = link[0].get('href')[-7:]

file.close()