import requests, json

from enum import Enum
from time import sleep
# 列挙型の定義
class Channels(Enum):
    DAYLY = "daily"
    TECHBLOGS = "techblogs"
    OTHERTECHBLOGS = "othertechblogs"

discord_channels={Channels.DAYLY:"https://discordapp.com/api/webhooks/1091710346466709684/R8SMkKPmuRx9PqwGOPqSdKCJkiA7T5zZ-0Pl96QT-b-8dSZDVQTYtVzjyP_u7J9h36Ev",
                  Channels.TECHBLOGS:"https://discordapp.com/api/webhooks/1091710531678781450/qr8_7aQ_s6k9rlclsIqGplcsXYCq0FjixnFlT4OgVDA_aqwO0-05WWIQlKOYdWFWu0Fz",
                  Channels.OTHERTECHBLOGS:"https://discordapp.com/api/webhooks/1091710702399533076/ZtgNz-KGF8vhicwvRLbBYnzOwbc1EYfZnDO7DeuiDQAJ9XuSN_fsV7bJA_9_BnBoBDLZ"}
def send_discord_and_slack(text,say,channel):
    say(text)
    webhook_url  = discord_channels[channel]
    split_text = text.split("\n")
    for i in split_text:
        main_content = {
                        'username': 'tech_news_bot',
                        'avatar_url': 'https://drive.google.com/file/d/1tdtv3bGehSVaf7ER0_SJqeIudeDbEwNY/view?usp=share_link',
                        'content': i
                    }
        headers      = {'Content-Type': 'application/json'}

        requests.post(webhook_url, json.dumps(main_content), headers=headers)
        sleep(1)