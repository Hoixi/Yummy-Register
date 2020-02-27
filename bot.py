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
    await bot.send_message(channel , "Vay aq")
    
@bot.command(pass_context=True)
async def yum(ctx):
    await bot.add_role(ctx.message.author , discord.Role = "annen")
    

bot.run(os.environ.get('token'))
