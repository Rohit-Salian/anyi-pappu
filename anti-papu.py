import discord
import os

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    name = discord.utils.get(message.guild.members, name="chungusranger")
    if message.author == name:
        if 'x.com' in message.content or 'twitter.com' in message.content:
            await message.delete()

str='MTIxNjc5NDYzMzg3OTgxNDI2NA.GBdEm1.asVBjYBzR5aotVm-wasYoSs8PqcZy2R5AIMaZM'
client.run(str)
