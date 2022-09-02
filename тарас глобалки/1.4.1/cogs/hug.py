import disnake
from disnake.ext import commands
import random
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config
import main

prefix = config.prefix
bot = main.bot

class hug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name = "hug", description="Сказати від імені бота", aliases=["обійми", "ргп"])
    async def hug(self, ctx, member: disnake.Member = None):
        if member is None:
            emb = disnake.Embed(title="Помилка :(", colour=disnake.Color.red())
            emb.add_field(name="Вкажіть кого обійняти!", value=(f'{prefix}обійми <member>'))
            emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
            await ctx.reply(embed=emb)
        else:
            if member == ctx.message.author:
                emb = disnake.Embed(title="Помилка :(", colour=disnake.Color.red())
                emb.add_field(name="Ти дебіл самого себе обміймати?!", value=(f'{prefix}обійми <member>'))
                emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                await ctx.reply(embed=emb)
            else:
                possible_responses = [
                    'https://i.gifer.com/2w.gif',
                    'https://i.gifer.com/WDf.gif',
                    'https://i.gifer.com/28oq.gif',
                    'https://i.gifer.com/BaLU.gif',
                    'https://i.gifer.com/239B.gif',
                    'https://i.gifer.com/TOhR.gif',
                    'https://i.gifer.com/1Wbv.gif',
                    'https://i.gifer.com/SZpi.gif',
                ]
                emb = disnake.Embed(title=f"Користучав `{ctx.author.display_name}` обійняв користувача `{member.display_name}`", colour=disnake.Color.green())
                emb.set_image(url=f'{random.choice(possible_responses)}')
                emb.set_footer(text="Вітаю вас! ", icon_url=bot.user.display_avatar.url)
                await ctx.reply(embed=emb)


def setup(bot):
    bot.add_cog(hug(bot))