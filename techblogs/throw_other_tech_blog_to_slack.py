from slackbot_init._init_ import app
from techblogs import techblog_rss
from dotenv import load_dotenv

load_dotenv()

@app.message("techblogs")
def message_hello1(message, say):

    say("*TechBlogs*\n\n"+techblog_rss.get_rss_tech_blog("https://yamadashy.github.io/tech-blog-rss-feed/feeds/rss.xml"))

@app.message("infoq")
def message_hello1(message, say):

    say("*Architecture*\n\n"+techblog_rss.get_rss_tech_blog("https://feed.infoq.com/"))


