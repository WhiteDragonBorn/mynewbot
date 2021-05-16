import discord
from discord.ext import commands
from discord.ext.commands import bot

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is ready')


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.content == 'саня':
            await message.channel.send('саня')


client = MyClient()
client.run('ODQzNTM1NDQxNTM4MTg3MzE1.YKFRmQ.IgN5kf_MI6Gi8YbUBfwoO9gJbi0')
