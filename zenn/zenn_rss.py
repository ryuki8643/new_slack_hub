import requests
from bs4 import BeautifulSoup


def read_rss_zenn():
    url = 'https://zenn.dev/feed'
    req = requests.get(url)
    txt = BeautifulSoup(req.text, 'html.parser')
    print("a", txt)

    rank = 1
    rss_ranks = []
    for item in txt.findAll('item'):
        rss_ranks.append(str(rank) + item.title.text)
        rss_ranks.append(item.link.text)
        rank += 1
    return "\n".join(rss_ranks)
