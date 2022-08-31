from slackbot_init._init_ import app
from publishkey import publishkey_rss
@app.message("publishkey")
def message_hello1(message, say):

    say("*Publish Key*\n\n"+publishkey_rss.get_rss_publishkey("https://www.publickey1.jp/atom.xml"))