import disnake
from disnake.ext import commands
import random
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config
import main

prefix = config.prefix
bot = main.bot

class dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name = "dice", description="Інформація о боті", aliases = ["кості", "вшсу"])
    async def dice(self, ctx):
        dice1 = [1, 2, 3, 4, 5, 6]
        dice2 = [1, 2, 3, 4, 5, 6]
        result1 = random.choice(dice1)
        result2 = random.choice(dice2)
        allresult = result1 + result2

        if allresult == 7 or allresult == 11:
            emb = disnake.Embed(title="Ти переміг!", description=f"Тобі випало {result1} i {result2}! Всього: {allresult}", colour=disnake.Color.green())
            emb.set_author(name=ctx.command.description)
            emb.set_footer(text="Вітаю! " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
            await ctx.reply(embed=emb)
        else:
            emb = disnake.Embed(title="Ти програв :(",description=f"Тобі випало {result1} i {result2}! Всього: {allresult}", colour=disnake.Color.red())
            emb.set_author(name=ctx.command.description)
            emb.set_footer(text="В наступний раз пощастить! " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
            await ctx.reply(embed=emb)

def setup(bot):
    bot.add_cog(dice(bot))