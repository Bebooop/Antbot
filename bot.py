import os
import discord
from dotenv import load_dotenv
from antfacts import facts
import random

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(client.user)

@client.event
async def on_message(message):
    if message.content.startswith('/antfact'):
        await message.channel.send(facts[random.randint(0, len(facts))])


client.run(DISCORD_TOKEN)

