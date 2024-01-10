import discord
import random
import time
import logging
import coc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from coc import utils
import pandas as pd
import json
import datetime
from PIL import Image, ImageOps, ImageDraw, ImageFont
from discord.ext import commands, tasks
from discord.utils import get
from discord import Client
from discord import Guild
import os
from os import system
import asyncio
import functools
import itertools
import math
from async_timeout import timeout
import aiohttp
import urllib.parse
import inspect
from bs4 import BeautifulSoup
import sys
import numpy as np
import webbrowser
import base64
from io import BytesIO
from urllib.request import urlopen
from urllib.parse import urlencode
import string
from urllib.request import urlretrieve
from datetime import date, timedelta
import dns
import requests
import pymongo
from pymongo import MongoClient

coc_client = coc.login(
    os.environ['DEV_EMAIL'],
    os.environ['DEV_PASS'],
    key_names="coc.py tests99998",
    client=coc.EventsClient,
)
logging.basicConfig(level=logging.ERROR)

cluster1 = MongoClient("mongodb+srv://OTTO:OTTOdb@cluster0.aoshtcx.mongodb.net/?retryWrites=true&w=majority")
cluster2 = MongoClient("mongodb+srv://OTTO2:OTTOdb@cluster0.mr1zn5l.mongodb.net/?retryWrites=true&w=majority")
cluster3 = MongoClient("mongodb+srv://OTTO:OTTOdb@cluster0.btpxwn9.mongodb.net/?retryWrites=true&w=majority")
cluster4 = MongoClient("mongodb+srv://OTTO4:OTTOdb@cluster0.c6kshcf.mongodb.net/?retryWrites=true&w=majority")
cluster5 = MongoClient("mongodb+srv://OTTO5:OTTOdb@cluster0.glphgeg.mongodb.net/?retryWrites=true&w=majority")
db1 = cluster1["Namesdb"]
db2 = cluster2["Namesdb"]
db3 = cluster3["Namesdb"]
db4 = cluster4["Namesdb"]
db5 = cluster5["Namesdb"]

# clusterr = MongoClient("mongodb+srv://Jarvis:Daisy1Tom2Sam3@cluster0.keero.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# dbb = clusterr['Users']
# collectionn = dbb['VIP']

# #token = "ODQwNTY1NDY4MDkxOTA4MTE3.YJaDmA.cYJJkIGyLE3n8e2ixRIyXaWlJRM"
# token="ODgxNjE3NDg1NzE0MDM0NzE4.YSvcRA.GzKcYieyn1sr5t1uNHSZYXFLt5c"

bot = commands.Bot(command_prefix='+',
                   guild_subscriptions=True,
                   activity=discord.Game(name="WITH SUPERCELL"),
                   case_insensitive=True,
                   intents=discord.Intents.all())
bot.remove_command('help')


@bot.event
async def on_ready():
  print(f"{bot.user.name} IS UP!")
  channel = bot.get_channel(1000659983081414729)
  em = discord.Embed(title="",description=f"",timestamp=datetime.datetime.utcnow(),color=discord.Color.green())
  em.set_author(name="Bot restarted",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
  await channel.send(embed=em)


@commands.has_role(961301374115676170)
@bot.command()
@commands.guild_only()
async def proflink(ctx, tag: str):
	channel = bot.get_channel(961310467341549598)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0x00FF00)
		embed.set_author(
		    name="Command logs",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png"
		)
		embed.add_field(name="User",
		                value="{}".format(ctx.message.author),
		                inline=True)
		embed.add_field(name="User id",
		                value="{}".format(ctx.message.author.id),
		                inline=True)
		embed.add_field(name="Server name",
		                value="{}".format(ctx.message.guild.name),
		                inline=False)
		embed.add_field(name="Channel name",
		                value="{}".format(ctx.message.channel.mention),
		                inline=False)
		embed.add_field(name="Command name", value="proflink", inline=True)
		embed.set_footer(text='Logged')
		await channel.send(embed=embed)
		player = await coc_client.get_player(tag)
		if '#' in tag:
			tag = tag.replace('#', '')
		embed = discord.Embed(
		    title=f"{player.name} #{tag.upper()}",
		    timestamp=datetime.datetime.utcnow(),
		    description=
		    f'Click [here](https://link.clashofclans.com/en?action=OpenPlayerProfile&tag={tag}) to view the player profile in game.',
		    color=discord.Color.random())
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		await ctx.reply(embed=embed)


@proflink.error
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.CommandInvokeError):
		em = discord.Embed(title="",
		                   description="",
		                   timestamp=datetime.datetime.utcnow(),
		                   color=discord.Color.red())
		em.set_author(
		    name="Invalid tag",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0xFF0000)
		embed.add_field(name="Usage",
		                value="``+proflink <TAG>``",
		                inline=False)
		embed.add_field(name="Example",
		                value="``+proflink #2PYPP02Q``",
		                inline=False)
		embed.set_author(
		    name="Invalid syntax",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png"
		)
		embed.set_footer(text=f'Command used by {ctx.message.author}')
		await ctx.send(embed=embed)


# @commands.cooldown(1, 120, commands.BucketType.user)
# @commands.has_role(961301374115676170)
# @bot.command()
# @commands.guild_only()
# async def names(ctx, tag: str):
#   channel = bot.get_channel(961310467341549598)
#   if ctx.guild.id == 961299028128190474:
#     embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
#     embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
#     embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
#     embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
#     embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
#     embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
#     embed.add_field(name="Command name", value="names", inline=True)
#     embed.set_footer(text='Logged')
#     await channel.send(embed=embed)
#     embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
#     embed.set_author(name="Loading..",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif")
#     mmm = await ctx.reply(embed=embed)
#     found = []
#     if '#' not in tag:
#       tag = '#' + tag.upper()
#     player = await coc_client.get_player(tag)
#     bigfat = [
#         '2015-08', '2015-09', '2015-10', '2015-11', '2015-12', '2016-01',
#         '2016-02', '2016-03', '2016-04', '2016-05', '2016-06', '2016-07',
#         '2016-08', '2016-09', '2016-10', '2016-11', '2016-12', '2017-01',
#         '2017-02', '2017-03', '2017-04', '2017-05', '2017-06', '2017-07',
#         '2017-08', '2017-09', '2017-10', '2017-11', '2017-12', '2018-01',
#         '2018-02', '2018-03', '2018-04', '2018-05', '2018-06', '2018-07',
#         '2018-08', '2018-09', '2018-10', '2018-11', '2018-12', '2019-01',
#         '2019-02', '2019-03', '2019-04', '2019-05', '2019-06', '2019-07',
#         '2019-08', '2019-09', '2019-10', '2019-11', '2019-12', '2020-01',
#         '2020-02', '2020-03', '2020-04', '2020-05', '2020-06',
#         '2020-07', '2020-08', '2020-09', '2020-10', '2020-11', '2020-12',
#         '2021-01', '2021-02', '2021-03', '2021-04', '2021-05', '2021-06',
#         '2021-07', '2021-08'
#     ]
#     after_bigfat = ['2021-09', '2021-10', '2021-11', '2021-12']
#     if 1 == 1:
#       for i in bigfat:
#         f = open(f'{i}.json', )
#         new_embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
#         new_embed.add_field(name="Scanning",value=f'{i}',inline=False)
#         new_embed.set_author(name="Loading..",icon_url= "https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif")
#         await mmm.edit(embed=new_embed)
#         data = json.load(f)
#         if tag in data:
#           po = data[f'{tag}']
#           found.append(f'**{i}** : {po}')
#       for j in after_bigfat:
#         m = open(f'{j}.json', 'r', encoding="utf8")
#         new_embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
#         new_embed.add_field(name="Scanning", value=f'{j}',inline=False)
#         new_embed.set_author(name="Loading..",icon_url= "https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif")
#         await mmm.edit(embed=new_embed)
#         data2 = json.load(m)
#         len_data2 = len(data2)
#         for i in range(len_data2):
#           if data2[i]["tag"] == tag:
#             found.append(f"**{j}** : {data2[i]['name']}")
#       if len(found) != 0:  
#         line = '\n'.join(map(str, found))
#         embed = discord.Embed(title=f'{player.name} {player.tag}',description=f'{line}',timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
#         embed.set_footer(text=f"Requested by {ctx.message.author}")
#         await ctx.send(embed=embed)
#         embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
#         embed.set_author(name="Process completed",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif")
#         embed.set_footer(text=f"Requested by {ctx.message.author}")
#         await mmm.edit(embed=embed)
#       else:
#         embed = discord.Embed(title=player.name,description='No names found',timestamp=datetime.datetime.utcnow(),color=discord.Color.green())
#         embed.set_footer(text=f"Requested by {ctx.message.author}")
#         await mmm.edit(embed=embed)
#     else:
#       embed = discord.Embed(title=f"Could not find old names..",color=discord.Color.red())
#       embed.set_footer(text=f"Requested by {ctx.message.author}")
#       await mmm.edit(embed=embed)

newfat = ['201508', '201509', '201510', '201511', '201512', '201601', '201602', '201603', '201604', '201605', '201606', '201607', '201608', '201609', '201610', '201611', '201612', '201701', '201702', '201703', '201704', '201705', '201706', '201707', '201708', '201709', '201710', '201711', '201712', '201801', '201802', '201803', '201804', '201805', '201806', '201807', '201808', '201809', '201810', '201811', '201812', '201901', '201902', '201903', '201904', '201905']
afternewfat = ['201906', '201907', '201908', '201909', '201910', '201911', '201912', '202001', '202002', '202003', '202004', '202005']
afterafternewfat = ['202006', '202007', '202008', '202009', '202010', '202011', '202012', '202101']
a3newfat = ['202102', '202103', '202104', '202105', '202106', '202107']
a4newfat = ['202108', '202109', '202110', '202111', '202112']

@commands.cooldown(1, 25, commands.BucketType.user)
@commands.has_role(961301374115676170)
@bot.command()
@commands.guild_only()
async def names(ctx, tag: str):
  channel = bot.get_channel(961310467341549598)
  if ctx.guild.id == 961299028128190474:
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
    embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
    embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
    embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
    embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
    embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
    embed.add_field(name="Command name", value="names", inline=True)
    embed.set_footer(text='Logged')
    await channel.send(embed=embed)
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
    embed.set_author(name="Loading..",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif")
    mmm = await ctx.reply(embed=embed)
    found = []
    player = await coc_client.get_player(tag)
    for i in newfat:
        collection = db1[f"{'Names'+i}"]
        results = collection.find({"_id": player.tag})
        for result in results:
            found.append(f"**{i[:4]+'-'+i[4:]}** : {result['name']}")
    for i in afternewfat:
        collection = db2[f"{'Names'+i}"]
        results = collection.find({"_id": player.tag})
        for result in results:
            found.append(f"**{i[:4]+'-'+i[4:]}** : {result['name']}")
    for i in afterafternewfat:
        collection = db3[f"{'Names'+i}"]
        results = collection.find({"_id": player.tag})
        for result in results:
            found.append(f"**{i[:4]+'-'+i[4:]}** : {result['name']}")
    for i in a3newfat:
        collection = db4[f"{'Names'+i}"]
        results = collection.find({"_id": player.tag})
        for result in results:
            found.append(f"**{i[:4]+'-'+i[4:]}** : {result['name']}")
    for i in a4newfat:
        collection = db5[f"{'Names'+i}"]
        results = collection.find({"_id": player.tag})
        for result in results:
            found.append(f"**{i[:4]+'-'+i[4:]}** : {result['name']}")
    if len(found) != 0:  
      line = '\n'.join(map(str, found))
      embed = discord.Embed(title=f'{player.name} {player.tag}',description=f'{line}',timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
      embed.set_footer(text=f"Requested by {ctx.message.author}")
      await mmm.edit(embed=embed)
    else:
      embed = discord.Embed(title=f"{player.name} {player.tag}",description='No names found',timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
      embed.set_footer(text=f"Requested by {ctx.message.author}")
      await mmm.edit(embed=embed)


@commands.has_role(961301374115676170)
@bot.command()
@commands.guild_only()
async def help(ctx):
    channel = bot.get_channel(961310467341549598)
    if ctx.guild.id == 961299028128190474:
        embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
        embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
        embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
        embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
        embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
        embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
        embed.add_field(name="Command name", value="help", inline=True)
        embed.set_footer(text='Logged')
        await channel.send(embed=embed)
        embed = discord.Embed(title="Hi, I'm O.T.T.O from the Builder Base!🤡",timestamp=datetime.datetime.utcnow(), description="**COMMANDS**",color=discord.Color.random())
        embed.add_field(name="+info", value="Get player's basic info\nUsage : +info <TAG>", inline=False)
        embed.add_field(name="+names", value="Get name change info\nUsage : +names <TAG>", inline=False)
        embed.add_field(name="+creation", value="Get creation date\nUsage : +creation <TAG>", inline=False)
        embed.add_field(name="+local", value="Get player's local history\nUsage : +local <TAG>", inline=False)
        embed.add_field(name="+lastsession", value="Get player's last session\nUsage : +lastsession <TAG>", inline=False)
        embed.add_field(name="+tags", value="Get some nice dead accounts\nUsage : +tags", inline=False)
        embed.add_field(name="+gatacc", value="Get a account of the rank and season you want\nUsage : +getacc <YEAR-MONTH> <RANK>", inline=False)
        embed.add_field(name="+receipt", value="Generates a fake receipt\nUsage : +receipt <DATE> <AMOUNT> <CURRENCY SYMBOL> <ORDER ID> <TYPE>", inline=False)
        embed.add_field(name="+receipt2", value="Generates a fake receipt (Full screen size)\nUsage : +receipt2 <DATE> <AMOUNT> <CURRENCY SYMBOL> <ORDER ID> <TYPE>", inline=False)
        embed.add_field(name="+receipt3", value="Generates a fake Google Play receipt\nUsage : +receipt3 <DATE> <AMOUNT> <CURRENCY SYMBOL> <TYPE>", inline=False)
        embed.add_field(name="+devices", value="Get stats of most used devices brands yearly in the given country\nUsage : +devices <country name> <FROM YEAR> <TO YEAR>", inline=False)
        embed.add_field(name="+androids", value="Get most used android devices currently in the given country\nUsage : +androids <country name>", inline=False)
        embed.add_field(name="+appledevs", value="Get most used apple devices year wise\nUsage : +appledevs", inline=False)
        embed.add_field(name="+proflink", value="Get player profile link\nUsage : +proflink <TAG>", inline=False)
        embed.add_field(name="+skins", value="Get skin's information\nUsage : +skins", inline=False)
        embed.add_field(name="+tempemails", value="Get some temporary email ids\nUsage : +tempemails", inline=False)
        embed.add_field(name="+inbox", value="Shows last mail in the inbox of temporary email\nUsage : +inbox <USED TEMPORARY EMAIL>", inline=False)
        await ctx.reply(embed=embed)

@help.error
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)

@names.error
async def on_command_error(ctx, error):
	######
	if isinstance(error, commands.CommandOnCooldown):
		em = discord.Embed(
		    title="",
		    description=f"Try again in {error.retry_after:.2f}s.",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="Hold On",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.CommandInvokeError):
		em = discord.Embed(title="",
		                   description="",
		                   timestamp=datetime.datetime.utcnow(),
		                   color=discord.Color.red())
		em.set_author(
		    name="Invalid tag",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0xFF0000)
		embed.add_field(name="Usage", value="``+names <TAG>``", inline=False)
		embed.add_field(name="Example ",
		                value="``+names #YLUJY90R``",
		                inline=False)
		embed.set_author(
		    name="Invalid syntax",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png"
		)
		embed.set_footer(text=f'Command used by {ctx.message.author}')
		await ctx.send(embed=embed)


@commands.guild_only()
@commands.has_role(961301374115676170)
@bot.command()
async def receipt(ctx, arg: str, price: float, cur: str, codek: str, *,
                  typee: str):
	channel = bot.get_channel(961310467341549598)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0x00FF00)
		embed.set_author(
		    name="Command logs",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png"
		)
		embed.add_field(name="User",
		                value="{}".format(ctx.message.author),
		                inline=True)
		embed.add_field(name="User id",
		                value="{}".format(ctx.message.author.id),
		                inline=True)
		embed.add_field(name="Server name",
		                value="{}".format(ctx.message.guild.name),
		                inline=False)
		embed.add_field(name="Channel name",
		                value="{}".format(ctx.message.channel.mention),
		                inline=False)
		embed.add_field(name="Command name", value="receipt", inline=True)
		embed.set_footer(text='Logged')
		await channel.send(embed=embed)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		embed.set_author(
		    name="Loading..",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif"
		)
		embed.set_footer(text=f'Requested by {ctx.message.author}')
		mmm = await ctx.reply(embed=embed)
		price = cur + str(price)
		tax = cur + str(price)
		x = tax.split('.')
		if len(x[1]) == 1:
			tax = tax + '0'
		if len(arg) == 9:
			mon = arg[0:3].upper()
			day = arg[3:5]
			year = arg[5:]
			date = mon + ' ' + day + ', ' + year
		if len(arg) == 7:
			mon = arg[0:3].upper()
			day = arg[3:]

			date = mon + ' ' + day

		code = codek
		# for i in range(2):
		#     code += random.choice(string.ascii_uppercase)
		# for i in range(7):
		#     x = random.randint(1, 2)
		#     if x == 1:
		#         code += random.choice(string.ascii_uppercase)
		#     else:
		#         y = random.randint(0, 9)
		#         if y == 7:
		#             y = 8
		#         code += str(y)
		layer1 = Image.open("forged.png").convert("RGBA")
		final = Image.new("RGBA", layer1.size)
		final.paste(layer1, (0, 0), layer1)
		fnt = ImageFont.truetype('aba.ttf', 22)
		d = ImageDraw.Draw(final)

		d.text((677, 13), code, font=fnt, fill=(96, 96, 98))
		f = ImageDraw.Draw(final)

		f.text((24, 13), date, font=fnt, fill=(96, 96, 98))
		p = ImageDraw.Draw(final)

		p.text((736, 65), price, font=fnt, fill=(251, 251, 253))
		p2 = ImageDraw.Draw(final)

		p2.text((712, 171), price, font=fnt, fill=(251, 251, 253))
		p2 = ImageDraw.Draw(final)

		p2.text((260, 63), typee, font=fnt, fill=(216, 216, 218))
		p2 = ImageDraw.Draw(final)
		final.save("complete.png", format="png")
		await ctx.send(file=discord.File('complete.png'))
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		embed.set_author(
		    name="Process completed",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif"
		)
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		await mmm.edit(embed=embed)


@receipt.error
async def on_command_error(ctx, error):
  ######
  if isinstance(error, commands.MissingRole):
    em = discord.Embed(title="",description="DM <@920337055706386443> to buy the bot ez",timestamp=datetime.datetime.utcnow(),color=discord.Color.red())
    em.set_author( name="You can't use the bot commands",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png")
    em.set_footer(text=f"Command used by {ctx.message.author}")
    await ctx.send(embed=em)
  ######
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0xFF0000)
    embed.add_field(name="Usage",value="``+receipt <DATE> <AMOUNT> <CURRENCY SYMBOL> <ORDER ID> <TYPE>``",inline=False)
    embed.add_field(name="Example",value="``+receipt FEB072020 4.9 $ M2MNMO56 Gold Pass``",inline=False)
    embed.set_author( name="Invalid syntax",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png")
    embed.set_footer(text=f'Command used by {ctx.message.author}')
    await ctx.send(embed=embed)
  #######
  if isinstance(error, commands.CommandInvokeError):
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0xFF0000)
    embed.add_field(name="Usage",value="``+receipt <DATE> <AMOUNT> <CURRENCY SYMBOL> <ORDER ID> <TYPE>``",inline=False)
    embed.add_field(name="Example",value="``+receipt FEB072020 4.9 $ M2MNMO56 Gold Pass``",inline=False)
    embed.set_author( name="Invalid syntax",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png")
    embed.set_footer(text=f'Command used by {ctx.message.author}')
    await ctx.send(embed=embed)
      


@commands.guild_only()
@commands.has_role(961301374115676170)
@bot.command()
async def receipt2(ctx, arg: str, price: float, cur: str, codek: str, *,
                   type: str):
	channel = bot.get_channel(961310467341549598)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0x00FF00)
		embed.set_author(
		    name="Command logs",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png"
		)
		embed.add_field(name="User",
		                value="{}".format(ctx.message.author),
		                inline=True)
		embed.add_field(name="User id",
		                value="{}".format(ctx.message.author.id),
		                inline=True)
		embed.add_field(name="Server name",
		                value="{}".format(ctx.message.guild.name),
		                inline=False)
		embed.add_field(name="Channel name",
		                value="{}".format(ctx.message.channel.mention),
		                inline=False)
		embed.add_field(name="Command name", value="receipt2", inline=True)
		embed.set_footer(text='Logged')
		await channel.send(embed=embed)
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		embed.set_author(
		    name="Loading..",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif"
		)
		embed.set_footer(text=f'Requested by {ctx.message.author}')
		mmm = await ctx.reply(embed=embed)
		price = cur + str(price)
		tax = cur + str(price)
		x = tax.split('.')
		if len(x[1]) == 1:
			tax = tax + '0'
		if len(arg) == 9:
			day = arg[0:2]
			mon = arg[2:5].upper()
			year = arg[5:]
			date = day + ' ' + mon + ' ' + year
		if len(arg) == 7:
			mon = arg[0:2].upper()
			year = arg[2:]
			date = mon + ' ' + year
		typee = type
		code = codek
		l = "1871622"
		y = f"{random.randint(0, 9)}"
		h = f"{random.randint(0, 9)}"
		j = f"{random.randint(0, 9)}"
		k = f"{random.randint(0, 9)}"
		to = l + y + h + j + k
		doc = str(to)
		# for i in range(2):
		#     code += random.choice(string.ascii_uppercase)
		# for i in range(7):
		#     x = random.randint(1, 2)
		#     if x == 1:
		#         code += random.choice(string.ascii_uppercase)
		#     else:
		#         y = random.randint(0, 9)
		#         if y == 7:
		#             y = 8
		#         code += str(y)
		layer1 = Image.open("gg.png").convert("RGBA")
		final = Image.new("RGBA", layer1.size)
		final.paste(layer1, (0, 0), layer1)
		fnt = ImageFont.truetype('aba.ttf', 22)
		d = ImageDraw.Draw(final)

		d.text((25, 256), code, font=fnt, fill=(251, 251, 253))
		f = ImageDraw.Draw(final)

		f.text((25, 350), date, font=fnt, fill=(251, 251, 253))
		p = ImageDraw.Draw(final)

		p.text((348, 350), price, font=fnt, fill=(251, 251, 253))
		p2 = ImageDraw.Draw(final)

		p2.text((520, 832), price, font=fnt, fill=(251, 251, 253))
		p2 = ImageDraw.Draw(final)

		x = 528
		if len(price) == 5:
			x = 516
		if len(price) == 6:
			x = 504
		if len(price) == 7:
			x = 492
		if len(price) == 8:
			x = 480
		p2.text((x, 721), price, font=fnt, fill=(251, 251, 253))
		p2 = ImageDraw.Draw(final)

		p2.text((110, 721), typee, font=fnt, fill=(251, 251, 253))
		p2 = ImageDraw.Draw(final)

		p2.text((348, 256), doc, font=fnt, fill=(251, 251, 253))
		p2 = ImageDraw.Draw(final)
		final.save("complete2.png", format="png")
		await ctx.send(file=discord.File('complete2.png'))
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		embed.set_author(
		    name="Process completed",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif"
		)
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		await mmm.edit(embed=embed)


@receipt2.error
async def on_command_error(ctx, error):
  ######
  if isinstance(error, commands.MissingRole):
    em = discord.Embed(title="",description="DM <@920337055706386443> to buy the bot ez",timestamp=datetime.datetime.utcnow(),color=discord.Color.red())
    em.set_author(name="You can't use the bot commands",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png")
    em.set_footer(text=f"Command used by {ctx.message.author}")
    await ctx.send(embed=em)
  ######
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0xFF0000)
    embed.add_field(name="Usage",value="``+receipt2 <DATE> <AMOUNT> <CURRENCY SYMBOL> <ORDER ID> <TYPE>``",inline=False)
    embed.add_field(name="Example",value="``+receipt2 18MAY2020 4.9 $ M2MNMO56 Gold Pass``",inline=False)
    embed.set_author(name="Invalid syntax",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png")
    embed.set_footer(text=f'Command used by {ctx.message.author}')
    await ctx.send(embed=embed)
  #######
  if isinstance(error, commands.CommandInvokeError):
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0xFF0000)
    embed.add_field(name="Usage",value="``+receipt2 <DATE> <AMOUNT> <CURRENCY SYMBOL> <ORDER ID> <TYPE>``",inline=False)
    embed.add_field(name="Example",value="``+receipt2 18MAY2020 4.9 $ M2MNMO56 Gold Pass``",inline=False)
    embed.set_author(name="Invalid syntax",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png")
    embed.set_footer(text=f'Command used by {ctx.message.author}')
    await ctx.send(embed=embed)


def getno():
	y = f"{random.randint(0, 9)}"
	h = f"{random.randint(0, 9)}"
	j = f"{random.randint(0, 9)}"
	k = f"{random.randint(0, 9)}"
	to = y + h + j + k
	return (to)


@commands.guild_only()
@commands.has_role(961301374115676170)
@bot.command()
async def receipt3(ctx, arg: str, price: float, cur: str, *, typee: str):
	channel = bot.get_channel(961310467341549598)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
		embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
		embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
		embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
		embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
		embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
		embed.add_field(name="Command name", value="receipt3", inline=True)
		embed.set_footer(text='Logged')
		await channel.send(embed=embed)
		embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
		embed.set_author(name="Loading..",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif")
		embed.set_footer(text=f'Requested by {ctx.message.author}')
		mmm = await ctx.reply(embed=embed)
		price1 = cur + str(price)
		price2 = "Total: " + cur + str(price)
		type = typee + " (Clash of Clans)"
		if len(arg) == 9:
			mon = arg[0:3].lower().capitalize()
			day = arg[3:5]
			year = arg[5:]
			date = mon + ' ' + day + ', ' + year
		if len(arg) == 7:
			mon = arg[0:3].upper()
			day = arg[3:]

			date = mon + ' ' + day

		code2 = f"{getno()}" + f"{random.randint(0, 9)}"
		code = f"GPA.{getno()}-{getno()}-{getno()}-"
		# for i in range(2):
		#     code += random.choice(string.ascii_uppercase)
		# for i in range(7):
		#     x = random.randint(1, 2)
		#     if x == 1:
		#         code += random.choice(string.ascii_uppercase)
		#     else:
		#         y = random.randint(0, 9)
		#         if y == 7:
		#             y = 8
		#         code += str(y)
		layer1 = Image.open("blankrece.png").convert("RGBA")
		final = Image.new("RGBA", layer1.size)
		final.paste(layer1, (0, 0), layer1)
		fnt = ImageFont.truetype('aba.ttf', 26)
		d = ImageDraw.Draw(final)

		d.text((238, 419), code, font=fnt, fill=(96, 96, 98))
		f = ImageDraw.Draw(final)

		f.text((200, 499), date, font=fnt, fill=(96, 96, 98))
		p = ImageDraw.Draw(final)

		x = 441
		x2 = 371
		if len(price1) == 5:
			x = 452
			x2 = 382
		if len(price1) == 4:
			x = 465
			x2 = 395
		if len(price1) == 3:
			x = 474
			x2 = 404
		p.text((x, 723), price1, font=fnt, fill=(96, 96, 98))
		p2 = ImageDraw.Draw(final)

		p2.text((x2, 817), price2, font=fnt, fill=(96, 96, 98))
		p2 = ImageDraw.Draw(final)

		if len(type) > 28:
			typee = type[:29]
			typeee = type[29:]
			p2.text((72, 703), typee, font=fnt, fill=(96, 96, 98))
			p2 = ImageDraw.Draw(final)
			p2.text((72, 743), typeee, font=fnt, fill=(96, 96, 98))
		else:
			p2.text((72, 703), type, font=fnt, fill=(96, 96, 98))
			p2 = ImageDraw.Draw(final)

		p2.text((66, 459), code2, font=fnt, fill=(96, 96, 98))
		p2 = ImageDraw.Draw(final)

		p2.text((280, 933), "Google Play balance", font=fnt, fill=(96, 96, 98))
		p2 = ImageDraw.Draw(final)

		final.save("complete3.png", format="png")
		await ctx.send(file=discord.File('complete3.png'))
		embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
		embed.set_author(name="Process completed",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif")
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		await mmm.edit(embed=embed)


@receipt3.error
async def on_command_error(ctx, error):
  ######
  if isinstance(error, commands.MissingRole):
    em = discord.Embed(title="",description="DM <@920337055706386443> to buy the bot ez",timestamp=datetime.datetime.utcnow(),color=discord.Color.red())
    em.set_author(name="You can't use the bot commands",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png")
    em.set_footer(text=f"Command used by {ctx.message.author}")
    await ctx.send(embed=em)
  ######
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0xFF0000)
    embed.add_field(name="Usage",value="``+receipt3 <DATE> <AMOUNT> <CURRENCY SYMBOL> <TYPE>``",inline=False)
    embed.add_field(name="Example",value="``+receipt3 FEB072020 4.9 $ Gold Pass``",inline=False)
    embed.set_author(name="Invalid syntax",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png")
    embed.set_footer(text=f'Command used by {ctx.message.author}')
    await ctx.send(embed=embed)
  #######
  if isinstance(error, commands.CommandInvokeError):
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0xFF0000)
    embed.add_field(name="Usage",value="``+receipt3 <DATE> <AMOUNT> <CURRENCY SYMBOL> <TYPE>``",inline=False)
    embed.add_field(name="Example",value="``+receipt3 FEB072020 4.9 $ Gold Pass``",inline=False)
    embed.set_author(name="Invalid syntax",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png")
    embed.set_footer(text=f'Command used by {ctx.message.author}')
    await ctx.send(embed=embed)


@commands.guild_only()
@commands.has_role(961301374115676170)
@bot.command()
async def creation(ctx, tag: str):
  channel = bot.get_channel(961310467341549598)
  if ctx.guild.id == 961299028128190474:
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
    embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
    embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
    embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
    embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
    embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
    embed.add_field(name="Command name", value="creation", inline=True)
    embed.set_footer(text='Logged')
    await channel.send(embed=embed)
    player = await coc_client.get_player(tag)
    if '#' in tag:
      tag = tag.split('#')
      tag = tag[1]
    if len(tag) == 7:
      tag = '0' + tag
    if len(tag) == 9:
      tag = tag.lower()
      if tag.startswith('2'):
        date = 'Late 2014 - late 2015'
      if tag.startswith('8'):
        date = 'Early 2015 - mid 2015'
      if tag.startswith('9'):
        date = '2016'
      if tag.startswith('p'):
        date = 'Late 2016 - 2017'
      if tag.startswith('y'):
        date = 'Late 2017 - 2018'
      if tag.startswith('l'):
        date = 'Late 2018 - 2019'
      if tag.startswith('q'):
        date = '2020 - 2021'
    if len(tag) == 8:
      tag = tag.lower()
      if tag.startswith('2'):
        date = 'Late 2014 - late 2015'
      elif tag.startswith('8'):
        date = 'Early 2015 - mid 2015'
      else:
        date = 'Mid 2013 - 2014'
    if len(tag) <= 6:
      date = '2012'
    tag = tag.upper()
    embed = discord.Embed(title=f"{player.name} #{tag}",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
    embed.add_field(name="Account was created arround",value=f"{date}",inline=False)
    embed.set_footer(text=f"Requested by {ctx.message.author}")
    await ctx.reply(embed=embed)


@creation.error
async def on_command_error(ctx, error):
	######
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0xFF0000)
		embed.add_field(name="Usage",
		                value="``+creation <ACCOUNT TAG>``",
		                inline=False)
		embed.add_field(name="Example",
		                value="``+creation #YJUVGP2R2``",
		                inline=False)
		embed.set_author(
		    name="Invalid syntax",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png"
		)
		embed.set_footer(text=f'Command used by {ctx.message.author}')
		await ctx.send(embed=embed)
	######
	if isinstance(error, commands.CommandInvokeError):
		em = discord.Embed(title="",
		                   description="",
		                   timestamp=datetime.datetime.utcnow(),
		                   color=discord.Color.red())
		em.set_author(
		    name="Invalid tag",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)


@commands.cooldown(1, 10, commands.BucketType.user)
@commands.guild_only()
@commands.has_role(961301374115676170)
@bot.command()
async def devices(ctx, country: str, start: int, end: int):
	channel = bot.get_channel(961310467341549598)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0x00FF00)
		embed.set_author(
		    name="Command logs",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png"
		)
		embed.add_field(name="User",
		                value="{}".format(ctx.message.author),
		                inline=True)
		embed.add_field(name="User id",
		                value="{}".format(ctx.message.author.id),
		                inline=True)
		embed.add_field(name="Server name",
		                value="{}".format(ctx.message.guild.name),
		                inline=False)
		embed.add_field(name="Channel name",
		                value="{}".format(ctx.message.channel.mention),
		                inline=False)
		embed.add_field(name="Command name", value="devices", inline=True)
		embed.set_footer(text='Logged')
		await channel.send(embed=embed)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		embed.set_author(
		    name="Loading..",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif"
		)
		mmm = await ctx.reply(embed=embed)
		if country.lower() == 'usa' or country.lower() == 'us':
			country = 'united-states-of-america'
		if country.lower() == 'uk':
			country = 'united-kingdom'
		if country == 'united-kingdom':
			huh = 'GB'
			bong = 'United%20Kingdom'
		elif country == 'united-states-of-america':
			huh = 'US'
			bong = 'United%20States%20of%20America'
		else:
			bong = country.lower().capitalize()
			with open('country_code.json', 'r') as f:
				it = json.load(f)
				huh = it[bong]
				print(huh)

		x = []
		y = []
		url = f'https://gs.statcounter.com/vendor-market-share/mobile-tablet/chart.php?bar=1&device=Mobile%20%26%20Tablet&device_hidden=mobile%2Btablet&multi-device=true&statType_hidden=vendor&region_hidden={huh}&granularity=yearly&statType=Device%20Vendor&region={bong}&fromInt={start}&toInt={end}&fromYear={start}&toYear={end}&csv=1'
		df = pd.read_csv(url, on_bad_lines="skip")
		coll = []
		for col in df.columns:
			coll.append(col)
		for i in range(len(df['Device Vendor'])):
			x.append(df['Device Vendor'][i])
			y.append(df[f'{coll[1]}'][i]) 
		embed = discord.Embed(title=f'**Devices used yearly in {country}**',
		                      description=f'From year {start} to {end}',
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		for i in range(len(x)):
			embed.add_field(name=f'**{x[i]}**', value=f'{y[i]}%', inline=True)
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		await mmm.edit(embed=embed)

@devices.error
async def on_command_error(ctx, error):
	######
	if isinstance(error, commands.CommandOnCooldown):
		em = discord.Embed(
		    title="",
		    description=f"Try again in {error.retry_after:.2f}s.",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="Hold On",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.CommandInvokeError):
		em = discord.Embed(title="",
		                   description="",
		                   timestamp=datetime.datetime.utcnow(),
		                   color=discord.Color.red())
		em.set_author(
		    name="Invalid country name",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0xFF0000)
		embed.add_field(
		    name="Usage",
		    value=
		    "``+devices <country name lowercased> <FROM YEAR> <TO YEAR>``",
		    inline=False)
		embed.add_field(name="Example 1",
		                value="``+devices us 2014 2015``",
		                inline=False)
		embed.add_field(name="Example 2",
		                value="``+devices uk 2016 2018``",
		                inline=False)
		embed.add_field(name="Example 3",
		                value="``+devices japan 2013 2015``",
		                inline=False)
		embed.set_author(
		    name="Invalid syntax",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png"
		)
		embed.set_footer(text=f'Command used by {ctx.message.author}')
		await ctx.send(embed=embed)


@commands.cooldown(1, 5, commands.BucketType.user)
@commands.guild_only()
@commands.has_role(961301374115676170)
@bot.command()
async def androids(ctx, country: str):
	channel = bot.get_channel(961310467341549598)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0x00FF00)
		embed.set_author(
		    name="Command logs",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png"
		)
		embed.add_field(name="User",
		                value="{}".format(ctx.message.author),
		                inline=True)
		embed.add_field(name="User id",
		                value="{}".format(ctx.message.author.id),
		                inline=True)
		embed.add_field(name="Server name",
		                value="{}".format(ctx.message.guild.name),
		                inline=False)
		embed.add_field(name="Channel name",
		                value="{}".format(ctx.message.channel.mention),
		                inline=False)
		embed.add_field(name="Command name", value="androids", inline=True)
		embed.set_footer(text='Logged')
		await channel.send(embed=embed)

		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		embed.set_author(
		    name="Loading..",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif"
		)
		mmm = await ctx.reply(embed=embed)
		if country.lower() == 'usa' or country.lower() == 'us':
			country = 'united-states-of-america'
		if country.lower() == 'uk':
			country = 'united-kingdom'
		if country == 'united-kingdom':
			huh = 'gb'
		elif country == 'united-states-of-america':
			huh = 'us'
		else:
			bong = country.lower().capitalize()
			with open('country_code.json', 'r') as f:
				it = json.load(f)
				huh = it[bong]
				huh = huh.lower()
				print(huh)
		url = f"https://www.appbrain.com/stats/top-android-phones-tablets-by-country?country={huh}"
		data = requests.get(url)
		doc = BeautifulSoup(data.text, "html.parser")
		j = doc.find_all("script")[11]
		a = f"{j}"
		k = a.split("=")[4]
		p = k[10:]
		p = p.split(',"header"')
		p = p[0]
		with open("sample.json", "w") as outfile:
			outfile.write(p)
		f = open('sample.json')
		d = json.load(f)
		list = []
		for i in range(len(d)):
			list.append(d[i]["modelName"])
		line = '\n\n'.join(map(str, list))
		embed = discord.Embed(title="",
		                      description=f"```{line}```",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		embed.set_author(name=f"Mostly used android devices in {country}")
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		await ctx.reply(embed=embed)
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		embed.set_author(
		    name="Process completed",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif"
		)
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		await mmm.edit(embed=embed)


@androids.error
async def on_command_error(ctx, error):
	######
	if isinstance(error, commands.CommandOnCooldown):
		em = discord.Embed(
		    title="",
		    description=f"Try again in {error.retry_after:.2f}s.",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="Hold On",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.CommandInvokeError):
		em = discord.Embed(title="",
		                   description="",
		                   timestamp=datetime.datetime.utcnow(),
		                   color=discord.Color.red())
		em.set_author(
		    name="Invalid country name",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0xFF0000)
		embed.add_field(name="Usage",
		                value="``+androids <country name lowercased>``",
		                inline=False)
		embed.add_field(name="Example", value="``+androids us``", inline=False)
		embed.set_author(
		    name="Invalid syntax",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png"
		)
		embed.set_footer(text=f'Command used by {ctx.message.author}')
		await ctx.send(embed=embed)


@commands.guild_only()
@commands.has_role(961301374115676170)
@bot.command()
async def tags(ctx):
  channel = bot.get_channel(961310467341549598)
  if ctx.guild.id == 961299028128190474:
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
    embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
    embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
    embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
    embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
    embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
    embed.add_field(name="Command name", value="tags", inline=True)
    embed.set_footer(text='Logged')
    await channel.send(embed=embed)
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
    embed.set_author(name="Loading..",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif")
    mmm = await ctx.reply(embed=embed)
    foundtags = []
    foundth = []
    m = open('sorteddeadtags.json', 'r', encoding="utf8")
    data = json.load(m)
    len_data = len(data)
    for i in range(0, 10):
      s = random.randint(0, len_data)
      t = data[s]["tag"]
      tl = data[s]["th_level"]
      foundtags.append(t)
      foundth.append(tl)
    len_f = len(foundtags)
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
    embed.set_author(name="Dead Accounts",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif")
    for i in range(0, len_f):
      tag = foundtags[i]
      if '#' in tag:
        ntag = tag.replace('#', '')
        player = await coc_client.get_player(tag)
        thlvl = foundth[i]
        embed.add_field(name=f"**{player.name}**",value=f"Tag : {tag}\nTown Hall : {thlvl}\n[View in game](https://link.clashofclans.com/en?action=OpenPlayerProfile&tag={ntag})",inline=True)
    embed.set_footer(text=f"Requested by {ctx.message.author}")
    await mmm.edit(embed=embed)


@tags.error
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)


@commands.cooldown(1, 5, commands.BucketType.user)
@commands.guild_only()
@commands.has_role(961301374115676170)
@bot.command()
async def local(ctx, arg: str):
	channel = bot.get_channel(961310467341549598)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0x00FF00)
		embed.set_author(
		    name="Command logs",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png"
		)
		embed.add_field(name="User",
		                value="{}".format(ctx.message.author),
		                inline=True)
		embed.add_field(name="User id",
		                value="{}".format(ctx.message.author.id),
		                inline=True)
		embed.add_field(name="Server name",
		                value="{}".format(ctx.message.guild.name),
		                inline=False)
		embed.add_field(name="Channel name",
		                value="{}".format(ctx.message.channel.mention),
		                inline=False)
		embed.add_field(name="Command name", value="local", inline=True)
		embed.set_footer(text='Logged')
		await channel.send(embed=embed)
		player = await coc_client.get_player(f'{arg}')
		if '#' in arg:
			tag = arg.split('#')
			tag = tag[1]
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		embed.set_author(
		    name="Loading..",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif"
		)
		mmm = await ctx.reply(embed=embed)
		url = f"https://www.clashofstats.com/players/{tag}/history/"
		data = requests.get(url)
		doc = BeautifulSoup(data.text, "html.parser")
		lim = len(doc.find_all("div", class_="v-list-item__subtitle"))
		print(lim)
		embed = discord.Embed(
		    title="",
		    timestamp=datetime.datetime.utcnow(),
		    description=
		    f"**{player.name} {arg}**\nClick [here](https://www.clashofstats.com/players/{tag}/history/) to view player's clan history on COS.",
		    color=discord.Color.random())
		embed.set_author(
		    name="Local History",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png"
		)
		for i in range(0, lim):
			j = doc.find_all("div", class_="v-list-item__title")[4 + i].text
			kl = " ".join(j.split())
			l = doc.find_all("div", class_="v-list-item__subtitle")[i].text
			lo = "None"
			if '-' in kl:
				clantag = kl.split('#')
				clantag = "#" + f"{clantag[len(clantag)-1]}"
				clan = await coc_client.get_clan(clantag)
				lo = clan.location
				embed.add_field(
				    name=f'{clan.name} {clan.tag}',
				    value=
				    f'Location : {lo}\nTotal stay : {" ".join(l.split())}',
				    inline=False)
			else:
				embed.add_field(
				    name=f'{j}',
				    value=
				    f'Location : {lo}\nTotal stay : {" ".join(l.split())}',
				    inline=False)
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		await ctx.reply(embed=embed)
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		embed.set_author(
		    name="Process completed",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif"
		)
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		await mmm.edit(embed=embed)


@local.error
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.CommandInvokeError):
		em = discord.Embed(title="",
		                   description="",
		                   timestamp=datetime.datetime.utcnow(),
		                   color=discord.Color.red())
		em.set_author(
		    name="No local history available for this tag",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.CommandOnCooldown):
		em = discord.Embed(
		    title="",
		    description=f"Try again in {error.retry_after:.2f}s.",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="Hold On",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0xFF0000)
		embed.add_field(name="Usage", value="``+local <TAG>``", inline=False)
		embed.add_field(name="Example",
		                value="``+local #QCU28LPV``",
		                inline=False)
		embed.set_author(
		    name="Invalid syntax",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png"
		)
		embed.set_footer(text=f'Command used by {ctx.message.author}')
		await ctx.send(embed=embed)


@commands.cooldown(1, 10, commands.BucketType.user)
@commands.guild_only()
@commands.has_role(961301374115676170)
@bot.command()
async def lastsession(ctx, arg: str):
  channel = bot.get_channel(961310467341549598)
  if ctx.guild.id == 961299028128190474:
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
    embed.set_author( name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
    embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
    embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
    embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
    embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
    embed.add_field(name="Command name", value="lastsession", inline=True)
    embed.set_footer(text='Logged')
    await channel.send(embed=embed)
    if '#' in arg:
      tag = arg.split('#')
      tag = tag[1]
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
    embed.set_author(name="Loading..",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif")
    mmm = await ctx.reply(embed=embed)
    player = await coc_client.get_player(f'{arg}')
    list = []
    url = f"https://www.clashofstats.com/players/{tag}/history/progress-log/"
    data = requests.get(url)
    doc = BeautifulSoup(data.text, "html.parser")
    lim = len(doc.find_all("h3", class_="subsection-title"))
    if lim >= 1:
        list.append("\n**Home Village**")
        if lim > 3:
            lim = 3
        for i in range(0,lim):
            list.append(doc.find_all("h3", class_="subsection-title")[i].text)
    url = f"https://www.clashofstats.com/players/{tag}/history/progress-log/builder-base"
    data = requests.get(url)
    doc = BeautifulSoup(data.text, "html.parser")
    lim = len(doc.find_all("h3", class_="subsection-title"))
    if lim >= 1:
        list.append("\n**Builder Base**")
        if lim > 3:
            lim = 3
        for i in range(0,lim):
            list.append(doc.find_all("h3", class_="subsection-title")[i].text)
    if len(list) !=0:
      line = '\n'.join(map(str, list))
      embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),description=f"**{player.name} {arg}**\n{line}",color=discord.Color.random())
      embed.set_author(name="Last Session",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
      embed.set_footer(text=f"Requested by {ctx.message.author}")
      await mmm.edit(embed=embed)
    else:
      em = discord.Embed(title="",description="",timestamp=datetime.datetime.utcnow(),color=discord.Color.red())
      em.set_author(name="No last session available for this tag",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png")
      em.set_footer(text=f"Command used by {ctx.message.author}")
      await mmm.edit(embed=em)
    # embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),description=f"**{player.name} {arg}**",color=discord.Color.random())
    # embed.set_author(name="Last Session",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
    # try:
    #   url = f"https://www.clashofstats.com/players/{tag}/history/progress-log/"
    #   data = requests.get(url)
    #   doc = BeautifulSoup(data.text, "html.parser")
    #   j1 = doc.find_all("h3", class_="subsection-title")[0].text
    #   embed.add_field(name='Last session for Home Village',value=f'{j1}',inline=False)
    # except:
    #   url = f"https://www.clashofstats.com/players/{tag}/history/progress-log/builder-base"
    #   data = requests.get(url)
    #   doc = BeautifulSoup(data.text, "html.parser")
    #   j1 = doc.find_all("h3", class_="subsection-title")[0].text
    #   embed.add_field(name='Last session for Builder Base',value=f'{j1}',inline=False)
    # embed.set_footer(text=f"Requested by {ctx.message.author}")
    # await ctx.reply(embed=embed)
    # embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
    # embed.set_author(name="Process completed",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif")
    # embed.set_footer(text=f"Requested by {ctx.message.author}")
    # await mmm.edit(embed=embed)


@lastsession.error
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.CommandInvokeError):
		em = discord.Embed(title="",
		                   description="",
		                   timestamp=datetime.datetime.utcnow(),
		                   color=discord.Color.red())
		em.set_author(
		    name="No last session available for this tag",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.CommandOnCooldown):
		em = discord.Embed(
		    title="",
		    description=f"Try again in {error.retry_after:.2f}s.",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="Hold On",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0xFF0000)
		embed.add_field(name="Usage",
		                value="``+lastsession <TAG>``",
		                inline=False)
		embed.add_field(name="Example",
		                value="``+lastsession #QCU28LPV``",
		                inline=False)
		embed.set_author(
		    name="Invalid syntax",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png"
		)
		embed.set_footer(text=f'Command used by {ctx.message.author}')
		await ctx.send(embed=embed)


contents = [
    "**2012**\n📲 iPhone 4, iPad and iPhone 5.\n\n⚠️ Keep in mind that the account(s) could have more devices.",
    "**2013**\n📲 iPhone 5, iPad and if it has 2014 trees: iPhone 6.\n\n⚠️ Keep in mind that the account(s) could have more devices.",
    "**2014**\n📲 iPhone 5 (Try iPhone 6 and iPad first), iPad Air, iPhone 6.\n\n⚠️ Keep in mind that the account(s) could have more devices.",
    "**2015**\n📲 iPhone 6, iPad Mini/Air.\n\n⚠️ Keep in mind that the account(s) could have more devices.",
    "**2016**\n📲 iPhone 6S, iPad Air/Mini, try iPhone 7 if the account was created in Late 2016. (September/October)\n\n⚠️ Keep in mind that the account(s) could have more devices.",
    "**2017**\n📲 iPhone 7, iPad Pro, try iPhone 8 and X if the account was created in Late 2017. (September/October)\n\n⚠️ Keep in mind that the account(s) could have more devices.",
    "**2018**\n📲 iPhone 8, iPhone X, iPad Pro, try iPhone XS/XR if the account was created in Late 2018. (October/November)\n\n⚠️ Keep in mind that the account(s) could have more devices."
]


@commands.guild_only()
@commands.has_role(961301374115676170)
@bot.command()
async def appledevs(ctx):
	channel = bot.get_channel(961310467341549598)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0x00FF00)
		embed.set_author(
		    name="Command logs",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png"
		)
		embed.add_field(name="User",
		                value="{}".format(ctx.message.author),
		                inline=True)
		embed.add_field(name="User id",
		                value="{}".format(ctx.message.author.id),
		                inline=True)
		embed.add_field(name="Server name",
		                value="{}".format(ctx.message.guild.name),
		                inline=False)
		embed.add_field(name="Channel name",
		                value="{}".format(ctx.message.channel.mention),
		                inline=False)
		embed.add_field(name="Command name", value="appledevs", inline=True)
		embed.set_footer(text='Logged')
		await channel.send(embed=embed)
		pages = 7
		cur_page = 1
		hellp = discord.Embed(title="📲 Apple Devices",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		hellp.set_footer(text=f"Requested by {ctx.message.author}")
		hellp.add_field(
		    name=f"🗒 Apple Devices for year »",
		    value=f"\n{contents[cur_page-1]}\n\n**Page {cur_page}/{pages}**",
		    inline=False)
		message = await ctx.reply(embed=hellp)
		await message.add_reaction("◀️")
		await message.add_reaction("▶️")

		def check(reaction, user):
			return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

		while True:
			try:
				reaction, user = await bot.wait_for("reaction_add",
				                                    timeout=60,
				                                    check=check)
				if str(reaction.emoji) == "▶️" and cur_page != pages:
					cur_page += 1
					hellp = discord.Embed(title="📲 Apple Devices",
					                      timestamp=datetime.datetime.utcnow(),
					                      color=discord.Color.random())
					hellp.set_footer(text=f"Requested by {ctx.message.author}")
					hellp.add_field(
					    name=f"🗒 Apple Devices for year »",
					    value=
					    f"\n{contents[cur_page-1]}\n\n**Page {cur_page}/{pages}**",
					    inline=False)
					await message.edit(embed=hellp)
					await message.remove_reaction(reaction, user)
				elif str(reaction.emoji) == "◀️" and cur_page > 1:
					cur_page -= 1
					hellp = discord.Embed(title="📲 Apple Devices",
					                      timestamp=datetime.datetime.utcnow(),
					                      color=discord.Color.random())
					hellp.set_footer(text=f"Requested by {ctx.message.author}")
					hellp.add_field(
					    name=f"🗒 Apple Devices for year »",
					    value=
					    f"\n{contents[cur_page-1]}\n\n**Page {cur_page}/{pages}**",
					    inline=False)
					await message.edit(embed=hellp)
					await message.remove_reaction(reaction, user)
				else:
					await message.remove_reaction(reaction, user)
			except asyncio.TimeoutError:
				await message.clear_reactions()
				break


@appledevs.error
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)


skinss = [
    "**Year 2019**\n\n**Gladiator King**\nSeason : April 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Gladiator Queen**\nSeason : May 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**P.E.K.K.A King**\nSeason : June 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Valkyrie Queen**\nSeason : July 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Party Warden**\nSeason : August 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Autumn Queen**\nSeason : September 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Skeleton King**\nSeason : October 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Ice Queen**\nSeason : November 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Jolly King**\nSeason : December 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌",
    "**Year 2020**\n\n**Primal Warden**\nSeason : January 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Warrior Queen¹**\nSeason : January 2020 / February 2021 / February 2022\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Primal King**\nSeason : February 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Primal Queen**\nSeason : March 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Clockwork Warden**\nSeason : April 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Clockwork King**\nSeason : May 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Clockwork Queen**\nSeason : June 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Gladiator Warden**\nSeason : July 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Party King**\nSeason : August 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Pirate Queen**\nSeason : September 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Pirate Warden**\nSeason : October 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Champion King²**\nSeason : October 2020 / November 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Pirate King**\nSeason : November 202\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Winter Champion**\nSeason : December 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌",
    "**Year 2021**\n\n**Warden of the North**\nSeason : January 2021\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Rogue Queen**\nSeason : February 2021\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Warrior King³**\nSeason : February 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Rogue King**\nSeason : March 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Jungle Champion4**\nSeason : April 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Jungle Warden**\nSeason : May 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Jungle Queen**\nSeason : June 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Fierce King5**\nSeason : June 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Jungle King**\nSeason : July 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Party Queen**\nSeason : August 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Beat King6**\nSeason : August 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Gladiator Champion**\nSeason : September 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Warden Maste**\nSeason : October 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Golem King**\nSeason : November 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Champion Queen7**\nSeason : November 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Jolly Warden**\nSeason : December 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Ice King**\nSeason : December 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅",
    "**Year 2022**\n\n**Shadow Queen**\nSeason : January 2022\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Lunar King9³**\nSeason : February 2022\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Warrior Warden**\nSeason : February 2022\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Shadow Champion**\nSeason : March 2022\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Primal Champion10**\nSeason : March 2022\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Shadow King**\nSeason : April 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Shadow Warden11**\nSeason : April 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅"
]


@commands.guild_only()
@commands.has_role(961301374115676170)
@bot.command()
async def skins(ctx):
	channel = bot.get_channel(961310467341549598)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0x00FF00)
		embed.set_author(
		    name="Command logs",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png"
		)
		embed.add_field(name="User",
		                value="{}".format(ctx.message.author),
		                inline=True)
		embed.add_field(name="User id",
		                value="{}".format(ctx.message.author.id),
		                inline=True)
		embed.add_field(name="Server name",
		                value="{}".format(ctx.message.guild.name),
		                inline=False)
		embed.add_field(name="Channel name",
		                value="{}".format(ctx.message.channel.mention),
		                inline=False)
		embed.add_field(name="Command name", value="skins", inline=True)
		embed.set_footer(text='Logged')
		await channel.send(embed=embed)
		pages = 4
		cur_page = 1
		embed = discord.Embed(
		    title="Skins Information",
		    description=
		    f"\n{skinss[cur_page-1]}\n\n**Page {cur_page}/{pages}**",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.random())
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		message = await ctx.reply(embed=embed)
		await message.add_reaction("◀️")
		await message.add_reaction("▶️")

		def check(reaction, user):
			return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

		while True:
			try:
				reaction, user = await bot.wait_for("reaction_add",
				                                    timeout=60,
				                                    check=check)
				if str(reaction.emoji) == "▶️" and cur_page != pages:
					cur_page += 1
					embed = discord.Embed(
					    title="Skins Information",
					    description=
					    f"\n{skinss[cur_page-1]}\n\n**Page {cur_page}/{pages}**",
					    timestamp=datetime.datetime.utcnow(),
					    color=discord.Color.random())
					embed.set_footer(text=f"Requested by {ctx.message.author}")
					await message.edit(embed=embed)
					await message.remove_reaction(reaction, user)
				elif str(reaction.emoji) == "◀️" and cur_page > 1:
					cur_page -= 1
					embed = discord.Embed(
					    title="Skins Information",
					    description=
					    f"\n{skinss[cur_page-1]}\n\n**Page {cur_page}/{pages}**",
					    timestamp=datetime.datetime.utcnow(),
					    color=discord.Color.random())
					embed.set_footer(text=f"Requested by {ctx.message.author}")
					await message.edit(embed=embed)
					await message.remove_reaction(reaction, user)
				else:
					await message.remove_reaction(reaction, user)
			except asyncio.TimeoutError:
				await message.clear_reactions()
				break


@skins.error
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)


# @bot.command()
# async def test(ctx):
#   em = discord.Embed(
#       title="",
#       description="```hdbfhjbda jhabdfuhaif ujsdhafuhucivuhjf jahduhndjvn jhauidfjniue ijhdufhuiahfe ukhdfuiheuf uhjeudfihsdfhnuhef jdhfuhunjf uefhujnf jehfuidfui sdfheuifhnu jhsefjioefb fjehfeuifn jehuiefh efifjieufh UEFHEFHEUFKJ UEFHUIDFHN JUEFHUEF  UEFHEIFUKH EUFUEFUI HEBFUH JDFHUEF JUefhiuefu```",
#       timestamp=datetime.datetime.utcnow(),
#       color=discord.Color.red())
#   em.set_author(
#       name="You can't use the bot commands",
#       icon_url=
#       "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
#   )
#   em.set_footer(text=f"Command used by {ctx.message.author}")
#   await ctx.send(embed=em)

@commands.has_role(961301374115676170)
@bot.command()
@commands.guild_only()
async def tempemails(ctx):
	channel = bot.get_channel(961310467341549598)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0x00FF00)
		embed.set_author(
		    name="Command logs",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png"
		)
		embed.add_field(name="User",
		                value="{}".format(ctx.message.author),
		                inline=True)
		embed.add_field(name="User id",
		                value="{}".format(ctx.message.author.id),
		                inline=True)
		embed.add_field(name="Server name",
		                value="{}".format(ctx.message.guild.name),
		                inline=False)
		embed.add_field(name="Channel name",
		                value="{}".format(ctx.message.channel.mention),
		                inline=False)
		embed.add_field(name="Command name", value="tempemails", inline=True)
		embed.set_footer(text='Logged')
		await channel.send(embed=embed)
		url = "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=5"
		r = requests.get(url)
		h = r.json()
		embed = discord.Embed(
		    title="",
		    description=f"```{h[0]}\n\n{h[1]}\n\n{h[2]}\n\n{h[3]}\n\n{h[4]}```",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.random())
		embed.set_author(
		    name="Generated some temp emails",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif"
		)
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		await ctx.reply(embed=embed)


# @tempemails.error
# async def on_command_error(ctx, error):
# 	######
# 	if isinstance(error, commands.MissingRole):
# 		em = discord.Embed(
# 		    title="",
# 		    description="DM <@920337055706386443> to buy the bot ez",
# 		    timestamp=datetime.datetime.utcnow(),
# 		    color=discord.Color.red())
# 		em.set_author(
# 		    name="You can't use the bot commands",
# 		    icon_url=
# 		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
# 		)
# 		em.set_footer(text=f"Command used by {ctx.message.author}")
# 		await ctx.send(embed=em)


@commands.has_role(961301374115676170)
@bot.command()
@commands.guild_only()
async def inbox(ctx, email: str):
	channel = bot.get_channel(961310467341549598)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0x00FF00)
		embed.set_author(
		    name="Command logs",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png"
		)
		embed.add_field(name="User",value="{}".format(ctx.message.author),
		                inline=True)
		embed.add_field(name="User id",
		                value="{}".format(ctx.message.author.id),
		                inline=True)
		embed.add_field(name="Server name",
		                value="{}".format(ctx.message.guild.name),
		                inline=False)
		embed.add_field(name="Channel name",
		                value="{}".format(ctx.message.channel.mention),
		                inline=False)
		embed.add_field(name="Command name", value="inbox", inline=True)
		embed.set_footer(text='Logged')
		await channel.send(embed=embed)
		ema = email.split("@")
		l = ema[0]
		d = ema[1]
		url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={l}&domain={d}"
		r = requests.get(url)
		h = r.json()
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		embed.set_author(
		    name=f"Last mail in inbox of {email}",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif"
		)
		embed.add_field(name="Sender's email",
		                value=f"{h[0]['from']}",
		                inline=False)
		embed.add_field(name="Subject",
		                value=f"{h[0]['subject']}",
		                inline=False)
		embed.add_field(
		    name="Date & Time",
		    value=
		    f"{h[0]['date']}\n\n**React with  💬  to see the body of email**",
		    inline=False)
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		mmm = await ctx.reply(embed=embed)
		await mmm.add_reaction("💬")

		def check(reaction, user):
			return user == ctx.author and str(reaction.emoji) in ["💬"]

		while True:
			try:
				reaction, user = await bot.wait_for("reaction_add",
				                                    timeout=60,
				                                    check=check)
				if str(reaction.emoji) == "💬":
					url2 = f"https://www.1secmail.com/api/v1/?action=readMessage&login={l}&domain={d}&id={h[0]['id']}"
					r2 = requests.get(url2)
					h2 = r2.json()
					embed = discord.Embed(
					    title="Body of email",
					    description=f"```{h2['textBody']}```",
					    timestamp=datetime.datetime.utcnow(),
					    color=discord.Color.random())
					embed.set_footer(text=f"Requested by {ctx.message.author}")
					await mmm.edit(embed=embed)
					await mmm.clear_reactions()
				else:
					await mmm.remove_reaction(reaction, user)
			except asyncio.TimeoutError:
				await mmm.clear_reactions()
				break


@inbox.error
async def on_command_error(ctx, error):
	######
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.CommandInvokeError):
		em = discord.Embed(title="",
		                   description="",
		                   timestamp=datetime.datetime.utcnow(),
		                   color=discord.Color.red())
		em.set_author(
		    name="Invalid email",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0xFF0000)
		embed.add_field(name="Usage",
		                value="``+inbox <tempemail>``",
		                inline=False)
		embed.add_field(name="Example ",
		                value="``+inbox bhdhvbha@yahoo.com``",
		                inline=False)
		embed.set_author(
		    name="Invalid syntax",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png"
		)
		embed.set_footer(text=f'Command used by {ctx.message.author}')
		await ctx.send(embed=embed)


@commands.has_role(961301374115676170)
@bot.command()
@commands.guild_only()
async def info(ctx, tag: str):
  channel = bot.get_channel(961310467341549598)
  if ctx.guild.id == 961299028128190474:
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
    embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
    embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
    embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
    embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
    embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
    embed.add_field(name="Command name", value="info", inline=True)
    embed.set_footer(text='Logged')
    await channel.send(embed=embed)
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
    embed.set_author(name="Loading..",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif")
    mmm = await ctx.reply(embed=embed)
    player = await coc_client.get_player(tag)
    clanname = player.clan
    if player.clan == None:
      clanname = "Not in clan"
      clantag = "None"
    else:
      clantag =  player.clan.tag
    e = discord.Embed(title=f"{player.name} {player.tag}",description=f"**Town hall level :** {player.town_hall}\n**XP Level :** {player.exp_level}\n**War stars :** {player.war_stars}\n**Clan name :** {clanname}\n**Clan tag :** {clantag}",timestamp=datetime.datetime.utcnow(),colour=discord.Colour.random())
    l = player.league.icon.url
    if l == None:
      l = "https://cdn.discordapp.com/attachments/936276886852603945/971646122210787379/e--YMyIexEQQhE4imLoJcwhYn6Uy8KqlgyY3_kFV6t4.png"
    e.set_thumbnail(url=l)
    e.add_field(name="Town hall weapon level",value=player.town_hall_weapon,inline=False)
    e.add_field(name="Attack wins", value=player.attack_wins, inline=True)
    e.add_field(name="Defence wins", value=player.defense_wins,inline=True)
    e.add_field(name="Donation given",value=player.donations,inline=False)
    e.add_field(name="Donation received",value=player.received,inline=False)
    e.add_field(name="All time best",value=player.best_trophies,inline=False)
    try:
      e.add_field(name="Legend trophies",value=player.legend_statistics.legend_trophies,inline=False)
    except:
      e.add_field(name="Legend trophies",value="0 legend trophies",inline=False)
    if "#" in tag:
      tag1 = tag.replace("#","")
    url = f"https://www.clashofstats.com/players/{tag1}/summary"
    data = requests.get(url)
    doc = BeautifulSoup(data.text, "html.parser")
    her = doc.find_all("span",class_="progress-list__value")[0].text
    oes = doc.find_all("span",class_="small-secondary-text")[0].text
    heroes = her + oes
    tro = doc.find_all("span",class_="progress-list__value")[1].text
    ops = doc.find_all("span",class_="small-secondary-text")[1].text
    troops = tro + ops
    spe = doc.find_all("span",class_="progress-list__value")[2].text
    lls = doc.find_all("span",class_="small-secondary-text")[2].text
    spells = spe + lls
    bbhero1 = doc.find_all("span",class_="progress-list__value")[3].text
    bbhero2 = doc.find_all("span",class_="small-secondary-text")[3].text
    bbhero = bbhero1 + bbhero2
    bbtro = doc.find_all("span",class_="progress-list__value")[4].text
    bbops = doc.find_all("span",class_="small-secondary-text")[4].text
    bbtroops = bbtro + bbops
    heromoji = get(ctx.message.guild.emojis, name="heroes")
    troopmoji = get(ctx.message.guild.emojis, name="troop")
    spemoji = get(ctx.message.guild.emojis, name="spell")
    bbtroopmoji = get(ctx.message.guild.emojis, name="bbtroop")
    bbheromoji = get(ctx.message.guild.emojis, name="bbhero")
    e.add_field(name="Home Village", value=f'**{heromoji}Heroes** ``{heroes.replace(" ", "")}``\n**{troopmoji}Troops** ``{troops.replace(" ", "")}``\n**{spemoji}Spells** ``{spells.replace(" ", "")}``',inline=False)
    e.add_field(name="Builder Base", value=f'**{bbheromoji}Battle Machine** ``{bbhero.replace(" ", "")}``\n**{bbtroopmoji}Troops** ``{bbtroops.replace(" ", "")}``',inline=True)
    e.add_field(name="Links", value=f"[Open in game]({player.share_link})\n[Clash of Stats]({url})",inline=False)
    e.set_footer(text=f"Requested by {ctx.message.author}")
    await mmm.edit(embed=e)

@commands.has_role(961301374115676170)
@bot.command()
@commands.guild_only()
async def getacc(ctx, season: str, rank: int):
  channel = bot.get_channel(961310467341549598)
  if ctx.guild.id == 961299028128190474:
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
    embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
    embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
    embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
    embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
    embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
    embed.add_field(name="Command name", value="getacc", inline=True)
    embed.set_footer(text='Logged')
    await channel.send(embed=embed)
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
    embed.set_author(name="Loading..",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif")
    embed.set_footer(text=f'Requested by {ctx.message.author}')
    mmm = await ctx.reply(embed=embed)
    page = rank/200
    check_float = isinstance(page, float)
    if check_float is True:
      page = math.ceil(page)   
    url = f"https://clashspot.net/en/rankings/players-legend-league/season/{season}/players?p={page}"
    data1 = requests.get(f"https://clashspot.net/en/rankings/players-legend-league/season/{season}/players")
    doc1 = BeautifulSoup(data1.text, "html.parser")
    limit = doc1.find_all("strong")[0].text.replace(",","").replace(" players","")
    if rank>int(limit):
      embed = discord.Embed(title=f"Last rank of season ``{season}`` is ``{limit}``!",timestamp=datetime.datetime.utcnow(),color=discord.Color.red())
      await ctx.reply(embed=embed)
    else:
      data = requests.get(url)
      doc = BeautifulSoup(data.text, "html.parser")
      findrank = doc.find_all("td",class_="col-position")
      for i in range(len(findrank)):
        if findrank[i].text.strip().replace(",","").replace(".","") == f"{rank}":
          player = await coc_client.get_player(doc.find_all("span",class_="player-tag")[i].text)
          clanname = player.clan
          if player.clan == None:
            clanname = "Not in clan"
            clantag = "None"
          else:
            clantag =  player.clan.tag
          e = discord.Embed(title=f"{player.name} {player.tag}",description=f"**Season :** ``{season}`` **Rank : ** ``{rank}``\n**Town hall level :** {player.town_hall}\n**XP Level :** {player.exp_level}\n**War stars :** {player.war_stars}\n**Clan name :** {clanname}\n**Clan tag :** {clantag}",timestamp=datetime.datetime.utcnow(),colour=discord.Colour.random())
          l = player.league.icon.url
          if l == None:
            l = "https://cdn.discordapp.com/attachments/936276886852603945/971646122210787379/e--YMyIexEQQhE4imLoJcwhYn6Uy8KqlgyY3_kFV6t4.png"
          e.set_thumbnail(url=l)
          e.add_field(name="Town hall weapon level",value=player.town_hall_weapon,inline=False)
          e.add_field(name="Attack wins", value=player.attack_wins, inline=True)
          e.add_field(name="Defence wins", value=player.defense_wins,inline=True)
          e.add_field(name="Donation given",value=player.donations,inline=False)
          e.add_field(name="Donation received",value=player.received,inline=False)
          e.add_field(name="All time best",value=player.best_trophies,inline=False)
          try:
            e.add_field(name="Legend trophies",value=player.legend_statistics.legend_trophies,inline=False)
          except:
            e.add_field(name="Legend trophies",value="0 legend trophies",inline=False)
          if "#" in player.tag:
            tag1 = player.tag.replace("#","")
          e.add_field(name="Links", value=f"[Open in game]({player.share_link})\n[Clash of Stats]({url})",inline=False)
          e.set_footer(text=f"Requested by {ctx.message.author}")
          await mmm.edit(embed=e)

@getacc.error
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.CommandInvokeError):
		em = discord.Embed(title="",
		                   description="The specified season could be wrong or The player have been banned",
		                   timestamp=datetime.datetime.utcnow(),
		                   color=discord.Color.red())
		em.set_author(
		    name="ERROR",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0xFF0000)
		embed.add_field(name="Usage", value="``+getacc <SEASON> <RANK>``", inline=False)
		embed.add_field(name="Example",
		                value="``+getacc 2017-05 5``",
		                inline=False)
		embed.set_author(
		    name="Invalid syntax",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png"
		)
		embed.set_footer(text=f'Command used by {ctx.message.author}')
		await ctx.send(embed=embed)
  
@info.error
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.CommandInvokeError):
		em = discord.Embed(title="",
		                   description="",
		                   timestamp=datetime.datetime.utcnow(),
		                   color=discord.Color.red())
		em.set_author(
		    name="Invalid tag",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0xFF0000)
		embed.add_field(name="Usage", value="``+info <TAG>``", inline=False)
		embed.add_field(name="Example",
		                value="``+info #2PYPP02Q``",
		                inline=False)
		embed.set_author(
		    name="Invalid syntax",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png"
		)
		embed.set_footer(text=f'Command used by {ctx.message.author}')
		await ctx.send(embed=embed)


# @commands.cooldown(1, 5, commands.BucketType.default)
# @commands.has_role(961301374115676170)
# @bot.command()
# @commands.guild_only()
# async def troops(ctx, tag: str):
#   channel = bot.get_channel(961310467341549598)
#   if ctx.guild.id == 961299028128190474:
#     embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
#     embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
#     embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
#     embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
#     embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
#     embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
#     embed.add_field(name="Command name", value="troops", inline=True)
#     embed.set_footer(text='Logged')
#     await channel.send(embed=embed)
#     p = discord.Embed(title="",timestamp=datetime.datetime.utcnow(), color=discord.Color.random())
#     p.set_author(name="Loading..",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif")
#     mmm = await ctx.reply(embed=p)
#     player = await coc_client.get_player(tag)
#     if '#' in tag:
#       tag1 = tag.split('#')
#       tag1 = tag1[1]
#     else:
#       tag1 = tag
#     option = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(executable_path="BraveSoftware/Brave-Browser/Application/brave.exe", options=option)
#     driver.maximize_window()
    
#     driver.get(f'https://www.clashofstats.com/players/{tag1}/army#tabs')
#     time.sleep(1)
#     driver.execute_script("window.scrollBy(0,50)", "")
#     time.sleep(1)
#     driver.get_screenshot_as_file("troops1.png")
#     driver.quit()
#     im = Image.open('troops1.png')
    
#     width, height = im.size
    
#     left = 0
#     top = 0
#     right = 784
#     bottom = 533
#     im1 = im.crop((left, top, right, bottom))
#     im1 = im1.save("troops1.png")
#     e = discord.Embed(title=f"{player.name} {player.tag}",description="**Troops**",colour=discord.Colour.random())
    
#     file = discord.File("troops1.png", filename="troops1.png")
#     e.set_image(url="attachment://troops1.png")
#     await ctx.send(file=file, embed=e)
#     embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
#     embed.set_author(name="Process completed",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif")
#     embed.set_footer(text=f"Requested by {ctx.message.author}")
#     await mmm.edit(embed=embed)


# @troops.error
# async def on_command_error(ctx, error):
# 	if isinstance(error, commands.MissingRole):
# 		em = discord.Embed(
# 		    title="",
# 		    description="DM <@920337055706386443> to buy the bot ez",
# 		    timestamp=datetime.datetime.utcnow(),
# 		    color=discord.Color.red())
# 		em.set_author(
# 		    name="You can't use the bot commands",
# 		    icon_url=
# 		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
# 		)
# 		em.set_footer(text=f"Command used by {ctx.message.author}")
# 		await ctx.send(embed=em)
# 	if isinstance(error, commands.CommandInvokeError):
# 		em = discord.Embed(title="",
# 		                   description="",
# 		                   timestamp=datetime.datetime.utcnow(),
# 		                   color=discord.Color.red())
# 		em.set_author(
# 		    name="Invalid tag",
# 		    icon_url=
# 		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
# 		)
# 		em.set_footer(text=f"Command used by {ctx.message.author}")
# 		await ctx.send(embed=em)
# 	if isinstance(error, commands.MissingRequiredArgument):
# 		embed = discord.Embed(title="",
# 		                      timestamp=datetime.datetime.utcnow(),
# 		                      color=0xFF0000)
# 		embed.add_field(name="Usage", value="``+troops <TAG>``", inline=False)
# 		embed.add_field(name="Example",
# 		                value="``+troops #2PYPP02Q``",
# 		                inline=False)
# 		embed.set_author(
# 		    name="Invalid syntax",
# 		    icon_url=
# 		    "https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png"
# 		)
# 		embed.set_footer(text=f'Command used by {ctx.message.author}')
# 		await ctx.send(embed=embed)
# 	if isinstance(error, commands.CommandOnCooldown):
# 		em = discord.Embed(
# 		    title="",
# 		    description=f"Try again in {error.retry_after:.2f}s.",
# 		    timestamp=datetime.datetime.utcnow(),
# 		    color=discord.Color.red())
# 		em.set_author(
# 		    name="Hold On",
# 		    icon_url=
# 		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
# 		)
# 		em.set_footer(text=f"Command used by {ctx.message.author}")
# 		await ctx.send(embed=em)
# @bot.event
# async def on_message(message):
#   if "phish" in message.content:
#     await message.delete()
#     mmm = await message.channel.send("Don't mention 🎣 type of word again!")
#     await asyncio.sleep(2)
#     await mmm.delete()


# Owner commands #
    
@commands.has_role(961330754539888670)
@bot.command()
@commands.guild_only()
async def cdt(ctx):
  m = open("sorteddeadtags.json","r",encoding="utf8")
  data = json.load(m)
  await ctx.reply(f"Total dead tags in database : {len(data)}")

@commands.has_role(961330754539888670)
@bot.command()
@commands.guild_only()
async def restart(ctx):
  channel = bot.get_channel(961310467341549598)
  if ctx.guild.id == 961299028128190474:
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
    embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
    embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
    embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
    embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
    embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
    embed.add_field(name="Command name", value="restart", inline=True)
    embed.set_footer(text='Logged')
    await channel.send(embed=embed)
    em = discord.Embed(title="Restarting...",description=f"",timestamp=datetime.datetime.utcnow(),color=discord.Color.red())
    em.set_footer(text=f"Command used by {ctx.message.author}")
    await ctx.reply(embed=em)
    system("python restarter.py")
    system('kill 1')

@commands.has_role(961330754539888670)
@bot.command(name="cc")
@commands.guild_only()
import discord
import random
import time
import logging
import coc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from coc import utils
import pandas as pd
import json
import datetime
from PIL import Image, ImageOps, ImageDraw, ImageFont
from discord.ext import commands, tasks
from discord.utils import get
from discord import Client
from discord import Guild
import os
from os import system
import asyncio
import functools
import itertools
import math
from async_timeout import timeout
import aiohttp
import urllib.parse
import inspect
from bs4 import BeautifulSoup
import sys
import numpy as np
import webbrowser
import base64
from io import BytesIO
from urllib.request import urlopen
from urllib.parse import urlencode
import string
from urllib.request import urlretrieve
from datetime import date, timedelta
import dns
import requests
import pymongo
from pymongo import MongoClient

coc_client = coc.login(
    os.environ['DEV_EMAIL'],
    os.environ['DEV_PASS'],
    key_names="coc.py tests99998",
    client=coc.EventsClient,
)
logging.basicConfig(level=logging.ERROR)

cluster1 = MongoClient("mongodb+srv://OTTO:OTTOdb@cluster0.aoshtcx.mongodb.net/?retryWrites=true&w=majority")
cluster2 = MongoClient("mongodb+srv://OTTO2:OTTOdb@cluster0.mr1zn5l.mongodb.net/?retryWrites=true&w=majority")
cluster3 = MongoClient("mongodb+srv://OTTO:OTTOdb@cluster0.btpxwn9.mongodb.net/?retryWrites=true&w=majority")
cluster4 = MongoClient("mongodb+srv://OTTO4:OTTOdb@cluster0.c6kshcf.mongodb.net/?retryWrites=true&w=majority")
cluster5 = MongoClient("mongodb+srv://OTTO5:OTTOdb@cluster0.glphgeg.mongodb.net/?retryWrites=true&w=majority")
db1 = cluster1["Namesdb"]
db2 = cluster2["Namesdb"]
db3 = cluster3["Namesdb"]
db4 = cluster4["Namesdb"]
db5 = cluster5["Namesdb"]

# clusterr = MongoClient("mongodb+srv://Jarvis:Daisy1Tom2Sam3@cluster0.keero.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# dbb = clusterr['Users']
# collectionn = dbb['VIP']

# #token = "ODQwNTY1NDY4MDkxOTA4MTE3.YJaDmA.cYJJkIGyLE3n8e2ixRIyXaWlJRM"
# token="ODgxNjE3NDg1NzE0MDM0NzE4.YSvcRA.GzKcYieyn1sr5t1uNHSZYXFLt5c"

bot = commands.Bot(command_prefix='+',
                   guild_subscriptions=True,
                   activity=discord.Game(name="WITH SUPERCELL"),
                   case_insensitive=True,
                   intents=discord.Intents.all())
bot.remove_command('help')


@bot.event
async def on_ready():
  print(f"{bot.user.name} IS UP!")
  channel = bot.get_channel(1000659983081414729)
  em = discord.Embed(title="",description=f"",timestamp=datetime.datetime.utcnow(),color=discord.Color.green())
  em.set_author(name="Bot restarted",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
  await channel.send(embed=em)


@commands.has_role(961301374115676170)
@bot.command()
@commands.guild_only()
async def proflink(ctx, tag: str):
	channel = bot.get_channel(961310467341549598)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0x00FF00)
		embed.set_author(
		    name="Command logs",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png"
		)
		embed.add_field(name="User",
		                value="{}".format(ctx.message.author),
		                inline=True)
		embed.add_field(name="User id",
		                value="{}".format(ctx.message.author.id),
		                inline=True)
		embed.add_field(name="Server name",
		                value="{}".format(ctx.message.guild.name),
		                inline=False)
		embed.add_field(name="Channel name",
		                value="{}".format(ctx.message.channel.mention),
		                inline=False)
		embed.add_field(name="Command name", value="proflink", inline=True)
		embed.set_footer(text='Logged')
		await channel.send(embed=embed)
		player = await coc_client.get_player(tag)
		if '#' in tag:
			tag = tag.replace('#', '')
		embed = discord.Embed(
		    title=f"{player.name} #{tag.upper()}",
		    timestamp=datetime.datetime.utcnow(),
		    description=
		    f'Click [here](https://link.clashofclans.com/en?action=OpenPlayerProfile&tag={tag}) to view the player profile in game.',
		    color=discord.Color.random())
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		await ctx.reply(embed=embed)


@proflink.error
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.CommandInvokeError):
		em = discord.Embed(title="",
		                   description="",
		                   timestamp=datetime.datetime.utcnow(),
		                   color=discord.Color.red())
		em.set_author(
		    name="Invalid tag",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0xFF0000)
		embed.add_field(name="Usage",
		                value="``+proflink <TAG>``",
		                inline=False)
		embed.add_field(name="Example",
		                value="``+proflink #2PYPP02Q``",
		                inline=False)
		embed.set_author(
		    name="Invalid syntax",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png"
		)
		embed.set_footer(text=f'Command used by {ctx.message.author}')
		await ctx.send(embed=embed)


# @commands.cooldown(1, 120, commands.BucketType.user)
# @commands.has_role(961301374115676170)
# @bot.command()
# @commands.guild_only()
# async def names(ctx, tag: str):
#   channel = bot.get_channel(961310467341549598)
#   if ctx.guild.id == 961299028128190474:
#     embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
#     embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
#     embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
#     embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
#     embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
#     embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
#     embed.add_field(name="Command name", value="names", inline=True)
#     embed.set_footer(text='Logged')
#     await channel.send(embed=embed)
#     embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
#     embed.set_author(name="Loading..",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif")
#     mmm = await ctx.reply(embed=embed)
#     found = []
#     if '#' not in tag:
#       tag = '#' + tag.upper()
#     player = await coc_client.get_player(tag)
#     bigfat = [
#         '2015-08', '2015-09', '2015-10', '2015-11', '2015-12', '2016-01',
#         '2016-02', '2016-03', '2016-04', '2016-05', '2016-06', '2016-07',
#         '2016-08', '2016-09', '2016-10', '2016-11', '2016-12', '2017-01',
#         '2017-02', '2017-03', '2017-04', '2017-05', '2017-06', '2017-07',
#         '2017-08', '2017-09', '2017-10', '2017-11', '2017-12', '2018-01',
#         '2018-02', '2018-03', '2018-04', '2018-05', '2018-06', '2018-07',
#         '2018-08', '2018-09', '2018-10', '2018-11', '2018-12', '2019-01',
#         '2019-02', '2019-03', '2019-04', '2019-05', '2019-06', '2019-07',
#         '2019-08', '2019-09', '2019-10', '2019-11', '2019-12', '2020-01',
#         '2020-02', '2020-03', '2020-04', '2020-05', '2020-06',
#         '2020-07', '2020-08', '2020-09', '2020-10', '2020-11', '2020-12',
#         '2021-01', '2021-02', '2021-03', '2021-04', '2021-05', '2021-06',
#         '2021-07', '2021-08'
#     ]
#     after_bigfat = ['2021-09', '2021-10', '2021-11', '2021-12']
#     if 1 == 1:
#       for i in bigfat:
#         f = open(f'{i}.json', )
#         new_embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
#         new_embed.add_field(name="Scanning",value=f'{i}',inline=False)
#         new_embed.set_author(name="Loading..",icon_url= "https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif")
#         await mmm.edit(embed=new_embed)
#         data = json.load(f)
#         if tag in data:
#           po = data[f'{tag}']
#           found.append(f'**{i}** : {po}')
#       for j in after_bigfat:
#         m = open(f'{j}.json', 'r', encoding="utf8")
#         new_embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
#         new_embed.add_field(name="Scanning", value=f'{j}',inline=False)
#         new_embed.set_author(name="Loading..",icon_url= "https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif")
#         await mmm.edit(embed=new_embed)
#         data2 = json.load(m)
#         len_data2 = len(data2)
#         for i in range(len_data2):
#           if data2[i]["tag"] == tag:
#             found.append(f"**{j}** : {data2[i]['name']}")
#       if len(found) != 0:  
#         line = '\n'.join(map(str, found))
#         embed = discord.Embed(title=f'{player.name} {player.tag}',description=f'{line}',timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
#         embed.set_footer(text=f"Requested by {ctx.message.author}")
#         await ctx.send(embed=embed)
#         embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
#         embed.set_author(name="Process completed",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif")
#         embed.set_footer(text=f"Requested by {ctx.message.author}")
#         await mmm.edit(embed=embed)
#       else:
#         embed = discord.Embed(title=player.name,description='No names found',timestamp=datetime.datetime.utcnow(),color=discord.Color.green())
#         embed.set_footer(text=f"Requested by {ctx.message.author}")
#         await mmm.edit(embed=embed)
#     else:
#       embed = discord.Embed(title=f"Could not find old names..",color=discord.Color.red())
#       embed.set_footer(text=f"Requested by {ctx.message.author}")
#       await mmm.edit(embed=embed)

newfat = ['201508', '201509', '201510', '201511', '201512', '201601', '201602', '201603', '201604', '201605', '201606', '201607', '201608', '201609', '201610', '201611', '201612', '201701', '201702', '201703', '201704', '201705', '201706', '201707', '201708', '201709', '201710', '201711', '201712', '201801', '201802', '201803', '201804', '201805', '201806', '201807', '201808', '201809', '201810', '201811', '201812', '201901', '201902', '201903', '201904', '201905']
afternewfat = ['201906', '201907', '201908', '201909', '201910', '201911', '201912', '202001', '202002', '202003', '202004', '202005']
afterafternewfat = ['202006', '202007', '202008', '202009', '202010', '202011', '202012', '202101']
a3newfat = ['202102', '202103', '202104', '202105', '202106', '202107']
a4newfat = ['202108', '202109', '202110', '202111', '202112']

@commands.cooldown(1, 25, commands.BucketType.user)
@commands.has_role(961301374115676170)
@bot.command()
@commands.guild_only()
async def names(ctx, tag: str):
  channel = bot.get_channel(961310467341549598)
  if ctx.guild.id == 961299028128190474:
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
    embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
    embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
    embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
    embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
    embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
    embed.add_field(name="Command name", value="names", inline=True)
    embed.set_footer(text='Logged')
    await channel.send(embed=embed)
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
    embed.set_author(name="Loading..",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif")
    mmm = await ctx.reply(embed=embed)
    found = []
    player = await coc_client.get_player(tag)
    for i in newfat:
        collection = db1[f"{'Names'+i}"]
        results = collection.find({"_id": player.tag})
        for result in results:
            found.append(f"**{i[:4]+'-'+i[4:]}** : {result['name']}")
    for i in afternewfat:
        collection = db2[f"{'Names'+i}"]
        results = collection.find({"_id": player.tag})
        for result in results:
            found.append(f"**{i[:4]+'-'+i[4:]}** : {result['name']}")
    for i in afterafternewfat:
        collection = db3[f"{'Names'+i}"]
        results = collection.find({"_id": player.tag})
        for result in results:
            found.append(f"**{i[:4]+'-'+i[4:]}** : {result['name']}")
    for i in a3newfat:
        collection = db4[f"{'Names'+i}"]
        results = collection.find({"_id": player.tag})
        for result in results:
            found.append(f"**{i[:4]+'-'+i[4:]}** : {result['name']}")
    for i in a4newfat:
        collection = db5[f"{'Names'+i}"]
        results = collection.find({"_id": player.tag})
        for result in results:
            found.append(f"**{i[:4]+'-'+i[4:]}** : {result['name']}")
    if len(found) != 0:  
      line = '\n'.join(map(str, found))
      embed = discord.Embed(title=f'{player.name} {player.tag}',description=f'{line}',timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
      embed.set_footer(text=f"Requested by {ctx.message.author}")
      await mmm.edit(embed=embed)
    else:
      embed = discord.Embed(title=f"{player.name} {player.tag}",description='No names found',timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
      embed.set_footer(text=f"Requested by {ctx.message.author}")
      await mmm.edit(embed=embed)


@commands.has_role(961301374115676170)
@bot.command()
@commands.guild_only()
async def help(ctx):
    channel = bot.get_channel(961310467341549598)
    if ctx.guild.id == 961299028128190474:
        embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
        embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
        embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
        embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
        embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
        embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
        embed.add_field(name="Command name", value="help", inline=True)
        embed.set_footer(text='Logged')
        await channel.send(embed=embed)
        embed = discord.Embed(title="Hi, I'm O.T.T.O from the Builder Base!🤡",timestamp=datetime.datetime.utcnow(), description="**COMMANDS**",color=discord.Color.random())
        embed.add_field(name="+info", value="Get player's basic info\nUsage : +info <TAG>", inline=False)
        embed.add_field(name="+names", value="Get name change info\nUsage : +names <TAG>", inline=False)
        embed.add_field(name="+creation", value="Get creation date\nUsage : +creation <TAG>", inline=False)
        embed.add_field(name="+local", value="Get player's local history\nUsage : +local <TAG>", inline=False)
        embed.add_field(name="+lastsession", value="Get player's last session\nUsage : +lastsession <TAG>", inline=False)
        embed.add_field(name="+tags", value="Get some nice dead accounts\nUsage : +tags", inline=False)
        embed.add_field(name="+gatacc", value="Get a account of the rank and season you want\nUsage : +getacc <YEAR-MONTH> <RANK>", inline=False)
        embed.add_field(name="+receipt", value="Generates a fake receipt\nUsage : +receipt <DATE> <AMOUNT> <CURRENCY SYMBOL> <ORDER ID> <TYPE>", inline=False)
        embed.add_field(name="+receipt2", value="Generates a fake receipt (Full screen size)\nUsage : +receipt2 <DATE> <AMOUNT> <CURRENCY SYMBOL> <ORDER ID> <TYPE>", inline=False)
        embed.add_field(name="+receipt3", value="Generates a fake Google Play receipt\nUsage : +receipt3 <DATE> <AMOUNT> <CURRENCY SYMBOL> <TYPE>", inline=False)
        embed.add_field(name="+devices", value="Get stats of most used devices brands yearly in the given country\nUsage : +devices <country name> <FROM YEAR> <TO YEAR>", inline=False)
        embed.add_field(name="+androids", value="Get most used android devices currently in the given country\nUsage : +androids <country name>", inline=False)
        embed.add_field(name="+appledevs", value="Get most used apple devices year wise\nUsage : +appledevs", inline=False)
        embed.add_field(name="+proflink", value="Get player profile link\nUsage : +proflink <TAG>", inline=False)
        embed.add_field(name="+skins", value="Get skin's information\nUsage : +skins", inline=False)
        embed.add_field(name="+tempemails", value="Get some temporary email ids\nUsage : +tempemails", inline=False)
        embed.add_field(name="+inbox", value="Shows last mail in the inbox of temporary email\nUsage : +inbox <USED TEMPORARY EMAIL>", inline=False)
        await ctx.reply(embed=embed)

@help.error
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)

@names.error
async def on_command_error(ctx, error):
	######
	if isinstance(error, commands.CommandOnCooldown):
		em = discord.Embed(
		    title="",
		    description=f"Try again in {error.retry_after:.2f}s.",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="Hold On",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.CommandInvokeError):
		em = discord.Embed(title="",
		                   description="",
		                   timestamp=datetime.datetime.utcnow(),
		                   color=discord.Color.red())
		em.set_author(
		    name="Invalid tag",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0xFF0000)
		embed.add_field(name="Usage", value="``+names <TAG>``", inline=False)
		embed.add_field(name="Example ",
		                value="``+names #YLUJY90R``",
		                inline=False)
		embed.set_author(
		    name="Invalid syntax",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png"
		)
		embed.set_footer(text=f'Command used by {ctx.message.author}')
		await ctx.send(embed=embed)


@commands.guild_only()
@commands.has_role(961301374115676170)
@bot.command()
async def receipt(ctx, arg: str, price: float, cur: str, codek: str, *,
                  typee: str):
	channel = bot.get_channel(961310467341549598)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0x00FF00)
		embed.set_author(
		    name="Command logs",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png"
		)
		embed.add_field(name="User",
		                value="{}".format(ctx.message.author),
		                inline=True)
		embed.add_field(name="User id",
		                value="{}".format(ctx.message.author.id),
		                inline=True)
		embed.add_field(name="Server name",
		                value="{}".format(ctx.message.guild.name),
		                inline=False)
		embed.add_field(name="Channel name",
		                value="{}".format(ctx.message.channel.mention),
		                inline=False)
		embed.add_field(name="Command name", value="receipt", inline=True)
		embed.set_footer(text='Logged')
		await channel.send(embed=embed)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		embed.set_author(
		    name="Loading..",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif"
		)
		embed.set_footer(text=f'Requested by {ctx.message.author}')
		mmm = await ctx.reply(embed=embed)
		price = cur + str(price)
		tax = cur + str(price)
		x = tax.split('.')
		if len(x[1]) == 1:
			tax = tax + '0'
		if len(arg) == 9:
			mon = arg[0:3].upper()
			day = arg[3:5]
			year = arg[5:]
			date = mon + ' ' + day + ', ' + year
		if len(arg) == 7:
			mon = arg[0:3].upper()
			day = arg[3:]

			date = mon + ' ' + day

		code = codek
		# for i in range(2):
		#     code += random.choice(string.ascii_uppercase)
		# for i in range(7):
		#     x = random.randint(1, 2)
		#     if x == 1:
		#         code += random.choice(string.ascii_uppercase)
		#     else:
		#         y = random.randint(0, 9)
		#         if y == 7:
		#             y = 8
		#         code += str(y)
		layer1 = Image.open("forged.png").convert("RGBA")
		final = Image.new("RGBA", layer1.size)
		final.paste(layer1, (0, 0), layer1)
		fnt = ImageFont.truetype('aba.ttf', 22)
		d = ImageDraw.Draw(final)

		d.text((677, 13), code, font=fnt, fill=(96, 96, 98))
		f = ImageDraw.Draw(final)

		f.text((24, 13), date, font=fnt, fill=(96, 96, 98))
		p = ImageDraw.Draw(final)

		p.text((736, 65), price, font=fnt, fill=(251, 251, 253))
		p2 = ImageDraw.Draw(final)

		p2.text((712, 171), price, font=fnt, fill=(251, 251, 253))
		p2 = ImageDraw.Draw(final)

		p2.text((260, 63), typee, font=fnt, fill=(216, 216, 218))
		p2 = ImageDraw.Draw(final)
		final.save("complete.png", format="png")
		await ctx.send(file=discord.File('complete.png'))
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		embed.set_author(
		    name="Process completed",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif"
		)
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		await mmm.edit(embed=embed)


@receipt.error
async def on_command_error(ctx, error):
  ######
  if isinstance(error, commands.MissingRole):
    em = discord.Embed(title="",description="DM <@920337055706386443> to buy the bot ez",timestamp=datetime.datetime.utcnow(),color=discord.Color.red())
    em.set_author( name="You can't use the bot commands",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png")
    em.set_footer(text=f"Command used by {ctx.message.author}")
    await ctx.send(embed=em)
  ######
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0xFF0000)
    embed.add_field(name="Usage",value="``+receipt <DATE> <AMOUNT> <CURRENCY SYMBOL> <ORDER ID> <TYPE>``",inline=False)
    embed.add_field(name="Example",value="``+receipt FEB072020 4.9 $ M2MNMO56 Gold Pass``",inline=False)
    embed.set_author( name="Invalid syntax",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png")
    embed.set_footer(text=f'Command used by {ctx.message.author}')
    await ctx.send(embed=embed)
  #######
  if isinstance(error, commands.CommandInvokeError):
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0xFF0000)
    embed.add_field(name="Usage",value="``+receipt <DATE> <AMOUNT> <CURRENCY SYMBOL> <ORDER ID> <TYPE>``",inline=False)
    embed.add_field(name="Example",value="``+receipt FEB072020 4.9 $ M2MNMO56 Gold Pass``",inline=False)
    embed.set_author( name="Invalid syntax",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png")
    embed.set_footer(text=f'Command used by {ctx.message.author}')
    await ctx.send(embed=embed)
      


@commands.guild_only()
@commands.has_role(961301374115676170)
@bot.command()
async def receipt2(ctx, arg: str, price: float, cur: str, codek: str, *,
                   type: str):
	channel = bot.get_channel(961310467341549598)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0x00FF00)
		embed.set_author(
		    name="Command logs",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png"
		)
		embed.add_field(name="User",
		                value="{}".format(ctx.message.author),
		                inline=True)
		embed.add_field(name="User id",
		                value="{}".format(ctx.message.author.id),
		                inline=True)
		embed.add_field(name="Server name",
		                value="{}".format(ctx.message.guild.name),
		                inline=False)
		embed.add_field(name="Channel name",
		                value="{}".format(ctx.message.channel.mention),
		                inline=False)
		embed.add_field(name="Command name", value="receipt2", inline=True)
		embed.set_footer(text='Logged')
		await channel.send(embed=embed)
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		embed.set_author(
		    name="Loading..",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif"
		)
		embed.set_footer(text=f'Requested by {ctx.message.author}')
		mmm = await ctx.reply(embed=embed)
		price = cur + str(price)
		tax = cur + str(price)
		x = tax.split('.')
		if len(x[1]) == 1:
			tax = tax + '0'
		if len(arg) == 9:
			day = arg[0:2]
			mon = arg[2:5].upper()
			year = arg[5:]
			date = day + ' ' + mon + ' ' + year
		if len(arg) == 7:
			mon = arg[0:2].upper()
			year = arg[2:]
			date = mon + ' ' + year
		typee = type
		code = codek
		l = "1871622"
		y = f"{random.randint(0, 9)}"
		h = f"{random.randint(0, 9)}"
		j = f"{random.randint(0, 9)}"
		k = f"{random.randint(0, 9)}"
		to = l + y + h + j + k
		doc = str(to)
		# for i in range(2):
		#     code += random.choice(string.ascii_uppercase)
		# for i in range(7):
		#     x = random.randint(1, 2)
		#     if x == 1:
		#         code += random.choice(string.ascii_uppercase)
		#     else:
		#         y = random.randint(0, 9)
		#         if y == 7:
		#             y = 8
		#         code += str(y)
		layer1 = Image.open("gg.png").convert("RGBA")
		final = Image.new("RGBA", layer1.size)
		final.paste(layer1, (0, 0), layer1)
		fnt = ImageFont.truetype('aba.ttf', 22)
		d = ImageDraw.Draw(final)

		d.text((25, 256), code, font=fnt, fill=(251, 251, 253))
		f = ImageDraw.Draw(final)

		f.text((25, 350), date, font=fnt, fill=(251, 251, 253))
		p = ImageDraw.Draw(final)

		p.text((348, 350), price, font=fnt, fill=(251, 251, 253))
		p2 = ImageDraw.Draw(final)

		p2.text((520, 832), price, font=fnt, fill=(251, 251, 253))
		p2 = ImageDraw.Draw(final)

		x = 528
		if len(price) == 5:
			x = 516
		if len(price) == 6:
			x = 504
		if len(price) == 7:
			x = 492
		if len(price) == 8:
			x = 480
		p2.text((x, 721), price, font=fnt, fill=(251, 251, 253))
		p2 = ImageDraw.Draw(final)

		p2.text((110, 721), typee, font=fnt, fill=(251, 251, 253))
		p2 = ImageDraw.Draw(final)

		p2.text((348, 256), doc, font=fnt, fill=(251, 251, 253))
		p2 = ImageDraw.Draw(final)
		final.save("complete2.png", format="png")
		await ctx.send(file=discord.File('complete2.png'))
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		embed.set_author(
		    name="Process completed",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif"
		)
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		await mmm.edit(embed=embed)


@receipt2.error
async def on_command_error(ctx, error):
  ######
  if isinstance(error, commands.MissingRole):
    em = discord.Embed(title="",description="DM <@920337055706386443> to buy the bot ez",timestamp=datetime.datetime.utcnow(),color=discord.Color.red())
    em.set_author(name="You can't use the bot commands",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png")
    em.set_footer(text=f"Command used by {ctx.message.author}")
    await ctx.send(embed=em)
  ######
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0xFF0000)
    embed.add_field(name="Usage",value="``+receipt2 <DATE> <AMOUNT> <CURRENCY SYMBOL> <ORDER ID> <TYPE>``",inline=False)
    embed.add_field(name="Example",value="``+receipt2 18MAY2020 4.9 $ M2MNMO56 Gold Pass``",inline=False)
    embed.set_author(name="Invalid syntax",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png")
    embed.set_footer(text=f'Command used by {ctx.message.author}')
    await ctx.send(embed=embed)
  #######
  if isinstance(error, commands.CommandInvokeError):
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0xFF0000)
    embed.add_field(name="Usage",value="``+receipt2 <DATE> <AMOUNT> <CURRENCY SYMBOL> <ORDER ID> <TYPE>``",inline=False)
    embed.add_field(name="Example",value="``+receipt2 18MAY2020 4.9 $ M2MNMO56 Gold Pass``",inline=False)
    embed.set_author(name="Invalid syntax",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png")
    embed.set_footer(text=f'Command used by {ctx.message.author}')
    await ctx.send(embed=embed)


def getno():
	y = f"{random.randint(0, 9)}"
	h = f"{random.randint(0, 9)}"
	j = f"{random.randint(0, 9)}"
	k = f"{random.randint(0, 9)}"
	to = y + h + j + k
	return (to)


@commands.guild_only()
@commands.has_role(961301374115676170)
@bot.command()
async def receipt3(ctx, arg: str, price: float, cur: str, *, typee: str):
	channel = bot.get_channel(961310467341549598)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
		embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
		embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
		embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
		embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
		embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
		embed.add_field(name="Command name", value="receipt3", inline=True)
		embed.set_footer(text='Logged')
		await channel.send(embed=embed)
		embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
		embed.set_author(name="Loading..",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif")
		embed.set_footer(text=f'Requested by {ctx.message.author}')
		mmm = await ctx.reply(embed=embed)
		price1 = cur + str(price)
		price2 = "Total: " + cur + str(price)
		type = typee + " (Clash of Clans)"
		if len(arg) == 9:
			mon = arg[0:3].lower().capitalize()
			day = arg[3:5]
			year = arg[5:]
			date = mon + ' ' + day + ', ' + year
		if len(arg) == 7:
			mon = arg[0:3].upper()
			day = arg[3:]

			date = mon + ' ' + day

		code2 = f"{getno()}" + f"{random.randint(0, 9)}"
		code = f"GPA.{getno()}-{getno()}-{getno()}-"
		# for i in range(2):
		#     code += random.choice(string.ascii_uppercase)
		# for i in range(7):
		#     x = random.randint(1, 2)
		#     if x == 1:
		#         code += random.choice(string.ascii_uppercase)
		#     else:
		#         y = random.randint(0, 9)
		#         if y == 7:
		#             y = 8
		#         code += str(y)
		layer1 = Image.open("blankrece.png").convert("RGBA")
		final = Image.new("RGBA", layer1.size)
		final.paste(layer1, (0, 0), layer1)
		fnt = ImageFont.truetype('aba.ttf', 26)
		d = ImageDraw.Draw(final)

		d.text((238, 419), code, font=fnt, fill=(96, 96, 98))
		f = ImageDraw.Draw(final)

		f.text((200, 499), date, font=fnt, fill=(96, 96, 98))
		p = ImageDraw.Draw(final)

		x = 441
		x2 = 371
		if len(price1) == 5:
			x = 452
			x2 = 382
		if len(price1) == 4:
			x = 465
			x2 = 395
		if len(price1) == 3:
			x = 474
			x2 = 404
		p.text((x, 723), price1, font=fnt, fill=(96, 96, 98))
		p2 = ImageDraw.Draw(final)

		p2.text((x2, 817), price2, font=fnt, fill=(96, 96, 98))
		p2 = ImageDraw.Draw(final)

		if len(type) > 28:
			typee = type[:29]
			typeee = type[29:]
			p2.text((72, 703), typee, font=fnt, fill=(96, 96, 98))
			p2 = ImageDraw.Draw(final)
			p2.text((72, 743), typeee, font=fnt, fill=(96, 96, 98))
		else:
			p2.text((72, 703), type, font=fnt, fill=(96, 96, 98))
			p2 = ImageDraw.Draw(final)

		p2.text((66, 459), code2, font=fnt, fill=(96, 96, 98))
		p2 = ImageDraw.Draw(final)

		p2.text((280, 933), "Google Play balance", font=fnt, fill=(96, 96, 98))
		p2 = ImageDraw.Draw(final)

		final.save("complete3.png", format="png")
		await ctx.send(file=discord.File('complete3.png'))
		embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
		embed.set_author(name="Process completed",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif")
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		await mmm.edit(embed=embed)


@receipt3.error
async def on_command_error(ctx, error):
  ######
  if isinstance(error, commands.MissingRole):
    em = discord.Embed(title="",description="DM <@920337055706386443> to buy the bot ez",timestamp=datetime.datetime.utcnow(),color=discord.Color.red())
    em.set_author(name="You can't use the bot commands",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png")
    em.set_footer(text=f"Command used by {ctx.message.author}")
    await ctx.send(embed=em)
  ######
  if isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0xFF0000)
    embed.add_field(name="Usage",value="``+receipt3 <DATE> <AMOUNT> <CURRENCY SYMBOL> <TYPE>``",inline=False)
    embed.add_field(name="Example",value="``+receipt3 FEB072020 4.9 $ Gold Pass``",inline=False)
    embed.set_author(name="Invalid syntax",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png")
    embed.set_footer(text=f'Command used by {ctx.message.author}')
    await ctx.send(embed=embed)
  #######
  if isinstance(error, commands.CommandInvokeError):
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0xFF0000)
    embed.add_field(name="Usage",value="``+receipt3 <DATE> <AMOUNT> <CURRENCY SYMBOL> <TYPE>``",inline=False)
    embed.add_field(name="Example",value="``+receipt3 FEB072020 4.9 $ Gold Pass``",inline=False)
    embed.set_author(name="Invalid syntax",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png")
    embed.set_footer(text=f'Command used by {ctx.message.author}')
    await ctx.send(embed=embed)


@commands.guild_only()
@commands.has_role(961301374115676170)
@bot.command()
async def creation(ctx, tag: str):
  channel = bot.get_channel(961310467341549598)
  if ctx.guild.id == 961299028128190474:
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
    embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
    embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
    embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
    embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
    embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
    embed.add_field(name="Command name", value="creation", inline=True)
    embed.set_footer(text='Logged')
    await channel.send(embed=embed)
    player = await coc_client.get_player(tag)
    if '#' in tag:
      tag = tag.split('#')
      tag = tag[1]
    if len(tag) == 7:
      tag = '0' + tag
    if len(tag) == 9:
      tag = tag.lower()
      if tag.startswith('2'):
        date = 'Late 2014 - late 2015'
      if tag.startswith('8'):
        date = 'Early 2015 - mid 2015'
      if tag.startswith('9'):
        date = '2016'
      if tag.startswith('p'):
        date = 'Late 2016 - 2017'
      if tag.startswith('y'):
        date = 'Late 2017 - 2018'
      if tag.startswith('l'):
        date = 'Late 2018 - 2019'
      if tag.startswith('q'):
        date = '2020 - 2021'
    if len(tag) == 8:
      tag = tag.lower()
      if tag.startswith('2'):
        date = 'Late 2014 - late 2015'
      elif tag.startswith('8'):
        date = 'Early 2015 - mid 2015'
      else:
        date = 'Mid 2013 - 2014'
    if len(tag) <= 6:
      date = '2012'
    tag = tag.upper()
    embed = discord.Embed(title=f"{player.name} #{tag}",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
    embed.add_field(name="Account was created arround",value=f"{date}",inline=False)
    embed.set_footer(text=f"Requested by {ctx.message.author}")
    await ctx.reply(embed=embed)


@creation.error
async def on_command_error(ctx, error):
	######
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0xFF0000)
		embed.add_field(name="Usage",
		                value="``+creation <ACCOUNT TAG>``",
		                inline=False)
		embed.add_field(name="Example",
		                value="``+creation #YJUVGP2R2``",
		                inline=False)
		embed.set_author(
		    name="Invalid syntax",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png"
		)
		embed.set_footer(text=f'Command used by {ctx.message.author}')
		await ctx.send(embed=embed)
	######
	if isinstance(error, commands.CommandInvokeError):
		em = discord.Embed(title="",
		                   description="",
		                   timestamp=datetime.datetime.utcnow(),
		                   color=discord.Color.red())
		em.set_author(
		    name="Invalid tag",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)


@commands.cooldown(1, 10, commands.BucketType.user)
@commands.guild_only()
@commands.has_role(961301374115676170)
@bot.command()
async def devices(ctx, country: str, start: int, end: int):
	channel = bot.get_channel(961310467341549598)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0x00FF00)
		embed.set_author(
		    name="Command logs",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png"
		)
		embed.add_field(name="User",
		                value="{}".format(ctx.message.author),
		                inline=True)
		embed.add_field(name="User id",
		                value="{}".format(ctx.message.author.id),
		                inline=True)
		embed.add_field(name="Server name",
		                value="{}".format(ctx.message.guild.name),
		                inline=False)
		embed.add_field(name="Channel name",
		                value="{}".format(ctx.message.channel.mention),
		                inline=False)
		embed.add_field(name="Command name", value="devices", inline=True)
		embed.set_footer(text='Logged')
		await channel.send(embed=embed)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		embed.set_author(
		    name="Loading..",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif"
		)
		mmm = await ctx.reply(embed=embed)
		if country.lower() == 'usa' or country.lower() == 'us':
			country = 'united-states-of-america'
		if country.lower() == 'uk':
			country = 'united-kingdom'
		if country == 'united-kingdom':
			huh = 'GB'
			bong = 'United%20Kingdom'
		elif country == 'united-states-of-america':
			huh = 'US'
			bong = 'United%20States%20of%20America'
		else:
			bong = country.lower().capitalize()
			with open('country_code.json', 'r') as f:
				it = json.load(f)
				huh = it[bong]
				print(huh)

		x = []
		y = []
		url = f'https://gs.statcounter.com/vendor-market-share/mobile-tablet/chart.php?bar=1&device=Mobile%20%26%20Tablet&device_hidden=mobile%2Btablet&multi-device=true&statType_hidden=vendor&region_hidden={huh}&granularity=yearly&statType=Device%20Vendor&region={bong}&fromInt={start}&toInt={end}&fromYear={start}&toYear={end}&csv=1'
		df = pd.read_csv(url, on_bad_lines="skip")
		coll = []
		for col in df.columns:
			coll.append(col)
		for i in range(len(df['Device Vendor'])):
			x.append(df['Device Vendor'][i])
			y.append(df[f'{coll[1]}'][i]) 
		embed = discord.Embed(title=f'**Devices used yearly in {country}**',
		                      description=f'From year {start} to {end}',
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		for i in range(len(x)):
			embed.add_field(name=f'**{x[i]}**', value=f'{y[i]}%', inline=True)
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		await mmm.edit(embed=embed)

@devices.error
async def on_command_error(ctx, error):
	######
	if isinstance(error, commands.CommandOnCooldown):
		em = discord.Embed(
		    title="",
		    description=f"Try again in {error.retry_after:.2f}s.",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="Hold On",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.CommandInvokeError):
		em = discord.Embed(title="",
		                   description="",
		                   timestamp=datetime.datetime.utcnow(),
		                   color=discord.Color.red())
		em.set_author(
		    name="Invalid country name",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0xFF0000)
		embed.add_field(
		    name="Usage",
		    value=
		    "``+devices <country name lowercased> <FROM YEAR> <TO YEAR>``",
		    inline=False)
		embed.add_field(name="Example 1",
		                value="``+devices us 2014 2015``",
		                inline=False)
		embed.add_field(name="Example 2",
		                value="``+devices uk 2016 2018``",
		                inline=False)
		embed.add_field(name="Example 3",
		                value="``+devices japan 2013 2015``",
		                inline=False)
		embed.set_author(
		    name="Invalid syntax",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png"
		)
		embed.set_footer(text=f'Command used by {ctx.message.author}')
		await ctx.send(embed=embed)


@commands.cooldown(1, 5, commands.BucketType.user)
@commands.guild_only()
@commands.has_role(961301374115676170)
@bot.command()
async def androids(ctx, country: str):
	channel = bot.get_channel(961310467341549598)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0x00FF00)
		embed.set_author(
		    name="Command logs",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png"
		)
		embed.add_field(name="User",
		                value="{}".format(ctx.message.author),
		                inline=True)
		embed.add_field(name="User id",
		                value="{}".format(ctx.message.author.id),
		                inline=True)
		embed.add_field(name="Server name",
		                value="{}".format(ctx.message.guild.name),
		                inline=False)
		embed.add_field(name="Channel name",
		                value="{}".format(ctx.message.channel.mention),
		                inline=False)
		embed.add_field(name="Command name", value="androids", inline=True)
		embed.set_footer(text='Logged')
		await channel.send(embed=embed)

		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		embed.set_author(
		    name="Loading..",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif"
		)
		mmm = await ctx.reply(embed=embed)
		if country.lower() == 'usa' or country.lower() == 'us':
			country = 'united-states-of-america'
		if country.lower() == 'uk':
			country = 'united-kingdom'
		if country == 'united-kingdom':
			huh = 'gb'
		elif country == 'united-states-of-america':
			huh = 'us'
		else:
			bong = country.lower().capitalize()
			with open('country_code.json', 'r') as f:
				it = json.load(f)
				huh = it[bong]
				huh = huh.lower()
				print(huh)
		url = f"https://www.appbrain.com/stats/top-android-phones-tablets-by-country?country={huh}"
		data = requests.get(url)
		doc = BeautifulSoup(data.text, "html.parser")
		j = doc.find_all("script")[11]
		a = f"{j}"
		k = a.split("=")[4]
		p = k[10:]
		p = p.split(',"header"')
		p = p[0]
		with open("sample.json", "w") as outfile:
			outfile.write(p)
		f = open('sample.json')
		d = json.load(f)
		list = []
		for i in range(len(d)):
			list.append(d[i]["modelName"])
		line = '\n\n'.join(map(str, list))
		embed = discord.Embed(title="",
		                      description=f"```{line}```",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		embed.set_author(name=f"Mostly used android devices in {country}")
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		await ctx.reply(embed=embed)
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		embed.set_author(
		    name="Process completed",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif"
		)
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		await mmm.edit(embed=embed)


@androids.error
async def on_command_error(ctx, error):
	######
	if isinstance(error, commands.CommandOnCooldown):
		em = discord.Embed(
		    title="",
		    description=f"Try again in {error.retry_after:.2f}s.",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="Hold On",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.CommandInvokeError):
		em = discord.Embed(title="",
		                   description="",
		                   timestamp=datetime.datetime.utcnow(),
		                   color=discord.Color.red())
		em.set_author(
		    name="Invalid country name",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0xFF0000)
		embed.add_field(name="Usage",
		                value="``+androids <country name lowercased>``",
		                inline=False)
		embed.add_field(name="Example", value="``+androids us``", inline=False)
		embed.set_author(
		    name="Invalid syntax",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png"
		)
		embed.set_footer(text=f'Command used by {ctx.message.author}')
		await ctx.send(embed=embed)


@commands.guild_only()
@commands.has_role(961301374115676170)
@bot.command()
async def tags(ctx):
  channel = bot.get_channel(961310467341549598)
  if ctx.guild.id == 961299028128190474:
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
    embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
    embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
    embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
    embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
    embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
    embed.add_field(name="Command name", value="tags", inline=True)
    embed.set_footer(text='Logged')
    await channel.send(embed=embed)
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
    embed.set_author(name="Loading..",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif")
    mmm = await ctx.reply(embed=embed)
    foundtags = []
    foundth = []
    m = open('sorteddeadtags.json', 'r', encoding="utf8")
    data = json.load(m)
    len_data = len(data)
    for i in range(0, 10):
      s = random.randint(0, len_data)
      t = data[s]["tag"]
      tl = data[s]["th_level"]
      foundtags.append(t)
      foundth.append(tl)
    len_f = len(foundtags)
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
    embed.set_author(name="Dead Accounts",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif")
    for i in range(0, len_f):
      tag = foundtags[i]
      if '#' in tag:
        ntag = tag.replace('#', '')
        player = await coc_client.get_player(tag)
        thlvl = foundth[i]
        embed.add_field(name=f"**{player.name}**",value=f"Tag : {tag}\nTown Hall : {thlvl}\n[View in game](https://link.clashofclans.com/en?action=OpenPlayerProfile&tag={ntag})",inline=True)
    embed.set_footer(text=f"Requested by {ctx.message.author}")
    await mmm.edit(embed=embed)


@tags.error
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)


@commands.cooldown(1, 5, commands.BucketType.user)
@commands.guild_only()
@commands.has_role(961301374115676170)
@bot.command()
async def local(ctx, arg: str):
	channel = bot.get_channel(961310467341549598)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0x00FF00)
		embed.set_author(
		    name="Command logs",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png"
		)
		embed.add_field(name="User",
		                value="{}".format(ctx.message.author),
		                inline=True)
		embed.add_field(name="User id",
		                value="{}".format(ctx.message.author.id),
		                inline=True)
		embed.add_field(name="Server name",
		                value="{}".format(ctx.message.guild.name),
		                inline=False)
		embed.add_field(name="Channel name",
		                value="{}".format(ctx.message.channel.mention),
		                inline=False)
		embed.add_field(name="Command name", value="local", inline=True)
		embed.set_footer(text='Logged')
		await channel.send(embed=embed)
		player = await coc_client.get_player(f'{arg}')
		if '#' in arg:
			tag = arg.split('#')
			tag = tag[1]
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		embed.set_author(
		    name="Loading..",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif"
		)
		mmm = await ctx.reply(embed=embed)
		url = f"https://www.clashofstats.com/players/{tag}/history/"
		data = requests.get(url)
		doc = BeautifulSoup(data.text, "html.parser")
		lim = len(doc.find_all("div", class_="v-list-item__subtitle"))
		print(lim)
		embed = discord.Embed(
		    title="",
		    timestamp=datetime.datetime.utcnow(),
		    description=
		    f"**{player.name} {arg}**\nClick [here](https://www.clashofstats.com/players/{tag}/history/) to view player's clan history on COS.",
		    color=discord.Color.random())
		embed.set_author(
		    name="Local History",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png"
		)
		for i in range(0, lim):
			j = doc.find_all("div", class_="v-list-item__title")[4 + i].text
			kl = " ".join(j.split())
			l = doc.find_all("div", class_="v-list-item__subtitle")[i].text
			lo = "None"
			if '-' in kl:
				clantag = kl.split('#')
				clantag = "#" + f"{clantag[len(clantag)-1]}"
				clan = await coc_client.get_clan(clantag)
				lo = clan.location
				embed.add_field(
				    name=f'{clan.name} {clan.tag}',
				    value=
				    f'Location : {lo}\nTotal stay : {" ".join(l.split())}',
				    inline=False)
			else:
				embed.add_field(
				    name=f'{j}',
				    value=
				    f'Location : {lo}\nTotal stay : {" ".join(l.split())}',
				    inline=False)
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		await ctx.reply(embed=embed)
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		embed.set_author(
		    name="Process completed",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif"
		)
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		await mmm.edit(embed=embed)


@local.error
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.CommandInvokeError):
		em = discord.Embed(title="",
		                   description="",
		                   timestamp=datetime.datetime.utcnow(),
		                   color=discord.Color.red())
		em.set_author(
		    name="No local history available for this tag",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.CommandOnCooldown):
		em = discord.Embed(
		    title="",
		    description=f"Try again in {error.retry_after:.2f}s.",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="Hold On",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0xFF0000)
		embed.add_field(name="Usage", value="``+local <TAG>``", inline=False)
		embed.add_field(name="Example",
		                value="``+local #QCU28LPV``",
		                inline=False)
		embed.set_author(
		    name="Invalid syntax",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png"
		)
		embed.set_footer(text=f'Command used by {ctx.message.author}')
		await ctx.send(embed=embed)


@commands.cooldown(1, 10, commands.BucketType.user)
@commands.guild_only()
@commands.has_role(961301374115676170)
@bot.command()
async def lastsession(ctx, arg: str):
  channel = bot.get_channel(961310467341549598)
  if ctx.guild.id == 961299028128190474:
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
    embed.set_author( name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
    embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
    embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
    embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
    embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
    embed.add_field(name="Command name", value="lastsession", inline=True)
    embed.set_footer(text='Logged')
    await channel.send(embed=embed)
    if '#' in arg:
      tag = arg.split('#')
      tag = tag[1]
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
    embed.set_author(name="Loading..",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif")
    mmm = await ctx.reply(embed=embed)
    player = await coc_client.get_player(f'{arg}')
    list = []
    url = f"https://www.clashofstats.com/players/{tag}/history/progress-log/"
    data = requests.get(url)
    doc = BeautifulSoup(data.text, "html.parser")
    lim = len(doc.find_all("h3", class_="subsection-title"))
    if lim >= 1:
        list.append("\n**Home Village**")
        if lim > 3:
            lim = 3
        for i in range(0,lim):
            list.append(doc.find_all("h3", class_="subsection-title")[i].text)
    url = f"https://www.clashofstats.com/players/{tag}/history/progress-log/builder-base"
    data = requests.get(url)
    doc = BeautifulSoup(data.text, "html.parser")
    lim = len(doc.find_all("h3", class_="subsection-title"))
    if lim >= 1:
        list.append("\n**Builder Base**")
        if lim > 3:
            lim = 3
        for i in range(0,lim):
            list.append(doc.find_all("h3", class_="subsection-title")[i].text)
    if len(list) !=0:
      line = '\n'.join(map(str, list))
      embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),description=f"**{player.name} {arg}**\n{line}",color=discord.Color.random())
      embed.set_author(name="Last Session",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
      embed.set_footer(text=f"Requested by {ctx.message.author}")
      await mmm.edit(embed=embed)
    else:
      em = discord.Embed(title="",description="",timestamp=datetime.datetime.utcnow(),color=discord.Color.red())
      em.set_author(name="No last session available for this tag",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png")
      em.set_footer(text=f"Command used by {ctx.message.author}")
      await mmm.edit(embed=em)
    # embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),description=f"**{player.name} {arg}**",color=discord.Color.random())
    # embed.set_author(name="Last Session",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
    # try:
    #   url = f"https://www.clashofstats.com/players/{tag}/history/progress-log/"
    #   data = requests.get(url)
    #   doc = BeautifulSoup(data.text, "html.parser")
    #   j1 = doc.find_all("h3", class_="subsection-title")[0].text
    #   embed.add_field(name='Last session for Home Village',value=f'{j1}',inline=False)
    # except:
    #   url = f"https://www.clashofstats.com/players/{tag}/history/progress-log/builder-base"
    #   data = requests.get(url)
    #   doc = BeautifulSoup(data.text, "html.parser")
    #   j1 = doc.find_all("h3", class_="subsection-title")[0].text
    #   embed.add_field(name='Last session for Builder Base',value=f'{j1}',inline=False)
    # embed.set_footer(text=f"Requested by {ctx.message.author}")
    # await ctx.reply(embed=embed)
    # embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
    # embed.set_author(name="Process completed",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif")
    # embed.set_footer(text=f"Requested by {ctx.message.author}")
    # await mmm.edit(embed=embed)


@lastsession.error
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.CommandInvokeError):
		em = discord.Embed(title="",
		                   description="",
		                   timestamp=datetime.datetime.utcnow(),
		                   color=discord.Color.red())
		em.set_author(
		    name="No last session available for this tag",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.CommandOnCooldown):
		em = discord.Embed(
		    title="",
		    description=f"Try again in {error.retry_after:.2f}s.",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="Hold On",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0xFF0000)
		embed.add_field(name="Usage",
		                value="``+lastsession <TAG>``",
		                inline=False)
		embed.add_field(name="Example",
		                value="``+lastsession #QCU28LPV``",
		                inline=False)
		embed.set_author(
		    name="Invalid syntax",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png"
		)
		embed.set_footer(text=f'Command used by {ctx.message.author}')
		await ctx.send(embed=embed)


contents = [
    "**2012**\n📲 iPhone 4, iPad and iPhone 5.\n\n⚠️ Keep in mind that the account(s) could have more devices.",
    "**2013**\n📲 iPhone 5, iPad and if it has 2014 trees: iPhone 6.\n\n⚠️ Keep in mind that the account(s) could have more devices.",
    "**2014**\n📲 iPhone 5 (Try iPhone 6 and iPad first), iPad Air, iPhone 6.\n\n⚠️ Keep in mind that the account(s) could have more devices.",
    "**2015**\n📲 iPhone 6, iPad Mini/Air.\n\n⚠️ Keep in mind that the account(s) could have more devices.",
    "**2016**\n📲 iPhone 6S, iPad Air/Mini, try iPhone 7 if the account was created in Late 2016. (September/October)\n\n⚠️ Keep in mind that the account(s) could have more devices.",
    "**2017**\n📲 iPhone 7, iPad Pro, try iPhone 8 and X if the account was created in Late 2017. (September/October)\n\n⚠️ Keep in mind that the account(s) could have more devices.",
    "**2018**\n📲 iPhone 8, iPhone X, iPad Pro, try iPhone XS/XR if the account was created in Late 2018. (October/November)\n\n⚠️ Keep in mind that the account(s) could have more devices."
]


@commands.guild_only()
@commands.has_role(961301374115676170)
@bot.command()
async def appledevs(ctx):
	channel = bot.get_channel(961310467341549598)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0x00FF00)
		embed.set_author(
		    name="Command logs",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png"
		)
		embed.add_field(name="User",
		                value="{}".format(ctx.message.author),
		                inline=True)
		embed.add_field(name="User id",
		                value="{}".format(ctx.message.author.id),
		                inline=True)
		embed.add_field(name="Server name",
		                value="{}".format(ctx.message.guild.name),
		                inline=False)
		embed.add_field(name="Channel name",
		                value="{}".format(ctx.message.channel.mention),
		                inline=False)
		embed.add_field(name="Command name", value="appledevs", inline=True)
		embed.set_footer(text='Logged')
		await channel.send(embed=embed)
		pages = 7
		cur_page = 1
		hellp = discord.Embed(title="📲 Apple Devices",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		hellp.set_footer(text=f"Requested by {ctx.message.author}")
		hellp.add_field(
		    name=f"🗒 Apple Devices for year »",
		    value=f"\n{contents[cur_page-1]}\n\n**Page {cur_page}/{pages}**",
		    inline=False)
		message = await ctx.reply(embed=hellp)
		await message.add_reaction("◀️")
		await message.add_reaction("▶️")

		def check(reaction, user):
			return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

		while True:
			try:
				reaction, user = await bot.wait_for("reaction_add",
				                                    timeout=60,
				                                    check=check)
				if str(reaction.emoji) == "▶️" and cur_page != pages:
					cur_page += 1
					hellp = discord.Embed(title="📲 Apple Devices",
					                      timestamp=datetime.datetime.utcnow(),
					                      color=discord.Color.random())
					hellp.set_footer(text=f"Requested by {ctx.message.author}")
					hellp.add_field(
					    name=f"🗒 Apple Devices for year »",
					    value=
					    f"\n{contents[cur_page-1]}\n\n**Page {cur_page}/{pages}**",
					    inline=False)
					await message.edit(embed=hellp)
					await message.remove_reaction(reaction, user)
				elif str(reaction.emoji) == "◀️" and cur_page > 1:
					cur_page -= 1
					hellp = discord.Embed(title="📲 Apple Devices",
					                      timestamp=datetime.datetime.utcnow(),
					                      color=discord.Color.random())
					hellp.set_footer(text=f"Requested by {ctx.message.author}")
					hellp.add_field(
					    name=f"🗒 Apple Devices for year »",
					    value=
					    f"\n{contents[cur_page-1]}\n\n**Page {cur_page}/{pages}**",
					    inline=False)
					await message.edit(embed=hellp)
					await message.remove_reaction(reaction, user)
				else:
					await message.remove_reaction(reaction, user)
			except asyncio.TimeoutError:
				await message.clear_reactions()
				break


@appledevs.error
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)


skinss = [
    "**Year 2019**\n\n**Gladiator King**\nSeason : April 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Gladiator Queen**\nSeason : May 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**P.E.K.K.A King**\nSeason : June 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Valkyrie Queen**\nSeason : July 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Party Warden**\nSeason : August 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Autumn Queen**\nSeason : September 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Skeleton King**\nSeason : October 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Ice Queen**\nSeason : November 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Jolly King**\nSeason : December 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌",
    "**Year 2020**\n\n**Primal Warden**\nSeason : January 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Warrior Queen¹**\nSeason : January 2020 / February 2021 / February 2022\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Primal King**\nSeason : February 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Primal Queen**\nSeason : March 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Clockwork Warden**\nSeason : April 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Clockwork King**\nSeason : May 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Clockwork Queen**\nSeason : June 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Gladiator Warden**\nSeason : July 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Party King**\nSeason : August 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Pirate Queen**\nSeason : September 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Pirate Warden**\nSeason : October 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Champion King²**\nSeason : October 2020 / November 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Pirate King**\nSeason : November 202\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Winter Champion**\nSeason : December 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌",
    "**Year 2021**\n\n**Warden of the North**\nSeason : January 2021\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Rogue Queen**\nSeason : February 2021\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Warrior King³**\nSeason : February 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Rogue King**\nSeason : March 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Jungle Champion4**\nSeason : April 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Jungle Warden**\nSeason : May 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Jungle Queen**\nSeason : June 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Fierce King5**\nSeason : June 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Jungle King**\nSeason : July 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Party Queen**\nSeason : August 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Beat King6**\nSeason : August 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Gladiator Champion**\nSeason : September 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Warden Maste**\nSeason : October 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Golem King**\nSeason : November 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Champion Queen7**\nSeason : November 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Jolly Warden**\nSeason : December 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Ice King**\nSeason : December 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅",
    "**Year 2022**\n\n**Shadow Queen**\nSeason : January 2022\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Lunar King9³**\nSeason : February 2022\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Warrior Warden**\nSeason : February 2022\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Shadow Champion**\nSeason : March 2022\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Primal Champion10**\nSeason : March 2022\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Shadow King**\nSeason : April 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Shadow Warden11**\nSeason : April 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅"
]


@commands.guild_only()
@commands.has_role(961301374115676170)
@bot.command()
async def skins(ctx):
	channel = bot.get_channel(961310467341549598)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0x00FF00)
		embed.set_author(
		    name="Command logs",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png"
		)
		embed.add_field(name="User",
		                value="{}".format(ctx.message.author),
		                inline=True)
		embed.add_field(name="User id",
		                value="{}".format(ctx.message.author.id),
		                inline=True)
		embed.add_field(name="Server name",
		                value="{}".format(ctx.message.guild.name),
		                inline=False)
		embed.add_field(name="Channel name",
		                value="{}".format(ctx.message.channel.mention),
		                inline=False)
		embed.add_field(name="Command name", value="skins", inline=True)
		embed.set_footer(text='Logged')
		await channel.send(embed=embed)
		pages = 4
		cur_page = 1
		embed = discord.Embed(
		    title="Skins Information",
		    description=
		    f"\n{skinss[cur_page-1]}\n\n**Page {cur_page}/{pages}**",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.random())
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		message = await ctx.reply(embed=embed)
		await message.add_reaction("◀️")
		await message.add_reaction("▶️")

		def check(reaction, user):
			return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

		while True:
			try:
				reaction, user = await bot.wait_for("reaction_add",
				                                    timeout=60,
				                                    check=check)
				if str(reaction.emoji) == "▶️" and cur_page != pages:
					cur_page += 1
					embed = discord.Embed(
					    title="Skins Information",
					    description=
					    f"\n{skinss[cur_page-1]}\n\n**Page {cur_page}/{pages}**",
					    timestamp=datetime.datetime.utcnow(),
					    color=discord.Color.random())
					embed.set_footer(text=f"Requested by {ctx.message.author}")
					await message.edit(embed=embed)
					await message.remove_reaction(reaction, user)
				elif str(reaction.emoji) == "◀️" and cur_page > 1:
					cur_page -= 1
					embed = discord.Embed(
					    title="Skins Information",
					    description=
					    f"\n{skinss[cur_page-1]}\n\n**Page {cur_page}/{pages}**",
					    timestamp=datetime.datetime.utcnow(),
					    color=discord.Color.random())
					embed.set_footer(text=f"Requested by {ctx.message.author}")
					await message.edit(embed=embed)
					await message.remove_reaction(reaction, user)
				else:
					await message.remove_reaction(reaction, user)
			except asyncio.TimeoutError:
				await message.clear_reactions()
				break


@skins.error
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)


# @bot.command()
# async def test(ctx):
#   em = discord.Embed(
#       title="",
#       description="```hdbfhjbda jhabdfuhaif ujsdhafuhucivuhjf jahduhndjvn jhauidfjniue ijhdufhuiahfe ukhdfuiheuf uhjeudfihsdfhnuhef jdhfuhunjf uefhujnf jehfuidfui sdfheuifhnu jhsefjioefb fjehfeuifn jehuiefh efifjieufh UEFHEFHEUFKJ UEFHUIDFHN JUEFHUEF  UEFHEIFUKH EUFUEFUI HEBFUH JDFHUEF JUefhiuefu```",
#       timestamp=datetime.datetime.utcnow(),
#       color=discord.Color.red())
#   em.set_author(
#       name="You can't use the bot commands",
#       icon_url=
#       "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
#   )
#   em.set_footer(text=f"Command used by {ctx.message.author}")
#   await ctx.send(embed=em)

@commands.has_role(961301374115676170)
@bot.command()
@commands.guild_only()
async def tempemails(ctx):
	channel = bot.get_channel(961310467341549598)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0x00FF00)
		embed.set_author(
		    name="Command logs",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png"
		)
		embed.add_field(name="User",
		                value="{}".format(ctx.message.author),
		                inline=True)
		embed.add_field(name="User id",
		                value="{}".format(ctx.message.author.id),
		                inline=True)
		embed.add_field(name="Server name",
		                value="{}".format(ctx.message.guild.name),
		                inline=False)
		embed.add_field(name="Channel name",
		                value="{}".format(ctx.message.channel.mention),
		                inline=False)
		embed.add_field(name="Command name", value="tempemails", inline=True)
		embed.set_footer(text='Logged')
		await channel.send(embed=embed)
		url = "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=5"
		r = requests.get(url)
		h = r.json()
		embed = discord.Embed(
		    title="",
		    description=f"```{h[0]}\n\n{h[1]}\n\n{h[2]}\n\n{h[3]}\n\n{h[4]}```",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.random())
		embed.set_author(
		    name="Generated some temp emails",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif"
		)
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		await ctx.reply(embed=embed)


# @tempemails.error
# async def on_command_error(ctx, error):
# 	######
# 	if isinstance(error, commands.MissingRole):
# 		em = discord.Embed(
# 		    title="",
# 		    description="DM <@920337055706386443> to buy the bot ez",
# 		    timestamp=datetime.datetime.utcnow(),
# 		    color=discord.Color.red())
# 		em.set_author(
# 		    name="You can't use the bot commands",
# 		    icon_url=
# 		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
# 		)
# 		em.set_footer(text=f"Command used by {ctx.message.author}")
# 		await ctx.send(embed=em)


@commands.has_role(961301374115676170)
@bot.command()
@commands.guild_only()
async def inbox(ctx, email: str):
	channel = bot.get_channel(961310467341549598)
	if ctx.guild.id == 961299028128190474:
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0x00FF00)
		embed.set_author(
		    name="Command logs",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png"
		)
		embed.add_field(name="User",value="{}".format(ctx.message.author),
		                inline=True)
		embed.add_field(name="User id",
		                value="{}".format(ctx.message.author.id),
		                inline=True)
		embed.add_field(name="Server name",
		                value="{}".format(ctx.message.guild.name),
		                inline=False)
		embed.add_field(name="Channel name",
		                value="{}".format(ctx.message.channel.mention),
		                inline=False)
		embed.add_field(name="Command name", value="inbox", inline=True)
		embed.set_footer(text='Logged')
		await channel.send(embed=embed)
		ema = email.split("@")
		l = ema[0]
		d = ema[1]
		url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={l}&domain={d}"
		r = requests.get(url)
		h = r.json()
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=discord.Color.random())
		embed.set_author(
		    name=f"Last mail in inbox of {email}",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif"
		)
		embed.add_field(name="Sender's email",
		                value=f"{h[0]['from']}",
		                inline=False)
		embed.add_field(name="Subject",
		                value=f"{h[0]['subject']}",
		                inline=False)
		embed.add_field(
		    name="Date & Time",
		    value=
		    f"{h[0]['date']}\n\n**React with  💬  to see the body of email**",
		    inline=False)
		embed.set_footer(text=f"Requested by {ctx.message.author}")
		mmm = await ctx.reply(embed=embed)
		await mmm.add_reaction("💬")

		def check(reaction, user):
			return user == ctx.author and str(reaction.emoji) in ["💬"]

		while True:
			try:
				reaction, user = await bot.wait_for("reaction_add",
				                                    timeout=60,
				                                    check=check)
				if str(reaction.emoji) == "💬":
					url2 = f"https://www.1secmail.com/api/v1/?action=readMessage&login={l}&domain={d}&id={h[0]['id']}"
					r2 = requests.get(url2)
					h2 = r2.json()
					embed = discord.Embed(
					    title="Body of email",
					    description=f"```{h2['textBody']}```",
					    timestamp=datetime.datetime.utcnow(),
					    color=discord.Color.random())
					embed.set_footer(text=f"Requested by {ctx.message.author}")
					await mmm.edit(embed=embed)
					await mmm.clear_reactions()
				else:
					await mmm.remove_reaction(reaction, user)
			except asyncio.TimeoutError:
				await mmm.clear_reactions()
				break


@inbox.error
async def on_command_error(ctx, error):
	######
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.CommandInvokeError):
		em = discord.Embed(title="",
		                   description="",
		                   timestamp=datetime.datetime.utcnow(),
		                   color=discord.Color.red())
		em.set_author(
		    name="Invalid email",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	######
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0xFF0000)
		embed.add_field(name="Usage",
		                value="``+inbox <tempemail>``",
		                inline=False)
		embed.add_field(name="Example ",
		                value="``+inbox bhdhvbha@yahoo.com``",
		                inline=False)
		embed.set_author(
		    name="Invalid syntax",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png"
		)
		embed.set_footer(text=f'Command used by {ctx.message.author}')
		await ctx.send(embed=embed)


@commands.has_role(961301374115676170)
@bot.command()
@commands.guild_only()
async def info(ctx, tag: str):
  channel = bot.get_channel(961310467341549598)
  if ctx.guild.id == 961299028128190474:
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
    embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
    embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
    embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
    embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
    embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
    embed.add_field(name="Command name", value="info", inline=True)
    embed.set_footer(text='Logged')
    await channel.send(embed=embed)
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
    embed.set_author(name="Loading..",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif")
    mmm = await ctx.reply(embed=embed)
    player = await coc_client.get_player(tag)
    clanname = player.clan
    if player.clan == None:
      clanname = "Not in clan"
      clantag = "None"
    else:
      clantag =  player.clan.tag
    e = discord.Embed(title=f"{player.name} {player.tag}",description=f"**Town hall level :** {player.town_hall}\n**XP Level :** {player.exp_level}\n**War stars :** {player.war_stars}\n**Clan name :** {clanname}\n**Clan tag :** {clantag}",timestamp=datetime.datetime.utcnow(),colour=discord.Colour.random())
    l = player.league.icon.url
    if l == None:
      l = "https://cdn.discordapp.com/attachments/936276886852603945/971646122210787379/e--YMyIexEQQhE4imLoJcwhYn6Uy8KqlgyY3_kFV6t4.png"
    e.set_thumbnail(url=l)
    e.add_field(name="Town hall weapon level",value=player.town_hall_weapon,inline=False)
    e.add_field(name="Attack wins", value=player.attack_wins, inline=True)
    e.add_field(name="Defence wins", value=player.defense_wins,inline=True)
    e.add_field(name="Donation given",value=player.donations,inline=False)
    e.add_field(name="Donation received",value=player.received,inline=False)
    e.add_field(name="All time best",value=player.best_trophies,inline=False)
    try:
      e.add_field(name="Legend trophies",value=player.legend_statistics.legend_trophies,inline=False)
    except:
      e.add_field(name="Legend trophies",value="0 legend trophies",inline=False)
    if "#" in tag:
      tag1 = tag.replace("#","")
    url = f"https://www.clashofstats.com/players/{tag1}/summary"
    data = requests.get(url)
    doc = BeautifulSoup(data.text, "html.parser")
    her = doc.find_all("span",class_="progress-list__value")[0].text
    oes = doc.find_all("span",class_="small-secondary-text")[0].text
    heroes = her + oes
    tro = doc.find_all("span",class_="progress-list__value")[1].text
    ops = doc.find_all("span",class_="small-secondary-text")[1].text
    troops = tro + ops
    spe = doc.find_all("span",class_="progress-list__value")[2].text
    lls = doc.find_all("span",class_="small-secondary-text")[2].text
    spells = spe + lls
    bbhero1 = doc.find_all("span",class_="progress-list__value")[3].text
    bbhero2 = doc.find_all("span",class_="small-secondary-text")[3].text
    bbhero = bbhero1 + bbhero2
    bbtro = doc.find_all("span",class_="progress-list__value")[4].text
    bbops = doc.find_all("span",class_="small-secondary-text")[4].text
    bbtroops = bbtro + bbops
    heromoji = get(ctx.message.guild.emojis, name="heroes")
    troopmoji = get(ctx.message.guild.emojis, name="troop")
    spemoji = get(ctx.message.guild.emojis, name="spell")
    bbtroopmoji = get(ctx.message.guild.emojis, name="bbtroop")
    bbheromoji = get(ctx.message.guild.emojis, name="bbhero")
    e.add_field(name="Home Village", value=f'**{heromoji}Heroes** ``{heroes.replace(" ", "")}``\n**{troopmoji}Troops** ``{troops.replace(" ", "")}``\n**{spemoji}Spells** ``{spells.replace(" ", "")}``',inline=False)
    e.add_field(name="Builder Base", value=f'**{bbheromoji}Battle Machine** ``{bbhero.replace(" ", "")}``\n**{bbtroopmoji}Troops** ``{bbtroops.replace(" ", "")}``',inline=True)
    e.add_field(name="Links", value=f"[Open in game]({player.share_link})\n[Clash of Stats]({url})",inline=False)
    e.set_footer(text=f"Requested by {ctx.message.author}")
    await mmm.edit(embed=e)

@commands.has_role(961301374115676170)
@bot.command()
@commands.guild_only()
async def getacc(ctx, season: str, rank: int):
  channel = bot.get_channel(961310467341549598)
  if ctx.guild.id == 961299028128190474:
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
    embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
    embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
    embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
    embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
    embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
    embed.add_field(name="Command name", value="getacc", inline=True)
    embed.set_footer(text='Logged')
    await channel.send(embed=embed)
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
    embed.set_author(name="Loading..",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif")
    embed.set_footer(text=f'Requested by {ctx.message.author}')
    mmm = await ctx.reply(embed=embed)
    page = rank/200
    check_float = isinstance(page, float)
    if check_float is True:
      page = math.ceil(page)   
    url = f"https://clashspot.net/en/rankings/players-legend-league/season/{season}/players?p={page}"
    data1 = requests.get(f"https://clashspot.net/en/rankings/players-legend-league/season/{season}/players")
    doc1 = BeautifulSoup(data1.text, "html.parser")
    limit = doc1.find_all("strong")[0].text.replace(",","").replace(" players","")
    if rank>int(limit):
      embed = discord.Embed(title=f"Last rank of season ``{season}`` is ``{limit}``!",timestamp=datetime.datetime.utcnow(),color=discord.Color.red())
      await ctx.reply(embed=embed)
    else:
      data = requests.get(url)
      doc = BeautifulSoup(data.text, "html.parser")
      findrank = doc.find_all("td",class_="col-position")
      for i in range(len(findrank)):
        if findrank[i].text.strip().replace(",","").replace(".","") == f"{rank}":
          player = await coc_client.get_player(doc.find_all("span",class_="player-tag")[i].text)
          clanname = player.clan
          if player.clan == None:
            clanname = "Not in clan"
            clantag = "None"
          else:
            clantag =  player.clan.tag
          e = discord.Embed(title=f"{player.name} {player.tag}",description=f"**Season :** ``{season}`` **Rank : ** ``{rank}``\n**Town hall level :** {player.town_hall}\n**XP Level :** {player.exp_level}\n**War stars :** {player.war_stars}\n**Clan name :** {clanname}\n**Clan tag :** {clantag}",timestamp=datetime.datetime.utcnow(),colour=discord.Colour.random())
          l = player.league.icon.url
          if l == None:
            l = "https://cdn.discordapp.com/attachments/936276886852603945/971646122210787379/e--YMyIexEQQhE4imLoJcwhYn6Uy8KqlgyY3_kFV6t4.png"
          e.set_thumbnail(url=l)
          e.add_field(name="Town hall weapon level",value=player.town_hall_weapon,inline=False)
          e.add_field(name="Attack wins", value=player.attack_wins, inline=True)
          e.add_field(name="Defence wins", value=player.defense_wins,inline=True)
          e.add_field(name="Donation given",value=player.donations,inline=False)
          e.add_field(name="Donation received",value=player.received,inline=False)
          e.add_field(name="All time best",value=player.best_trophies,inline=False)
          try:
            e.add_field(name="Legend trophies",value=player.legend_statistics.legend_trophies,inline=False)
          except:
            e.add_field(name="Legend trophies",value="0 legend trophies",inline=False)
          if "#" in player.tag:
            tag1 = player.tag.replace("#","")
          e.add_field(name="Links", value=f"[Open in game]({player.share_link})\n[Clash of Stats]({url})",inline=False)
          e.set_footer(text=f"Requested by {ctx.message.author}")
          await mmm.edit(embed=e)

@getacc.error
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.CommandInvokeError):
		em = discord.Embed(title="",
		                   description="The specified season could be wrong or The player have been banned",
		                   timestamp=datetime.datetime.utcnow(),
		                   color=discord.Color.red())
		em.set_author(
		    name="ERROR",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0xFF0000)
		embed.add_field(name="Usage", value="``+getacc <SEASON> <RANK>``", inline=False)
		embed.add_field(name="Example",
		                value="``+getacc 2017-05 5``",
		                inline=False)
		embed.set_author(
		    name="Invalid syntax",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png"
		)
		embed.set_footer(text=f'Command used by {ctx.message.author}')
		await ctx.send(embed=embed)
  
@info.error
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(
		    title="",
		    description="DM <@920337055706386443> to buy the bot ez",
		    timestamp=datetime.datetime.utcnow(),
		    color=discord.Color.red())
		em.set_author(
		    name="You can't use the bot commands",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.CommandInvokeError):
		em = discord.Embed(title="",
		                   description="",
		                   timestamp=datetime.datetime.utcnow(),
		                   color=discord.Color.red())
		em.set_author(
		    name="Invalid tag",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
		)
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="",
		                      timestamp=datetime.datetime.utcnow(),
		                      color=0xFF0000)
		embed.add_field(name="Usage", value="``+info <TAG>``", inline=False)
		embed.add_field(name="Example",
		                value="``+info #2PYPP02Q``",
		                inline=False)
		embed.set_author(
		    name="Invalid syntax",
		    icon_url=
		    "https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png"
		)
		embed.set_footer(text=f'Command used by {ctx.message.author}')
		await ctx.send(embed=embed)


# @commands.cooldown(1, 5, commands.BucketType.default)
# @commands.has_role(961301374115676170)
# @bot.command()
# @commands.guild_only()
# async def troops(ctx, tag: str):
#   channel = bot.get_channel(961310467341549598)
#   if ctx.guild.id == 961299028128190474:
#     embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
#     embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
#     embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
#     embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
#     embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
#     embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
#     embed.add_field(name="Command name", value="troops", inline=True)
#     embed.set_footer(text='Logged')
#     await channel.send(embed=embed)
#     p = discord.Embed(title="",timestamp=datetime.datetime.utcnow(), color=discord.Color.random())
#     p.set_author(name="Loading..",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/958779583606444032/output-onlinegiftools.gif")
#     mmm = await ctx.reply(embed=p)
#     player = await coc_client.get_player(tag)
#     if '#' in tag:
#       tag1 = tag.split('#')
#       tag1 = tag1[1]
#     else:
#       tag1 = tag
#     option = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(executable_path="BraveSoftware/Brave-Browser/Application/brave.exe", options=option)
#     driver.maximize_window()
    
#     driver.get(f'https://www.clashofstats.com/players/{tag1}/army#tabs')
#     time.sleep(1)
#     driver.execute_script("window.scrollBy(0,50)", "")
#     time.sleep(1)
#     driver.get_screenshot_as_file("troops1.png")
#     driver.quit()
#     im = Image.open('troops1.png')
    
#     width, height = im.size
    
#     left = 0
#     top = 0
#     right = 784
#     bottom = 533
#     im1 = im.crop((left, top, right, bottom))
#     im1 = im1.save("troops1.png")
#     e = discord.Embed(title=f"{player.name} {player.tag}",description="**Troops**",colour=discord.Colour.random())
    
#     file = discord.File("troops1.png", filename="troops1.png")
#     e.set_image(url="attachment://troops1.png")
#     await ctx.send(file=file, embed=e)
#     embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
#     embed.set_author(name="Process completed",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif")
#     embed.set_footer(text=f"Requested by {ctx.message.author}")
#     await mmm.edit(embed=embed)


# @troops.error
# async def on_command_error(ctx, error):
# 	if isinstance(error, commands.MissingRole):
# 		em = discord.Embed(
# 		    title="",
# 		    description="DM <@920337055706386443> to buy the bot ez",
# 		    timestamp=datetime.datetime.utcnow(),
# 		    color=discord.Color.red())
# 		em.set_author(
# 		    name="You can't use the bot commands",
# 		    icon_url=
# 		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
# 		)
# 		em.set_footer(text=f"Command used by {ctx.message.author}")
# 		await ctx.send(embed=em)
# 	if isinstance(error, commands.CommandInvokeError):
# 		em = discord.Embed(title="",
# 		                   description="",
# 		                   timestamp=datetime.datetime.utcnow(),
# 		                   color=discord.Color.red())
# 		em.set_author(
# 		    name="Invalid tag",
# 		    icon_url=
# 		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
# 		)
# 		em.set_footer(text=f"Command used by {ctx.message.author}")
# 		await ctx.send(embed=em)
# 	if isinstance(error, commands.MissingRequiredArgument):
# 		embed = discord.Embed(title="",
# 		                      timestamp=datetime.datetime.utcnow(),
# 		                      color=0xFF0000)
# 		embed.add_field(name="Usage", value="``+troops <TAG>``", inline=False)
# 		embed.add_field(name="Example",
# 		                value="``+troops #2PYPP02Q``",
# 		                inline=False)
# 		embed.set_author(
# 		    name="Invalid syntax",
# 		    icon_url=
# 		    "https://cdn.discordapp.com/attachments/936276886852603945/959042350586400828/er.png"
# 		)
# 		embed.set_footer(text=f'Command used by {ctx.message.author}')
# 		await ctx.send(embed=embed)
# 	if isinstance(error, commands.CommandOnCooldown):
# 		em = discord.Embed(
# 		    title="",
# 		    description=f"Try again in {error.retry_after:.2f}s.",
# 		    timestamp=datetime.datetime.utcnow(),
# 		    color=discord.Color.red())
# 		em.set_author(
# 		    name="Hold On",
# 		    icon_url=
# 		    "https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png"
# 		)
# 		em.set_footer(text=f"Command used by {ctx.message.author}")
# 		await ctx.send(embed=em)
# @bot.event
# async def on_message(message):
#   if "phish" in message.content:
#     await message.delete()
#     mmm = await message.channel.send("Don't mention 🎣 type of word again!")
#     await asyncio.sleep(2)
#     await mmm.delete()


# Owner commands #
    
@commands.has_role(961330754539888670)
@bot.command()
@commands.guild_only()
async def cdt(ctx):
  m = open("sorteddeadtags.json","r",encoding="utf8")
  data = json.load(m)
  await ctx.reply(f"Total dead tags in database : {len(data)}")

@commands.has_role(961330754539888670)
@bot.command()
@commands.guild_only()
async def restart(ctx):
  channel = bot.get_channel(961310467341549598)
  if ctx.guild.id == 961299028128190474:
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
    embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
    embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
    embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
    embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
    embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
    embed.add_field(name="Command name", value="restart", inline=True)
    embed.set_footer(text='Logged')
    await channel.send(embed=embed)
    em = discord.Embed(title="Restarting...",description=f"",timestamp=datetime.datetime.utcnow(),color=discord.Color.red())
    em.set_footer(text=f"Command used by {ctx.message.author}")
    await ctx.reply(embed=em)
    system("python restarter.py")
    system('kill 1')

@commands.has_role(961330754539888670)
@bot.command(name="cc")
@commands.guild_only()
async def id_(ctx, user: discord.Member):
  channel = bot.get_channel(961310467341549598)
  if ctx.guild.id == 961299028128190474:
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
    embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
    embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
    embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
    embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
    embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
    embed.add_field(name="Command name", value="cc", inline=True)
    embed.set_footer(text='Logged')
    await channel.send(embed=embed)
    guild = bot.guilds[0]
    nox = await bot.fetch_user(920337055706386443)
    category = discord.utils.get(ctx.guild.categories, name="BUYΞRS 4")
    overwrites = {
      guild.default_role:
      discord.PermissionOverwrite(read_messages=False),
      guild.me:
      discord.PermissionOverwrite(read_messages=True),
      nox:  discord.PermissionOverwrite(read_messages=True, send_messages=True),
      user: discord.PermissionOverwrite(read_messages=True, send_messages=True)
    }
    channel = await guild.create_text_channel(f'{user}',overwrites=overwrites,reason=None,category=category)
    em = discord.Embed(title="",description=f"{channel.mention}",timestamp=datetime.datetime.utcnow(),color=discord.Color.red())
    em.set_author(name=f"Created channel for {user}",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif")
    em.set_footer(text=f"Command used by {ctx.message.author}")
    await ctx.reply(embed=em)

@cdt.error
@restart.error
@id_.error
async def on_command_error(ctx, error):
	######
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(title="",description="Dumbass",timestamp=datetime.datetime.utcnow(),color=discord.Color.red())
		em.set_author(name="You can't use this bot command",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png")
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)


# restarter bot #

bot2 = commands.Bot(command_prefix='>',
                   guild_subscriptions=True,                  activity=discord.Activity(type=discord.ActivityType.watching, name='EVERYONE'),
                   case_insensitive=True,
                   intents=discord.Intents.all())
bot2.remove_command('help')


@bot2.event
async def on_ready():
  print(f"{bot2.user.name} IS UP!")
  channel = bot2.get_channel(1000659983081414729)
  em = discord.Embed(title="",description=f"",timestamp=datetime.datetime.utcnow(),color=discord.Color.green())
  em.set_author(name="Bot restarted",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
  await channel.send(embed=em)

@commands.has_role(961330754539888670)
@bot2.command()
@commands.guild_only()
async def reboot(ctx):
  channel = bot2.get_channel(961310467341549598)
  if ctx.guild.id == 961299028128190474:
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
    embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
    embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
    embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
    embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
    embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
    embed.add_field(name="Command name", value="restart", inline=True)
    embed.set_footer(text='Logged')
    await channel.send(embed=embed)
    em = discord.Embed(title="Restarting....",description=f"",timestamp=datetime.datetime.utcnow(),color=discord.Color.red())
    em.set_footer(text=f"Command used by {ctx.message.author}")
    await ctx.reply(embed=em)
    system("python restarter.py")
    system('kill 1')

@reboot.error
async def on_command_error(ctx, error):
	######
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(title="",description="Dumbass",timestamp=datetime.datetime.utcnow(),color=discord.Color.red())
		em.set_author(name="You can't use this bot command",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png")
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)

# bot.run(os.environ['TOKEN'])
# bot2.run(os.environ['TOKEN2'])
try:
  bot.run(os.environ['TOKEN'])
  # loop = asyncio.get_event_loop()
  # loop.create_task(bot.start(os.environ['TOKEN']))
  # # loop.create_task(bot2.start(os.environ['TOKEN2']))
  # loop.run_forever()
except discord.errors.HTTPException:
  print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
  system("restarter.py")
  system('kill 1')

@cdt.error
@restart.error
@id_.error
async def on_command_error(ctx, error):
	######
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(title="",description="Dumbass",timestamp=datetime.datetime.utcnow(),color=discord.Color.red())
		em.set_author(name="You can't use this bot command",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png")
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)


# restarter bot #

bot2 = commands.Bot(command_prefix='>',
                   guild_subscriptions=True,                  activity=discord.Activity(type=discord.ActivityType.watching, name='EVERYONE'),
                   case_insensitive=True,
                   intents=discord.Intents.all())
bot2.remove_command('help')


@bot2.event
async def on_ready():
  print(f"{bot2.user.name} IS UP!")
  channel = bot2.get_channel(1000659983081414729)
  em = discord.Embed(title="",description=f"",timestamp=datetime.datetime.utcnow(),color=discord.Color.green())
  em.set_author(name="Bot restarted",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
  await channel.send(embed=em)

@commands.has_role(961330754539888670)
@bot2.command()
@commands.guild_only()
async def reboot(ctx):
  channel = bot2.get_channel(961310467341549598)
  if ctx.guild.id == 961299028128190474:
    embed = discord.Embed(title="",timestamp=datetime.datetime.utcnow(),color=0x00FF00)
    embed.set_author(name="Command logs",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/961701740732882954/notepad-icon-png-14.png")
    embed.add_field(name="User",value="{}".format(ctx.message.author),inline=True)
    embed.add_field(name="User id",value="{}".format(ctx.message.author.id),inline=True)
    embed.add_field(name="Server name",value="{}".format(ctx.message.guild.name),inline=False)
    embed.add_field(name="Channel name",value="{}".format(ctx.message.channel.mention),inline=False)
    embed.add_field(name="Command name", value="restart", inline=True)
    embed.set_footer(text='Logged')
    await channel.send(embed=embed)
    em = discord.Embed(title="Restarting....",description=f"",timestamp=datetime.datetime.utcnow(),color=discord.Color.red())
    em.set_footer(text=f"Command used by {ctx.message.author}")
    await ctx.reply(embed=em)
    system("python restarter.py")
    system('kill 1')

@reboot.error
async def on_command_error(ctx, error):
	######
	if isinstance(error, commands.MissingRole):
		em = discord.Embed(title="",description="Dumbass",timestamp=datetime.datetime.utcnow(),color=discord.Color.red())
		em.set_author(name="You can't use this bot command",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959898325786693642/1024px-Cross_red_circle.svg.png")
		em.set_footer(text=f"Command used by {ctx.message.author}")
		await ctx.send(embed=em)

# bot.run(os.environ['TOKEN'])
# bot2.run(os.environ['TOKEN2'])
try:
  bot.run(os.environ['TOKEN'])
  # loop = asyncio.get_event_loop()
  # loop.create_task(bot.start(os.environ['TOKEN']))
  # # loop.create_task(bot2.start(os.environ['TOKEN2']))
  # loop.run_forever()
except discord.errors.HTTPException:
  print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
  system("restarter.py")
  system('kill 1')