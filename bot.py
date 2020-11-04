#!/usr/bin/env python3

import os

import discord
import traceback
from dotenv import load_dotenv
from discord.ext import commands


from os import listdir
from os.path import isfile, join


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
'''
Not needed since we are only doing a single server right now
GUILD = os.getenv('DISCORD_GUILD')
'''
BOT_URL = os.getenv('BOT_URL')
BOT_DESCRIPTION = os.getenv('BOT_DESCRIPTION')
WELCOME_CHANNEL = os.getenv('WELCOME_CHANNEL')

def get_prefix(bot, message):
    prefixes = ['!', '?']
    if not message.guild:
        # Only allow ? to be used in DMs
        return '?'
    return commands.when_mentioned_or(*prefixes)(bot, message)


intents = discord.Intents.all()
bot = commands.Bot(command_prefix=get_prefix,description=BOT_DESCRIPTION, intents=intents)







'''
Commands dir
'''
commands_dir = "commands"





@bot.event
async def on_ready():
    """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    await bot.change_presence(activity = discord.Activity(type=discord.ActivityType.listening,name="To you", url=BOT_URL))

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name=WELCOME_CHANNEL)
    await member.add_roles(discord.utils.get(member.guild.roles, name="PFY"))
    await channel.send("Say hello to our newest PFY {}!".format(member.mention))

if __name__ == '__main__':
    '''
    Autoload commands
    '''
    for extension in [f.replace('.py', '') for f in listdir(commands_dir) if isfile(join(commands_dir, f))]:
        try:
            print(f'Loaded {extension}.')
            bot.load_extension(commands_dir + "." + extension)
        except (discord.ClientException, ModuleNotFoundError):
            print(f'Failed to load extension {extension}.')
            traceback.print_exc()



bot.run(TOKEN, bot=True, reconnect=True)
