from slackbot_init._init_ import app
from Hacker_news.hacker_news_rss import get_rss_hacker_news
@app.message("hackernews")
def message_hello1(message, say):
    say(get_rss_hacker_news("https://news.ycombinator.com/front"))