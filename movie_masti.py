"""
PROJECT 		: LAZY DREAM (a.k.a. MOVIE MASTI)
VERSION			: 1.1
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
> optimised search pattern
> Enabled search loop to finish within 8-10 seconds
> Reduced redundant search

END
"""

#type the movie_name and city
movie_name = "befikre"
city = "bangalore"

#CAUTION, FROM HERE ONWARDS, ONLY DEVELOPERS MAY PROCEED. USERS, PLEASE KEEP YOUR HANDS AWAY
import urllib2
import webbrowser
from datetime import datetime
#if stupid gives an upper case, to handle it!!
city = city.lower()
#what to search for
search_string1 = "title=\"%s"%(movie_name)
search_string2 = "category\\/now showing\"},\"products\":[{\"name\":\"%s"%(movie_name)

found_url = False

#the website where movie is displayed
website = "https://in.bookmyshow.com/%s/movies/nowshowing"%(city)
loop = True
while loop:
	print datetime.now(), " Still Searching"
	#Fetch the url
	respons = urllib2.urlopen(website)
	html_script = respons.read()
	if found_url == False and search_string1.lower() in html_script.lower():		#Searching For Booking Link (search_string1)
		for text in html_script.split("\n"):
			if search_string1.lower() in text.lower():
				found_url = True													#Enabling search_string2 and disabling search_string1 
				moviecode = text.split("href=")[1].split(">")[0].split("\"")[1]		#Fetch the booking link
				booking_link = "https://in.bookmyshow.com%s"%(moviecode)
				break
	if found_url and search_string2.lower() in html_script.lower():					#Search for availibility provided booking link is present
		loop = False
		break
	if found_url:
		print "Movie Link- %s 	Bookings Not Open"%(booking_link)

print "Book Tickets Now!\nBook Here @ ", booking_link
webbrowser.open(booking_link)
