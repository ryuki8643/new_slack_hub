from qiita import qiita_rss, qiita_API
from slackbot_init._init_ import app
from send_text.send_text import send_discord_and_slack,Channels

@app.message("hello")
def message_hello(message, say):
    say(f"qiita hello <@{message['user']}>!")


@app.message("qiita")
def message_hello1(message, say):
    send_discord_and_slack("*QIITA*\n\n"+qiita_rss.read_rss_qiita_txt(),say,Channels.DAYLY)


@app.message("qiisum")
def message_hello2(message, say):
    for texts in qiita_API.summaries_of_qiita_pop():
        say(texts)



