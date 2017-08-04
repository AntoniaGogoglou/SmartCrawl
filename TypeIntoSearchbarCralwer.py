#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv
import time

filenameTitles="URLsToBuild801_900.txt"
filenameURLs="urlsForMASFrompubTitlesMainProceedingsPart9.txt"
urlsToCrawl=[]
with open(filenameTitles,"rb+") as f:
    reader=csv.reader(f)
    for r in reader:
        urlsToCrawl.append([r[0]+' '+'SOFSEM'])
f.close()

for u in urlsToCrawl:
    browser = webdriver.Chrome('/home/anto/pyth_mysql_code/SOFSEM/chromedriver')
    browser.get('https://academic.microsoft.com/#/search')
    elem = browser.find_element_by_class_name("searchControl")
    #elem = browser.find_element_by_name('p')  # Find the search box
    elem.send_keys(u)
    elem.send_keys(Keys.ENTER)
    elem.send_keys(Keys.RETURN)
    curURL=browser.current_url
    print curURL
    if u is urlsToCrawl[0]:
        with open(filenameURLs,"w+") as f:
            f.write("%s" % curURL)
            f.write("\n")
        f.close()
    else:        
        with open(filenameURLs,"a") as f:
            f.write("%s" % curURL)
            f.write("\n")
        f.close()
    time.sleep(5)
    browser.quit()

time.sleep(60)

filenameTitles="URLsToBuild901_1015.txt"
filenameURLs="urlsForMASFrompubTitlesMainProceedingsPart10.txt"
urlsToCrawl=[]
with open(filenameTitles,"rb+") as f:
    reader=csv.reader(f)
    for r in reader:
        urlsToCrawl.append([r[0]+' '+'SOFSEM'])
f.close()

for u in urlsToCrawl:
    browser = webdriver.Chrome('/home/anto/pyth_mysql_code/SOFSEM/chromedriver')
    browser.get('https://academic.microsoft.com/#/search')
    elem = browser.find_element_by_class_name("searchControl")
    #elem = browser.find_element_by_name('p')  # Find the search box
    elem.send_keys(u)
    elem.send_keys(Keys.ENTER)
    elem.send_keys(Keys.RETURN)
    curURL=browser.current_url
    print curURL
    if u is urlsToCrawl[0]:
        with open(filenameURLs,"w+") as f:
            f.write("%s" % curURL)
            f.write("\n")
        f.close()
    else:        
        with open(filenameURLs,"a") as f:
            f.write("%s" % curURL)
            f.write("\n")
        f.close()
    time.sleep(5)
    browser.quit()
    
