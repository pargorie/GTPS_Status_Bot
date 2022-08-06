import os
try:
    import discord
    from discord.ext import commands
    import random
    from discord import *
    import subprocess
    import psutil
    from discord.ext import tasks
except:
    os.system('pip install discord')



prefix = '-'
intents = discord.Intents().all()
intents.members = True
client = commands.Bot(command_prefix = prefix, intents = intents)


@client.event
async def on_ready():
    print("Bot is ready.")
    channel = client.get_channel("YOU CHANNEL ID FOR STATUS CHANNEL'S ID HERE")
    em = discord.Embed(title="Server is",color=0x12d600, description="🔴 Server is DOWN\n🌙Be patience!")
    await channel.send(embed=em)
    myLoop.start()

@tasks.loop(seconds = 10) # repeat after every 10 seconds
async def myLoop():
    channel = client.get_channel(993788813413462047)
    if "Fatih.exe" in (p.name() for p in psutil.process_iter()):
        await client.change_presence(activity=discord.Game(name="🟢Server is UP!"))
        em = discord.Embed(title="RichTopia\n━━━━━",color=0x12d600, description="🟢 Server is UP\n⭐Have fun everyone!")
        await channel.last_message.edit(embed=em)
    else:
        await client.change_presence(activity=discord.Game(name="🔴Server is DOWN!"))
        em = discord.Embed(title="RichTopia",color=0x12d600, description="🔴 Server is DOWN\n🌙Be patience!")
        await channel.last_message.edit(embed=em)


client.run("YOUR BOT'S TOKEN HERE")
