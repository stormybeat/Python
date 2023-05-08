import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('your token here')
client.run('MTA5NjE2MTQxODU4MTExNTA0Mg.GzZd_S.2MuDgBnOlqLhBuPIQ59pqbss8Lhe4i0m0jq1zI')