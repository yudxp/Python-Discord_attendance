# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import youtube_dl
intents = discord.Intents.default()
intents.members = True



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = commands.Bot(intents=intents, command_prefix='!')


#load default setting
#summon ibu 
#setting siapa aja yg ga di mute pas woe
#setting lagu apa yg maou di play


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, id=713297992680996954)
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@client.command()
async def pulang(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Ibu pulang dulu ya ..")

@client.command()
async def absen(ctx):
        names = list()
        channel = client.get_channel(713297992680996954)#934690619559936024
        #play('https://www.youtube.com/watch?v=dNQs_Bef_V8')
        #print(str(channel))
        if channel.members:
            for member in channel.members:
                #print(f'{member.name} !!!')
                names.append(f'{member.name}')
            await absen.channel.send('Yang hadir: '+'\n'.join(names))
        else:
            await absen.channel.send('Sepi bener')

@client.event
async def on_disconnect():
    print('Bot disconnected')

@client.event
async def on_resumed():
    print('Bot reconnected')

client.run(TOKEN)

    # with open(filename, 'w') as file:
    #     for member in channel.members:
    #         file.write(member.name + '\n')