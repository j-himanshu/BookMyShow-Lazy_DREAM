"""
PROJECT 		: LAZY DREAM (a.k.a. MOVIE MASTI)
VERSION			: 3.0
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
#CAUTION, FROM HERE ONWARDS, ONLY DEVELOPERS MAY PROCEED. USERS, PLEASE KEEP YOUR HANDS AWAY
import urllib2
import webbrowser
from datetime import datetime
#Get the movie_name and city
movie_name = raw_input("Enter Movie name : ")
city = raw_input("City? ")
#if stupid gives an upper case, to handle it!!
city = city.lower()
#what to search for
search_string0 = "title=\"%s"%(movie_name)
search_string1 = "/buytickets/%s"%(movie_name.replace(" ", "-"))
#Why search for information URL again and again?
found_url  = False
#the website where movies are displayed
website = "https://in.bookmyshow.com/%s/movies/nowshowing"%(city)
loop = True
while loop:
	print datetime.now(), " Still Searching"	
	response = urllib2.urlopen(website)						#Fetch the url
	html_script = response.read()
	if search_string1.lower() in html_script.lower():		#Searching For Booking Link (search_string1)
		for text in html_script.split("\n"):
			if search_string1.lower() in text.lower():
				moviecode = text.split("href=\"")[1].split("\"><")[0]				#Fetch the booking link
				booking_link = "https://in.bookmyshow.com%s"%(moviecode)
				loop = False
				print "Book Tickets Now @ ", booking_link
				webbrowser.open(booking_link)
				break
	elif found_url == False and search_string0.lower() in html_script.lower():
		for text in html_script.split("\n"):
			if search_string0.lower() in text.lower():
				found_url = True													#disabling search_string0
				moviecode = text.split("href=")[1].split(">")[0].split("\"")[1]		#Fetch the booking link
				booking_link = "https://in.bookmyshow.com%s"%(moviecode)
				print "Information Link Found @ ", booking_link
				break
	if found_url:
		print "Movie Link- %s 	Bookings Not Open"%(booking_link)
