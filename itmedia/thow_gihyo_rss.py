from slackbot_init._init_ import app
from itmedia import techblog_rss


@app.message("gihyo")
def message_hello1(message, say):

    say("*TechBlogs*\n\n"+techblog_rss.get_rss_tech_blog("https://gihyo.jp/dev/feed/rss2"))