import json 
import re 
import os
import requests

from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.mecab_tokenizer import MeCabTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor
from pysummarization.nlp_base import NlpBase
from pysummarization.similarityfilter.tfidf_cosine import TfIdfCosine

def summarize_text(document):
    auto_abstractor = AutoAbstractor()

    auto_abstractor.tokenizable_doc = MeCabTokenizer()

    auto_abstractor.delimiter_list = ["．","。", "\n"]

    abstractable_doc = TopNRankAbstractor()

    result_dict = auto_abstractor.summarize(document, abstractable_doc)

    result_text = ""

    for sentence in result_dict["summarize_result"]:
        result_text += sentence
    return result_text

def qiita_API_access(qiita_url):
    """get
    """
    qiita_headers = {
        'Content-Type': 'application/json',
        'Charset': 'utf-8',
        'Authorization': 'Bearer {}'.format(os.environ.get("QIITA_ACCESS_TOKEN"))
    }
    res = requests.get(url=qiita_url, headers=qiita_headers)
    # print('{}, {}'.format(res.status_code, res.url))
    return json.loads(res.text)

def text_preprocess_for_sum(text):
    def programming_text(pretext):
        if re.match("\t", pretext) or text == "":
            return False
        else:
            return True

    return re.sub(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", "",
                    "\n".join(
                        list(
                            filter(
                                programming_text, text.split("\n")))))


from qiita import qiita_rss, qiita_API

from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":


    qiita_dict = qiita_rss.read_rss_qiita_ids()
    qiita_dict["text"] = []
    qiita_dict["like"] = []


    auto_abstractor = AutoAbstractor()
    auto_abstractor.tokenizable_doc = MeCabTokenizer()
    auto_abstractor.delimiter_list = ["．","。", "\n"]
    abstractable_doc = TopNRankAbstractor()

    # NLPオブジェクト
    nlp_base = NlpBase()
    # トークナイザー設定（MeCab使用）
    nlp_base.tokenizable_doc = MeCabTokenizer()

    # Tf-Idf コサイン類似度フィルター
    filter_03 = TfIdfCosine()
    # NLPオブジェクト設定
    filter_03.nlp_base = nlp_base
    # 類似性limit：limit超える文は切り捨て
    filter_03.similarity_limit = 0.3

    # Tf-Idf コサイン類似度フィルター
    filter_05 = TfIdfCosine()
    # NLPオブジェクト設定
    filter_05.nlp_base = nlp_base
    # 類似性limit：limit超える文は切り捨て
    filter_05.similarity_limit = 0.5

    # Tf-Idf コサイン類似度フィルター
    filter_07 = TfIdfCosine()
    # NLPオブジェクト設定
    filter_07.nlp_base = nlp_base
    # 類似性limit：limit超える文は切り捨て
    filter_07.similarity_limit = 0.7

    

    for num in range(len(qiita_dict["title"])):
        url = qiita_dict["url"][num]
        article_id = re.findall("(?<=items/)[^]]+", url)[0]
        individual_url = 'https://qiita.com/api/v2/items/{}'.format(article_id)
        response_json = qiita_API_access(individual_url)

        document = text_preprocess_for_sum(response_json["body"])

        result_dict = auto_abstractor.summarize(document, abstractable_doc)
        result = ""
        for sentence in result_dict["summarize_result"]:
            result += sentence

        result_dict = auto_abstractor.summarize(document, abstractable_doc,filter_07)
        result07 = ""
        for sentence in result_dict["summarize_result"]:
            result07 += sentence

        result_dict = auto_abstractor.summarize(document, abstractable_doc,filter_05)
        result05 = ""
        for sentence in result_dict["summarize_result"]:
            result05 += sentence

        result_dict = auto_abstractor.summarize(document, abstractable_doc,filter_03)
        result03 = ""
        for sentence in result_dict["summarize_result"]:
            result03 += sentence


        qiita_dict["text"].append(
            "<類似度フィルタなし>：\n"+result+"\n"+
            "<0.7>\n"+result07+"\n"+
            "<0.5>\n"+result05+"\n"+
            "<0.3>\n"+result03+"\n"+
            url
        )
        qiita_dict["like"].append(response_json['likes_count'])

    results_list = []

    for num in reversed(range(len(qiita_dict["title"]))):
        qiita_sum_result = ""
        qiita_sum_result += "*" + str(num + 1) + "位 " + str(qiita_dict["like"][num]) + "☆" + qiita_dict["title"][
            num] + "*\n\n"
        qiita_sum_result += qiita_dict["text"][num]

        # print(qiita_dict["url"][num])
        results_list.append(qiita_sum_result)

    print("Pysummarization:")
    for t in results_list:
        print(t)