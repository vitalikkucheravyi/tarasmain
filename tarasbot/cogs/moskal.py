import disnake
from disnake.ext import commands
import sys
import random
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config
import main

prefix = config.prefix
bot = main.bot

class moskal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name = "moskal", description="Інформація о боті", aliases = ["москаль", "ьщілфд"])
    async def moskal(self, ctx,):
        moskal = random.randint(0, 100)

        if moskal <=30:
            emb = disnake.Embed(title="На скільки % ти москаль(все рандом!)", description=f"На {moskal}% ти москаль!", colour = disnake.Color.green())
            emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
            await ctx.send(embed=emb)
        elif moskal >30 and moskal <=50:
            emb = disnake.Embed(title="На скільки % ти москаль(все рандом!)", description=f"На {moskal}% ти москаль!", colour = disnake.Color.yellow())
            emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
            await ctx.send(embed=emb)
        elif moskal >50 and moskal <=80:
            emb = disnake.Embed(title="На скільки % ти москаль(все рандом!)", description=f"На {moskal}% ти москаль!", colour = disnake.Color.orange())
            emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
            await ctx.send(embed=emb)
        elif moskal >80 and moskal <= 100:
            emb = disnake.Embed(title="На скільки % ти москаль(все рандом!)", description=f"На {moskal}% ти москаль!", colour = disnake.Color.red())
            emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
            await ctx.send(embed=emb)

        
    

def setup(bot):
    bot.add_cog(moskal(bot))