# SmartCrawl
This is a series of easy to use scripts that utilize Python's BeautifulSoup and Selenium to crawl dynamically defined Javascript webpages (e.g. Microsoft Academic Search) and follow multiple links parsing and extracting only the useful information.


There are two different scripts, one that loads information from file and types it into the search bar of a webpage to extract the resulting URL and a second one to utilize this URL and extract relevant pieces from the HTML source code.

* extract_fromHtmlMAS.py : This script reads a URL corresponding to a particular publication from Microsoft Academic Search (https://academic.microsoft.com) and extracts the year and title of the publication, the number of citations and then redirects to the pages of citing papers to retrieve information regarding each paper that cites the publication at hand (e.g. the year each citation occurs). The results may expand to more than one pages and contrary to existing web crawler this one retrieves all the results dynamically. The resulting information is stored in a file (filename)
