from slackbot_init._init_ import app
from itmedia import techblog_rss

@app.message("developperio")
def message_hello1(message, say):
    say("*DevelopperIO*\n\n"+techblog_rss.get_rss_tech_blog("https://dev.classmethod.jp/feed/"))