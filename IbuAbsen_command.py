# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import mysql.connector
import re

#for cache the member, so it's realtime
intents = discord.Intents.default()
intents.members = True


#load data from dotenv file just make .env file filled with your credential
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot = commands.Bot(intents=intents, command_prefix='bu ')
#load mysql setting
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_database = os.getenv('DB_DATABASE')
mydb = mysql.connector.connect(
  host=db_host,
  user=db_user,
  password=db_pass,
  database=db_database
)

# print(mydb)

# async def absen_db(anggota):
#     mycursor = mydb.cursor()
#     names = list()
#     for x in anggota:
#         temp = tuple(re.split('\| |-',x))
#         names.append(temp)
#     sql = "INSERT INTO customers (party, ign, status) VALUES (%s, %s, %s)"
#     print(names)
#     mycursor.executemany(sql, names)
#     mydb.commit()
#     print(mycursor.rowcount, "was inserted.")
#     return

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

# @bot.command()
# async def absen(ctx):
#     names = list()
#     channel = ctx.message.author.voice.channel
#     if channel.members:
#         for member in channel.members:
#             names.append(f'{member.nick}')
#         await ctx.channel.send('Yang hadir: f'{ctx.message.created_at}'\n'+'\n'.join(names))    
#     else:
#         await ctx.channel.send('Sepi bener')

@bot.command()
async def absen(ctx):
    names = list()
    name_parse = list()
    channel = ctx.message.author.voice.channel
    if channel.members:
        for member in channel.members:
            names.append(f'{member.nick}')
        await ctx.channel.send('Yang hadir: '+ str(len(names)) +'\n'+'\n'.join(names)) 
        mycursor = mydb.cursor()
        for x in names:
            #temp = tuple(re.split('\| |-',x))
            temp = tuple(re.split('\| |-',x))
            name_parse.append(temp)
        sql = "INSERT INTO absen (party, ign) VALUES (%s, %s)"
        print(name_parse)
        mycursor.executemany(sql, name_parse)
        mydb.commit()
        print(mycursor.rowcount, "was inserted.")   
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
    voice.play(discord.FFmpegPCMAudio("audio/bacot.mp3"))   
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
    voice.play(discord.FFmpegPCMAudio("audio/ara_ara.mp3"))

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
    voice.play(discord.FFmpegPCMAudio("audio/senam.mp3"))

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
    voice.play(discord.FFmpegPCMAudio("audio/ada_ibu.mp3"))

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
    voice.play(discord.FFmpegPCMAudio("audio/memikirkan_dia.mp3"))

@bot.event
async def on_disconnect():
    print('Bot disconnected')

@bot.event
async def on_resumed():
    print('Bot reconnected')

bot.run(TOKEN)


#ada role Crimsonites, scout, admin (di ch woe/woc auto mute kecuali scout + admin + owner)
