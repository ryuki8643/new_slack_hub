import re

import requests
from bs4 import BeautifulSoup
import datetime


def read_rss_publishkey(url):
#    url = 'https://rss.itmedia.co.jp/rss/2.0/ait.xml'
    req = requests.get(url)
    txt = BeautifulSoup(req.text, 'html.parser')
    return txt


def day_check():
    return set([datetime.datetime.now().date(),(datetime.datetime.now()-datetime.timedelta(days=1)).date()])

def get_rss_publishkey(url):
    txt = read_rss_publishkey(url)

    rss_items = []
    valid_dates = day_check()
    contents=txt.findAll('item')
    if contents==[]:
        contents = txt.findAll('entry')
    for item in contents:

        if datetime.datetime.strptime(item.published.text[:10], '%Y-%m-%d').date() in valid_dates:
            if item.summary:
                rss_item = "*" + item.published.text[:10] + " " + \
                           item.title.text + "*\n" + \
                           item.summary.text + "\n" + \
                           item.link.get("href")
            else:
                rss_item = "*" + item.published.text[:10] + " " + \
                           item.title.text + "*\n" + \
                           item.link.get("href")

            rss_items.append(rss_item)
        else:
            break
    if rss_items:
        return "\n\n".join(reversed(rss_items))
    else:
        return "Today no article"

