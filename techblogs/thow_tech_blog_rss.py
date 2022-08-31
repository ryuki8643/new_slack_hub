from slackbot_init._init_ import app
from techblogs import techblog_rss


@app.message("gihyo")
def message_hello1(message, say):

    say("*TechBlogs*\n\n"+techblog_rss.get_rss_tech_blog("https://gihyo.jp/dev/feed/rss2"))

@app.message("aws")
def message_hello1(message, say):

    say("*aws*\n\n"+techblog_rss.get_rss_tech_blog("https://aws.amazon.com/jp/blogs/news/feed/"))

@app.message("mercari")
def message_hello1(message, say):

    say("Mercari*\n\n"+techblog_rss.get_rss_tech_blog("https://engineering.mercari.com/blog/feed.xml"))
@app.message("pfn")
def message_hello1(message, say):
    say("*Preferred Network*\n\n"+techblog_rss.get_rss_tech_blog("https://tech.preferred.jp/ja/feed/"))
@app.message("developperio")
def message_hello1(message, say):
    say("*DevelopperIO*\n\n"+techblog_rss.get_rss_tech_blog("https://dev.classmethod.jp/feed/"))
@app.message("itmedia")
def message_hello1(message, say):

    say("*ITmedia*\n\n"+techblog_rss.get_rss_tech_blog("https://rss.itmedia.co.jp/rss/2.0/ait.xml"))
@app.message("yahoo")
def message_hello1(message, say):
    say("*Yahoo*\n\n"+techblog_rss.get_rss_tech_blog("https://techblog.yahoo.co.jp/index.xml"))