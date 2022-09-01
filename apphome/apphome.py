from qiita import qiita_rss
from slackbot_init._init_ import app

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
                            "text": "Aws",
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
def approve_request(ack, body, client, say, message, event):
    ack()

    viewTemplate2=viewTemplate.copy()
    viewTemplate2["blocks"][-1]["text"]["text"]="*QIITA*\n\n"+qiita_rss.read_rss_qiita_txt()

    client.views_publish(

        user_id=body["user"]["id"],

        view=viewTemplate2
    )
