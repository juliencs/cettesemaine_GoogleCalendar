def webscrape(my_url):
	global title
	global name
	global date
	global location
	global title_strip 
	global name_strip
	global date_strip
	global location_strip
	title_strip = []
	name_strip = []
	date_strip = []
	location_strip = []
	#Note that you will need to install selenium with pip to use the webdriver function
	from selenium import webdriver
	#Here, I use Chrome as my web browser. Note that you will need to download chomedriver for selenium
	option = webdriver.ChromeOptions()
	option.add_argument("--incognito")
	#insert the location of the chromewebdriver executable
	driver = webdriver.Chrome(executable_path = "/Users/juliencouture-senecal/Desktop/webscrape/selenium/chromedriver", chrome_options = option)		
	driver.get(my_url)
	title = driver.find_elements_by_xpath("//div[@class='views-field views-field-title']")
	name = driver.find_elements_by_xpath("//div[@class='views-field views-field-field-name']")
	date = driver.find_elements_by_xpath("//div[@class='views-field views-field-field-date']")
	location = driver.find_elements_by_xpath("//div[@class='views-field views-field-field-location']")
	for i in range(len(date)):
		title_strip.append(title[i].text.replace(',', ''))
		name_strip.append(name[i].text.replace(',', ''))
		temp_date = date[i].text.strip('Monday').strip('Tuesday').strip('Wednesday').strip('Thursday').strip('Friday').strip('Saturday').strip('Sunday').replace(',', '').replace('January', '01').replace('February', '02').replace('March', '03').replace('April', '04').replace('May', '05').replace('June', '06').replace('July', '07').replace('August', '08').replace('September', '09').replace('October', '10').replace('November', '11').replace('December', '12').replace(' - ', ',').strip(' ').replace(' ', '/').replace('pm', ' PM').replace('am', ' AM')
		date_strip.append(temp_date.split(','))
		location_strip.append(location[i].text.replace(',', ''))
	driver.close()
def write_csv(file):
	import os
	from datetime import datetime  
	from datetime import timedelta
	#insert the location where you want the csv file to be in
	os.chdir("/Users/juliencouture-senecal/Desktop/webscrape")
	filename = str(file)+'.csv'
	f = open(filename, "w")
	headers = "Subject, Start Date, Start Time, End Time, Location\n"
	f.write(headers)
	for i in range(len(date_strip)):	
		f.write(title_strip[i].strip('.') + ' by ' + name_strip[i] + ',' + date_strip[i][0] + ','+ date_strip[i][1] +','+location_strip[i] + "\n")
	f.close()
webscrape('http://cettesemaine.utoronto.ca/?q=thisweek')
write_csv('cettesemaine')

