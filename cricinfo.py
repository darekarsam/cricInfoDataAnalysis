import requests
from bs4 import BeautifulSoup
from time import sleep
import sys
import pandas as pd


def crawl(url):
    while True:
        try:
            r = requests.get(url)
            return r
        except Exception as e:
            print e
            sleep(2)
            print "retrying to fetch URL!!!"


def main():
    # there are total 153 pages for the data from 1989 to 2013
    name = []
    batsmanStatus = []
    runs = []
    balls = []
    strikeRate = []
    opponent = []
    venue = []
    date = []
    count = 0
    for page in range(1, 154):
        count += 1
        sys.stdout.write("\r" + "Crawling Page: %d of 153" % count)
        sys.stdout.flush()
        url = "http://stats.espncricinfo.com/ci/engine/stats/"\
            "index.html?class=2;orderby=start;page={};"\
            "spanmax1=31+Dec+2013;spanmin1=1+jan+1989;spanval1=span;"\
            "team=6;template=results;type=batting;view=match".format(page)
        # Scrape the HTML at the url
        r = crawl(url)

        # Turn the HTML into a Beautiful Soup object
        soup = BeautifulSoup(r.text, "lxml")
        table = soup.find('table', attrs={'class': 'engineTable'})
        tbody = soup.find('tbody')
        rows = tbody.findAll('tr', attrs={'class': 'data1'})

        for tr in rows:
            cols = tr.findAll('td')
            record = [td.text for td in cols]
            name.append(str(record[0]))
            # if score contains '*' batsman is not out
            batsmanStatus.append(('out', 'not out')['*' in str(record[1])])
            runs.append(None if str(record[2]) == '-' else int(record[2]))
            # runs.append((int(record[2]),None)[])
            balls.append(None if str(record[3]) == '-' else int(record[3]))
            strikeRate.append(None if str(
                record[4]) == '-' else float(record[4]))
            opponent.append(str(record[6])[2:])
            venue.append(str(record[7]))
            date.append(str(record[8]))
            battingStat = pd.DataFrame({
                'player': name,
                'outStatus': batsmanStatus,
                'runs': runs,
                'ballsFaced': balls,
                'strikeRate': strikeRate,
                'opponent': opponent,
                'venue': venue,
                'date': date
            })

    print "\n"
    print battingStat.head()

if __name__ == "__main__":
    main()
