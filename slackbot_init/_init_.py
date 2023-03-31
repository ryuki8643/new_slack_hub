import os
from slack_bolt import App
import discord

from dotenv import load_dotenv

# .envファイルの内容を読み込みます
load_dotenv()


discord_client = discord.Client(intents=discord.Intents.all())

# ボットトークンとソケットモードハンドラーを使ってアプリを初期化します
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


