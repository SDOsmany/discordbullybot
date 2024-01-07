# bot.py
import os
from discord.ext import commands

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('bot_key')
CHANNEL_ID = os.getenv('channel_id')
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

    # Check if the message is "!" and respond
    if message.content == "!bully":
        await message.channel.send("You suck!")

    # This is necessary for other commands to work
    await bot.process_commands(message)

bot.run(TOKEN)