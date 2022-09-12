from discord_webhook import DiscordWebhook
from time import sleep

# ENVIA A MENSAGEM E APAGA APÓS 10 SEGUNDOS
url = 'https://discord.com/api/webhooks/938510068352180255/2aolYlPcByMMnHNHyBtzMoKyhkvWvIWhMeD8atto4IaIOxVNqB0HVFh7uMLIbHF-oraw'
message = 'mensagem inicial'

webhook = DiscordWebhook(url=url, content=message)
sent_webhook = webhook.execute()

sleep(10)

webhook.delete(sent_webhook)
