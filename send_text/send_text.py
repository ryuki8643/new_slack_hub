from slackbot_init._init_ import discord_client


discord_channels={"daily":1088383659062599770,"techblogs":1088383714431615006,"othertechblogs":1088383769980977173}
async def send_discord_and_slack(text):
    # say(text)
    await discord_client.wait_until_ready()
    channel = await discord_client.get_channel(discord_channels["daily"])
    await channel.send(text)
