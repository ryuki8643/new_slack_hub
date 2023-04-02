import os
import sys
import logging

sys.dont_write_bytecode = True
from slack_bolt.adapter.flask import SlackRequestHandler
from slack_sdk import WebClient
from qiita.throw_qiita_toslack import *
from zenn.throw_zenn_toslack import *
from techblogs.throw_other_tech_blog_to_slack import *
from techblogs.thow_tech_blog_rss import *
from techfeed.throw_techfeed_to_slack import *
from publishkey.throw_publishkey import *
from apphome.apphome import *
from googledev.throw_googledev_toslack import *
from Hacker_news.throw_hacker_news_toslack import *
from send_text.send_text import send_discord_and_slack
from concurrent.futures import ProcessPoolExecutor
from send_text.send_text import send_discord_and_slack, Channels

logging.basicConfig(level=logging.INFO)


from flask import Flask, request

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)


@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)


@flask_app.route("/")
def hello():
    return "Hello World!"


@flask_app.route("/test")
def test():
    # send_discord_and_slack("a",print,Channels.DAYLY)
    return "penguins"


def flask_run():
    flask_app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    print(len(viewTemplate["blocks"]))
    flask_run()
