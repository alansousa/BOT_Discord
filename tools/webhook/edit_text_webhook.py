from discord_webhook import DiscordWebhook
from time import sleep

url = 'https://discord.com/api/webhooks/938510068352180255/2aolYlPcByMMnHNHyBtzMoKyhkvWvIWhMeD8atto4IaIOxVNqB0HVFh7uMLIbHF-oraw'
message = 'mensagem inicial'

webhook = DiscordWebhook(url=url, content=message)

sent_webhook = webhook.execute()

webhook.content = 'mensagem alterada'

sleep(10)

sent_webhook = webhook.edit(sent_webhook)
