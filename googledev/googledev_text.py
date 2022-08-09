import requests
from bs4 import BeautifulSoup
import datetime


def read_article(url):
    req = requests.get(url)
    txt = BeautifulSoup(req.text, 'html.parser')
    return txt


def judge_date(date_text):
    # str = 'August 08, 2022'
    valid_dates = set([datetime.datetime.now().date(), (datetime.datetime.now() - datetime.timedelta(days=1)).date()])
    now_day = datetime.datetime.strptime(date_text, '%B %d, %Y').date()
    return now_day in valid_dates


def get_new_blog_from_google_dev():
    top_page = read_article('https://developers.googleblog.com/')
    cards_link_list = top_page.findAll('a', class_='dgc-card__href')
    dates_list = top_page.findAll('div', class_='dgc-card__info')
    results_list = []
    for article_num in range(len(dates_list)):
        query = dates_list[article_num].p.text
        if judge_date(query):
            geturl = cards_link_list[article_num].get("href")
            individual_article = read_article(geturl)
            for meta in individual_article.findAll("meta"):
                property_of_meta = meta.get("property")
                if property_of_meta == "og:title":
                    results_list.append(meta.get("content"))
                elif property_of_meta == "og:description":
                    results_list.append(meta.get("content"))
            results_list.append(geturl + "\n")
    return "\n".join(results_list)
