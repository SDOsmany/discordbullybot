# bot.py
import os
from discord.ext import commands

import discord
from dotenv import load_dotenv

import pandas as pd

# load the environment variables
load_dotenv()
TOKEN = os.getenv('bot_key')
CHANNEL_ID = os.getenv('channel_id')

# read the list of roasts
path = "roast_list.csv"
abs_path = os.path.abspath(path)
roasting_list = pd.read_csv(abs_path, header=None)

# initialize the bot
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    channel = bot.get_channel(int(CHANNEL_ID))
    await channel.send('Hello!')

@bot.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == bot.user:
        return

    if message.mentions:
        for mention in message.mentions:
            if "!bully" in message.content:
                response = str(mention) + " " + roasting_list.sample(n=1).iloc[0,0]
                await message.channel.send(response)
    # Check if the message is "!bully" and respond
    if message.content == "!bully":
        response = message.author.mention + " " + roasting_list.sample(n=1).iloc[0,0]
        await message.channel.send(response)

bot.run(TOKEN)