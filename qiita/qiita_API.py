import os
import json
import re

import requests
from qiita.qiita_rss import read_rss_qiita_ids
from qiita.summerize_text import summarize_text

from dotenv import load_dotenv

load_dotenv()


def summaries_of_qiita_pop():
    qiita_dict = read_rss_qiita_ids()
    qiita_dict["text"] = []
    qiita_dict["like"] = []

    def qiita_API_access(qiita_url):
        """get"""
        qiita_headers = {
            "Content-Type": "application/json",
            "Charset": "utf-8",
            "Authorization": "Bearer {}".format(os.environ.get("QIITA_ACCESS_TOKEN")),
        }
        res = requests.get(url=qiita_url, headers=qiita_headers)
        print("{}, {}".format(res.status_code, res.url))
        return json.loads(res.text)

    def text_preprocess_for_sum(text):
        def programming_text(pretext):
            if re.match("\t", pretext) or text == "":
                return False
            else:
                return True

        return re.sub(
            r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+",
            "",
            "\n".join(list(filter(programming_text, text.split("\n")))),
        )

    for num in range(len(qiita_dict["title"])):
        url = qiita_dict["url"][num]
        article_id = re.findall("(?<=items/)[^]]+", url)[0]
        individual_url = "https://qiita.com/api/v2/items/{}".format(article_id)
        response_json = qiita_API_access(individual_url)
        for i in response_json.keys():
            if type(response_json[i]) == int:
                print(i, response_json[i])
        qiita_dict["text"].append(
            summarize_text(text_preprocess_for_sum(response_json["body"])) + "\n" + url
        )
        qiita_dict["like"].append(response_json["likes_count"])

    results_list = []

    for num in reversed(range(len(qiita_dict["title"]))):
        qiita_sum_result = ""
        qiita_sum_result += (
            "*"
            + str(num + 1)
            + "位 "
            + str(qiita_dict["like"][num])
            + "☆"
            + qiita_dict["title"][num]
            + "*\n\n"
        )
        qiita_sum_result += qiita_dict["text"][num]

        print(qiita_dict["url"][num])
        results_list.append(qiita_sum_result)
    return results_list
