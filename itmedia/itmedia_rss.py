import requests
from bs4 import BeautifulSoup
import datetime


def read_rss_it_media():
    url = 'https://rss.itmedia.co.jp/rss/2.0/ait.xml'
    req = requests.get(url)
    txt = BeautifulSoup(req.text, 'html.parser')
    return txt


def day_check():
    now_day = datetime.datetime.now().isoweekday()
    day_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    return set(day_of_week[now_day - 1], day_of_week[now_day])


def read_rss_qiita_txt():
    txt = read_rss_it_media()

    rss_items = []
    valid_dates = day_check()
    for item in txt.findAll('item'):
        if item.pubDate[:3] in valid_dates:
            rss_item = "*" + item.pubDatea.text[5:16] + " " + item.title.text + "*\n" + item.description.text + "\n" + \
                       item.link.text
            rss_items.append(rss_item)

    return "\n".join(reversed(rss_items))