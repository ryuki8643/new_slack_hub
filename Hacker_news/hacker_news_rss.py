import re

import requests
from bs4 import BeautifulSoup
import datetime


def read_rss_hacker_news(url):
    req = requests.get(url)
    txt = BeautifulSoup(req.text, "html.parser")
    return txt


def get_rss_hacker_news(url):
    txt = read_rss_hacker_news(url)
    contents = txt.findAll("span", class_="titleline")
    rss_items = [
        "*Hacker News"
        + str((datetime.datetime.now() - datetime.timedelta(days=1)).date())
        + "*"
    ]
    num = 1
    for content in contents:
        if re.search(
            r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", content.find("a").get("href")
        ):
            rss_items += [
                "*" + str(num) + " " + content.text + "*",
                content.find("a").get("href"),
            ]
            num += 1
    return "\n".join(rss_items)
