#imports
import parameters
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from parsel import Selector

# specicifies the path to the chromedriver.exe
driver = webdriver.Chrome('/Users/bvojt/Desktop/GitHub/HatchTwitterBot/chromedriver_win32/chromedriver')

# navigates to the URL mentioned
driver.get('https://www.linkedin.com')

# locate email form by xpath and enters email
username = driver.find_element_by_xpath('//*[@id="session_key"]')
username.send_keys(parameters.linkedin_username)
sleep(0.5)

#locate password form by xpath and enters password
password = driver.find_element_by_xpath('//*[@id="session_password"]')
password.send_keys(parameters.linkedin_password)
sleep(0.5)

#locates submit button by xpath and clicks
log_in_button = driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div/div/form/button')
log_in_button.click()
sleep(1)

#navigates to google and performs search in new tab
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("http://www.google.com")
sleep(0.5)

#locates search box and types in search string
search_query = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

search_query.send_keys(parameters.search_query)
search_query.submit()
sleep(3)

#locate URL by_class_name
linkedin_urls = driver.find_elements_by_class_name('iUh30')

#variable linkedin_urls is equal to the list comprehension
linkedin_urls = [url.text for url in linkedin_urls]

driver.page_source

#For loop to go over each URL in list
for linkedin_url in linkedin_urls:

	#gets profile URl
	driver.get(linkedin_url)

	#pause
	sleep(5)

	#assigns the source code for the webpage to variable sel
	sel = Selector(text=driver.page_source)

#xpath to extract the h1 name
name = sel.xpath('//*[@id="ember351"]/div[2]/div[2]/div[1]/div[1]/h1')

if name:
	name = name.strip()

#xpath to extract the job title and current company
job_title = sel.xpath('//*[@id="ember351"]/div[2]/div[2]/div[1]/div[2]')

if job_title:
	job_title = job_title.strip()

#xpath to extract 


#exit