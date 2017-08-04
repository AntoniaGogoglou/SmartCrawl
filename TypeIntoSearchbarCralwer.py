#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv
import time

filenameTitles="Titles.txt"
filenameURLs="URLsFile.txt"
urlsToCrawl=[]
with open(filenameTitles,"rb+") as f:
    reader=csv.reader(f)
    for r in reader:
        # this is to make a conference specific search
        # a publication with the same title may exist in multiple venues so this way we select a particular venue
        urlsToCrawl.append([r[0]+' '+'SOFSEM'])
f.close()

for u in urlsToCrawl:
    # path to the location of chromedriver 
    browser = webdriver.Chrome('/home/ust/chromedriver')
    # load webpage
    browser.get('https://academic.microsoft.com/#/search')
    # find search bar
    elem = browser.find_element_by_class_name("searchControl")
    # type into search bar and send
    elem.send_keys(u)
    elem.send_keys(Keys.ENTER)
    elem.send_keys(Keys.RETURN)
    curURL=browser.current_url
    print curURL
    if u is urlsToCrawl[0]:
        # initiate file to write URLs
        with open(filenameURLs,"w+") as f:
            f.write("%s" % curURL)
            f.write("\n")
        f.close()
    else:        
        # if the file already exists, append
        with open(filenameURLs,"a") as f:
            f.write("%s" % curURL)
            f.write("\n")
        f.close()
    time.sleep(5)
    browser.quit()

time.sleep(60)


