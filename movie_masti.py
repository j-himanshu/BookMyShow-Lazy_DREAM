"""
PROJECT 		: LAZY DREAM (a.k.a. MOVIE MASTI)
VERSION			: BETA
CREATED BY 		: HIMANSHU JANAWADKAR
DATE 			: NOV 30, 2016
PURPOSE			: 1. PROMOTE LAZYNESS FOR PEOPLE WHO WANT TO SEARCH MOVIES ON bookmyshow.com
				  2. CONTINUESLY CHECKS FOR THE MOVIES, ONCE THE BOOKING STARTS, IT REDIRECTS YOU TO WEBSITE
				  3. BENEFITIAL FOR HOTSELLER MOVIES

			             <!- Note For Developers -->
             If you are trying to optimise the code and realized that
    it was the biggest mistake trying to figure out impossible ways to optimize,
then increment the following counter by the number of hours you wasted on this code

COUNTER 		: 12
LAST CHANGES 	: (All the developmental changes down here)


END
"""

#type the movie_name and city
movie_name = "kahaani 2"
city = "bangalore"

#CAUTION, FROM HERE ONWARDS, ONLY DEVELOPERS MAY PROCEED. USERS, PLEASE KEEP YOUR HANDS AWAY
import urllib2
import webbrowser
from datetime import datetime
#if stupid gives an upper case, to handle it!!
city = city.lower()
#what to search for
search_string1 = "category\\/now showing\"},\"products\":[{\"name\":\"%s"%(movie_name)
search_string2 = "title=\"%s"%(movie_name)

#the website where movie is displayed
website = "https://in.bookmyshow.com/%s/movies/nowshowing"%(city)
loop = True
while loop:
	print datetime.now(), " Still Searching"
	#Fetch the url
	respons = urllib2.urlopen(website)
	html_script = respons.read()
	if search_string1.lower() in html_script.lower():
		#Search the webpage
		for text in html_script.split("\n"):
			if search_string2.lower() in text.lower():
				loop = False
				break

moviecode = text.split("href=")[1].split(">")[0].split("\"")[1]		#Fetch the booking link
booking_link = "https://in.bookmyshow.com%s"%(moviecode)

print "Book Tickets Now!\nBook Here @ ", booking_link
webbrowser.open(booking_link)
