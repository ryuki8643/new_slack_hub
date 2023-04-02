from slackbot_init._init_ import app
from techblogs import techblog_rss
from send_text.send_text import send_discord_and_slack, Channels


@app.message("gihyo")
def message_hello1(message, say):
    send_discord_and_slack(
        "*Gihyo*\n\n"
        + techblog_rss.get_rss_tech_blog("https://gihyo.jp/dev/feed/rss2"),
        say,
        Channels.TECHBLOGS,
    )


@app.message("aws")
def message_hello1(message, say):
    send_discord_and_slack(
        "*aws*\n\n"
        + techblog_rss.get_rss_tech_blog("https://aws.amazon.com/jp/blogs/news/feed/"),
        say,
        Channels.TECHBLOGS,
    )


@app.message("mercari")
def message_hello1(message, say):
    send_discord_and_slack(
        "*Mercari*\n\n"
        + techblog_rss.get_rss_tech_blog(
            "https://engineering.mercari.com/blog/feed.xml"
        ),
        say,
        Channels.TECHBLOGS,
    )


@app.message("pfn")
def message_hello1(message, say):
    send_discord_and_slack(
        "*Preferred Network*\n\n"
        + techblog_rss.get_rss_tech_blog("https://tech.preferred.jp/ja/feed/"),
        say,
        Channels.TECHBLOGS,
    )


@app.message("developersio")
def message_hello1(message, say):
    send_discord_and_slack(
        "*DevelopperIO*\n\n"
        + techblog_rss.get_rss_tech_blog("https://dev.classmethod.jp/feed/"),
        say,
        Channels.TECHBLOGS,
    )


@app.message("itmedia")
def message_hello1(message, say):
    send_discord_and_slack(
        "*ITmedia*\n\n"
        + techblog_rss.get_rss_tech_blog("https://rss.itmedia.co.jp/rss/2.0/ait.xml"),
        say,
        Channels.TECHBLOGS,
    )


@app.message("yahoo")
def message_hello1(message, say):
    send_discord_and_slack(
        "*Yahoo*\n\n"
        + techblog_rss.get_rss_tech_blog("https://techblog.yahoo.co.jp/index.xml"),
        say,
        Channels.TECHBLOGS,
    )
