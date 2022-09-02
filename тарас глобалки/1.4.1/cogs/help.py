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

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name = "help", description="Команди бота", aliases = ["допомога", "рудз"])
    async def help(self, ctx):
        emb = disnake.Embed(title = "Допомога | Інформація про боті", colour = disnake.Color.green())
        emb.add_field(name="Команди бота:", value=f"{prefix}допомога(help)\n{prefix}бот(bot)\n{prefix}монетка(coin)\n{prefix}поцілунок(kiss)\n{prefix}куля(ball)\n{prefix}кості(dice)\n{prefix}попіт(popit)\n{prefix}обійми(hug)\n{prefix}кохання(love)\n{prefix}ідея(idea)\n{prefix}помилка(mistake)\n{prefix}прапор(prapor)")
        emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        await ctx.reply(embed = emb)

def setup(bot):
    bot.add_cog(help(bot))