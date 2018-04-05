import discord
from discord.ext import commands

class Tests():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def goodbye(self):
        """Says goodbye"""
        await self.bot.say("Good bye!")
    
def setup(bot):
    bot.add_cog(Tests(bot))
