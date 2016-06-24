import requests
from bs4 import BeautifulSoup
from time import sleep
import sys


def crawl(url):
    while True:
        try:
            r = requests.get(url)
            return r
        except Exception as e:
            print e
            sleep(2)
            print "retrying to fetch URL!!!"

# there are total 153 pages for the data from 1989 to 2013
for page in range(1, 153):
    url = "http://stats.espncricinfo.com/ci/engine/stats/"\
        "index.html?class=2;orderby=start;page={};"\
        "spanmax1=31+Dec+2013;spanmin1=1+jan+1989;spanval1=span;"\
        "team=6;template=results;type=batting;view=match".format(page)
    # Scrape the HTML at the url
    r = crawl(url)

    # Turn the HTML into a Beautiful Soup object
    soup = BeautifulSoup(r.text)
    table = soup.find('table', attrs={'class':'engineTable'})
    tbody = soup.find('tbody')
    rows = tbody.findAll('tr', attrs={'class':'data1'})
   
    for tr in rows:
			cols = tr.findAll('td')      
			for td in cols:
				print td.text
	# 		fh = open('table.txt','a')
	# 		fh.write(str(cols))
 #            # print str(td.text.encode('utf-8')) + "  "  
 #    #         raw_input()      
           
 #    #         # print rows

	# 