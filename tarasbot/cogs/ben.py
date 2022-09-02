import disnake
from disnake.ext import commands
import random
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config
import main

prefix = config.prefix
bot = main.bot

class ben(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name = "ben", description="Інформація о боті", aliases = ["бен", "иут"])
    async def ben(self, ctx, *, arg=None):
        if arg == None:
            emb = disnake.Embed(title="Помилка", colour=disnake.Color.red())
            emb.add_field(name="Потрібно ввести питання!", value=f"{prefix}бен <питання>")
            emb.set_image(url='https://media.giphy.com/media/g5MJW6fmUj5QjHwoRo/giphy.gif')
            emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
            await ctx.reply(embed=emb)
        else:
            ben = ['1', '2', '3', '4']
            ben1 = random.choice(ben)
            if ben1 == '1':
                emb = disnake.Embed(title="YES", colour=disnake.Color.red())
                emb.set_image(url='https://media.giphy.com/media/q3RFxDz0M69cyW3Sme/giphy.gif')
                emb.set_footer(text="Відправлено " + ctx.author.display_name,icon_url=ctx.author.display_avatar.url)
                await ctx.reply(embed=emb)
            elif ben1 == '2':
                emb = disnake.Embed(title="NO", colour=disnake.Color.red())
                emb.set_image(url='https://media.giphy.com/media/RJ4Id8Lmgy27Gcx89X/giphy.gif')
                emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                await ctx.reply(embed=emb)
            elif ben1 == '3':
                emb = disnake.Embed(title="HOHOHO", colour=disnake.Color.red())
                emb.set_image(url='https://media.giphy.com/media/QcGPz8N68J7oka7nqw/giphy.gif')
                emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                await ctx.reply(embed=emb)
            elif ben1 == '4':
                emb = disnake.Embed(title="NOT", colour=disnake.Color.red())
                emb.set_image(url='https://media.giphy.com/media/3v4xlo89Q7pFQj49Cg/giphy.gif')
                emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                await ctx.reply(embed=emb)
        

def setup(bot):
    bot.add_cog(ben(bot))