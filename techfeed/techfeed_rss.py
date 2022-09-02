import re

import requests
from bs4 import BeautifulSoup
import datetime


def read_rss_tech_feed(url):
#    url = 'https://rss.itmedia.co.jp/rss/2.0/ait.xml'
    req = requests.get(url)
    txt = BeautifulSoup(req.text, 'html.parser')
    return txt




def get_rss_tech_feed(url):
    txt = read_rss_tech_feed(url)

    rss_items = []

    contents=txt.findAll('item')
    if contents==[]:
        contents = txt.findAll('entry')

    for item in contents:
            if item.description:
                rss_item = "*"++item.title.text + "*\n" + \
                           item.description.text + "\n" + \
                           re.findall(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", item.text)[0]
            elif item.summary:
                rss_item = "*"+item.title.text + "*\n" + \
                           item.summary.text + "\n" + \
                           re.findall(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", item.text)[0]
            else:
                rss_item = "*"+item.title.text + "*\n" + \
                           item.link.text + \
                           re.findall(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", item.text)[0]
            rss_items.append(rss_item)
            break

    if rss_items:
        return re.sub(r'<.+?>','',"\n".join(reversed(rss_items)))
    else:
        return "Today no article"