from slackbot_init._init_ import app
from itmedia import techblog_rss


@app.message("yahoo")
def message_hello1(message, say):
    say("*Yahoo*\n\n"+techblog_rss.get_rss_tech_blog("https://techblog.yahoo.co.jp/index.xml"))