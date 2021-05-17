import discord
from discord.ext import commands
from discord.ext.commands import bot

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def pog(ctx):
    await ctx.send('FUCK YOU')

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print(f'Logged in as {self.user} (ID: {self.user.id})')
#         print('------')
#
#     async def repeat(ctx, times: int, content='repeating...'):
#         """Repeats a message multiple times."""
#         for i in range(times):
#             await ctx.send(content)
#
#     async def on_message(self, message):
#         # don't respond to ourselves
#         if message.author == self.user:
#             return
#
#         if message.content == 'саня':
#             await message.channel.send('сам такой!')
#
#         if message.content == 'пидор':
#             await message.channel.send('сам такой!')


# client = MyClient()
client.run('ODQzNTM1NDQxNTM4MTg3MzE1.YKFRmQ.8DOVCtpAqnXrHCnDJg246g3Th-M')
