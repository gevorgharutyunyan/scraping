from bs4 import BeautifulSoup
import requests
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


source = "4C +01.02"  # Source name for which other catalog names should be found
driver = webdriver.Chrome() # Used Google Chrome WEB browser
driver.get("https://openuniverse.asi.it/open_universe.html") # This page is used for scraping
driver.maximize_window()
element = driver.find_element_by_id('stringa_inserita_su_homepage') #Firstly need to fill input tag of a web page with source name
element.send_keys(source)    # Tag ID of an input tag is "stringa_inserita_su_homepage "
time.sleep(2)    # Need a delay maybe connection is not good

#found_source = driver.find_element_by_id('page').click() # If source name is found click on a main page to see more about source
found_source=element.send_keys(Keys.RETURN)
time.sleep(1) # Wait 5 seconds

try:
    time.sleep(2) # Again wait 20 second the whole page should be loaded
    titles = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[8]/table/tbody/tr/td[1]/div[1]/div[2]/a/span') #Find a span tag which contains other catalogs names
    html = titles.get_attribute('innerHTML') # Get inner text of tha span tag
    names = html.split("<br>") # Make a list using split function. <br> tag was used for new line in HTML
    del names[-1] # Last <br> tag replaced by "," and this should be deleted from the list
    print(names)
    driver.delete_all_cookies()
finally:
    driver.quit() # Anyway close the browser
#names =[ 'BZQJ2232+1143', 'PKS2230+114', 'WMAP47']

browser = webdriver.Chrome()
browser.get('http://www.google.com') # Search using all names in google.com
browser.maximize_window() #maximize chrome window after opening
clear_links=[] # gather all links in this list connected with source name
if names:
    for name in names:
       search = browser.find_element_by_name('q') # find search box
       search.send_keys(name) # fill search box with a source name
       search.send_keys(Keys.RETURN) # hit return after you entering source name
       time.sleep(2) # sleep for 5 seconds so you can see the results
       search_result = browser.find_elements_by_class_name("yuRUbf") #Each result has a class with name yuRUbf
       links = []
       for i in search_result:
           child = i.find_elements_by_tag_name("a") # separate <a> tags which contains searching result links
           for j in child:
               links.append(j.get_attribute('href')) #from <a> tag get only href
       browser.find_element_by_name('q').clear() # after filling search box and finding results clear searched name
       time.sleep(2)
       valid_links=[k for k in links if  "https://translate.google.com/" not in k] # links list contain other links which need to be removed
       if valid_links:
           for link in valid_links:
               clear_links.append(link)
browser.quit() # after getting all results close the browser
if clear_links:
    open_links = webdriver.Chrome() # then need to open browser again to open gathered links
    open_links.maximize_window()
    for info_link in range(len(clear_links)):
        open_links.get(clear_links[info_link])
        if (info_link != len(clear_links) - 1):
            open_links.execute_script("window.open('');") # open a new tab for each new link from clear_links
            chwd = open_links.window_handles
            open_links.switch_to.window(chwd[-1])
        time.sleep(2)


