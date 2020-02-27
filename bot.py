import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os

bot = discord.Client()
bot_prefix="!"
bot = commands.Bot(command_prefix=bot_prefix)

@bot.event
async def on_reaction_add(reaction,user,server):
    channel = reaction.message.channel
    role = discord.utils.get(server.roles, name="annen")
    await bot.add_roles(user.author, role)

bot.run(os.environ.get('token'))
