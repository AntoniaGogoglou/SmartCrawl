#!/usr/bin/python
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from assistantFunctionsCrawling import FunctionsForCrawlingMAS
import math
import csv
import time

start = time.time()
urlsToCrawl=[]
with open("URLsFile.txt","rb+") as f:
    reader=csv.reader(f)
    for r in reader:
        urlsToCrawl.append(r)
f.close()
for u in urlsToCrawl:
    # chrome options for going headless
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # supply path to the directory where you have chromedriver .exe latest version, that allows you to go headless
    driver = webdriver.Chrome('/home/ust/chromedriver',chrome_options=chrome_options)
    # provide your initial url pointing to a particular page (aka a sepcific search)
   
    url1=str(u[0])
    print "url1 is:"+url1
    soup1=FunctionsForCrawlingMAS.urlToSoup(url1,driver)
    (TitleToStore, PubYearToStore)=FunctionsForCrawlingMAS.FindTitleAndYearFromSoup( soup1 )
    ###print soup1
    (CitationCountAsString, CitationCountToStore)=FunctionsForCrawlingMAS.FindCitCountFromSoup(soup1)
    # sleep the process in case you intend to download lots of data so that you don't create a bottleneck at the servers you are querying
    time.sleep(5)
    if CitationCountToStore is not 0:
        # the code from here on is to get the link to the citations and extract the year of each one
        urlOfCitations=FunctionsForCrawlingMAS.BuildUrlForCitingPubs( CitationCountAsString )
        soup2=FunctionsForCrawlingMAS.urlToSoup( urlOfCitations, driver )
        # check if results more than 1 page (aka more than 8 citing papers)
        SearchResults = soup2.findAll("section", {"class":"pure-u-1-2 mobile-visible"})
        for div in SearchResults:
            if "results" in div.text:
                NumOfSearchResults=int(div.text.split("of ")[1].split(" results")[0])
        listOfCitationYears=[]
        if NumOfSearchResults<8:
            listOfCitationYearsTmp=FunctionsForCrawlingMAS.FindYearOfCitingPubsFromSoup( soup2 )
            listOfCitationYears.append(listOfCitationYearsTmp)
        else:
            listOfCitationYears=[]
            urlOfCitationsList=FunctionsForCrawlingMAS.F(NumOfSearchResults,urlOfCitations)
            for ur in urlOfCitationsList:
                soupTmp=FunctionsForCrawlingMAS.urlToSoup( ur, driver )
                listOfCitationYearsTmp=FunctionsForCrawlingMAS.FindYearOfCitingPubsFromSoup( soupTmp )
                listOfCitationYears.append(listOfCitationYearsTmp)      
    else:
        listOfCitationYears=[]
    driver.quit()
    # start storing values
    print listOfCitationYears
    flatListOfCitationYears=[item for sublist in listOfCitationYears for item in sublist]
    CitingPapersCount=len(flatListOfCitationYears)
    print "CitingPapersCount is:"+str(CitingPapersCount)
    # if this is the first publication you are retrieving, initialize the .txt file where you write the results
    # if you call this script recursively to append results for new publications
    filename="resultsFile.txt"
    if url1 is urlsToCrawl[0]:
        FunctionsForCrawlingMAS.WriteCitsAndYears(CitationCountToStore, CitingPapersCount, flatListOfCitationYears, filename, TitleToStore, PubYearToStore)
    else:
        FunctionsForCrawlingMAS.AppendCitsAndYears(CitationCountToStore, CitingPapersCount, flatListOfCitationYears, filename, TitleToStore, PubYearToStore)
    
end = time.time()
print "it took that much time"
print end-start
