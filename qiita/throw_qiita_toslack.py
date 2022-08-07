from qiita import qiita_rss,qiita_API
from slackbot_init._init_ import app


@app.message("hello")
def message_hello(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    say(f"Hey there <@{message['user']}>!")


@app.message("qiita")
def message_hello(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    say(qiita_rss.read_rss_qiita_txt())

@app.message("qiisum")
def message_hello(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    for texts in qiita_API.summaries_of_qiita_pop():
        say(texts)

@app.event("app_home_opened")
def handle_app_home_opened_events(body, logger):
    logger.info(body)
