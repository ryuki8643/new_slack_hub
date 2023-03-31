import os
from slack_bolt import App
import discord

from dotenv import load_dotenv


load_dotenv()


discord_client = discord.Client(intents=discord.Intents.all())


app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


