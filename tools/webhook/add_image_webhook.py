
from discord_webhook import DiscordWebhook

url = 'https://discord.com/api/webhooks/938510068352180255/2aolYlPcByMMnHNHyBtzMoKyhkvWvIWhMeD8atto4IaIOxVNqB0HVFh7uMLIbHF-oraw'

webhook = DiscordWebhook(url=url, username="Webhook with files")

# send two images
# trocar esse path pois nao funcionará quando rodar em sistemas UNIX
with open("D:\DEV\Teste_DoubleG\Curso\sonho.png", "rb") as f:
    webhook.add_file(file=f.read(), filename='sonho.png')

webhook.remove_file('example.jpg')

# only 'example2.jpg' is sent to the webhook
response = webhook.execute()
