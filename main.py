import requests
import coc
import logging
from bs4 import BeautifulSoup
from pymongo import MongoClient
import discord
from discord.ext import commands
import os
import dns
from discord import SlashCommand, option, guild_only, slash_command,components
from discord.ui import Button, View
from Commands.Admin import admin
from Functions import embeds, utils
from datetime import datetime
import json
from PIL import Image, ImageOps, ImageDraw, ImageFont
import string
import random
import pandas as pd
from matplotlib import pyplot as plt

# import dns.resolver
# dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
# dns.resolver.default_resolver.nameservers=['8.8.8.8']

####### +++++++++++++ DISCORD CLIENT +++++++++++++ #######

bot = commands.Bot(command_prefix=commands.when_mentioned,activity=discord.Activity(type=discord.ActivityType.watching, name="Over OTTOVΞRSΞ"))
bot.remove_command('help')

####### +++++++++++++ COC CLIENT +++++++++++++ #######

coc_client = coc.Client(key_names='otv2')

async def startClient(email, password):
    try:
        await coc_client.login(email=email, password=password)
        print(f"[+] cocClient")
    except Exception as Exc:
        print(f"Failed to setup clash api connection {Exc}")
        exit(1)


####### +++++++++++++ CONFIG +++++++++++++ #######

owner_ids = [920337055706386443, 1070704786573365248, 970187989596647514, 1072268303776612513]
log_channel_id = 1011155977736818759
server_ids = [961299028128190474]
public_channels = [987993252869312512,962246729200185364,961299028128190477,1000964661606359051,1000002641918689291,961302065001398322,968161031237021706]

####### +++++++++++++ SOME OTHER CONFIGS +++++++++++++ #######

billing_addresses_list = ["Kaiden Reynolds Jr.\n1002 S Pantano Rd\nTucson\nArkansas\n85710\nUS","Garvit Lodu\n1002 S Pantano Rd\nTucson\nArkansas\n85710\nUS","Rachael Keebler\n35433 Kenai Spur Hwy\nSoldotna\nAlabama\n99669\nUS","Deron O'Conner\n3142 SE Military Dr a129\nSan Antonio\nTexas\n78223\nUS"]

####### +++++++++++++ MONGO CLIENTS +++++++++++++ #######

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

newfat = ['201508', '201509', '201510', '201511', '201512', '201601', '201602', '201603', '201604', '201605', '201606', '201607', '201608', '201609', '201610', '201611', '201612', '201701', '201702', '201703', '201704', '201705', '201706', '201707', '201708', '201709', '201710', '201711', '201712', '201801', '201802', '201803', '201804', '201805', '201806', '201807', '201808', '201809', '201810', '201811', '201812', '201901', '201902', '201903', '201904', '201905']
afternewfat = ['201906', '201907', '201908', '201909', '201910', '201911', '201912', '202001', '202002', '202003', '202004', '202005']
afterafternewfat = ['202006', '202007', '202008', '202009', '202010', '202011', '202012', '202101']
a3newfat = ['202102', '202103', '202104', '202105', '202106', '202107']
a4newfat = ['202108', '202109', '202110', '202111', '202112']

@bot.event
async def on_ready():
    await startClient('onkardsagare2@gmail.com', 'Onkarcocapi@1234')
    print(f"[+] {bot.user} IS UP!")

####### +++++++++++++ OWNER COMMANDS +++++++++++++ #######

## +++++++++++++ GIVE PERMS COMMAND +++++++++++++ ##

@bot.slash_command(name="give_perms",description="OWNER'S COMMAND",guild_ids=server_ids)
@guild_only()
@option("user", description="Enter the username")
@option("sub", description="Enter sub type", choices=["Lifetime","7 Months", "2 Months and 2 weeks", "1 Month"])
async def give_command(ctx: discord.ApplicationContext,user: discord.User,sub: str,):
    if ctx.author.id in owner_ids:
        channel = bot.get_channel(int(log_channel_id))
        await channel.send(embed=embeds.logger(ctx,"give perms"))
        res = await admin.give_perms(user.id,sub)
        embed = discord.Embed(title="",description=f"**{user.mention} has been given {sub} perms!**\n\n**Started on :** {res[1]}\n**Expires on :** {res[2]}",timestamp=datetime.now(),color=0x0070fa)
        if user.avatar == None:
          url = "https://cdn.discordapp.com/embed/avatars/4.png"
        else: 
          url = user.avatar.url
        embed.set_thumbnail(url=url)
        await ctx.respond(embed=embed)
    else:
        await ctx.respond(f"You don't have permission to use this command!")

@bot.slash_command(name="give_perms2",description="OWNER'S COMMAND",guild_ids=server_ids)
@guild_only()
@option("user", description="Enter the username")
@option("sub", description="Enter sub type", choices=["Lifetime","7 Months", "2 Months and 2 weeks", "1 Month"])
async def give2_command(ctx: discord.ApplicationContext,user: discord.User,started: str,end: str,sub):
    if ctx.author.id in owner_ids:
        channel = bot.get_channel(int(log_channel_id))
        await channel.send(embed=embeds.logger(ctx,"give perms2"))
        res = await admin.give_perms2(user.id,started,end,sub)
        embed = discord.Embed(title="",description=f"**{user.mention} has been given {sub} perms!**\n\n**Started on :** {res[1]}\n**Expires on :** {res[2]}",timestamp=datetime.now(),color=0x0070fa)
        if user.avatar == None:
          url = "https://cdn.discordapp.com/embed/avatars/4.png"
        else: 
          url = user.avatar.url
        embed.set_thumbnail(url=url)
        await ctx.respond(embed=embed)
    else:
        await ctx.respond(f"You don't have permission to use this command!")

## +++++++++++++ REMOVE PERMS COMMAND +++++++++++++ ##

@bot.slash_command(name="remove_perms",description="OWNER'S COMMAND",guild_ids=server_ids)
@guild_only()
@option("user", description="Enter the username")
async def remove_command(ctx: discord.ApplicationContext,user: discord.User):
    if ctx.author.id in owner_ids:
        channel = bot.get_channel(int(log_channel_id))
        await channel.send(embed=embeds.logger(ctx,"remove perms"))
        res = await admin.remove_perms(user.id)

        if res == "REMOVED":
            embed = discord.Embed(title="",description=f"**Removed perms from {user.mention}**",timestamp=datetime.now(),color=0x0070fa)
            if user.avatar == None:
              url = "https://cdn.discordapp.com/embed/avatars/4.png"
            else: 
              url = user.avatar.url
            embed.set_thumbnail(url=url)
            await ctx.respond(embed=embed)
        elif res == "USER NOT FOUND":
            embed = discord.Embed(title="",description=f"**{user.mention} is not a buyer**",timestamp=datetime.now(),color=0x0070fa)
            if user.avatar == None:
              url = "https://cdn.discordapp.com/embed/avatars/4.png"
            else: 
              url = user.avatar.url
            embed.set_thumbnail(url=url)
            await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(title="",description=f"**ERROR IN DATA**",timestamp=datetime.now(),color=0x0070fa)
            if user.avatar == None:
              url = "https://cdn.discordapp.com/embed/avatars/4.png"
            else: 
              url = user.avatar.url
            embed.set_thumbnail(url=url)
            await ctx.respond(embed=embed)
    else:
        await ctx.respond(f"You don't have permission to use this command!")

## +++++++++++++  BUYERS LIST COMMAND +++++++++++++ ##

# class BuyersListView(View):
#     def __init__(self, ctx,list):
#         super().__init__(timeout=600)
#         self.ctx = ctx
#         self.list = list
#         self.cursor = 1
#     @discord.ui.button(label="", style=discord.ButtonStyle.primary,emoji="▶")
#     async def button_callback(self, button, interaction):
#         line = '\n'.join(map(str, self.list[0+(25*self.cursor):25+(25*self.cursor)]))
#         embed = discord.Embed(title=f"",description=line,timestamp=datetime.now(),color=0x0070fa)
#         embed.set_author(name=f"BUYERS")
#         self.cursor = self.cursor + 1
#         if self.cursor == 8: 
#             self.clear_items()
#         await interaction.response.edit_message(embed=embed,view=self)

@bot.slash_command(name="buyer",description="OWNER'S COMMAND",guild_ids=server_ids)
@guild_only()
async def buyer_command(ctx: discord.ApplicationContext, user: discord.User):
    if utils.is_buyer_valid(str(user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            await ctx.defer()
            channel = bot.get_channel(int(log_channel_id))
            await channel.send(embed=embeds.logger(ctx,"perms"))
            f = open("Database/buyers_data.json","r")
            data = json.load(f)
            for i in range(len(data)):
                if data[i]["user_id"] == str(user.id):
                    embed = discord.Embed(title="",description=f"**{user.mention} PERMS INFO**\n\n**Subscription type :** {data[i]['user_data']['sub_type']}\n**Started on :** {data[i]['user_data']['sub_start']}\n**Expires on :** {data[i]['user_data']['sub_end']}",timestamp=datetime.now(),color=0x0070fa)
                    if user.avatar == None:
                      url = "https://cdn.discordapp.com/embed/avatars/4.png"
                    else: 
                      url = user.avatar.url
                    embed.set_thumbnail(url=url)
                    await ctx.respond(embed=embed)
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))

## +++++++++++++ DEVICES COMMAND +++++++++++++ ##

country_names = ['Afghanistan', 'Ãƒâ€¦land-Islands', 'Albania', 'Algeria', 'American-samoa', 'AndorrA', 'Angola', 'Anguilla', 'Antarctica', 'Antigua-and-barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia-and-Herzegovina', 'Botswana', 'Bouvet-Island', 'Brazil', 'British-indian-ocean-territory', 'Brunei-Darussalam', 'Bulgaria', 'Burkina-faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape-Verde', 'Cayman-Islands', 'Central-african-republic', 'Chad', 'Chile', 'China', 'Christmas-Island', 'Cocos-Islands', 'Colombia', 'Comoros', 'Congo', 'Congo-new', 'Cook-islands', 'Costa-rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech-republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican-republic', 'Ecuador', 'Egypt', 'El-salvador', 'Equatorial-guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland-islands-(malvinas)', 'Faroe-islands', 'Fiji', 'Finland', 'France', 'French-guiana', 'French-polynesia', 'French-southern-territories', 'Gabon', 'Gambia', 'Georgia', 'Germany',
'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard-island-and-mcdonald-islands', 'Holy-see-(vatican-city-state)', 'Honduras', 'Hong-kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle-of-man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'North-korea', 'South-korea', 'Kuwait', 'Kyrgyzstan', 'Lao-people"s-democratic-republic', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libyan-arab-jamahiriya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia,-the-former-yugoslav-republic-of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall-islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia,-federated-states-of', 'Moldova,-republic-of', 'Monaco', 'Mongolia', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'Netherlands-antilles', 'New-caledonia', 'New-zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk-island', 'Northern-mariana-islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian-territory,-occupied', 'Panama', 'Papua-new-guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto-rico', 'Qatar', 'Reunion', 'Romania', 'Russia', 'RWANDA', 'Saint-helena', 'Saint-kitts-and-nevis', 'Saint-lucia', 'Saint-pierre-and-miquelon', 'Saint-vincent-and-the-grenadines', 'Samoa', 'San-marino', 'Sao-tome-and-principe', 'Saudi-arabia', 'Senegal', 'Serbia-and-Montenegro', 'Montenegro', 'Serbia', 'Seychelles', 'Sierra-leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon-islands', 'Somalia', 'South-africa', 'South-georgia-and-the-south-sandwich-islands', 'Spain', 'Sri-lanka', 'Sudan', 'Suriname', 'Svalbard-and-jan-mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian-arab-republic', 'Taiwan', 'Tajikistan', 'Tanzania,-united-republic-of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad-and-tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks-and-caicos-islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United-arab-emirates', 'United-kingdom', 'United-states-of-america', 'United-states-minor-outlying-islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Virgin-islands,-british', 'Virgin-islands,-u.s.', 'Wallis-and-futuna', 'Western-sahara', 'Yemen', 'Zambia', 'Zimbabwe']

async def complete_country_name(ctx: discord.AutocompleteContext):
    return [name for name in country_names if name.startswith(ctx.value.lower().capitalize())]

@bot.slash_command(name="devices",description="Get stats of most used device brands yearly in the given country",guild_ids=server_ids)
@guild_only()
@commands.cooldown(1, 25, commands.BucketType.guild)
@option("country", description="Enter the country name",autocomplete=complete_country_name)
@option("from_year", description="Enter the starting year",choices=[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022])
@option("till_year", description="Enter the ending year",choices=[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022])
async def dev_command(ctx: discord.ApplicationContext,country: str ,from_year: int, till_year: int):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            if from_year >= till_year:
                embed = discord.Embed(title="",description="``from_year`` **must be lower than** ``till_year``",color=0x0070fa)
                embed.set_author( name="Invalid syntax",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/1006471087741218856/image9876t.png")
                await ctx.respond(embed=embed)
            else:
                await ctx.defer()
                channel = bot.get_channel(int(log_channel_id))
                await channel.send(embed=embeds.logger(ctx,"devices"))
                region = country.lower().capitalize()
                with open('Database/country_code.json', 'r') as f:
                    it = json.load(f)
                    country_code = it[region]
                url = f"https://gs.statcounter.com/vendor-market-share/mobile-tablet/{country}/chart.php?bar=1&device=Mobile%20%26%20Tablet&device_hidden=mobile%2Btablet&multi-device=true&statType_hidden=vendor&region_hidden={country_code}&granularity=yearly&statType=Device%20Vendor&region={region}&fromInt={from_year}&toInt={till_year}&fromYear={from_year}&toYear={till_year}&csv=1"

                data = pd.read_csv(url, on_bad_lines="skip")
                data.head()
                df = pd.DataFrame(data)
                
                name = df['Device Vendor'].head(10)
                percentage = df[df.columns[1]].head(10)

                fig, ax = plt.subplots(figsize =(16, 9))

                ax.barh(name, percentage)

                for s in ['top', 'bottom', 'left', 'right']:
                    ax.spines[s].set_visible(False)

                ax.xaxis.set_ticks_position('none')
                ax.yaxis.set_ticks_position('none')
                
                ax.xaxis.set_tick_params(pad = 5)
                ax.yaxis.set_tick_params(pad = 10)

                ax.invert_yaxis()

                for i in ax.patches:
                    plt.text(i.get_width()+0.2, i.get_y()+0.5,
                            str(round((i.get_width()), 2))+"%",
                            fontsize = 10, fontweight ='bold',
                            color ='grey')
                
                plt.savefig('Assets/deviceschart.png', bbox_inches='tight')
                f = discord.File("Assets/deviceschart.png", filename="deviceschart.png")
                await ctx.respond(file=f)
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))

## +++++++++++++ ANDROIDS COMMAND +++++++++++++ ##

@bot.slash_command(name="androids",description="Get most used android devices currently in the given country",guild_ids=server_ids)
@guild_only()
@option("country", description="Enter the country name",autocomplete=complete_country_name)
async def androids_command(ctx: discord.ApplicationContext,country: str):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            await ctx.defer()
            channel = bot.get_channel(int(log_channel_id))
            await channel.send(embed=embeds.logger(ctx,"androids"))
            region = country.lower().capitalize()
            with open('Database/country_code.json', 'r') as f:
                it = json.load(f)
                country_code = it[region]
            url = f"https://www.appbrain.com/stats/top-android-phones-tablets-by-country?country={country_code}"
            data = requests.get(url)
            doc = BeautifulSoup(data.text, "html.parser")
            j = doc.find_all("script")[11]
            a = f"{j}"
            k = a.split("=")[4]
            p = k[10:]
            p = p.split(',"header"')
            p = p[0]
            with open("Database/androids.json", "w") as outfile:
                outfile.write(p)
            f = open('Database/androids.json')
            d = json.load(f)
            list = []
            for i in range(len(d)):
                list.append(d[i]["modelName"])
            line = '\n\n'.join(map(str, list))
            embed = discord.Embed(title=f"",description=f"{line}",timestamp=datetime.now(),color=0x0070fa)
            embed.set_author(name=f"Mostly used android devices in {country}")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/936276886852603945/1007595665486000209/IMG-20220812-WA0002.jpg")
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))

## +++++++++++++ APPLE DEVS COMMAND +++++++++++++ ##

@bot.slash_command(name="apples",description="Get info about most used apple devices yearly",guild_ids=server_ids)
@guild_only()
async def appledevs_command(ctx: discord.ApplicationContext):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            await ctx.defer()
            channel = bot.get_channel(int(log_channel_id))
            await channel.send(embed=embeds.logger(ctx,"apples"))
            embed = discord.Embed(title=f"",description=f"",timestamp=datetime.now(),color=0x0070fa)
            embed.set_author(name=f"APPLE DEVICES")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1004238181006315630/1010623884023836742/apple-512.png")
            embed.add_field(name="2012", value=f">>> iPhone 4\niPhone 5",inline=False)
            embed.add_field(name="2013", value=f">>> iPhone 5\niPad\nIf it has 2014 trees : iPhone 6",inline=False)
            embed.add_field(name="2014", value=f">>> iPhone 5 (Try iPhone 6 and iPad first)\niPad Air\niPhone 6",inline=False)
            embed.add_field(name="2015", value=f">>> iPhone 6\niPad Mini\niPad Air",inline=False)
            embed.add_field(name="2016", value=f">>> iPhone 6S\niPad Air\niPad Mini\nTry iPhone 7 if the account was created in Late 2016 (September/October)",inline=False)
            embed.add_field(name="2017", value=f">>> iPhone 7\niPad Pro\nTry iPhone 8 and X if the account was created in Late 2017 (September/October)",inline=False)
            embed.add_field(name="2018", value=f">>> iPhone 8\niPhone X\niPad Pro\nTry iPhone XS/XR if the account was created in Late 2018 (October/November)",inline=False)
            embed.add_field(name="2019", value=f">>> iPhone 8\niPhone X\niPhone XR\niPad Pro\nTry iPhone 11 if the account was created in Late 2019 (October/November)",inline=False)
            embed.add_field(name="2020", value=f">>> iPhone SE\niPhone X\niPhone 8\niPad Pro\niPhone 11\nTry iPhone 12 if the account was created in Late 2020 (October/November)",inline=False)
            embed.add_field(name="2021", value=f">>> iPhone 12\niPhone X\niPhone 8\niPad Pro\niPhone 11",inline=False)
            embed.add_field(name="2022", value=f">>> iPhone 13\niPhone 12\niPhone X\niPhone 8\niPad Pro\niPhone 11",inline=False)
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))


## +++++++++++++ NAMES COMMAND +++++++++++++ ##

@bot.slash_command(name="nc",description="Get name change info of given player tag",guild_ids=server_ids)
@guild_only()
@option("player_tag", description="Enter the player tag")
async def names_command(ctx: discord.ApplicationContext,player_tag: str):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            await ctx.defer()
            channel = bot.get_channel(int(log_channel_id))
            await channel.send(embed=embeds.logger(ctx,"nc"))
            try:
                found = []
                found_name = []
                player = await coc_client.get_player(player_tag)
                for i in newfat:
                    collection = db1[f"{'Names'+i}"]
                    results = collection.find({"_id": player.tag})
                    for result in results:
                        if result['name'] not in found_name:
                            found_name.append(result['name'])
                            found.append(f"**{i[:4]+'-'+i[4:]}** : {result['name']}")
                for i in afternewfat:
                    collection = db2[f"{'Names'+i}"]
                    results = collection.find({"_id": player.tag})
                    for result in results:
                        if result['name'] not in found_name:
                            found_name.append(result['name'])
                            found.append(f"**{i[:4]+'-'+i[4:]}** : {result['name']}")
                for i in afterafternewfat:
                    collection = db3[f"{'Names'+i}"]
                    results = collection.find({"_id": player.tag})
                    for result in results:
                        if result['name'] not in found_name:
                            found_name.append(result['name'])
                            found.append(f"**{i[:4]+'-'+i[4:]}** : {result['name']}")
                for i in a3newfat:
                    collection = db4[f"{'Names'+i}"]
                    results = collection.find({"_id": player.tag})
                    for result in results:
                        if result['name'] not in found_name:
                            found_name.append(result['name'])
                            found.append(f"**{i[:4]+'-'+i[4:]}** : {result['name']}")
                for i in a4newfat:
                    collection = db5[f"{'Names'+i}"]
                    results = collection.find({"_id": player.tag})
                    for result in results:
                        if result['name'] not in found_name:
                            found_name.append(result['name'])
                            found.append(f"**{i[:4]+'-'+i[4:]}** : {result['name']}")
                if len(found) != 0:  
                    line = '\n'.join(map(str, found))
                    embed = discord.Embed(title=f"{player.name} {player.tag}",description=f"{line}",timestamp=datetime.now(),color=0x0070fa)
                    await ctx.respond(embed=embed)
                else:
                    embed = discord.Embed(title=f"{player.name} {player.tag}",description='NO NAME CHANGE FOUND',timestamp=datetime.now(),color=0x0070fa)
                    await ctx.respond(embed=embed)
            except Exception as e:
                print(e)
                embed = discord.Embed(title="",description="",timestamp=datetime.now(),color=0x0070fa)
                embed.set_author(name="Invalid tag",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/1006471087741218856/image9876t.png")
                await ctx.respond(embed=embed)
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))

## +++++++++++++ LOCAL COMMAND +++++++++++++ ##

@bot.slash_command(name="local",description="Get player's local history",guild_ids=server_ids)
@guild_only()
@option("player_tag", description="Enter the player tag")
async def local_command(ctx: discord.ApplicationContext,player_tag: str):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            await ctx.defer()
            channel = bot.get_channel(int(log_channel_id))
            await channel.send(embed=embeds.logger(ctx,"local"))
            try:
                player = await coc_client.get_player(player_tag)
                if '#' in player_tag:
                    tag = player_tag.split('#')
                    tag = tag[1]
                else:
                    tag = player_tag
                url = f"https://www.clashofstats.com/players/{tag}/history/"
                data = requests.get(url)
                doc = BeautifulSoup(data.text, "html.parser")
                lim = len(doc.find_all("div", class_="v-list-item__subtitle"))
                if lim != 0:
                    local_list = []
                    days_stayed = []
                    final = []
                    for i in range(0, lim):
                        j = doc.find_all("div", class_="v-list-item__title")[4 + i].text
                        kl = " ".join(j.split())
                        l = doc.find_all("div", class_="v-list-item__subtitle")[i].text
                        lo = "None"
                        days = 0
                        if '-' in kl:
                            clantag = kl.split('#')
                            clantag = "#" + f"{clantag[len(clantag)-1]}"
                            clan = await coc_client.get_clan(clantag)
                            lo = str(clan.location)
                            if lo in local_list:
                                index = local_list.index(lo)
                                days = days_stayed[index]
                                stay = " ".join(l.split()).split()
                                if stay[2] == "Year":
                                    days = days + int(stay[1])*365
                                    days = days + int(stay[3])*30
                                    days = days + int(stay[5])
                                    days_stayed[index] = days
                                if stay[2] == "Month":
                                    days = days + int(stay[1])*30
                                    days = days + int(stay[3])
                                    days_stayed[index] = days
                                if stay[2] == "Day":
                                    days = days + int(stay[1])
                                    days_stayed[index] = days
                                if stay[2] == "Years":
                                    days = days + int(stay[1])*365
                                    days = days + int(stay[3])*30
                                    days = days + int(stay[5])
                                    days_stayed[index] = days
                                if stay[2] == "Months":
                                    days = days + int(stay[1])*30
                                    days = days + int(stay[3])
                                    days_stayed[index] = days
                                if stay[2] == "Days":
                                    days = days + int(stay[1])
                                    days_stayed[index] = days
                            else:
                                local_list.append(lo)
                                stay = " ".join(l.split()).split()
                                if stay[2] == "Year":
                                    days = days + int(stay[1])*365
                                    days = days + int(stay[3])*30
                                    days = days + int(stay[5])
                                    days_stayed.append(days)
                                if stay[2] == "Month":
                                    days = days + int(stay[1])*30
                                    days = days + int(stay[3])
                                    days_stayed.append(days)
                                if stay[2] == "Day":
                                    days = days + int(stay[1])
                                    days_stayed.append(days)
                                if stay[2] == "Years":
                                    days = days + int(stay[1])*365
                                    days = days + int(stay[3])*30
                                    days = days + int(stay[5])
                                    days_stayed.append(days)
                                if stay[2] == "Months":
                                    days = days + int(stay[1])*30
                                    days = days + int(stay[3])
                                    days_stayed.append(days)
                                if stay[2] == "Days":
                                    days = days + int(stay[1])
                                    days_stayed.append(days)
                        else:
                            if lo in local_list:
                                index = local_list.index(lo)
                                days = days_stayed[index]
                                stay = " ".join(l.split()).split()
                                if stay[2] == "Year":
                                    days = days + int(stay[1])*365
                                    days = days + int(stay[3])*30
                                    days = days + int(stay[5])
                                    days_stayed[index] = days
                                if stay[2] == "Month":
                                    days = days + int(stay[1])*30
                                    days = days + int(stay[3])
                                    days_stayed[index] = days
                                if stay[2] == "Day":
                                    days = days + int(stay[1])
                                    days_stayed[index] = days
                                if stay[2] == "Years":
                                    days = days + int(stay[1])*365
                                    days = days + int(stay[3])*30
                                    days = days + int(stay[5])
                                    days_stayed[index] = days
                                if stay[2] == "Months":
                                    days = days + int(stay[1])*30
                                    days = days + int(stay[3])
                                    days_stayed[index] = days
                                if stay[2] == "Days":
                                    days = days + int(stay[1])
                                    days_stayed[index] = days
                            else:
                                local_list.append(lo)
                                stay = " ".join(l.split()).split()
                                if stay[2] == "Year":
                                    days = days + int(stay[1])*365
                                    days = days + int(stay[3])*30
                                    days = days + int(stay[5])
                                    days_stayed.append(days)
                                if stay[2] == "Month":
                                    days = days + int(stay[1])*30
                                    days = days + int(stay[3])
                                    days_stayed.append(days)
                                if stay[2] == "Day":
                                    days = days + int(stay[1])
                                    days_stayed.append(days)
                                if stay[2] == "Years":
                                    days = days + int(stay[1])*365
                                    days = days + int(stay[3])*30
                                    days = days + int(stay[5])
                                    days_stayed.append(days)
                                if stay[2] == "Months":
                                    days = days + int(stay[1])*30
                                    days = days + int(stay[3])
                                    days_stayed.append(days)
                                if stay[2] == "Days":
                                    days = days + int(stay[1])
                                    days_stayed.append(days)
                    for i in range(len(local_list)):
                        final.append(f'{local_list[i]} : Total stay {days_stayed[i]} Days')
                    line = '\n'.join(map(str, final))
                    embed = discord.Embed(title="",timestamp=datetime.now(),description=f"**{player.name} {player_tag}**\n\n{line}",color=0x0070fa)
                    embed.set_author(name="LOCAL HISTORY",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/1007939747391483914/earth.gif")
                    await ctx.respond(embed=embed)
                else:
                    embed = discord.Embed(title="",description=f"**{player.name} {player_tag}**\nClick [here](https://www.clashofstats.com/players/{tag}/history/) to view player's clan history on COS.\n\nNO LOCAL HISTORY AVAILABLE FOR THIS PLAYER",timestamp=datetime.now(),color=0x0070fa)
                    embed.set_author(name="LOCAL HISTORY",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/1007939747391483914/earth.gif")
                    await ctx.respond(embed=embed)
            except:
                embed = discord.Embed(title="",description="",timestamp=datetime.now(),color=0x0070fa)
                embed.set_author(name="Invalid tag",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/1006471087741218856/image9876t.png")
                await ctx.respond(embed=embed)
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))

## +++++++++++++ PLAYER INFO COMMAND +++++++++++++ ##

@bot.slash_command(name="player_info",description="Get player's basic info",guild_ids=server_ids)
@guild_only()
@option("player_tag", description="Enter the player tag")
async def player_info_command(ctx: discord.ApplicationContext,player_tag: str):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            await ctx.defer()
            channel = bot.get_channel(int(log_channel_id))
            await channel.send(embed=embeds.logger(ctx,"player info"))
            try:
                player = await coc_client.get_player(player_tag)
                embed = discord.Embed(title=f"{player.name} {player.tag}",description=f">>> **<:xp:1008341627133231174> XP Level :** {player.exp_level}\n**<:th12:1011149311255519384> Town hall : **{player.town_hall}\n**<:warstar:1008365034763735110> War stars :** {player.war_stars}\n**<:left_arrow:1008357528679235605> Donation given :** {player.donations}\n**<:enter_arrow:1008357496076910623> Donation received :** {player.received}\n**<:cross_words:1008374186261090404> Attack wins :** {player.attack_wins}\n**<:shield:1008374102052044941> Defence wins :** {player.defense_wins}",timestamp=datetime.now(),color=0x0070fa)
                l = player.league.icon.url
                if l == None:
                    l = "https://cdn.discordapp.com/attachments/936276886852603945/971646122210787379/e--YMyIexEQQhE4imLoJcwhYn6Uy8KqlgyY3_kFV6t4.png"
                embed.set_thumbnail(url=l)
                clanname = player.clan
                if player.clan == None:
                    clanname = "Not in clan"
                    embed.add_field(name="<:clan_castle:1008368073365012571> CLAN",value=f">>> **Clan name :** {clanname}",inline=False)
                else:
                    clan = await coc_client.get_clan(player.clan.tag)
                    clantag =  clan.tag
                    clanlevel = clan.level
                    clanlang = clan.chat_language
                    clanlocation = clan.location
                    embed.add_field(name="<:clan_castle:1008368073365012571> CLAN",value=f">>> **Clan name :** {clanname}\n**Clan tag :** {clantag}\n**Clan level :** {clanlevel}\n**Clan language : ** {clanlang}\n**Clan location :** {clanlocation}",inline=False)
                try:
                    embed.add_field(name="<:legend_league:1008379175574458478> LEGEND LEAGUE",value=f">>> **All time best :** {player.best_trophies}\n**Legend league trophies :** {player.legend_statistics.legend_trophies}",inline=False)
                except:
                    embed.add_field(name="<:legend_league:1008379175574458478> LEGEND LEAGUE",value=f">>> **All time best :** {player.best_trophies}\n**Legend league trophies :** 0",inline=False)
                embed.add_field(name="<:openinbrowser:1008597275095871579> LINKS", value=f">>> [Open in game]({player.share_link})\n[Clash of Stats](https://www.clashofstats.com/players/{player.tag.replace('#','')}/summary)",inline=False)
                await ctx.respond(embed=embed)
            except:
                embed = discord.Embed(title="",description="",timestamp=datetime.now(),color=0x0070fa)
                embed.set_author(name="Invalid tag",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/1006471087741218856/image9876t.png")
                await ctx.respond(embed=embed)
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))

## +++++++++++++ CLAN INFO COMMAND +++++++++++++ ##

@bot.slash_command(name="clan_info",description="Get clan's basic info",guild_ids=server_ids)
@guild_only()
@option("clan_tag", description="Enter the clan tag")
async def clan_info_command(ctx: discord.ApplicationContext,clan_tag: str):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            await ctx.defer()
            channel = bot.get_channel(int(log_channel_id))
            await channel.send(embed=embeds.logger(ctx,"clan info"))
            try:
                clan = await coc_client.get_clan(clan_tag)
                embed = discord.Embed(title=f"{clan.name} {clan.tag}",description=f">>> **Level :** {clan.level}\n**Member count :** {clan.member_count}\n**Clan location :** {clan.location}\n**Clan language :** {clan.chat_language}\n**Public war log :** {clan.public_war_log}",timestamp=datetime.now(),color=0x0070fa)
                embed.set_thumbnail(url=clan.badge.url)
                if len(clan.description) >= 1:
                    embed.add_field(name="<:des:1008613152994361374> DESCRIPTION",value=f">>> ```{clan.description}```",inline=False)
                embed.add_field(name="<:openinbrowser:1008597275095871579> LINKS", value=f">>> [Open in game]({clan.share_link})\n[Clash of Stats](https://www.clashofstats.com/clans/{clan.tag.replace('#','')}/summary)",inline=False)
                await ctx.respond(embed=embed)

            except:
                embed = discord.Embed(title="",description="",timestamp=datetime.now(),color=0x0070fa)
                embed.set_author(name="Invalid tag",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/1006471087741218856/image9876t.png")
                await ctx.respond(embed=embed)
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))

## +++++++++++++ CREATION COMMAND +++++++++++++ ##

@bot.slash_command(name="creation",description="Get creation year of the account",guild_ids=server_ids)
@guild_only()
@option("player_tag", description="Enter the player tag")
async def creation_command(ctx: discord.ApplicationContext,player_tag: str):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            await ctx.defer()
            channel = bot.get_channel(int(log_channel_id))
            await channel.send(embed=embeds.logger(ctx,"creation"))
            try:
                player = await coc_client.get_player(player_tag)
                tag = player.tag.replace("#","")
                if len(tag) <= 6:
                    creation_date = '2012'
                elif len(tag) == 7:
                    if tag.startswith("U"):
                        creation_date = "December 2012"
                    elif tag.startswith("L"):
                        creation_date = "December 2012"
                    elif tag.startswith("2"):
                        creation_date = "December 2012"
                    else:
                        creation_date = "Early 2013"
                elif len(tag) == 8:
                    if tag.startswith("Q"):
                        creation_date = "Late 2013"
                    elif tag.startswith("G"):
                        creation_date = "Early-Mid 2013"
                    elif tag.startswith("R"):
                        creation_date = "Summer 2013"
                    elif tag.startswith("V"):
                        creation_date = "2014"
                    elif tag.startswith("P"):
                        creation_date = "Early-Middle 2014"
                    elif tag.startswith("9"):
                        creation_date = "Middle 2014"
                    else:
                        creation_date = "Middle 2014"
                elif len(tag) == 9:
                    if tag.startswith("8"):
                        creation_date = "Early-Mid 2015"
                    elif tag.startswith("2"):
                        creation_date = "Mid-Late 2015"
                    elif tag.startswith("9"):
                        creation_date = "2016"
                    elif tag.startswith("P"):
                        creation_date = "Late 2016-2017"
                    elif tag.startswith("Y"):
                        creation_date = "Late 2017-2018"
                    elif tag.startswith("L"):
                        creation_date = "Late 2018-2019"
                    elif tag.startswith("Q"):
                        creation_date = "Late 2020-2021"
                    else:
                        creation_date = "2022"
                else:
                    creation_date = "Not Found"

                embed = discord.Embed(title=f"{player.name} {player.tag}",description="",timestamp=datetime.now(),color=0x0070fa)
                embed.add_field(name="Account was created around",value=creation_date,inline=False)
                await ctx.respond(embed=embed)
            except:
                embed = discord.Embed(title="",description="",timestamp=datetime.now(),color=0x0070fa)
                embed.set_author(name="Invalid tag",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/1006471087741218856/image9876t.png")
                await ctx.respond(embed=embed)
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))

## +++++++++++++ LAST SESSION COMMAND +++++++++++++ ##

@bot.slash_command(name="last_session",description="Get player's last session",guild_ids=server_ids)
@guild_only()
@option("player_tag", description="Enter the player tag")
async def lastsession_command(ctx: discord.ApplicationContext,player_tag: str):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            await ctx.defer()
            channel = bot.get_channel(int(log_channel_id))
            await channel.send(embed=embeds.logger(ctx,"last session"))
            try:
                player = await coc_client.get_player(player_tag)
                list_home = []
                list_bb = []
                url = f"https://www.clashofstats.com/players/{player.tag.replace('#','')}/history/progress-log/"
                data = requests.get(url)
                doc = BeautifulSoup(data.text, "html.parser")
                lim = len(doc.find_all("h3", class_="subsection-title"))
                if lim >= 1:
                    if lim > 3:
                        lim = 3
                    for i in range(0,lim):
                        list_home.append(doc.find_all("h3", class_="subsection-title")[i].text)
                url = f"https://www.clashofstats.com/players/{player.tag.replace('#','')}/history/progress-log/builder-base"
                data = requests.get(url)
                doc = BeautifulSoup(data.text, "html.parser")
                lim = len(doc.find_all("h3", class_="subsection-title"))
                if lim >= 1:
                    if lim > 3:
                        lim = 3
                    for i in range(0,lim):
                        list_bb.append(doc.find_all("h3", class_="subsection-title")[i].text)
                if len(list_home or list_bb) !=0:
                    embed = discord.Embed(title="",timestamp=datetime.now(),description=f"**{player.name} {player.tag}**",color=0x0070fa)
                    embed.set_author(name="LAST SESSION",icon_url="https://cdn.discordapp.com/attachments/1008311551561830450/1008717722064003103/ls.png")
                    if len(list_home) != 0:
                        line_home = '\n'.join(map(str, list_home))
                        embed.add_field(name="Home Village",value=f">>> {line_home}",inline=False)
                    if len(list_bb) != 0:
                        line_bb = '\n'.join(map(str, list_bb))
                        embed.add_field(name="Builder Base",value=f">>> {line_bb}",inline=False)
                    await ctx.respond(embed=embed)
                else:
                    embed = discord.Embed(title="",description="",timestamp=datetime.now(),color=0x0070fa)
                    embed.set_author(name="No last session available for this tag",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/1006471087741218856/image9876t.png")
                    await ctx.respond(embed=embed)
            except:
                embed = discord.Embed(title="",description="",timestamp=datetime.now(),color=0x0070fa)
                embed.set_author(name="Invalid tag",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/1006471087741218856/image9876t.png")
                await ctx.respond(embed=embed)
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))

## +++++++++++++ DEAD TAGS COMMAND +++++++++++++ ##

@bot.slash_command(name="dead_tags",description="Get some nice dead account tags (Random Town Hall Level and Local)",guild_ids=server_ids)
@guild_only()
async def dead_tags_2_command(ctx: discord.ApplicationContext):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            await ctx.defer()
            channel = bot.get_channel(int(log_channel_id))
            await channel.send(embed=embeds.logger(ctx,"dead tags"))
            m = open("Database/dead_tags.json", 'r', encoding="utf8")
            data = json.load(m)
            len_data = len(data)
            embed = discord.Embed(title="",timestamp=datetime.now(),description="",color=0x0070fa)
            embed.set_author(name="DEAD TAGS",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/1009446248912269372/scan3.png")
            for i in range(0, 5):
                radint = random.randint(0, len_data)
                tag = data[radint]["tag"]
                player = await coc_client.get_player(tag)
                if player.clan != None:
                    clan = await coc_client.get_clan(player.clan.tag)
                    embed.add_field(name=f"{player.name} {player.tag}",value=f">>> **XP Level :** {player.exp_level}\n**Town hall level :** {player.town_hall}\n**War stars : ** {player.war_stars}\n**Possible local :** {clan.location}\n[Open in game]({player.share_link})",inline=False)
                else:
                    embed.add_field(name=f"{player.name} {player.tag}",value=f">>> **XP Level :** {player.exp_level}\n**Town hall level :** {player.town_hall}\n**War stars : ** {player.war_stars}\n[Open in game]({player.share_link})",inline=False)
            await ctx.respond(embed=embed) 
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))

## +++++++++++++ DEAD TAGS 2 COMMAND +++++++++++++ ##

@bot.slash_command(name="dead_tags_2",description="Get some nice dead account tags of given Town Hall level",guild_ids=server_ids)
@guild_only()
@option("town_hall_level", description="Select Town Hall level",choices=["14", "15"])
async def dead_tags_command(ctx: discord.ApplicationContext, town_hall_level):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            await ctx.defer()
            channel = bot.get_channel(int(log_channel_id))
            await channel.send(embed=embeds.logger(ctx,"dead tags 2"))
            tagsFile = f"Database/dead_tags_{town_hall_level}.json"
            m = open(tagsFile, 'r', encoding="utf8")
            data = json.load(m)
            len_data = len(data)
            embed = discord.Embed(title="",timestamp=datetime.now(),description="",color=0x0070fa)
            embed.set_author(name=f"TH{town_hall_level} DEAD TAGS",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/1009446248912269372/scan3.png")
            for i in range(0, 5):
                radint = random.randint(0, len_data)
                tag = data[radint]["tag"]
                player = await coc_client.get_player(tag)
                if player.clan != None:
                    clan = await coc_client.get_clan(player.clan.tag)
                    embed.add_field(name=f"{player.name} {player.tag}",value=f">>> **XP Level :** {player.exp_level}\n**Town hall level :** {player.town_hall}\n**War stars : ** {player.war_stars}\n**Possible local :** {clan.location}\n[Open in game]({player.share_link})",inline=False)
                else:
                    embed.add_field(name=f"{player.name} {player.tag}",value=f">>> **XP Level :** {player.exp_level}\n**Town hall level :** {player.town_hall}\n**War stars : ** {player.war_stars}\n[Open in game]({player.share_link})",inline=False)
            await ctx.respond(embed=embed) 
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))

## +++++++++++++ DEAD TAGS 2 COMMAND +++++++++++++ ##

@bot.slash_command(name="dead_tags_ios",description="Get some nice dead IOS account tags",guild_ids=server_ids)
@guild_only()
async def dead_tags_command(ctx: discord.ApplicationContext):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            await ctx.defer()
            channel = bot.get_channel(int(log_channel_id))
            await channel.send(embed=embeds.logger(ctx,"dead tags ios"))
            m = open('Database/dead_tags_ios.json', 'r', encoding="utf8")
            data = json.load(m)
            len_data = len(data)
            embed = discord.Embed(title="",timestamp=datetime.now(),description="",color=0x0070fa)
            embed.set_author(name="IOS DEAD TAGS",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/1009446248912269372/scan3.png")
            for i in range(0, 5):
                radint = random.randint(0, len_data)
                tag = data[radint]["tag"]
                player = await coc_client.get_player(tag)
                if player.clan != None:
                    clan = await coc_client.get_clan(player.clan.tag)
                    embed.add_field(name=f"{player.name} {player.tag}",value=f">>> **XP Level :** {player.exp_level}\n**Town hall level :** {player.town_hall}\n**War stars : ** {player.war_stars}\n**NC count :** {data[radint]['nc_count']}\n**Max walls :** {data[radint]['maxed_walls_for_th']}\n**Possible local :** {clan.location}\n[Open in game]({player.share_link})",inline=False)
                else:
                    embed.add_field(name=f"{player.name} {player.tag}",value=f">>> **XP Level :** {player.exp_level}\n**Town hall level :** {player.town_hall}\n**War stars : ** {player.war_stars}\n**NC count :** {data[radint]['nc_count']}\n**Max walls :** {data[radint]['maxed_walls_for_th']}\n[Open in game]({player.share_link})",inline=False)
            await ctx.respond(embed=embed) 
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))
      
## +++++++++++++ IP COMMAND +++++++++++++ ##

@bot.slash_command(name="ip_lookup",description="Ip lookup",guild_ids=server_ids)
@guild_only()
@option("ip", description="Enter the IP address")
async def ip_lookup_command(ctx: discord.ApplicationContext,ip:str):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            await ctx.defer()
            channel = bot.get_channel(int(log_channel_id))
            await channel.send(embed=embeds.logger(ctx,"ip lookup"))
            url = f"http://ip-api.com/json/{ip}"
            res = requests.get(url)
            data = res.json()
            if data['status'] != 'fail':
                embed = discord.Embed(title="",timestamp=datetime.now(),description=f">>> **Country :** {data['country']}\n**Country Code :** {data['countryCode']}\n**Region :** {data['regionName']}\n**Region Code :** {data['region']}\n**City :** {data['city']}\n**Timezone :** {data['timezone']}\n**Network :** {data['isp']}",color=0x0070fa)
                embed.set_author(name="IP LOOKUP",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/1009446248912269372/scan3.png")
                await ctx.respond(embed=embed)
            else:
                embed = discord.Embed(title="",description="",timestamp=datetime.now(),color=0x0070fa)
                embed.set_author(name="Invalid IP",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/1006471087741218856/image9876t.png")
                await ctx.respond(embed=embed)
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))

## +++++++++++++ RECEIPT APPLE FULL SCREEN COMMAND +++++++++++++ ##

@bot.slash_command(name="receipt_apple",description="Generates a fake apple receipt (Full screen size)",guild_ids=server_ids)
@guild_only()
@option("date_month", description="Enter the month",choices=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"])
@option("date_year", description="Enter the year",choices=["2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023", "2024"])
@option("currency", description="Enter the currency symbol")
@option("amount", description="Enter the amount")
@option("item_name", description="Enter the item name (Name of purchased item/product)")
@option("billing_address", description="If selected Yes bot will generate a fake US billing address for the receipt or it will be blank",choices=["Yes","No"])
@option("date_day", description="Enter the day (numbered)",min_length=2,max_length=2,required=False,default=00)
@option("order_id", description="Enter the order id (eg. M2KJUSDH7)",required=False,default=None)
async def ios_receipt_command(ctx: discord.ApplicationContext,date_month:str,date_year:str,currency:str,amount:str,item_name:str,billing_address:str,date_day: str,order_id:str):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            await ctx.defer()
            channel = bot.get_channel(int(log_channel_id))
            await channel.send(embed=embeds.logger(ctx,"receipt ios"))
            if date_day != 00:
                date = f"{date_month} {date_day}, {date_year}"
            else: 
                date = f"{date_month}, {date_year}"
            total_amount = currency + amount
            if order_id == None:
                order_id = "M"
                for i in range(2):
                    order_id = order_id + random.choice(string.ascii_uppercase)
                for i in range(7):
                    x = random.randint(1, 2)
                    if x == 1:
                        order_id = order_id + random.choice(string.ascii_uppercase)
                    else:
                        y = random.randint(0, 9)
                        if y == 7:
                            y = 8
                        order_id = order_id + str(y)
            document_no = "1871622" + f"{random.randint(0, 9)}" + f"{random.randint(0, 9)}" + f"{random.randint(0, 9)}" + f"{random.randint(0, 9)}"
            layer1 = Image.open("Assets/asset_ios_receipt.png").convert("RGBA")
            final = Image.new("RGBA", layer1.size)
            final.paste(layer1, (0, 0), layer1)
            fnt = ImageFont.truetype('Fonts/JunePro-Regular.ttf', 22)
            d = ImageDraw.Draw(final)

            d.text((25, 253), order_id, font=fnt, fill=(251, 251, 253))
            f = ImageDraw.Draw(final)

            f.text((25, 347), date, font=fnt, fill=(251, 251, 253))
            p = ImageDraw.Draw(final)

            p.text((348, 347), total_amount, font=fnt, fill=(251, 251, 253))
            p2 = ImageDraw.Draw(final)

            p2.text((515, 828), total_amount, font=fnt, fill=(251, 251, 253))
            p2 = ImageDraw.Draw(final)
            
            if billing_address == "Yes":
                p2.text((25, 443), random.choice(billing_addresses_list), font=fnt, fill=(251, 251, 253))
                p2 = ImageDraw.Draw(final)

            x = 522
            if len(total_amount) == 5:
                x = 510
            if len(total_amount) == 6:
                x = 498
            if len(total_amount) == 7:
                x = 486
            if len(total_amount) == 8:
                x = 484

            p2.text((x, 718), total_amount, font=fnt, fill=(251, 251, 253))
            p2 = ImageDraw.Draw(final)

            p2.text((110, 718), item_name, font=fnt, fill=(251, 251, 253))
            p2 = ImageDraw.Draw(final)

            p2.text((348, 253), document_no, font=fnt, fill=(251, 251, 253))
            p2 = ImageDraw.Draw(final)
            final.save("Assets/ios_receipt.png", format="png")
            f = discord.File("Assets/ios_receipt.png", filename="ios_receipt.png")
            await ctx.respond(file=f)
           
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))

## +++++++++++++ RECEIPT APPLE MEDIUM SIZE COMMAND +++++++++++++ ##

@bot.slash_command(name="receipt_apple_2",description="Generates a fake apple receipt (Medium size, Doesn't need date and order id)",guild_ids=server_ids)
@guild_only()
@option("currency", description="Enter the currency symbol")
@option("amount", description="Enter the amount")
@option("item_name", description="Enter the item name (Name of purchased item/product)")
async def ios_receipt_2_command(ctx: discord.ApplicationContext,currency:str,amount:str,item_name:str):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            await ctx.defer()
            channel = bot.get_channel(int(log_channel_id))
            await channel.send(embed=embeds.logger(ctx,"receipt ios 2"))
            total_amount = currency + amount
            layer1 = Image.open("Assets/assest_ios_receipt_2.png").convert("RGBA")
            final = Image.new("RGBA", layer1.size)
            final.paste(layer1, (0, 0), layer1)
            fnt = ImageFont.truetype('Fonts/JunePro-Regular.ttf', 40)
            fnt2 = ImageFont.truetype('Fonts/JunePro-Semibold.ttf', 43)

            d = ImageDraw.Draw(final)
            card_number = "8" + str(random.randint(1,9)) + str(random.randint(1,9)) + str(random.randint(1,9))
            d.text((949, 124), card_number, font=fnt, fill=(174, 174, 183))

            p = ImageDraw.Draw(final)
            x = 994
            if len(total_amount) >=3:
                x = x - 25*(len(total_amount)-2)
                if "." in total_amount:
                    x = x + 13
            p.text((x, 267), total_amount, font=fnt, fill=(251, 251, 253))

            p2 = ImageDraw.Draw(final)
            x = 994
            if len(total_amount) >=3:
                x = x - 27*(len(total_amount)-2)
                if "." in total_amount:
                    x = x + 15
            p2.text((x, 496), total_amount, font=fnt2, fill=(251, 251, 253))

            p2 = ImageDraw.Draw(final)
            p2.text((252, 264), item_name, font=fnt2, fill=(251, 251, 553))

            final.save("Assets/ios_receipt_2.png", format="png")
            f = discord.File("Assets/ios_receipt_2.png", filename="ios_receipt_2.png")
            await ctx.respond(file=f)
           
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))

## +++++++++++++ RECEIPT APPLE SMALL SIZE COMMAND +++++++++++++ ##

@bot.slash_command(name="receipt_apple_3",description="Generates a fake apple receipt (Small size, Doesn't need order id)",guild_ids=server_ids)
@guild_only()
@option("currency", description="Enter the currency symbol")
@option("amount", description="Enter the amount")
@option("item_name", description="Enter the item name (Name of purchased item/product)")
@option("date_month", description="Enter the month",choices=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
@option("date_year", description="Enter the year",choices=["2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022", "2023", "2024"])
@option("date_day", description="Enter the day (numbered)",min_length=2,max_length=2,required=False,default=00)
async def ios_receipt_3_command(ctx: discord.ApplicationContext,currency:str,amount:str,item_name:str,date_month:str,date_year:str,date_day:str):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            await ctx.defer()
            channel = bot.get_channel(int(log_channel_id))
            await channel.send(embed=embeds.logger(ctx,"receipt ios 3"))
            total_amount = currency + amount
            if date_day != 00:
                date = f"{date_month} {date_day}, {date_year}"
            else: 
                date = f"{date_month}, {date_year}"
            layer1 = Image.open("Assets/asset_ios_receipt_3.png").convert("RGBA")
            final = Image.new("RGBA", layer1.size)
            final.paste(layer1, (0, 0), layer1)
            W, H = (1170,218)
            d = ImageDraw.Draw(final)
            fnt2 = ImageFont.truetype('Fonts/JunePro-Semibold.ttf', 52)
            w, h = d.textsize(item_name,font=fnt2)
            d.text(((W-w)/2,(H-h)/2), item_name, font=fnt2, fill=(251, 251, 553))

            p = ImageDraw.Draw(final)
            x = 1075
            if len(total_amount) >=3:
                x = x - 25*(len(total_amount)-2)
                if "." in total_amount:
                    x = x + 13
            fnt = ImageFont.truetype('Fonts/JunePro-Regular.ttf', 41)
            p.text((x, 335), total_amount, font=fnt, fill=(251, 251, 553))

            p2 = ImageDraw.Draw(final)
            fnt = ImageFont.truetype('Fonts/JunePro-Regular.ttf', 42)
            p2.text((198, 330), item_name, font=fnt, fill=(251, 251, 553))

            p2 = ImageDraw.Draw(final)
            fnt = ImageFont.truetype('Fonts/JunePro-Regular.ttf', 36)
            p2.text((469, 594), date, font=fnt, fill=(251, 251, 553))

            final.save("Assets/ios_receipt_3.png", format="png")
            f = discord.File("Assets/ios_receipt_3.png", filename="ios_receipt_3.png")
            await ctx.respond(file=f)
           
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))

## +++++++++++++ RECEIPT GOOGLE PLAY COMMAND +++++++++++++ ##

@bot.slash_command(name="receipt_google_play",description="Generates a fake google play receipt",guild_ids=server_ids)
@guild_only()
@option("currency", description="Enter the currency symbol")
@option("amount", description="Enter the amount")
@option("item_name", description="Enter the item name (Name of purchased item/product)")
@option("date_month", description="Enter the month",choices=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
@option("date_year", description="Enter the year",choices=["2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022", "2023", "2024"])
@option("date_day", description="Enter the day (numbered)",min_length=2,max_length=2,required=False,default=00)
async def google_play_receipt_command(ctx: discord.ApplicationContext,currency:str,amount:str,item_name:str,date_month:str,date_year:str,date_day:str):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            await ctx.defer()
            channel = bot.get_channel(int(log_channel_id))
            await channel.send(embed=embeds.logger(ctx,"receipt google play"))
            total_amount = currency + amount
            if date_day != 00:
                date = f"{date_month} {date_day}, {date_year}"
            else: 
                date = f"{date_month}, {date_year}"
            if date_day != 00:
                date = f"{date_month} {date_day}, {date_year}"
            else: 
                date = f"{date_month}, {date_year}"
            type = item_name + " (Clash of Clans)"
            code2 = f"{utils.getno()}" + f"{random.randint(0, 9)}"
            code = f"GPA.{utils.getno()}-{utils.getno()}-{utils.getno()}-"
            layer1 = Image.open("Assets/asset_google_play_receipt.png").convert("RGBA")
            final = Image.new("RGBA", layer1.size)
            final.paste(layer1, (0, 0), layer1)
            fnt = ImageFont.truetype('Fonts/google_receipt.ttf', 26)
            d = ImageDraw.Draw(final)

            d.text((238, 419), code, font=fnt, fill=(96, 96, 98))
            f = ImageDraw.Draw(final)

            f.text((200, 499), date, font=fnt, fill=(96, 96, 98))
            p = ImageDraw.Draw(final)

            x = 441
            x2 = 371
            if len(total_amount) == 5:
                x = 452
                x2 = 382
            if len(total_amount) == 4:
                x = 465
                x2 = 395
            if len(total_amount) == 3:
                x = 474
                x2 = 404
            p.text((x, 723), total_amount, font=fnt, fill=(96, 96, 98))
            p2 = ImageDraw.Draw(final)

            p2.text((x2, 817), "Total: " + total_amount, font=fnt, fill=(96, 96, 98))
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

            final.save("Assets/google_play_receipt.png", format="png")
            f = discord.File("Assets/google_play_receipt.png", filename="google_play_receipt.png")
            await ctx.respond(file=f)
           
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))

## +++++++++++++ TEMP EMAIL COMMAND +++++++++++++ ##

@bot.slash_command(name="temp_email",description="Generates a temporary email address (Generated email won't work after 10 min)",guild_ids=server_ids)
@guild_only()
async def temp_email_command(ctx: discord.ApplicationContext):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            await ctx.defer()
            channel = bot.get_channel(int(log_channel_id))
            await channel.send(embed=embeds.logger(ctx,"temp email"))
            url = "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=5"
            r = requests.get(url)
            h = r.json()
            embed = discord.Embed(title=f"",description=f"• {h[0]}",timestamp=datetime.now(),color=0x0070fa)
            embed.set_author(name=f"TEMP EMAIL",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/1011504564224139314/email.png")
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))

## +++++++++++++ TEMP EMAIL INBOX COMMAND +++++++++++++ ##

class InboxView(View):
    def __init__(self, ctx,l,d,h):
        super().__init__(timeout=600)
        self.ctx = ctx
        self.l = l
        self.d = d
        self.h = h
    @discord.ui.button(label="Show email body", style=discord.ButtonStyle.primary, emoji="📩")
    async def button_callback(self, button, interaction):
        url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={self.l}&domain={self.d}&id={self.h[0]['id']}"
        r = requests.get(url)
        h = r.json()
        self.clear_items()
        embed = discord.Embed(title=f"",description=f"```{h['textBody']}```",timestamp=datetime.now(),color=0x0070fa)
        embed.set_author(name=f"EMAIL BODY")
        await interaction.response.edit_message(embed=embed,view=self)

@bot.slash_command(name="temp_email_inbox",description="Shows last mail received in the inbox of temporary email",guild_ids=server_ids)
@guild_only()
@option("temp_email", description="Enter the teporary email address")
async def temp_email_inbox_command(ctx: discord.ApplicationContext,temp_email:str):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            await ctx.defer()
            channel = bot.get_channel(int(log_channel_id))
            await channel.send(embed=embeds.logger(ctx,"temp email inbox"))
            try:
                ema = temp_email.split("@")
                l = ema[0]
                d = ema[1]
                url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={l}&domain={d}"
                r = requests.get(url)
                h = r.json()
                embed = discord.Embed(title=f"",description=f"",timestamp=datetime.now(),color=0x0070fa)
                embed.set_author(name=f"INBOX",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/1010761334687801344/unknown.png")
                embed.add_field(name="SENDER",value=f">>> {h[0]['from']}",inline=False)
                embed.add_field(name="SUBJECT", value=f">>> {h[0]['subject']}",inline=False)
                embed.add_field(name="DATE & TIME",value=f">>> {h[0]['date']}",inline=False)
                await ctx.respond(embed=embed,view=InboxView(ctx,l,d,h))
            except:
                embed = discord.Embed(title=f"",description=f"No mails found",timestamp=datetime.now(),color=0x0070fa)
                embed.set_author(name=f"INBOX",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/1010761334687801344/unknown.png")
                await ctx.respond(embed=embed)
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))

## +++++++++++++ SKINS COMMAND +++++++++++++ ##

skinss = [
    "**Year 2019**\n\n**Gladiator King**\nSeason : April 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Gladiator Queen**\nSeason : May 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**P.E.K.K.A King**\nSeason : June 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Valkyrie Queen**\nSeason : July 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Party Warden**\nSeason : August 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Autumn Queen**\nSeason : September 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Skeleton King**\nSeason : October 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Ice Queen**\nSeason : November 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Jolly King**\nSeason : December 2019\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌",
    "**Year 2020**\n\n**Primal Warden**\nSeason : January 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Warrior Queen¹**\nSeason : January 2020 / February 2021 / February 2022\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Primal King**\nSeason : February 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Primal Queen**\nSeason : March 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Clockwork Warden**\nSeason : April 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Clockwork King**\nSeason : May 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Clockwork Queen**\nSeason : June 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Gladiator Warden**\nSeason : July 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Party King**\nSeason : August 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Pirate Queen**\nSeason : September 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Pirate Warden**\nSeason : October 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Champion King²**\nSeason : October 2020 / November 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Pirate King**\nSeason : November 202\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Winter Champion**\nSeason : December 2020\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌",
    "**Year 2021**\n\n**Warden of the North**\nSeason : January 2021\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Rogue Queen**\nSeason : February 2021\nCan buy with gems : ✅\nIs gold : ✅\nIs legendary : ❌\n\n**Warrior King³**\nSeason : February 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Rogue King**\nSeason : March 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Jungle Champion4**\nSeason : April 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Jungle Warden**\nSeason : May 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Jungle Queen**\nSeason : June 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Fierce King5**\nSeason : June 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Jungle King**\nSeason : July 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Party Queen**\nSeason : August 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Beat King6**\nSeason : August 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Gladiator Champion**\nSeason : September 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Warden Maste**\nSeason : October 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Golem King**\nSeason : November 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Champion Queen7**\nSeason : November 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Jolly Warden**\nSeason : December 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Ice King**\nSeason : December 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅",
    "**Year 2022**\n\n**Shadow Queen**\nSeason : January 2022\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Lunar King9³**\nSeason : February 2022\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Warrior Warden**\nSeason : February 2022\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Shadow Champion**\nSeason : March 2022\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Primal Champion10**\nSeason : March 2022\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅\n\n**Shadow King**\nSeason : April 2021\nCan buy with gems : ❌\nIs gold : ✅\nIs legendary : ❌\n\n**Shadow Warden11**\nSeason : April 2021\nCan buy with gems : ❌\nIs gold : ❌\nIs legendary : ✅"
]

class SkinsView(View):
    def __init__(self, ctx):
        super().__init__(timeout=600)
        self.ctx = ctx
    @discord.ui.button(label="2019", style=discord.ButtonStyle.primary)
    async def button1_callback(self, button, interaction):
        for x in self.children:
            if x.disabled == True:
                x.disabled = False
        button.disabled = True
        embed = discord.Embed(title=f"",description=f"{skinss[0]}",timestamp=datetime.now(),color=0x0070fa)
        embed.set_author(name=f"SKINS")
        await interaction.response.edit_message(embed=embed,view=self)
    @discord.ui.button(label="2020", style=discord.ButtonStyle.primary)
    async def button2_callback(self, button, interaction):
        for x in self.children:
            if x.disabled == True:
                x.disabled = False
        button.disabled = True
        embed = discord.Embed(title=f"",description=f"{skinss[1]}",timestamp=datetime.now(),color=0x0070fa)
        embed.set_author(name=f"SKINS")
        await interaction.response.edit_message(embed=embed,view=self)
    @discord.ui.button(label="2021", style=discord.ButtonStyle.primary)
    async def button3_callback(self, button, interaction):
        for x in self.children:
            if x.disabled == True:
                x.disabled = False
        button.disabled = True
        embed = discord.Embed(title=f"",description=f"{skinss[2]}",timestamp=datetime.now(),color=0x0070fa)
        embed.set_author(name=f"SKINS")
        await interaction.response.edit_message(embed=embed,view=self)
    @discord.ui.button(label="2022", style=discord.ButtonStyle.primary)
    async def button4_callback(self, button, interaction):
        for x in self.children:
            if x.disabled == True:
                x.disabled = False
        button.disabled = True
        embed = discord.Embed(title=f"",description=f"{skinss[3]}",timestamp=datetime.now(),color=0x0070fa)
        embed.set_author(name=f"SKINS")
        await interaction.response.edit_message(embed=embed,view=self)

@bot.slash_command(name="skins",description="Get skin's information",guild_ids=server_ids)
@guild_only()
async def skins_command(ctx: discord.ApplicationContext):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            await ctx.defer()
            channel = bot.get_channel(int(log_channel_id))
            await channel.send(embed=embeds.logger(ctx,"skins"))
            embed = discord.Embed(title=f"",description=f"{skinss[0]}",timestamp=datetime.now(),color=0x0070fa)
            embed.set_author(name=f"SKINS")
            await ctx.respond(embed=embed,view=SkinsView(ctx))
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))

## +++++++++++++ TOP 200 LOCAL COMMAND +++++++++++++ ##

local_country = ['Afghanistan', 'Ã…land Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Ascension Island', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Canary Islands', 'Cape Verde', 'Caribbean Netherlands', 'Cayman Islands', 'Central African Republic', 'Ceuta and Melilla', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo (DRC)', 'Congo (Republic)', 'Cook Islands', 'Costa Rica', 'CÃ´te dâ€™Ivoire', 'Croatia', 'Cuba', 'CuraÃ§ao', 'Cyprus', 'Czech Republic', 'Denmark', 'Diego Garcia', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard & McDonald Islands', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau', 'North Macedonia', 'Madagascar', 'Malawi', 'Malaysia',
'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar (Burma)', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'North Korea', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn Islands', 'Poland',
'Portugal', 'Puerto Rico', 'Qatar', 'RÃ©union', 'Romania', 'Russia', 'Rwanda', 'Saint BarthÃ©lemy', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin', 'Saint Pierre and Miquelon', 'Samoa', 'San Marino', 'SÃ£o TomÃ© and PrÃ\xadncipe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'St. Vincent & Grenadines', 'Sudan', 'Suriname', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tristan da Cunha', 'Tunisia',
'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'U.S. Outlying Islands', 'U.S. Virgin Islands', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']
async def complete_country_name2(ctx: discord.AutocompleteContext):
    return [name for name in local_country if name.startswith(ctx.value.lower().capitalize())]

class LocalTopView(View):
    def __init__(self, ctx,list,country):
        super().__init__(timeout=600)
        self.ctx = ctx
        self.list = list
        self.country = country
        self.cursor = 1
    @discord.ui.button(label="", style=discord.ButtonStyle.primary,emoji="▶")
    async def button2_callback(self, button, interaction):
        line = '\n'.join(map(str, self.list[0+(25*self.cursor):25+(25*self.cursor)]))
        embed = discord.Embed(title="",timestamp=datetime.now(),description=f"**• Local : {self.country}**\n\n{line}",color=0x0070fa)
        embed.set_author(name="TOP 200",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/1007939747391483914/earth.gif")
        self.cursor = self.cursor + 1
        if self.cursor == 8: 
            self.clear_items()
        await interaction.response.edit_message(embed=embed,view=self)

@bot.slash_command(name="top_200_local",description="Get top 200 players of given local",guild_ids=server_ids)
@guild_only()
@option("country", description="Enter the country name",autocomplete=complete_country_name2)
async def top_200_local_command(ctx: discord.ApplicationContext,country: str):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
                await ctx.defer()
                channel = bot.get_channel(int(log_channel_id))
                await channel.send(embed=embeds.logger(ctx,"top 200 local"))
                with open('Database/local_ids.json', 'r') as f:
                    it = json.load(f)
                    country_id = it[country]
                list = []
                players = await coc_client.get_location_players(country_id,limit=200)
                rank = 1
                for player in players:
                    list.append(f"{rank}. {player.name}  {player.tag}\n")
                    rank = rank + 1
                line = '\n'.join(map(str, list[0:25]))
                embed = discord.Embed(title="",timestamp=datetime.now(),description=f"**• Local : {country}**\n\n{line}",color=0x0070fa)
                embed.set_author(name="TOP 200",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/1007939747391483914/earth.gif")
                await ctx.respond(embed=embed,view=LocalTopView(ctx,list,country))
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))

## +++++++++++++ STONE ACC COMMAND +++++++++++++ ##

stone_tags =['#LYUCQ8', '#29ULV8', '#RRVLCL', '#2P8RJ0', '#QGRUV8', '#QLPUG0', '#L8GUUG', '#RYURYL', '#QYPQL0', '#G2GP8P', '#YRRL0', '#Q20QGP', '#2Q82GU', '#8V8000', '#8Y9CLG', '#9988P', '#98QYQ8', '#PPYQYL', '#9VQ80', '#Y2VRL0', '#P929YL', '#R20V80', '#9Y2U8U', '#9QYGP0', '#YUV800', '#LRG0G0', '#QV8RVL', '#P8QPY8', '#809QVL', '#9QYGP0', '#QJU9L0', '#8PR80', '#82RL8P', '#8902YL', '#YLG0R8', '#9JL0G0', '#2QR2GP', '#YPCQ8', '#GUGVJ0', '#J92YRL', '#QRU88U', '#LU20Y8']

@bot.slash_command(name="stone_tag",description="Get a stone account tag",guild_ids=server_ids)
@guild_only()
async def stone_tag_command(ctx: discord.ApplicationContext):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            await ctx.defer()
            channel = bot.get_channel(int(log_channel_id))
            await channel.send(embed=embeds.logger(ctx,"stone tag"))
            tag = stone_tags[random.randint(0,len(stone_tags)-1)]
            player = await coc_client.get_player(tag)
            embed = discord.Embed(title=f"{player.name} {player.tag}",description=f">>> **<:xp:1008341627133231174> XP Level :** {player.exp_level}\n**<:th12:1011149311255519384> Town hall : **{player.town_hall}\n**<:warstar:1008365034763735110> War stars :** {player.war_stars}\n**<:left_arrow:1008357528679235605> Donation given :** {player.donations}\n**<:enter_arrow:1008357496076910623> Donation received :** {player.received}\n**<:cross_words:1008374186261090404> Attack wins :** {player.attack_wins}\n**<:shield:1008374102052044941> Defence wins :** {player.defense_wins}",timestamp=datetime.now(),color=0x0070fa)
            embed.add_field(name="<:openinbrowser:1008597275095871579> LINKS", value=f">>> [Open in game]({player.share_link})\n[Clash of Stats](https://www.clashofstats.com/players/{player.tag.replace('#','')}/summary)",inline=False)
            embed.set_author(name="STONE TAG")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1008311551561830450/1011151295249391707/unknown.png")
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))

## +++++++++++++ PERMS COMMAND +++++++++++++ ##

@bot.slash_command(name="perms",description="Get info about your permissions",guild_ids=server_ids)
@guild_only()
async def perms_command(ctx: discord.ApplicationContext):
    if utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'VALID':
        if ctx.channel_id not in public_channels:
            await ctx.defer()
            channel = bot.get_channel(int(log_channel_id))
            await channel.send(embed=embeds.logger(ctx,"perms"))
            f = open("Database/buyers_data.json","r")
            data = json.load(f)
            for i in range(len(data)):
                if data[i]["user_id"] == str(ctx.interaction.user.id):
                    embed = discord.Embed(title="",description=f"**{ctx.interaction.user.mention} PERMS INFO**\n\n**Subscription type :** {data[i]['user_data']['sub_type']}\n**Started on :** {data[i]['user_data']['sub_start']}\n**Expires on :** {data[i]['user_data']['sub_end']}",timestamp=datetime.now(),color=0x0070fa)
                    if ctx.interaction.user.avatar == None:
                      url = "https://cdn.discordapp.com/embed/avatars/4.png"
                    else: 
                      url = ctx.interaction.user.avatar.url
                    embed.set_thumbnail(url=url)
                    await ctx.respond(embed=embed)
        else:
            await ctx.respond("You can't use the bot commands in public channels.")
    elif utils.is_buyer_valid(str(ctx.interaction.user.id)) == 'EXPIRED':
        await ctx.respond(embed=embeds.perms_expired(ctx))
    else:
        await ctx.respond(embed=embeds.no_perms(ctx))

@bot.slash_command(name="create_channel",description="Creates channel for buyer",guild_ids=server_ids)
@option("user", description="Select member")
@guild_only()
async def id_(ctx, user: discord.Member):
  await ctx.defer()
  if ctx.author.id in owner_ids:
    channel = bot.get_channel(int(log_channel_id))
    await channel.send(embed=embeds.logger(ctx,"create channel"))
    guild = bot.guilds[0]
    nox = await bot.fetch_user(920337055706386443)
    poppa = await bot.fetch_user(1072268303776612513)
    category = discord.utils.get(ctx.guild.categories, name="BUYΞRS 6")
    overwrites = {
      guild.default_role:
      discord.PermissionOverwrite(read_messages=False),
      guild.me:
      discord.PermissionOverwrite(read_messages=True),
      nox:  discord.PermissionOverwrite(read_messages=True, send_messages=True),
      poppa:  discord.PermissionOverwrite(read_messages=True, send_messages=True),
      user: discord.PermissionOverwrite(read_messages=True, send_messages=True)
    }
    channel = await guild.create_text_channel(f'{user}',overwrites=overwrites,reason=None,category=category)
    em = discord.Embed(title="",description=f"{channel.mention}",timestamp=datetime.now(),color=0x0070fa)
    em.set_author(name=f"Created channel for {user}",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/959823990313070602/ShyCautiousAfricanpiedkingfisher-max-1mb.gif")
    em.set_footer(text=f"Command used by {ctx.interaction.user}")
    await ctx.respond(embed=em)
  else:
    await ctx.respond(f"You don't have permission to use this command!")

@bot.slash_command(name="role",description="Role members",guild_ids=server_ids)
@option("user", description="Select member")
@option("role", description="Select role", choices=["Verified", "Demo Access", "Buyer", "Verified, Demo Access and Buyer"])
@guild_only()
async def id_(ctx, user: discord.Member, role: str):
  await ctx.defer()
  if ctx.author.id in owner_ids:
    channel = bot.get_channel(int(log_channel_id))
    await channel.send(embed=embeds.logger(ctx,"role"))
    if role == "Verified":
      role1 = user.guild.get_role(987991468968906823)
      await user.add_roles(role1)
    elif role == "Demo Access":
      role1 = user.guild.get_role(1012621040259694644)
      await user.add_roles(role1)
    elif role == "Buyer":
      role1 = user.guild.get_role(987991468968906823)
      await user.add_roles(role1)
      role1 = user.guild.get_role(961301374115676170)
      await user.add_roles(role1)
    else:
      role = user.guild.get_role(961301374115676170)
      await user.add_roles(role)
    embed = discord.Embed(title="",description=f"**{user.mention} has been given {role} role.**",timestamp=datetime.now(),color=0x0070fa)
    if user.avatar == None:
      url = "https://cdn.discordapp.com/embed/avatars/4.png"
    else: 
      url = user.avatar.url
    embed.set_thumbnail(url=url)
    await ctx.respond(embed=embed)
  else:
    await ctx.respond(f"You don't have permission to use this command!")


bot.run('MTAxMTE1MzUwMDMyNTAzMTk0Ng.GCG5uz.XZ1ipnLqR2x1tVs-7TLf3iEQ_4OXdKUbFiGKeM')
