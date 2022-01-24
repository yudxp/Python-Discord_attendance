# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content == 'absen bu':
        await message.channel.send('ia nanti yaaa!!')
    elif message.content == 'hi bu':
        response = 'Selamat pagi  ' + str(message.author)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException        

@client.event
async def on_disconnect():
    print('Bot disconnected')

client.run(TOKEN)