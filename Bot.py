import discord
from discord.ext import commands
import random
from discord.ext.commands import bot


client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is ready') # Если всё загрузилось правильно - вывыдет ф-ию принта

# class MyClient(discord.Client):
# @client.event
# async def on_ready(self):
#     print(f'Logged in as {self.user} (ID: {self.user.id})')
#     print('------')

#
# @client.event
# async def on_member_join(member):
#     print(f'{member} has joined a server.')
#
#
# @client.event
# async def on_member_remove(member):
#     print(f'{member} has leaved a server.')
#
#

#
# async def on_message(self, message):
#     # don't respond to ourselves
#     if message.author == self.user:
#         return
#     if message.content == 'Павло':
#         await message.channel.send('саня')
#
#     if message.content == 'пидор':
#         await message.channel.send('сам такой!')


@client.command()
async def latency(ctx): # простая комманда, чтобы узнать задержку бота (в развитии видимо)
    await ctx.channel.send(f"Bots latency is around {round(client.latency * 1000)}ms")

@client.command(aliases=["8ball"]) # aliases добавляет команды, с помощью которых можно вызвать бота 
async def _8ball(ctx, *, question): # рандомный ответ из 2-х (пока что) на любой вопрос
    responses = ["NO FUCK YOU",
                 "CMON LETS GO"]
    await ctx.channel.send(f'{random.choice(responses)}')

@client.command()
async def add(ctx, left: int, right: int): # складываем два ЦЕЛЫХ числа
    """Adds two numbers together."""
    await ctx.channel.send(left + right)

@client.command()
async def clear(ctx, amount=3): # стираем сообщения в чате, по умолчанию будет стирать 3 сообщения
    await ctx.channel.purge(limit=(amount + 1)) # +1 нужен. чтобы он ваш вызов .clear также стёр

# client = MyClient()
client.run('')
