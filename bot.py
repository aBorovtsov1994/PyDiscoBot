#bot.py
import os

import discord
from dotenv import load_dotenv
#using .env files as the environmental variables for the bot and server tokens to be used in the bot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
