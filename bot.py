
#Author: Austin Han, Joshua Flemming
#Game Ideas: gambling (regular & 공기), blackjack, 윷놀이

import discord
import random
from discord.ext import commands
import asyncio
import os

bot = commands.Bot(command_prefix = '>')

@bot.event
async def on_ready():
    print('Bot is ready')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server')


#react to self-assign roles
@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 747968975278702592 and payload.event_type == 'REACTION_ADD':
        print(f'{payload.emoji}')
        roles = payload.member.guild.roles
        if payload.emoji.name == '👀':
             role = discord.utils.get(roles, name = 'asian')
             await payload.member.add_roles(role)
        elif payload.emoji.name == '👅':
             role = discord.utils.get(roles, name = 'chinese')
             await payload.member.add_roles(role)
        elif payload.emoji.name == '🍆':
             role = discord.utils.get(roles, name = 'korean')
             await payload.member.add_roles(role)
        elif payload.emoji.name == '💯':
             role = discord.utils.get(roles, name = 'peasant')
             await payload.member.add_roles(role)
        elif payload.emoji.name == '👂':
             role = discord.utils.get(roles, name = 'jingson')
             await payload.member.add_roles(role)

#remove react to self-remove roles
@bot.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == 747968975278702592 and payload.event_type == 'REACTION_REMOVE':
         guild_id = payload.guild_id
         user_id = payload.user_id
         user = bot.get_user(user_id)
         server = bot.get_guild(guild_id)
         member = server.get_member(user_id)
         roles = server.roles
         if payload.emoji.name == '👀':
             role = discord.utils.get(roles, name = 'asian')
             await member.remove_roles(role)
         elif payload.emoji.name == '👅':
             role = discord.utils.get(roles, name = 'chinese')
             await member.remove_roles(role)
         elif payload.emoji.name == '🍆':
             role = discord.utils.get(roles, name = 'korean')
             await member.remove_roles(role)
         elif payload.emoji.name == '💯':
             role = discord.utils.get(roles, name = 'peasant')
             await member.remove_roles(role)
         elif payload.emoji.name == '👂':
             role = discord.utils.get(roles, name = 'jingson')
             await member.remove_roles(role)

#provide Facebook link to official UMCP KSA page
@bot.command()
async def facebook(ctx):
    print('works')
    await ctx.send('https://www.facebook.com/UMCPKSA12')

@bot.command()
async def coinflip(ctx):
    str = 'null'
    if random.randint(1,2) %2 == 0:
        str = 'HEADS'
    else:
        str = 'TAILS'
    await ctx.send(str)

#send Code Names link
@bot.command()
async def codename(ctx):
    await ctx.send('https://www.horsepaste.com/ksaislit')

@bot.command()
async def roles(ctx):
    await ctx.send('Type: \n'+
                    '"!gen"\t: General Body\n'
                    '"!heaven"\t: Heaven Family\n'
                    '"!earth"\t: Earth Family\n'
                    '"!sun"\t: Sun Family\n'
                    '"!moon"\t: Moon Family\n'
                    '"!kdrama"\t: K-Drama binger\n'
                    '"!kpop"\t: K-Pop stan')

@bot.event
async def on_message(message):
    msg = message.content.lower()
    if 'ksa' in msg:
        await message.add_reaction(':ksa:748290833471766610')
    elif 'bitch' in msg:
        await message.channel.send('fuck you')
    elif 'sad' in msg:
        await message.channel.send('It really do be like that')
    elif 'depress' in msg:
        await message.channel.send('1-800-273-8255')

bot.run(os.environ.get('KSABOT_TOKEN'))
