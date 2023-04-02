import requests, json, os

from enum import Enum
from time import sleep
from dotenv import load_dotenv


load_dotenv()


# 列挙型の定義
class Channels(Enum):
    DAYLY = "daily"
    TECHBLOGS = "techblogs"
    OTHERTECHBLOGS = "othertechblogs"


discord_channels = {
    Channels.DAYLY: os.environ.get("DISCORD_WEBHOOK_DAILY"),
    Channels.TECHBLOGS: os.environ.get("DISCORD_WEBHOOK_TECHBLOG"),
    Channels.OTHERTECHBLOGS: os.environ.get("DISCORD_WEBHOOK_OTHERTECHBLOG"),
}


def send_discord_and_slack(text, say, channel):
    say(text)
    webhook_url = discord_channels[channel]
    split_text = text.split("\n")
    skip = False
    for i in range(len(split_text)):
        if split_text[i] == "":
            continue
        if skip:
            skip = False
            continue
        send_text = split_text[i]
        if i + 1 < len(split_text):
            if split_text[i + 1][:5] == "<http":
                send_text += "\n" + split_text[i + 1]
                skip = True

        main_content = {
            "username": "tech_news_bot",
            "avatar_url": "https://drive.google.com/file/d/1tdtv3bGehSVaf7ER0_SJqeIudeDbEwNY/view?usp=share_link",
            "content": send_text,
        }
        headers = {"Content-Type": "application/json"}

        response = int(
            requests.post(
                webhook_url, json.dumps(main_content), headers=headers
            ).status_code
        )
        while response >= 400:
            print(response)
            print(split_text[i], main_content["content"])
            response = int(
                requests.post(
                    webhook_url, json.dumps(main_content), headers=headers
                ).status_code
            )
            sleep(1)
        sleep(1)
