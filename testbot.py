#!/usr/bin/env python3
import discord
import asyncio
import configparser
from discord.ext import commands

#client = discord.Client()
config = configparser.ConfigParser()
config.read('config.ini')
defaultConfig = config['DEFAULT']
token = defaultConfig['token']
prefix = defaultConfig['prefix']
bot = commands.Bot(command_prefix=prefix)
startup_extensions = ['commands.test_commands']
em = discord.Embed(title='My Embed Title', description='My **Embed** Content.', colour=discord.Colour.blue())

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))

@bot.command()
async def hello():
    """Responds as Ewan would."""
    await bot.say("Hello there")

@bot.command(pass_context=True)
async def embed(ctx):
    """Sends response as Embed object"""
    em.title = "I'm an embedded object"
    em.description = "This is my description"
    await bot.send_message(ctx.message.channel, embed=em)
#@client.event
## Receive message
#async def on_message(message):
#    usrIn = message.content.split()
#    if len(usrIn) < 2:
#        userIn.append('blank')
#    preflen = len(prefix)
#    response = ""
#    if message.content[0:preflen] == prefix:
#        command = usrIn[0][preflen:]
#        print ("User: " + message.author.name)
#        print ("Message: " + message.content)
#        print ("Command: " + command + "\n")
#        #List commands here
#        if command == 'hello':      #test command
#            response = "hello there!"
#            em = discord.Embed(title='My Embed Title', description='My **Embed** Content.', colour=discord.Colour.blue())
#
#        elif command == 'help':
#            response = "Available commands:\n\t!hello"
#
#        else:
#            response = "Command not recognized.\nPlease use " + prefix + "help for a list of commands"
#
##        await client.send_message(message.channel, response)
#        await client.send_message(message.channel, embed=em)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run(token)
