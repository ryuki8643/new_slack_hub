from slackbot_init._init_ import app
from itmedia import techblog_rss


@app.message("mercari")
def message_hello1(message, say):

    say("*Mercari*\n\n"+techblog_rss.get_rss_tech_blog("https://yamadashy.github.io/tech-blog-rss-feed/feeds/rss.xml"))