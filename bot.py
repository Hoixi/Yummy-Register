import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os

bot = discord.Client()
bot_prefix="!"
bot = commands.Bot(command_prefix=bot_prefix)

@bot.event
async def on_reaction_add(reaction,user):
    channel = reaction.message.channel
    yummy = discord.utils.find(lambda g : g.id == '672019759729999884' , bot.servers)
    role = discord.utils.get(yummy.roles, name="annen")
    await bot.add_roles(user.author, role)

bot.run(os.environ.get('token'))
