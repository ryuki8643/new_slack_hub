import os
import sys
import logging

sys.dont_write_bytecode = True
from slack_bolt.adapter.flask import SlackRequestHandler
from slack_sdk import WebClient
from qiita.throw_qiita_toslack import *
from zenn.throw_zenn_toslack import *
from itmedia.throw_itmedia_toslack import *
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
    flask_app.run(host="0.0.0.0", port=8000)
