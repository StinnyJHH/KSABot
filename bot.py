#Author: Austin Han, Joshua Fleming
#Game Ideas: gambling (regular & 공기), blackjack, 윷놀이

import discord
import random
import re
import asyncio
import os
from discord.ext import commands
from googletrans import Translator

bot = commands.Bot(command_prefix = '>')
translator = Translator()
bot.remove_command('help')

#allows you to know the bot's ready for use
@bot.event
async def on_ready():
    print('Bot is ready')

#allows you to know the bot's ready for use
@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server')

#reply and react to key words
@bot.event
async def on_message(message):
    await bot.process_commands(message)

    msg = message.content.lower()
    if 'ksa' in msg:
        await message.add_reaction(':ksa:748290833471766610')
    if 'sad' in msg:
        await message.channel.send('It really do be like that')
    if 'depress' in msg:
        await message.channel.send('1-800-273-8255, but Vitamin D also helps')

#react to self-assign roles
@bot.event
async def on_raw_reaction_add(payload):
    #for KSA
    if payload.message_id == 750151216071442502 and payload.event_type == 'REACTION_ADD':
        roles = payload.member.guild.roles

        #KSA server roles
        if str(payload.emoji.name) == 'sun':
            role = discord.utils.get(roles, name = 'Sun Family')
            await payload.member.add_roles(role) 
        elif str(payload.emoji.name) == 'heaven':
            role = discord.utils.get(roles, name = 'Heaven Family')
            await payload.member.add_roles(role)
        elif str(payload.emoji.name) == 'earth':
            role = discord.utils.get(roles, name = 'Earth Family')
            await payload.member.add_roles(role)
        elif str(payload.emoji.name) == 'moon':
            role = discord.utils.get(roles, name = 'Moon Family')
            await payload.member.add_roles(role)

    if payload.message_id == 747968975278702592 and payload.event_type == 'REACTION_ADD':   
        #test server roles
        if str(payload.emoji.name) == 'eyes':
             role = discord.utils.get(roles, name = 'asian')
             await payload.member.add_roles(role)
        elif str(payload.emoji.name) == 'tongue':
             role = discord.utils.get(roles, name = 'chinese')
             await payload.member.add_roles(role)
        elif str(payload.emoji.name) == 'eggplant':
             role = discord.utils.get(roles, name = 'korean')
             await payload.member.add_roles(role)
        elif str(payload.emoji.name) == '100':
             role = discord.utils.get(roles, name = 'peasant')
             await payload.member.add_roles(role)
        #why is mine an ear
        elif str(payload.emoji.name) == 'ear':
             role = discord.utils.get(roles, name = 'jingson')
             await payload.member.add_roles(role)

#remove react to self-remove roles
@bot.event
async def on_raw_reaction_remove(payload):

    guild_id = payload.guild_id
    user_id = payload.user_id
    user = bot.get_user(user_id)
    server = bot.get_guild(guild_id)
    member = server.get_member(user_id)
    roles = server.roles

    #KSA server roles
    if payload.message_id == 750151216071442502 and payload.event_type == 'REACTION_REMOVE':
        if str(payload.emoji.name) == 'sun':
            role = discord.utils.get(roles, name = 'Sun Family')
            await member.remove_roles(role) 
        elif str(payload.emoji.name) == 'heaven':
            role = discord.utils.get(roles, name = 'Heaven Family')
            await payload.member.remove_roles(role)
        elif str(payload.emoji.name) == 'earth':
            role = discord.utils.get(roles, name = 'Earth Family')
            await payload.member.remove_roles(role)
        elif str(payload.emoji.name) == 'moon':
            role = discord.utils.get(roles, name = 'Moon Family')
            await payload.member.remove_roles(role)

    if payload.message_id == 747968975278702592 and payload.event_type == 'REACTION_REMOVE':
        if str(payload.emoji.name) == 'eyes':
            role = discord.utils.get(roles, name = 'asian')
            await member.remove_roles(role)
        elif str(payload.emoji.name) == 'tongue':
            role = discord.utils.get(roles, name = 'chinese')
            await member.remove_roles(role)
        elif str(payload.emoji.name) == 'eggplant':
            role = discord.utils.get(roles, name = 'korean')
            await member.remove_roles(role)
        elif str(payload.emoji.name) == '100':
            role = discord.utils.get(roles, name = 'peasant')
            await member.remove_roles(role)
        elif str(payload.emoji.name) == 'ear':
            role = discord.utils.get(roles, name = 'jingson')
            await member.remove_roles(role)

#provide Facebook link to official UMCP KSA page
@bot.command()
async def facebook(ctx):
    await ctx.send('https://www.facebook.com/UMCPKSA12')

@bot.command()
async def insta(ctx):
    await ctx.send('https://www.instagram.com/umdksa/')

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

#Korean to English translate
@bot.command()
async def translate(ctx):
    #python regular expression to eliminate the command 
    #from the translating portion of the message
    part = re.split('^>translate ', ctx.message.content)
    string_to_translate = part[1]

    #ensure language of the given string is korean
    if str(translator.detect(string_to_translate).lang) == 'ko':
        result = translator.translate(string_to_translate, dest = 'en').text
    else:
        result = 'Please provide a word, phrase, or sentence typed in Korean'
    await ctx.send(result)

#lay out the bot's functionality to the user
#@bot.command()
#async def help(ctx):

bot.run(os.environ.get('KSABOT_TOKEN'))
