import discord
from discord.ext import commands



client = discord.Client()

@client.event
async def on_raw_reaction_add(peyload):
    message_id = peyload.message_id
    if message_id == 682667145787867393:
        guild_id = peyload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        role = discord.utils.get(guild.roles, name='annen')
        if role is not None:
            member = discord.utils.find(lambda m : m.id == peyload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
            else:
                print("Kullanıcı Yok")
        else:
            print("Rol Yok")        

@client.event
async def on_raw_reaction_remove(peyload):
    message_id = peyload.message_id
    if message_id == 682667145787867393:
        guild_id = peyload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        role = discord.utils.get(guild.roles, name='annen')
        if role is not None:
            member = discord.utils.find(lambda m : m.id == peyload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
            else:
                print("Kullanıcı Yok")
        else:
            print("Rol Yok")
    

client.run(os.environ.get('token'))
