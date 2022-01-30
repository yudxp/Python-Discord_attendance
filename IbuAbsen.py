# bot.py
import os
import discord
from dotenv import load_dotenv
intents = discord.Intents.default()
intents.members = True


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    guild = discord.utils.get(client.guilds, name=GUILD)
    if message.author == client.user:
        return
    elif message.content == 'absen bu':
        names = list()
        channel = client.get_channel(713296831651643404)#934690619559936024
        #print(str(channel))
        if channel.members:
            for member in channel.members:
                names.append(f'{member.name}')
            await message.channel.send('Yang hadir: '+'\n'.join(names))
        else:
            await message.channel.send('Ni pada kemana yak!')
    elif message.content == 'pagi bu':
        response = 'Selamat pagi  ' + str(message.author) + ' 🥰🥰🥰'
        print(str(message.author) + "say hi")
        await message.channel.send(response)
    elif message.content == 'ibu cantik deh':
        response = 'Bisa aja kamu ' + str(message.author)+ ' ❤️❤️❤️'
        print(str(message.author) + " menggombal")
        await message.channel.send(response)
    elif message.content == 'berisik bu':
        names = list()
        channel = client.get_channel(713296831651643404)
        for member in channel.members:
            await member.edit(mute=True)
            print("Muted member", member)
        await message.channel.send("Diam ya anak-anak 😡😡😡 !!!")
    elif message.content == 'nanya bu':
        names = list()
        channel = client.get_channel(713296831651643404)
        for member in channel.members:
            await member.edit(mute=False)
            print("Muted member", member)
        await message.channel.send('Ia silakan yang mau tanya?')

    elif message.content == 'raise-exception':
        raise discord.DiscordException        

@client.event
async def on_disconnect():
    print('Bot disconnected')

@client.event
async def on_resumed():
    print('Bot reconnected')

client.run(TOKEN)