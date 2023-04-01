from slackbot_init._init_ import app
from Hacker_news.hacker_news_rss import get_rss_hacker_news
from send_text.send_text import send_discord_and_slack,Channels

@app.message("hackernews")
def message_hello1(message, say):
    send_discord_and_slack(get_rss_hacker_news("https://news.ycombinator.com/front"),say,Channels.TECHBLOGS)