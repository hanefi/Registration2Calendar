from mechanize import Browser
from bs4 import BeautifulSoup
import urllib2
import re

my_user_id="YOUR_USER_ID"
my_user_pass="YOUR_USER_PASSWORD"

def getSchedule(user_id,user_pass):

	browser = Browser()
	browser.set_handle_robots(False)
	browser.open("https://registration.boun.edu.tr/home.htm")

	browser.select_form(nr=0)
	browser['user_id'] = user_id
	browser['user_pass'] = user_pass

	response = browser.submit()

	content = response.read().decode('utf8', 'ignore')

	return content

def getCourseList(schedule):

	courseList = []
	soup = BeautifulSoup(schedule)

	conflictPattern = re.compile(r"(Conflict\d+)")
	classPattern = re.compile(r"(\w+)\s*(\S+)\s+(\S+)\s*(\S+)")

	idTable = soup.table.extract()
	programTable = soup.table.extract()

	days = programTable.find_all("tr")

	for dayNo in xrange(1,6):
		slots = days[dayNo].find_all("td")
		for slotNo in xrange(1,14):	
			text = slots[slotNo].get_text()
#			print u"day '{day}', slot '{slot}', text '{text}'".format(day=dayNo,slot=slotNo,text=text)
#			print text , ";"
			conflict = conflictPattern.search(text)
			if(conflict==None):
				lecture = classPattern.search(text)
				if(lecture!=None):
					courseList.append((dayNo,slotNo,lecture.groups()))

	return courseList

schedule = getSchedule(my_user_id,my_user_pass)
courseList = getCourseList(schedule)

