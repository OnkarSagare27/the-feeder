import discord
from datetime import datetime
from Functions import utils

def logger(ctx,command_name):
  embed = discord.Embed(title="",timestamp=datetime.now(),color=0x0070fa)
  embed.set_author(name=f"COMMAND LOG")
  if ctx.interaction.user.avatar == None:
    url = "https://cdn.discordapp.com/embed/avatars/4.png"
  else: 
    url = ctx.interaction.user.avatar.url
  embed.set_thumbnail(url=url)
  embed.add_field(name="User",value="{}".format(ctx.interaction.user),inline=True)
  embed.add_field(name="User id",value="{}".format(ctx.interaction.user.id),inline=True)
  embed.add_field(name="Server name",value="{}".format(ctx.interaction.guild.name),inline=False)
  embed.add_field(name="Channel name",value="{}".format(ctx.interaction.channel.mention),inline=False)
  embed.add_field(name="Command name", value=f"{command_name}", inline=True)
  embed.set_footer(text='Logged')
  return(embed)

def no_perms(ctx):
    embed = discord.Embed(title="",description="DM <@920337055706386443> to buy the bot",color=0x0070fa)
    embed.set_author( name="You can't use the bot commands",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/1006466535881183272/image3837.png")
    return(embed)

def perms_expired(ctx):
    embed = discord.Embed(title="",description="DM <@920337055706386443> to buy the bot",color=discord.Color.red())
    embed.set_author( name="Your subscription has expired",icon_url="https://cdn.discordapp.com/attachments/936276886852603945/1006466535881183272/image3837.png")
    return(embed)