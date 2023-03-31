import os
from slack_bolt import App
import discord

from dotenv import load_dotenv


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
discord_client = discord.Client(intents=intents)


app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


