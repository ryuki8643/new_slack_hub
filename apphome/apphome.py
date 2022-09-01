import os

from googledev import googledev_text
from publishkey import publishkey_rss
from qiita import qiita_rss
from slackbot_init._init_ import app
from techblogs import techblog_rss
from techfeed import techfeed_rss
from zenn import zenn_rss
from dotenv import load_dotenv

load_dotenv()

viewTemplate = {
    "type": "home",
    "callback_id": "home_view",

    "blocks": [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": " *this app is collecting feed* \nfor each channel throw articles"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*daily_article_hub* qiita, zenn, techfeed, publishkey \n *techblog* googledev, itmedia, developperio, yahoo, gihyo, pfn, mercari, aws \n *othertechblog* techblogs, infoq"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Choose article you want"
            },
            "accessory": {
                "type": "static_select",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select an item",
                    "emoji": True
                },
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "Qiita",
                            "emoji": True
                        },
                        "value": "qiita"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "Zenn",
                            "emoji": True
                        },
                        "value": "zenn"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "Techfeed",
                            "emoji": True
                        },
                        "value": "techfeed"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "publishkey",
                            "emoji": True
                        },
                        "value": "publishkey"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "Google Developper",
                            "emoji": True
                        },
                        "value": "googledev"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "Itmedia",
                            "emoji": True
                        },
                        "value": "itmedia"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "developperio",
                            "emoji": True
                        },
                        "value": "developperio"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "yahoo",
                            "emoji": True
                        },
                        "value": "yahoo"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "技術評論社",
                            "emoji": True
                        },
                        "value": "gihyo"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "pfn",
                            "emoji": True
                        },
                        "value": "pfn"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "Mercari",
                            "emoji": True
                        },
                        "value": "mercari"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "AWS",
                            "emoji": True
                        },
                        "value": "aws"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "techblogs",
                            "emoji": True
                        },
                        "value": "techblogs"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "infoq",
                            "emoji": True
                        },
                        "value": "infoq"
                    }
                ],
                "action_id": "static_select-action"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "This is Home"
            }
        }
    ]
}


@app.event("app_home_opened")
def update_home_tab(client, event, logger):
    client.views_publish(

        user_id=event["user"],

        view=viewTemplate
    )


@app.action("static_select-action")
def approve_request(ack, body, client, say, message, event, payload):
    ack()
    query = payload['selected_option']['value']
    viewTemplate2 = viewTemplate.copy()
    if query == "qiita":
        viewTemplate2["blocks"][-1]["text"]["text"] = "*QIITA*\n\n" + qiita_rss.read_rss_qiita_txt()
    elif query == "zenn":
        viewTemplate2["blocks"][-1]["text"]["text"] = "*Zenn*\n\n" + zenn_rss.read_rss_zenn()
    elif query == "googledev":
        viewTemplate2["blocks"][-1]["text"][
            "text"] = "*Google Developer Blog*\n\n" + googledev_text.get_new_blog_from_google_dev()
    elif query == "publishkey":
        viewTemplate2["blocks"][-1]["text"]["text"] = "*Publish Key*\n\n" + publishkey_rss.get_rss_publishkey(
            "https://www.publickey1.jp/atom.xml")
    elif query == "techfeed":
        viewTemplate2["blocks"] += [{
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Techfeed All*\n\n" + techfeed_rss.get_rss_tech_feed(
            "https://techfeed.io/feeds/categories/all?userId=" + os.environ["TECHFEED_USER_ID"])
            }
        }, {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Techfeed Web FrontEnd*\n\n" + techfeed_rss.get_rss_tech_feed(
            "https://techfeed.io/feeds/categories/Web%20%2F%20Frontend?userId=" + os.environ[
                "TECHFEED_USER_ID"])
            }
        }, {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Techfeed Cloud Backend*\n\n" + techfeed_rss.get_rss_tech_feed(
            "https://techfeed.io/feeds/categories/Cloud%20%2F%20Backend?userId=" + os.environ[
                "TECHFEED_USER_ID"])
            }
        } , {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Techfeed Programming*\n\n" + techfeed_rss.get_rss_tech_feed(
            "https://techfeed.io/feeds/categories/Programming?userId=" + os.environ["TECHFEED_USER_ID"])
                }
            }
        ]
    elif query == "gihyo":
        viewTemplate2["blocks"][-1]["text"]["text"] = "*Gihyo*\n\n" + techblog_rss.get_rss_tech_blog(
            "https://gihyo.jp/dev/feed/rss2")
    elif query == "aws":
        viewTemplate2["blocks"][-1]["text"]["text"] = "*aws*\n\n" + techblog_rss.get_rss_tech_blog(
            "https://aws.amazon.com/jp/blogs/news/feed/")
    elif query == "mercari":
        viewTemplate2["blocks"][-1]["text"]["text"] = "*Mercari*\n\n" + techblog_rss.get_rss_tech_blog(
            "https://engineering.mercari.com/blog/feed.xml")
    elif query == "pfn":
        viewTemplate2["blocks"][-1]["text"]["text"] = "*Preferred Network*\n\n" + techblog_rss.get_rss_tech_blog(
            "https://tech.preferred.jp/ja/feed/")
    elif query == "developperio":
        viewTemplate2["blocks"][-1]["text"]["text"] = "*DevelopperIO*\n\n" + techblog_rss.get_rss_tech_blog(
            "https://dev.classmethod.jp/feed/")
    elif query == "itmedia":
        viewTemplate2["blocks"][-1]["text"]["text"] = "*ITmedia*\n\n" + techblog_rss.get_rss_tech_blog(
            "https://rss.itmedia.co.jp/rss/2.0/ait.xml")
    elif query == "yahoo":
        viewTemplate2["blocks"][-1]["text"]["text"] = "*Yahoo*\n\n" + techblog_rss.get_rss_tech_blog(
            "https://techblog.yahoo.co.jp/index.xml")
    elif query == "techblogs":
        viewTemplate2["blocks"][-1]["text"]["text"] = "*TechBlogs*\n\n" + techblog_rss.get_rss_tech_blog(
            "https://yamadashy.github.io/tech-blog-rss-feed/feeds/rss.xml")[:2900]+"\n...and more"
    elif query == "infoq":
        viewTemplate2["blocks"][-1]["text"]["text"] = "*Architecture*\n\n" + techblog_rss.get_rss_tech_blog(
            "https://feed.infoq.com/")

    client.views_publish(

        user_id=body["user"]["id"],

        view=viewTemplate2
    )
