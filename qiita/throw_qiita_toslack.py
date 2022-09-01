from qiita import qiita_rss, qiita_API
from slackbot_init._init_ import app


@app.message("hello")
def message_hello(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    say(f"qiita hello <@{message['user']}>!")


@app.message("qiita")
def message_hello1(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    say("*QIITA*\n\n"+qiita_rss.read_rss_qiita_txt())


@app.message("qiisum")
def message_hello2(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    for texts in qiita_API.summaries_of_qiita_pop():
        say(texts)



