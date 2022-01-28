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
bot = commands.Bot(intents=intents, command_prefix='bu ')



@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@bot.command()
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
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

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

@bot.command()
async def pulang(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        voice.cleanup()
        await voice.disconnect()
    else:
        await ctx.voice.send("Ibu pulang dulu ya ..")

@bot.command()
async def absen(ctx):
        names = list()
        channel = bot.get_channel(713297992680996954)#934690619559936024#713296831651643404
        #play('https://www.youtube.com/watch?v=dNQs_Bef_V8')
        #print(str(channel))
        if channel.members:
            for member in channel.members:
                #print(f'{member.name} !!!')
                names.append(f'{member.name}')
            await ctx.channel.send('Yang hadir: '+'\n'.join(names))
        else:
            await ctx.channel.send('Sepi bener')

@bot.command()
async def mute(ctx):
        channel = bot.get_channel(713297992680996954)
        for member in channel.members:
            await member.edit(mute=True)
            print("Muted member", member)
        await ctx.send("Diam ya anak-anak 😡😡😡 !!!")

@bot.command()
async def unmute(ctx):
        channel = bot.get_channel(713297992680996954)
        for member in channel.members:
            await member.edit(mute=False)
            print("Muted member", member)
        await ctx.send("Monggo ngomong!")

@bot.command()
async def laper(ctx,arg):
    if arg=="laper":
        await ctx.send("Makan lah anjir!")

# @bot.command()
# async def bacot(ctx):
#     voiceChannel = discord.utils.get(ctx.guild.voice_channels, id=713297992680996954)
#     await voiceChannel.connect()
#     voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
#     voice.play(discord.FFmpegPCMAudio("bacot.mp3"))
#     await ctx.author.edit(voice_channel=None)

@bot.command()
async def bacot(ctx):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels)
    voiceChannel.connect()
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        voice.play(discord.FFmpegPCMAudio("bacot.mp3"))
        await ctx.author.edit(voice_channel=None)
    else :
        print("err")



@bot.command()
async def senam(ctx):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels)
    await voiceChannel.connect()
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("senam.mp3"))

@bot.event
async def on_disconnect():
    print('Bot disconnected')

@bot.event
async def on_resumed():
    print('Bot reconnected')

bot.run(TOKEN)


#ada role Crimsonites, scout, admin (di ch woe/woc auto mute kecuali scout + admin + owner)
