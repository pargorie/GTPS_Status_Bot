import os
try:
    import discord
    from discord.ext import commands
    import random
    import time
    import json
    from discord import *
    import subprocess
    import psutil
    from discord.ext import tasks
    import asyncio
except:
    os.system('pip install discord')



prefix = '-'
intents = discord.Intents().all()
intents.members = True
client = commands.Bot(command_prefix = prefix, intents = intents)




@client.event
async def on_ready():
    print("Bot is ready.")
    channel = client.get_channel(993788813413462047)
    em = discord.Embed(title="RichTopia",color=0x12d600, description="\n\n 🔴 Server is DOWN\n\n ⭐ Have fun everyone!\n\n\n\n\n")
    await channel.send(embed=em)
    myLoop.start()




@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')
    role = discord.utils.get(member.guild.roles, id=993194515336790060)
    await member.add_roles(role)
    em = discord.Embed(color=0x12d600, description=f"**Welcome {member.mention}, you're {len(list(member.guild.members))}!**")
    em.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    em.set_image(url=f"{member.avatar_url}")
    channel = client.get_channel(993419545236742195)



@tasks.loop(seconds = 10) # repeat after every 10 seconds
async def myLoop():
    channel = client.get_channel(993788813413462047)
    if "Fatih.exe" in (p.name() for p in psutil.process_iter()):
        await client.change_presence(activity=discord.Game(name="🟢RichTopia UP!"))
        em = discord.Embed(title="RichTopia\n━━━━━",color=0x12d600, description="🟢 Server is UP\n⭐Have fun everyone!")
        await channel.last_message.edit(embed=em)
    else:
        await client.change_presence(activity=discord.Game(name="🔴RichTopia DOWN!"))
        em = discord.Embed(title="RichTopia",color=0x12d600, description="🔴 Server is DOWN\n🌙Be patience!")
        await channel.last_message.edit(embed=em)

@client.event
async def on_member_remove(member):
        print(f'{member} has left a server.')


client.run("OTkzNzgzMjAyMDU5NjU3MjI2.G-dTQ_.5QGTihc-P1OLYaRbATxwJNnp3qBB-DUfe-66rU")
