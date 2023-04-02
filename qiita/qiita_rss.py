import requests
import re
from bs4 import BeautifulSoup


def read_rss_qiita():
    url = "https://qiita.com/popular-items/feed.atom"
    req = requests.get(url)
    txt = BeautifulSoup(req.text, "html.parser")
    return txt


def url_regex(url):
    print(url)
    return re.findall("[^]]+(?=\?)", url)[0]


def read_rss_qiita_txt():
    txt = read_rss_qiita()

    rank = 1
    rss_ranks = []
    for item in txt.findAll("entry"):
        rss_ranks.append(str(rank) + item.title.text)
        rss_ranks.append(url_regex(item.link.get("href")))
        rank += 1
    return "\n".join(rss_ranks)


def read_rss_qiita_ids():
    txt = read_rss_qiita()

    rss_dict = {"url": [], "title": []}
    for item in txt.findAll("entry"):
        rss_dict["url"].append(url_regex(item.link.get("href")))
        rss_dict["title"].append(item.title.text)

    return rss_dict
