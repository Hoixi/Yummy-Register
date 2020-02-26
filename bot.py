import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os

bot = discord.Client()
bot_prefix="!"
bot = commands.Bot(command_prefix=bot_prefix)

@bot.event
async def on_ready():
    serverr = bot.get_server('672019759729999884')
    channel = bot.get_channel('682247713756020857')  
    message = await bot.send_message(channel, "Kuralları okuyup kabul ettiyseniz lütfen aşağıda ki onay simgesine tıklayınız.")    
    role = discord.utils.get(channel.server.roles, name="annen")
    while True:
        reaction = await bot.wait_for_reaction(emoji="🏃", message=message)
        await bot.send_message(channel, "Kayıdınız Tamamlandı!")       
        await bot.add_roles(reaction.message.author, role)

bot.run(os.environ.get('token'))
