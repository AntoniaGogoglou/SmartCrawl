#!/usr/bin/python
# same code as extract_fromHTML.py kust formatted into functions
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
with open("urlsForMASFrompubTitlesMainProceedingsPart6.txt","rb+") as f:
    reader=csv.reader(f)
    for r in reader:
        urlsToCrawl.append(r)
f.close()
for u in urlsToCrawl:
    # chrome options for going headless
    # requires Chrome 59 and one of the latest versions of chromedriver as provided in the git repository of this project
    # sudo pip install bs4 
    # sudo pip install selenium
    # https://chromedriver.storage.googleapis.com/index.html
    # at least chromdriver 2.29
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # supply path to the directory where you have chromedriver .exe latest version, that allows you to go headless
    driver = webdriver.Chrome('/home/anto/pyth_mysql_code/SOFSEM/chromedriver',chrome_options=chrome_options)
    # provide your initial url pointing to a particular publication
    #url1= "https://academic.microsoft.com/#/search?iq=%40Well-Founded%20Metamodeling%20for%20Model-Driven%20Architecture%40&q=Well-Founded%20Metamodeling%20for%20Model-Driven%20Architecture&filters=&from=0&sort=0"
    url1=str(u[0])
    print "url1 is:"+url1
    soup1=FunctionsForCrawlingMAS.urlToSoup(url1,driver)
    (TitleToStore, PubYearToStore)=FunctionsForCrawlingMAS.FindTitleAndYearFromSoup( soup1 )
    ###print soup1
    (CitationCountAsString, CitationCountToStore)=FunctionsForCrawlingMAS.FindCitCountFromSoup(soup1)
    # if the paper is ever cited
    time.sleep(5)
    if CitationCountToStore is not 0:
        # the code from here on is to get the link to the citations and extract the year of each one
        urlOfCitations=FunctionsForCrawlingMAS.BuildUrlForCitingPubs( CitationCountAsString )
        
        soup2=FunctionsForCrawlingMAS.urlToSoup( urlOfCitations, driver )
        # check if results more than 1 page (aka more than 8 citing papers)
        SearchResults = soup2.findAll("section", {"class":"pure-u-1-2 mobile-visible"})
        for div in SearchResults:
            #print(div.text)
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
    print "CitationCountToStore is:"+str(CitationCountToStore)
    # listOfCitationYears is a List of Lists
    print listOfCitationYears
    flatListOfCitationYears=[item for sublist in listOfCitationYears for item in sublist]
    CitingPapersCount=len(flatListOfCitationYears)
    print "CitingPapersCount is:"+str(CitingPapersCount)
    # if this is the first publication you are retrieving, initialize the .txt file where you write the results
    # if you call this script recursively to append results for new publications
    filename="SOFSEMTitlesWithCitationCountsAndYearsOfCitsPart6.txt"
    if url1 is urlsToCrawl[0]:
        FunctionsForCrawlingMAS.WriteCitsAndYears(CitationCountToStore, CitingPapersCount, flatListOfCitationYears, filename, TitleToStore, PubYearToStore)
    else:
        FunctionsForCrawlingMAS.AppendCitsAndYears(CitationCountToStore, CitingPapersCount, flatListOfCitationYears, filename, TitleToStore, PubYearToStore)
    
end = time.time()
print "it took that much time"
print end-start

start = time.time()
urlsToCrawl=[]
with open("urlsForMASFrompubTitlesMainProceedingsPart7.txt","rb+") as f:
    reader=csv.reader(f)
    for r in reader:
        urlsToCrawl.append(r)
f.close()
for u in urlsToCrawl:
    # chrome options for going headless
    # requires Chrome 59 and one of the latest versions of chromedriver as provided in the git repository of this project
    # sudo pip install bs4 
    # sudo pip install selenium
    # https://chromedriver.storage.googleapis.com/index.html
    # at least chromdriver 2.29
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # supply path to the directory where you have chromedriver .exe latest version, that allows you to go headless
    driver = webdriver.Chrome('/home/anto/pyth_mysql_code/SOFSEM/chromedriver',chrome_options=chrome_options)
    # provide your initial url pointing to a particular publication
    #url1= "https://academic.microsoft.com/#/search?iq=%40Well-Founded%20Metamodeling%20for%20Model-Driven%20Architecture%40&q=Well-Founded%20Metamodeling%20for%20Model-Driven%20Architecture&filters=&from=0&sort=0"
    url1=str(u[0])
    print "url1 is:"+url1
    soup1=FunctionsForCrawlingMAS.urlToSoup(url1,driver)
    (TitleToStore, PubYearToStore)=FunctionsForCrawlingMAS.FindTitleAndYearFromSoup( soup1 )
    ###print soup1
    (CitationCountAsString, CitationCountToStore)=FunctionsForCrawlingMAS.FindCitCountFromSoup(soup1)
    # if the paper is ever cited
    time.sleep(5)
    if CitationCountToStore is not 0:
        # the code from here on is to get the link to the citations and extract the year of each one
        urlOfCitations=FunctionsForCrawlingMAS.BuildUrlForCitingPubs( CitationCountAsString )
        
        soup2=FunctionsForCrawlingMAS.urlToSoup( urlOfCitations, driver )
        # check if results more than 1 page (aka more than 8 citing papers)
        SearchResults = soup2.findAll("section", {"class":"pure-u-1-2 mobile-visible"})
        for div in SearchResults:
            #print(div.text)
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
    print "CitationCountToStore is:"+str(CitationCountToStore)
    # listOfCitationYears is a List of Lists
    print listOfCitationYears
    flatListOfCitationYears=[item for sublist in listOfCitationYears for item in sublist]
    CitingPapersCount=len(flatListOfCitationYears)
    print "CitingPapersCount is:"+str(CitingPapersCount)
    # if this is the first publication you are retrieving, initialize the .txt file where you write the results
    # if you call this script recursively to append results for new publications
    filename="SOFSEMTitlesWithCitationCountsAndYearsOfCitsPart7.txt"
    if url1 is urlsToCrawl[0]:
        FunctionsForCrawlingMAS.WriteCitsAndYears(CitationCountToStore, CitingPapersCount, flatListOfCitationYears, filename, TitleToStore, PubYearToStore)
    else:
        FunctionsForCrawlingMAS.AppendCitsAndYears(CitationCountToStore, CitingPapersCount, flatListOfCitationYears, filename, TitleToStore, PubYearToStore)
    
end = time.time()
print "it took that much time"
print end-start


start = time.time()
urlsToCrawl=[]
with open("urlsForMASFrompubTitlesMainProceedingsPart8.txt","rb+") as f:
    reader=csv.reader(f)
    for r in reader:
        urlsToCrawl.append(r)
f.close()
for u in urlsToCrawl:
    # chrome options for going headless
    # requires Chrome 59 and one of the latest versions of chromedriver as provided in the git repository of this project
    # sudo pip install bs4 
    # sudo pip install selenium
    # https://chromedriver.storage.googleapis.com/index.html
    # at least chromdriver 2.29
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # supply path to the directory where you have chromedriver .exe latest version, that allows you to go headless
    driver = webdriver.Chrome('/home/anto/pyth_mysql_code/SOFSEM/chromedriver',chrome_options=chrome_options)
    # provide your initial url pointing to a particular publication
    #url1= "https://academic.microsoft.com/#/search?iq=%40Well-Founded%20Metamodeling%20for%20Model-Driven%20Architecture%40&q=Well-Founded%20Metamodeling%20for%20Model-Driven%20Architecture&filters=&from=0&sort=0"
    url1=str(u[0])
    print "url1 is:"+url1
    soup1=FunctionsForCrawlingMAS.urlToSoup(url1,driver)
    (TitleToStore, PubYearToStore)=FunctionsForCrawlingMAS.FindTitleAndYearFromSoup( soup1 )
    ###print soup1
    (CitationCountAsString, CitationCountToStore)=FunctionsForCrawlingMAS.FindCitCountFromSoup(soup1)
    # if the paper is ever cited
    time.sleep(5)
    if CitationCountToStore is not 0:
        # the code from here on is to get the link to the citations and extract the year of each one
        urlOfCitations=FunctionsForCrawlingMAS.BuildUrlForCitingPubs( CitationCountAsString )
        
        soup2=FunctionsForCrawlingMAS.urlToSoup( urlOfCitations, driver )
        # check if results more than 1 page (aka more than 8 citing papers)
        SearchResults = soup2.findAll("section", {"class":"pure-u-1-2 mobile-visible"})
        for div in SearchResults:
            #print(div.text)
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
    print "CitationCountToStore is:"+str(CitationCountToStore)
    # listOfCitationYears is a List of Lists
    print listOfCitationYears
    flatListOfCitationYears=[item for sublist in listOfCitationYears for item in sublist]
    CitingPapersCount=len(flatListOfCitationYears)
    print "CitingPapersCount is:"+str(CitingPapersCount)
    # if this is the first publication you are retrieving, initialize the .txt file where you write the results
    # if you call this script recursively to append results for new publications
    filename="SOFSEMTitlesWithCitationCountsAndYearsOfCitsPart8.txt"
    if url1 is urlsToCrawl[0]:
        FunctionsForCrawlingMAS.WriteCitsAndYears(CitationCountToStore, CitingPapersCount, flatListOfCitationYears, filename, TitleToStore, PubYearToStore)
    else:
        FunctionsForCrawlingMAS.AppendCitsAndYears(CitationCountToStore, CitingPapersCount, flatListOfCitationYears, filename, TitleToStore, PubYearToStore)
    
end = time.time()
print "it took that much time"
print end-start

start = time.time()
urlsToCrawl=[]
with open("urlsForMASFrompubTitlesMainProceedingsPart9.txt","rb+") as f:
    reader=csv.reader(f)
    for r in reader:
        urlsToCrawl.append(r)
f.close()
for u in urlsToCrawl:
    # chrome options for going headless
    # requires Chrome 59 and one of the latest versions of chromedriver as provided in the git repository of this project
    # sudo pip install bs4 
    # sudo pip install selenium
    # https://chromedriver.storage.googleapis.com/index.html
    # at least chromdriver 2.29
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # supply path to the directory where you have chromedriver .exe latest version, that allows you to go headless
    driver = webdriver.Chrome('/home/anto/pyth_mysql_code/SOFSEM/chromedriver',chrome_options=chrome_options)
    # provide your initial url pointing to a particular publication
    #url1= "https://academic.microsoft.com/#/search?iq=%40Well-Founded%20Metamodeling%20for%20Model-Driven%20Architecture%40&q=Well-Founded%20Metamodeling%20for%20Model-Driven%20Architecture&filters=&from=0&sort=0"
    url1=str(u[0])
    print "url1 is:"+url1
    soup1=FunctionsForCrawlingMAS.urlToSoup(url1,driver)
    (TitleToStore, PubYearToStore)=FunctionsForCrawlingMAS.FindTitleAndYearFromSoup( soup1 )
    ###print soup1
    (CitationCountAsString, CitationCountToStore)=FunctionsForCrawlingMAS.FindCitCountFromSoup(soup1)
    # if the paper is ever cited
    time.sleep(5)
    if CitationCountToStore is not 0:
        # the code from here on is to get the link to the citations and extract the year of each one
        urlOfCitations=FunctionsForCrawlingMAS.BuildUrlForCitingPubs( CitationCountAsString )
        
        soup2=FunctionsForCrawlingMAS.urlToSoup( urlOfCitations, driver )
        # check if results more than 1 page (aka more than 8 citing papers)
        SearchResults = soup2.findAll("section", {"class":"pure-u-1-2 mobile-visible"})
        for div in SearchResults:
            #print(div.text)
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
    print "CitationCountToStore is:"+str(CitationCountToStore)
    # listOfCitationYears is a List of Lists
    print listOfCitationYears
    flatListOfCitationYears=[item for sublist in listOfCitationYears for item in sublist]
    CitingPapersCount=len(flatListOfCitationYears)
    print "CitingPapersCount is:"+str(CitingPapersCount)
    # if this is the first publication you are retrieving, initialize the .txt file where you write the results
    # if you call this script recursively to append results for new publications
    filename="SOFSEMTitlesWithCitationCountsAndYearsOfCitsPart9.txt"
    if url1 is urlsToCrawl[0]:
        FunctionsForCrawlingMAS.WriteCitsAndYears(CitationCountToStore, CitingPapersCount, flatListOfCitationYears, filename, TitleToStore, PubYearToStore)
    else:
        FunctionsForCrawlingMAS.AppendCitsAndYears(CitationCountToStore, CitingPapersCount, flatListOfCitationYears, filename, TitleToStore, PubYearToStore)
    
end = time.time()
print "it took that much time"
print end-start

start = time.time()
urlsToCrawl=[]
with open("urlsForMASFrompubTitlesMainProceedingsPart10.txt","rb+") as f:
    reader=csv.reader(f)
    for r in reader:
        urlsToCrawl.append(r)
f.close()
for u in urlsToCrawl:
    # chrome options for going headless
    # requires Chrome 59 and one of the latest versions of chromedriver as provided in the git repository of this project
    # sudo pip install bs4 
    # sudo pip install selenium
    # https://chromedriver.storage.googleapis.com/index.html
    # at least chromdriver 2.29
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # supply path to the directory where you have chromedriver .exe latest version, that allows you to go headless
    driver = webdriver.Chrome('/home/anto/pyth_mysql_code/SOFSEM/chromedriver',chrome_options=chrome_options)
    # provide your initial url pointing to a particular publication
    #url1= "https://academic.microsoft.com/#/search?iq=%40Well-Founded%20Metamodeling%20for%20Model-Driven%20Architecture%40&q=Well-Founded%20Metamodeling%20for%20Model-Driven%20Architecture&filters=&from=0&sort=0"
    url1=str(u[0])
    print "url1 is:"+url1
    soup1=FunctionsForCrawlingMAS.urlToSoup(url1,driver)
    (TitleToStore, PubYearToStore)=FunctionsForCrawlingMAS.FindTitleAndYearFromSoup( soup1 )
    ###print soup1
    (CitationCountAsString, CitationCountToStore)=FunctionsForCrawlingMAS.FindCitCountFromSoup(soup1)
    # if the paper is ever cited
    time.sleep(5)
    if CitationCountToStore is not 0:
        # the code from here on is to get the link to the citations and extract the year of each one
        urlOfCitations=FunctionsForCrawlingMAS.BuildUrlForCitingPubs( CitationCountAsString )
        
        soup2=FunctionsForCrawlingMAS.urlToSoup( urlOfCitations, driver )
        # check if results more than 1 page (aka more than 8 citing papers)
        SearchResults = soup2.findAll("section", {"class":"pure-u-1-2 mobile-visible"})
        for div in SearchResults:
            #print(div.text)
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
    print "CitationCountToStore is:"+str(CitationCountToStore)
    # listOfCitationYears is a List of Lists
    print listOfCitationYears
    flatListOfCitationYears=[item for sublist in listOfCitationYears for item in sublist]
    CitingPapersCount=len(flatListOfCitationYears)
    print "CitingPapersCount is:"+str(CitingPapersCount)
    # if this is the first publication you are retrieving, initialize the .txt file where you write the results
    # if you call this script recursively to append results for new publications
    filename="SOFSEMTitlesWithCitationCountsAndYearsOfCitsPart10.txt"
    if url1 is urlsToCrawl[0]:
        FunctionsForCrawlingMAS.WriteCitsAndYears(CitationCountToStore, CitingPapersCount, flatListOfCitationYears, filename, TitleToStore, PubYearToStore)
    else:
        FunctionsForCrawlingMAS.AppendCitsAndYears(CitationCountToStore, CitingPapersCount, flatListOfCitationYears, filename, TitleToStore, PubYearToStore)
    
end = time.time()
print "it took that much time"
print end-start
