import discord
from discord.ext import commands
from discord.utils import get
import os
import youtube_dl


client = discord.Client()
bot_prefix="y!"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    game = discord.Game("Kendi Haremi ile")
    await client.change_presence(status=discord.Status.idle, activity=game)


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
 

@client.command(pass_context=True, aliases=['j', 'join'])
async def baglan(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")

    await ctx.send(f"Joined {channel}")

client.run(os.environ.get('token'))
