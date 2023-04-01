from slackbot_init._init_ import app
from publishkey import publishkey_rss
from send_text.send_text import send_discord_and_slack,Channels

@app.message("publishkey")
def message_hello1(message, say):

    send_discord_and_slack("*Publish Key*\n\n"+publishkey_rss.get_rss_publishkey("https://www.publickey1.jp/atom.xml"),say,Channels.DAYLY)