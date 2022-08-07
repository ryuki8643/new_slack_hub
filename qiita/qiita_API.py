import os
import json
import re

import requests
from slack_bolt import App
from qiita.qiita_rss import read_rss_qiita_ids

from dotenv import load_dotenv

qiita_dict = read_rss_qiita_ids()
qiita_dict["text"] = []


def qiita_API_access(qiita_url):
    """get
    """
    qiita_headers = {
        'Content-Type': 'application/json',
        'Charset': 'utf-8',
        'Authorization': 'Bearer {}'.format(os.environ.get("QIITA_ACCESS_TOKEN"))
    }
    res = requests.get(url=qiita_url, headers=qiita_headers)
    print('{}, {}'.format(res.status_code, res.url))
    return json.loads(res.text)


for url in reversed(qiita_dict["url"]):
    article_id = re.findall("(?<=items/)[^]]+(?=\?)", url)[0]
    individual_url = 'https://qiita.com/api/v2/items/{}'.format(article_id)
    response_json = qiita_API_access(individual_url)


