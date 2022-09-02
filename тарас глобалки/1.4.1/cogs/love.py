import disnake
from disnake.ext import commands
import asyncio
from asyncio import sleep
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config
import main

prefix = config.prefix
bot = main.bot

class love(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name = "love", description="Сказати від імені бота", aliases=["кохання", "дщму"])
    async def love(self, ctx):
        message = await ctx.send(":black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::black_heart:\n:black_heart::heart::black_heart::heart::black_heart::heart::black_heart::heart::black_heart:\n:heart::black_heart::black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart:\n:heart::black_heart::black_heart::black_heart::black_heart::black_heart::black_heart::black_heart::heart:\n:black_heart::heart::black_heart::black_heart::black_heart::black_heart::black_heart::heart::black_heart:\n:black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::black_heart:\n:black_heart::black_heart::black_heart::heart::black_heart::heart::black_heart::black_heart::black_heart:\n:black_heart::black_heart::black_heart::black_heart::heart::black_heart::black_heart::black_heart::black_heart:")
        await asyncio.sleep(1)
        await message.edit(content=":heart::heart::heart::black_heart::heart::black_heart::black_heart::black_heart::black_heart::heart::heart::heart::black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::heart::heart::heart::heart::black_heart:\n:black_heart::heart::black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::heart::black_heart::black_heart::black_heart::black_heart:\n:black_heart::heart::black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::heart::black_heart::black_heart::black_heart::black_heart:\n:black_heart::heart::black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::heart::heart::heart::heart::black_heart:\n:black_heart::heart::black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::heart::black_heart::black_heart::black_heart::black_heart:\n:black_heart::heart::black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::black_heart::heart::black_heart::heart::black_heart::black_heart::heart::black_heart::black_heart::black_heart::black_heart:\n:heart::heart::heart::black_heart::heart::heart::heart::black_heart::black_heart::heart::heart::heart::black_heart::black_heart::black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::heart::heart::heart::black_heart:")
        await asyncio.sleep(1)
        await message.edit(content=":heart::black_heart::black_heart::black_heart::heart::black_heart::black_heart::heart::heart::heart::black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart:\n:black_heart::heart::black_heart::heart::black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart:\n:black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart:\n:black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart:\n:black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart:\n:black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart::heart::black_heart::black_heart::black_heart::heart::black_heart:\n:black_heart::black_heart::heart::black_heart::black_heart::black_heart::black_heart::heart::heart::heart::black_heart::black_heart::black_heart::heart::heart::heart::black_heart::black_heart:")


def setup(bot):
    bot.add_cog(love(bot))