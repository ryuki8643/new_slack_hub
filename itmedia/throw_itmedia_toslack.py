from slackbot_init._init_ import app
from itmedia import techblog_rss


@app.message("itmedia")
def message_hello1(message, say):

    say("*ITmedia*\n\n"+techblog_rss.get_rss_tech_blog("https://rss.itmedia.co.jp/rss/2.0/ait.xml"))

