from slackbot_init._init_ import app
from itmedia import techblog_rss


@app.message("aws")
def message_hello1(message, say):

    say("*aws*\n\n"+techblog_rss.get_rss_tech_blog("https://aws.amazon.com/jp/blogs/news/feed/"))

@app.message("aws")
def message_hello1(message, say):

    say("*AWS*\n\n"+techblog_rss.get_rss_tech_blog("https://aws.amazon.com/jp/blogs/news/feed/"))
@app.message("mercari")
def message_hello1(message, say):

    say("Mercari*\n\n"+techblog_rss.get_rss_tech_blog("https://engineering.mercari.com/blog/feed.xml"))
@app.message("aws")
def message_hello1(message, say):

    say("*aws*\n\n"+techblog_rss.get_rss_tech_blog("https://aws.amazon.com/jp/blogs/news/feed/"))
@app.message("aws")
def message_hello1(message, say):

    say("*aws*\n\n"+techblog_rss.get_rss_tech_blog("https://aws.amazon.com/jp/blogs/news/feed/"))