# This example requires the 'message_content' intent.
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTA5NjE2MTQxODU4MTExNTA0Mg.GzZd_S.2MuDgBnOlqLhBuPIQ59pqbss8Lhe4i0m0jq1zI')