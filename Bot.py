import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready')

client.run('ODQzNTM1NDQxNTM4MTg3MzE1.YKFRmQ.ZV_LJj9EQTUAtfQCZV8Lfk0Nxb4')

