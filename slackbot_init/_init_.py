import os
from slack_bolt import App
from dotenv import load_dotenv


load_dotenv()


app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)
