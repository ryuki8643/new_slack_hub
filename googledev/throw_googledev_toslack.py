from slackbot_init._init_ import app
from googledev import googledev_text


@app.message("googledev")
def message_hello1(message, say):
    say("*Google Developer Blog*\n\n"+googledev_text.get_new_blog_from_google_dev())
