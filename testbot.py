#!/usr/bin/env python3
import discord
import asyncio
import configparser

client = discord.Client()
config = configparser.ConfigParser()
config.read('config.ini')
defaultConfig = config['DEFAULT']
token = defaultConfig['token']
prefix = defaultConfig['prefix']

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
# Receive message
async def on_message(message):
    usrIn = message.content.split()
    preflen = len(prefix)
    response = ""
    if message.content[0:preflen] == prefix:
        command = usrIn[0][preflen:]
        print ("User: " + message.author.name)
        print ("Message: " + message.content)
        print ("Command: " + command + "\n")
        #List commands here
        if command == 'hello':      #test command
            response = "hello there!"
            em = discord.Embed(title='My Embed Title', description='My Embed Content.', colour=discord.Colour.blue())

        elif command == 'help':
            response = "Available commands:\n\t!hello"

        else:
            response = "Command not recognized.\nPlease use " + prefix + "help for a list of commands"

#        await client.send_message(message.channel, response)
        await client.send_message(message.channel, embed=em)

client.run(token)
