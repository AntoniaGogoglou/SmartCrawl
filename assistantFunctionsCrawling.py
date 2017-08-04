#!/usr/bin/python

from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import math

class FunctionsForCrawlingMAS:
    @staticmethod
    # retrieve soup (aka HTML source) from URL
    def urlToSoup( url, driver):
        driver.get(url)
        time.sleep(5)
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content,"html.parser")
        return soup;
        
    @staticmethod
    # retrieve a particular field (class) from HTML content, e.g. citation count
    def FindCitCountFromSoup( soup ):
        CitationCount = soup.findAll("a", {"class": "c-count"})
        # check if list CitationCount is empty, aka if the paper has any citations
        if not CitationCount:
            CitationCountToStore=0
            CitationCountAsString=str(0)
        else:
            for div in CitationCount:
                #print(div.text)
                CitationCountToStore=str(div.text.split("(")[1].split(")")[0])
            CitationCountAsString=str(CitationCount)
        #print CitationCountAsString
        return CitationCountAsString, CitationCountToStore;
    
    @staticmethod
    # retrieve a particular field (class) from HTML content, e.g. title and year
    def FindTitleAndYearFromSoup( soup ):    
        Title = soup.findAll("a", {"class": "blue-title"})
        TitleToStore=""
        PubYearToStore=""
        for div in Title:
            print div
            #tmp=div.text
            #tmp = tmp.encode('utf-8', 'ignore').decode('utf-8')
            #print "tmp is:" + tmp
            #TitleToStore=str(div.text.encode('utf-8', 'ignore').decode('utf-8'))
            TitleToStore=str(div.text.encode('ascii', 'ignore').decode('utf-8'))
            print "TitleToStore is:"+TitleToStore
            # how to check for a particular publishing venue (e.g. the SOFSEM conference)
            if "SOFSEM" not in TitleToStore:
                break;
            
        PubYear = soup.findAll("section", {"class": "paper-year"})
        for div in PubYear:
            PubYearToStore=str(div.text)
        return TitleToStore, PubYearToStore;
    @staticmethod    
    # retrieve URLs for citing publications
    def BuildUrlForCitingPubs( CitationCountAsString ):
        hrefString=CitationCountAsString.split('href="#')
        hrefStringFinal=hrefString[1].split(';filters')[0]
        #now I have my second url, new content, new soup
        urlOfCitations="https://academic.microsoft.com/#"+hrefStringFinal
        return urlOfCitations;
    
    @staticmethod    
    # retrieve soup for the citing publication URLs
    def FindYearOfCitingPubsFromSoup( soup ):
        CitationYears = soup.findAll("section", {"class": "paper-year"})
        listOfCitationYears=[]
        for citpap in CitationYears:
            for div in citpap:
                listOfCitationYears.append(str(div.text))
        return listOfCitationYears;
        
    @staticmethod
    # ensures that all pages of the results are crawled (Microsoft Academic Search displays 8 results per page)
    def F(NumOfSearchResults,urlOfCitations):
        NumOfPages=int(math.ceil(NumOfSearchResults/8.0))
        #print NumOfPages
        #print urlOfCitations
        urlOfCitationsList=[]
        for i in range(1,NumOfPages+1):
            strtPoint=(i-1)*8
            urlOfCitationsBase=urlOfCitations[:-4]
            urlOfCitationsTmp=urlOfCitationsBase+"&filters=&from="+str(strtPoint)+"&sort=0"
            urlOfCitationsList.append(urlOfCitationsTmp)
        return urlOfCitationsList;
    
    @staticmethod    
    # initialize file and write retrieved values
    def WriteCitsAndYears(CitationCountToStore, CitingPapersCount, listOfCitationYears, filenameString, TitleToStore, PubYearToStore):
        with open(filenameString,"w+") as f:
            f.write("%s," % CitationCountToStore)
            f.write("%s," % CitingPapersCount)
            f.write("%s," % PubYearToStore)
            f.write("%s" % TitleToStore)
            f.write("\n")
            if not listOfCitationYears:
                f.write("%s" % 0)
            else:
                for eachyear in listOfCitationYears[:-1]:
                    f.write("%s," % eachyear)
                else:
                    f.write("%s" %listOfCitationYears[-1])    
            f.write("\n")
        f.close()
        print "Citations and Years written in SOFSEMTitlesWithCitationCountsAndYearsOfCits.txt"
        return;
    
    @staticmethod
    # if folder already created, append newly retrieved information on new URLs
    def AppendCitsAndYears(CitationCountToStore, CitingPapersCount, listOfCitationYears, filenameString, TitleToStore, PubYearToStore):
        with open(filenameString,"a") as f:
            f.write("%s," % CitationCountToStore)
            f.write("%s," % CitingPapersCount)
            f.write("%s," % PubYearToStore)
            f.write("%s" % TitleToStore)
            f.write("\n")
            if not listOfCitationYears:
                f.write("%s" % 0)
            else:
                for eachyear in listOfCitationYears[:-1]:
                    f.write("%s," % eachyear)
                else:
                    f.write("%s" %listOfCitationYears[-1])    
            f.write("\n")
        f.close()
        return;


