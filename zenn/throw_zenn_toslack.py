import zenn.zenn_rss
from slackbot_init._init_ import app

@app.message("zenn")
def message_hello(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    say("*Zenn*\n\n"+zenn.zenn_rss.read_rss_zenn())