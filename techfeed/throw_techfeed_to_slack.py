import os

from slackbot_init._init_ import app
from techfeed import techfeed_rss
from dotenv import load_dotenv

load_dotenv()

@app.message("techfeed")
def message_hello1(message, say):

    say("*Techfeed All*\n\n"+techfeed_rss.get_rss_tech_feed("https://techfeed.io/feeds/categories/all?userId="+os.environ["TECHFEED_USER_ID"]))
    say("*Techfeed Web FrontEnd*\n\n" + techfeed_rss.get_rss_tech_feed(
        "https://techfeed.io/feeds/categories/Web%20%2F%20Frontend?userId=" + os.environ["TECHFEED_USER_ID"]))
    say("*Techfeed Cloud Backend*\n\n" + techfeed_rss.get_rss_tech_feed(
        "https://techfeed.io/feeds/categories/Cloud%20%2F%20Backend?userId=" + os.environ["TECHFEED_USER_ID"]))
    say("*Techfeed Programming*\n\n" + techfeed_rss.get_rss_tech_feed(
        "https://techfeed.io/feeds/categories/Programming?userId=" + os.environ["TECHFEED_USER_ID"]))
