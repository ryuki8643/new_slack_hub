import requests
from bs4 import BeautifulSoup


def get_rss_qiita():
    url = 'https://qiita.com/popular-items/feed.atom'
    req = requests.get(url)
    txt = BeautifulSoup(req.text, 'html.parser')
    print("a", txt)

    rank = 1
    for item in txt.findAll('entry'):
        print(rank, item.title.text)
        rank += 1
