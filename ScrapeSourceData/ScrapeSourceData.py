from bs4 import BeautifulSoup
import requests
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


"""source = "CTA 102"  # Source name for which other catalog names should be found
driver = webdriver.Chrome() # Used Google Chrome WEB browser
driver.get("https://openuniverse.asi.it/open_universe.html") # This page is used for scraping

element = driver.find_element_by_id('stringa_inserita_su_homepage') #Firstly need to fill input tag of a web page with source name
element.send_keys(source)    # Tag ID of an input tag is "stringa_inserita_su_homepage "
time.sleep(10)    # Need a delay maybe connection is not good

found_source = driver.find_element_by_id('page').click() # If source name is found click on a main page to see more about source
time.sleep(5) # Wait 5 seconds

try:
    time.sleep(20) # Again wait 20 second the whole page should be loaded
    titles = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[8]/table/tbody/tr/td[1]/div[1]/div[2]/a/span') #Find a span tag which contains other catalogs names
    html = titles.get_attribute('innerHTML') # Get inner text of tha span tag
    names = html.split("<br>") # Make a list using split function. <br> tag was used for new line in HTML
    del names[-1] # Last <br> tag replaced by "," and this should be deleted from the list
    print(names)
finally:
    driver.quit() # Anyway close the browser
"""

# Used Google Chrome WEB browser

names =['PKSB2230+114', 'BZQJ2232+1143', 'PKS2230+114', 'WMAP47', '5BZQJ2232+1143', 'GB6B2230+1128', 'PLCKERC143G077.43-38.58', 'WMAP5J1254+1142', 'GB6J2232+1143', 'PLCKERC070G077.43-38.58', '1RXSJ223236.8+114331', '2FGLJ2232.4+1143', '1Jy2230+114', 'PCCS1030G077.44-38.58', '2E2230.1+1128', 'PLCKERC217G077.44-38.57', 'PCCS1044G077.44-38.59', '1FGL_J2232.5+1144', 'CTA102', 'PLCKERC353G077.43-38.58', 'PLCKERC044G077.43-38.58']

#for i in names:
#    matched_elements = browser.get("https://www.google.com/search?q=" + i)


browser = webdriver.Chrome()
browser.get('http://www.google.com')

search = browser.find_element_by_name('q')
search.send_keys("PKSB2230+114")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the results
#browser.quit()

"""links = browser.find_elements_by_class_name("//ol[@class='web_regular_results']//h3//a")
results = []


for link in links:
    href = link.get_attribute("href")
    print(href)
    results.append(href)
    browser.close()
"""