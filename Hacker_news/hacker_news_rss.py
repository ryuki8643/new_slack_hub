import re

import requests
from bs4 import BeautifulSoup
import datetime


def read_rss_hacker_news(url):
    #    url = 'https://rss.itmedia.co.jp/rss/2.0/ait.xml'
    req = requests.get(url)
    txt = BeautifulSoup(req.text, "html.parser")
    return txt


def get_rss_hacker_news(url):
    txt = read_rss_hacker_news(url)
    contents = txt.findAll("a", class_="titlelink")

    rss_items = [
        "*Hacker News"
        + str((datetime.datetime.now() - datetime.timedelta(days=1)).date())
        + "*"
    ]
    num = 1
    for content in contents:
        if re.search(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", content.get("href")):
            rss_items += [
                "*" + str(num) + " " + content.text + "*",
                content.get("href"),
            ]
            num += 1
    return "\n".join(rss_items)
