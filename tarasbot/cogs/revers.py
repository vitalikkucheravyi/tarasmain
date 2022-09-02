import disnake
from disnake.ext import commands
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config
import main

prefix = config.prefix
bot = main.bot

class revers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name = "revers", description="Інформація о боті", aliases = ["реверс", "кумукі"])
    async def revers(self, ctx, *, arg = None):
        if arg == None: 
            emb = disnake.Embed(title = "Помилка :(", description="**Введіть текст!**", colour = disnake.Color.red())
            emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
            await ctx.reply(embed=emb)
        else:
            text = arg [::-1]
            emb = disnake.Embed(title = "Реверс тексту", description=text, colour = disnake.Color.random())
            emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
            await ctx.send(embed=emb)
 
    

def setup(bot):
    bot.add_cog(revers(bot))