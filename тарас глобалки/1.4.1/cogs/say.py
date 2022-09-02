from logging import PlaceHolder
import disnake
from disnake.ext import commands
import datetime
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config
import main

prefix = config.prefix
bot = main.bot

class say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name = "say", description="Сказати від імені бота", aliases = ["сказати", "іфн"])
    async def help(self, ctx, *, arg = None):
        if arg is None:
            emb = disnake.Embed(title = "Помилка", description="Вкажіть текст!", color=disnake.Colour.red())
            emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
            await ctx.reply(embed = emb)
        else:
            await ctx.send(arg)
            await ctx.message.delete()
            return 

def setup(bot):
    bot.add_cog(say(bot))