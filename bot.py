import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os

bot = discord.Client()
bot_prefix="!"
bot = commands.Bot(command_prefix=bot_prefix)

@bot.event
async def on_ready():
    yummy = discord.utils.find(lambda g : g.id == '672019759729999884' , bot.servers)
    channel = bot.get_channel('682247713756020857')  
    messagee = await bot.send_message(channel, "Kuralları okuyup kabul ettiyseniz lütfen aşağıda ki onay simgesine tıklayınız.")    
    role = discord.utils.get(yummy.roles, name="annen")
    while True:
        reaction = await bot.wait_for_reaction(emoji="🏃", message=message)
        await bot.send_message(channel, "Kayıdınız Tamamlandı!")       
        await reaction.message.author.add_roles(role)

bot.run(os.environ.get('token'))
