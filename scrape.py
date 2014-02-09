#!/usr/bin/env python

import datetime
import json
import time

from bs4 import BeautifulSoup
from dateutil.parser import *
import requests

def scrape_restaurant_list():
    """
    Scrape the restaurant list HTML from the Lane County government site.
    It's ASPX, so we have to set headers and pass form data for the POST to work.
    """
    url = "http://apps.lanecounty.org/RIS/default.aspx"
    headers = {}

    headers['Accept'] = "*/*"
    headers['Accept-Encoding'] = "gzip,deflate,sdch"
    headers['Accept-Language'] = "en-US,en;q=0.8"
    headers['Cache-Control'] = "no-cache"
    headers['Connection'] = "keep-alive"
    headers['Content-Length'] = "1801"
    headers['Content-Type'] = "application/x-www-form-urlencoded; charset=UTF-8"
    headers['Cookie'] = "__utma=81114762.1679424036.1391963586.1391963586.1391963586.1; __utmc=81114762; __utmz=81114762.1391963586.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ASP.NET_SessionId=0nsclsuv4jhg1i3i0dt3vjui"
    headers['DNT'] = "1"
    headers['Host'] = "apps.lanecounty.org"
    headers['Origin'] = "http://apps.lanecounty.org"
    headers['Referer'] = "http://apps.lanecounty.org/RIS/"
    headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36"
    headers['X-MicrosoftAjax'] = "Delta=true"
    headers['X-Requested-With'] = "XMLHttpRequest"

    data = {}
    data['ctl00$ToolkitScriptManager1'] = "ctl00$ToolkitScriptManager1|ctl00$cphBody$btnSearch"
    data['ctl00_ToolkitScriptManager1_HiddenField'] = ""
    data['__EVENTTARGET'] = ""
    data['__EVENTARGUMENT'] = ""
    data['__VIEWSTATE'] = "8+exSzYLzSpkVIyOcXVWYVwga62fvqR3hgaHpNfl2stQI0gsW0VT4htMxje05p1y9WScXqoA+SOrSUg3aLqlflDaaJp2UwuyE+1zwdYJe9fZcEz7kEEfvP5/Uo6q6hifLK1i5+oMQYNiLzLybeF23rEJuRVXYGjs8tkbgHdXAqtbmQxaN+0bz2XoEWCwLfaVOOTBKdSb1DZAJQsCYPRFPqAK5OXU4GuudzDQXQxJXHttwgCXqPBpQUwFbiD3cFZNx+ZVaqqm2Mi3ET0N5WYGzlBQxYEUYqGXu82MdfD5tDvC8ZCmrKjSHtOxahjVQyVx6lPm7Nv9Y3ST00gf2aLz81miFCfdLc2ZU0wG91Yx2GXCFs5++/BDDYio6kkkijmZ+vbkPp663JmJNf13hi324eIwIW88AR8tnIMOQprj8tC4uycJxENVowKcJ2z5D8vODYz4fywFVNlMhdrAzzRlZSg0GY3+v7hqcr1vIWITBTchHyMZ6zUZovpp1TUbM0w+IQ9Y+lDEYPgUJ8s2IFgGdfNy3GneeWmEFHQ8o5auWYfmWSSWzFZn12URk9fGnV7D9OItsAdVg2tZi1ODSXycReQtsIhWQKbB2zEG11pds27IQUHdYFBVqLIi2E8aAQnFgkIlUrQpyKVG6lKC8X4lGUaKKB2UuJfk/tfIb2wLCYGL3Sq7dha5tGm19Q8AP951NRjjzbTSU28AET8fWBC714lAbvzgbItVNTdaEEhEWikwySdRmYBCSfgdHJPPQO3zzkRrkybEt8jlgcFs5aHANGj2s91F9d51EksmPfwLKa3BqxsBi5YXeiiCsQBcZ8G4MHanZ44KtjtKbku/YTCh35A/rG9L46zp1nO+2GzmXnjfC3AREryBpvbrZpq+xuIoOy1yMg0roqDf3gxofYKQff8RKpgk1xHb6mtTwdOYam/cUlEAQa2jchZ+fHf5XLwUNI5H8spcVYqiUclQ521r9QAWGywMaPMibNq9P5wvfPnAQXYk"
    data['__EVENTVALIDATION'] = "Mr+OWSYAZz6OpJCusGPB9XLNMcSy0/wMIRYsqfHsQcePZif2p+U3pRZ0KHWG2UsciSKV/g519qwMG0huj6MkuXycGYKa0lXIAqJuEmwg6qYj0gvJRCNaGwPyeXXMnPQZsVinZ5+7dFgk8j9vYekMuZsJLWqL4fg1R3mSaBZfQ3OUukuoVI9XByD1MLDDok4iFh4zijo7IjvV5udidPqKun2DoFk8UtzfGKo2xj1tOpN1Gc6eZrSqarBYJa6Vz7zBK6LldECTpiecKXxQjeKLCd5L1k2hwlVImpCErH8iYsxrvy/KNEWkZ5i1de58txZN8T+UDz80vh4B2AD5mziFDt3WOWnH/8tk5OYiP+BGbPc+Nmhq"
    data['ctl00$cphBody$txtbRestaurantName'] = ""
    data['ctl00$cphBody$ddlstCity'] = "%"
    data['ctl00$cphBody$ddlstScoreRange'] = "All Scores"
    data['__ASYNCPOST'] = "true"
    data['ctl00$cphBody$btnSearch'] = "Search"

    "Requesting restaurant list."
    r = requests.post(url, headers=headers, data=data)

    "Restaurant list recieved."
    if r.status_code == 200:

        "Writing new list file."
        with open('data/restaurant_list.html', 'wb') as writefile:
            writefile.write(r.content)

    else:
        "Download failed."

def parse_restaurant_list():
    """
    Parses the restaurant list HTML into a nice JSON file of restaurants.
    """

    "Parsing restaurant HTML."
    with open('data/restaurant_list.html', 'rb') as readfile:
        html = str(readfile.read())

    soup = BeautifulSoup(html)
    rows = soup.select('tr.gridfield')
    rows += soup.select('tr.altgridfield')

    restaurant_list = []

    print "Parsing %s restaurants." % len(rows)
    for row in rows:
        restaurant_dict = {}
        restaurant_dict['url'] = 'http://apps.lanecounty.org/RIS/%s' % row.select('a')[0]['href']
        restaurant_dict['name'] = row.select('a')[0].text
        restaurant_dict['id'] = restaurant_dict['url'].split('http://apps.lanecounty.org/RIS/Restaurant.aspx?rid=')[1]

        restaurant_dict['most_recent_inspection'] = {}
        restaurant_dict['most_recent_inspection']['inspection_type'] = row.select('td')[1].text.replace('\n', '').replace('\r', '').strip()
        restaurant_dict['most_recent_inspection']['score'] = row.select('td')[3].text.strip().replace('\n', '').replace('\r', '').strip()

        parsed_date = parse(row.select('td')[2].text.replace('\n', '').replace('\r', '').strip())
        restaurant_dict['most_recent_inspection']['inspection_date'] = int(time.mktime(parsed_date.timetuple()))

        restaurant_dict['dirty_address'] = row.select('td')[0].contents[3].replace(u'\xc2', '').replace(u'\xa0', ' ').encode('utf-8').strip()

        try:
            restaurant_dict['address'] = row.select('td')[0].contents[3].replace(u'\xc2', '').replace(u'\xa0', ' ').encode('utf-8').split(',')[0].strip()
            restaurant_dict['city'] = row.select('td')[0].contents[3].replace(u'\xc2', '').replace(u'\xa0', ' ').encode('utf-8').split(',')[1].split()[0].strip()
            restaurant_dict['state'] = row.select('td')[0].contents[3].replace(u'\xc2', '').replace(u'\xa0', ' ').encode('utf-8').split(',')[1].split()[1].strip()
            restaurant_dict['zip_code'] = row.select('td')[0].contents[3].replace(u'\xc2', '').replace(u'\xa0', ' ').encode('utf-8').split(',')[1].split()[2].strip()
        except IndexError:
            restaurant_dict['address'] = None
            restaurant_dict['city'] = None
            restaurant_dict['state'] = None
            restaurant_dict['zip_code'] = None

        print "  + %s" % restaurant_dict['name']
        restaurant_list.append(restaurant_dict)

    print "Writing %s restaurants to JSON." % len(restaurant_list)
    with open('data/restaurant_list.json', 'wb') as writefile:
        writefile.write(json.dumps(restaurant_list))

if __name__ == "__main__":
    scrape_restaurant_list()
    parse_restaurant_list()
