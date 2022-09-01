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


logging.basicConfig(level=logging.INFO)
# アプリを起動します

from flask import Flask, request

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

@flask_app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    print(len(viewTemplate["blocks"]))
    flask_app.run(host="0.0.0.0", port=8000)
