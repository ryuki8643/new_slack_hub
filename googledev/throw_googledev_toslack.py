from slackbot_init._init_ import app
from googledev import googledev_text
from send_text.send_text import send_discord_and_slack,Channels

@app.message("googledev")
def message_hello1(message, say):
    send_discord_and_slack("*Google Developer Blog*\n\n"+googledev_text.get_new_blog_from_google_dev(),say,Channels.TECHBLOGS)
