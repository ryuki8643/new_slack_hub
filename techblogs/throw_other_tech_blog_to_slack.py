from slackbot_init._init_ import app
from techblogs import techblog_rss
from dotenv import load_dotenv
from send_text.send_text import send_discord_and_slack,Channels

load_dotenv()

@app.message("techblogs")
def message_hello1(message, say):

    send_discord_and_slack("*TechBlogs*\n\n"+techblog_rss.get_rss_tech_blog("https://yamadashy.github.io/tech-blog-rss-feed/feeds/rss.xml"),say,Channels.OTHERTECHBLOGS)

@app.message("infoq")
def message_hello1(message, say):

    send_discord_and_slack("*Architecture*\n\n"+techblog_rss.get_rss_tech_blog("https://feed.infoq.com/"),say,Channels.OTHERTECHBLOGS)


