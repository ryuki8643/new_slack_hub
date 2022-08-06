import requests
from bs4 import BeautifulSoup


def read_rss_qiita():
    url = 'https://qiita.com/popular-items/feed.atom'
    req = requests.get(url)
    txt = BeautifulSoup(req.text, 'html.parser')
    print("a", txt)

    rank = 1
    rss_ranks = []
    for item in txt.findAll('entry'):
        rss_ranks.append(str(rank) + item.title.text)
        rank += 1
    return "\n".join(rss_ranks)
