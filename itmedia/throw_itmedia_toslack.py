from slackbot_init._init_ import app
from itmedia import itmedia_rss


@app.message("itmedia")
def message_hello1(message, say):

    say("*ITmedia*\n\n"+itmedia_rss.read_rss_it_media_txt())
