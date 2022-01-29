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
async def pulang(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.voice.send("Ibu pulang dulu ya ..")

@bot.command()
async def absen(ctx):
    names = list()
    channel = ctx.message.author.voice.channel
    if channel.members:
        for member in channel.members:
            #print(f'{member.name} !!!')
            names.append(f'{member.nick}')
        await ctx.channel.send('Absen '+f'{ctx.message.created_at}'+'\n'+'\n'.join(names))
    else:
        await ctx.channel.send('Sepi bener')

@bot.command()
async def laper(ctx):
    await ctx.send("Makan lah anjir!")

@bot.command()
async def bacot(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not in voice channel")
        return
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    voice.play(discord.FFmpegPCMAudio("bacot.mp3"))   
    for member in channel.members:
        await member.edit(mute=True)
        print("Muted member", member)
    await ctx.send("Diam ya anak-anak 😡😡😡 !!!")

@bot.command()
async def unmute(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not in voice channel")
        return
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    for member in channel.members:
        await member.edit(mute=False)
        print("Muted member", member)
    await ctx.send("Silakan yang mau bertanya !!!")

@bot.command()
async def ara(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not in voice channel")
        return
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    voice.play(discord.FFmpegPCMAudio("ara_ara.mp3"))

@bot.command()
async def senam(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not in voice channel")
        return
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    voice.play(discord.FFmpegPCMAudio("senam.mp3"))

@bot.command()
async def sini(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not in voice channel")
        return
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    voice.play(discord.FFmpegPCMAudio("ada_ibu.mp3"))

@bot.command()
async def galau(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not in voice channel")
        return
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    voice.play(discord.FFmpegPCMAudio("memikirkan_dia.mp3"))

@bot.event
async def on_disconnect():
    print('Bot disconnected')

@bot.event
async def on_resumed():
    print('Bot reconnected')

bot.run(TOKEN)


#ada role Crimsonites, scout, admin (di ch woe/woc auto mute kecuali scout + admin + owner)
