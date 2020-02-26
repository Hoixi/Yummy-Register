import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os

bot = discord.Client()
bot_prefix="!"
bot = commands.Bot(command_prefix=bot_prefix)

@bot.event
async def on_ready():
    channel = bot.get_channel('682247713756020857')
    message = await channel.send('hmm…')
    while True:
        reaction = await bot.wait_for_reaction(emoji="🏃", message=message)
        

bot.run(os.environ.get('token'))
