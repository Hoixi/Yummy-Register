import discord
from discord.ext import commands
import os


client = discord.Client()

@client.event
async def on_raw_reaction_add(peyload):
    message_id = peyload.message_id
    if message_id == 682696747126227110:
        guild_id = peyload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        role = discord.utils.get(guild.roles, name='Approved Collector🦉')
        if role is not None:
            member = discord.utils.find(lambda m : m.id == peyload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                channel = client.get_channel(682692982561964054)
                await channel.send( '<@%s> <#682212655783477364> kanalına hoş geldin.<#681960108426657933> kanalındaki bilgileri okumayı unutmayın. İyi eğlenceler :)' % peyload.user_id)
                user = client.get_user( peyload.user_id)
                await user.send(" ```Waifu Hunt Komutları \n $w = Animelerden Waifu verir \n $wg = Oyunlardan Waifu verir \n $im = Waifu bilgisi verir \n $mm = Hareminizi görüntüler \n $mu = Hareme ekleme hakkı takibi```")
            else:
                print("Kullanıcı Yok")
        else:
            print("Rol Yok")        

@client.event
async def on_raw_reaction_remove(peyload):
    message_id = peyload.message_id
    if message_id == 682696747126227110:
        guild_id = peyload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        role = discord.utils.get(guild.roles, name='Approved Collector🦉')
        if role is not None:
            member = discord.utils.find(lambda m : m.id == peyload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
            else:
                print("Kullanıcı Yok")
        else:
            print("Rol Yok")  
    

client.run(os.environ.get('token'))
