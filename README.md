# SmartCrawl
This is a series of easy to use scripts that utilize Python's BeautifulSoup and Selenium to crawl dynamically defined Javascript webpages (e.g. Microsoft Academic Search) and follow multiple links parsing and extracting only the useful information.


There are two different scripts, one that loads information from file and types it into the search bar of a webpage to extract the resulting URL and a second one to utilize this URL and extract relevant pieces from the HTML source code.

* extract_fromHtmlMAS.py : This script extracts HTML content (tags, etc.) from dynamically defined online sources. In our use case, it reads a URL corresponding to a particular publication from Microsoft Academic Search (https://academic.microsoft.com) and extracts the year and title of the publication, the number of citations and then redirects to the pages of citing publications to retrieve information regarding each paper that cites the publication at hand (e.g. the year each citation occurs). The results may expand to more than one pages and, contrary to existing web crawlers, this one retrieves all the results dynamically. The resulting information is stored in a file (resultsFile).

* TypeIntoSearchbarCralwer.py : This script simulates typing information into online search bars. In our use case, it reads titles of publications from a file and types them into Microsoft Academic Search search bar to retrieve the respective URL. The respective URL is then stored and then loaded from extract_fromHtmlMAS.py.

* assistantFunctionsCrawling.py : This class contains helpful functions that utilize HTML content retrieval, URL manipulation, etc.


The use case of retrieving publication data is only one of the possible uses for the above combination of scripts and functions. Basically, any dynamically defined online content can be crawled using a combination of Selenium and BeautifulSoup. 

Crawl away!
