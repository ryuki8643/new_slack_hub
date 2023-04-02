import zenn.zenn_rss
from slackbot_init._init_ import app
from send_text.send_text import send_discord_and_slack, Channels


@app.message("zenn")
def message_hello(message, say):
    send_discord_and_slack(
        "*Zenn*\n\n" + zenn.zenn_rss.read_rss_zenn(), say, Channels.DAYLY
    )
