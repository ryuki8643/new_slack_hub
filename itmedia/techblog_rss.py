import re

import requests
from bs4 import BeautifulSoup
import datetime


def read_rss_tech_blog(url):
#    url = 'https://rss.itmedia.co.jp/rss/2.0/ait.xml'
    req = requests.get(url)
    txt = BeautifulSoup(req.text, 'html.parser')
    return txt


def day_check():
    now_day = datetime.datetime.now().isoweekday()
    day_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    return set([ day_of_week[now_day]])


def get_rss_tech_blog(url):
    txt = read_rss_tech_blog(url)

    rss_items = []
    valid_dates = day_check()
    for item in txt.findAll('item'):
        if item.pubdate.text[:3] in valid_dates:
            if item.description:
                rss_item = "*" + item.pubdate.text[5:16] + " " + \
                           item.title.text + "*\n" + \
                           item.description.text + "\n" + \
                           re.findall(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", item.text)[0]
            else:
                rss_item = "*" + item.pubdate.text[5:16] + " " + \
                           item.title.text + "*\n" + \
                           item.link.text + \
                           re.findall(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", item.text)[0]
            rss_items.append(rss_item)
        else:
            break
    if rss_items:
        return "\n\n".join(reversed(rss_items))
    else:
        return "Today no article"
