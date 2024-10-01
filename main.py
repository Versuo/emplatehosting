import discord
from discord.ext import commands
import os
import webserver

DISCORD_TOKEN = os.environ['discordkey']
MENTIONED_USER_ID = '1270487884452986940'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(commands_prefix='!', intents=intents)

@bot.event
async def on_message(message):
    if MENTIONED_USER_ID in [str(user.id) for user in message.mentions]:
        try: 
            for i in range(50):
                await message.author.end("GET SPAMMED")
        except discord.Forbidden:
            await message.channel.send(f"{message.author.mention}, FFJFJFFF
    awiat bot.process_commands(message)

webserver.keep_alive()
bot.run(DISCORD_TOKEN)