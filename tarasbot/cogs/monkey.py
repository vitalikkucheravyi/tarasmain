import disnake
from disnake.ext import commands

import requests
import json
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config
import main

prefix = config.prefix
bot = main.bot

class panda(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name = "panda", description="Сказати від імені бота", aliases=["панда", "зфтвф"])
    async def panda(self, ctx):
        response = requests.get('https://some-random-api.ml/img/panda')
        json_data = json.loads(response.text)

        emb = disnake.Embed(title = "Панда", colour = 0xff9900)
        emb.set_image(url = json_data['link'])
        await ctx.send(embed = emb)
        
def setup(bot):
    bot.add_cog(panda(bot))