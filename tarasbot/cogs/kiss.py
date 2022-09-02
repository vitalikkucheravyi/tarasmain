import disnake
from disnake.ext import commands
import random
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config
import main

prefix = config.prefix
bot = main.bot

class kiss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name = "kiss", description="Сказати від імені бота", aliases=["поцілунок", "лшіі"])
    async def kiss(self, ctx, member: disnake.Member = None):
        if member is None:
            emb = disnake.Embed(title="Помилка :(", colour=disnake.Color.red())
            emb.add_field(name="Вкажіть кого поцілувати!",
                          value=(f'{prefix}поцілунок <member>'))
            emb.set_author(name=ctx.command.description)
            emb.set_footer(text="Відправлено " + ctx.author.display_name,
                           icon_url=ctx.author.display_avatar.url)
            await ctx.reply(embed=emb)
        else:
            if member == ctx.message.author:
                emb = disnake.Embed(title="Помилка :(", colour=disnake.Color.red())
                emb.add_field(name="Ти дебіл самого себе цілувати?!", value=(f'{prefix}поцілунок <member>'))
                emb.set_author(name=ctx.command.description)
                emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                await ctx.reply(embed=emb)
            else:
                possible_responses = [
                    'https://media0.giphy.com/media/KmxmoHUGPDjfQXqGgv/giphy.gif?cid=ecf05e47p1skpdxcyqbtc93yi7e0p4xveue1i3dfqjm1q3b8&rid=giphy.gif&ct=g',
                    'https://media.giphy.com/media/naAaDvbAoOYdW/giphy.gif',
                    'https://media.giphy.com/media/Vh3T3uY2vdgqZOTHH7/giphy.gif',
                    'https://media.giphy.com/media/QtqjZtkLNuRPi/giphy.gif',
                    'https://media.giphy.com/media/dMYVHzANYb9p6/giphy.gif',
                    'https://media.giphy.com/media/9G0AdBbVrkV3O/giphy.gif',
                    'https://media.giphy.com/media/fyM2loi1ZpOV2/giphy.gif',
                    'https://media.giphy.com/media/x28cIQSn19Tbi/giphy.gif',
                    'https://media.giphy.com/media/r4UG27LD5Ee5y/giphy.gif',
                ]
                emb = disnake.Embed(title=f"Користучав `{ctx.author.display_name}` поцілував користувача `{member.display_name}`", colour=disnake.Color.green())
                emb.set_image(url=f'{random.choice(possible_responses)}')
                emb.set_footer(text="Вітаю вас! ", icon_url=bot.user.display_avatar.url)
                await ctx.send(embed=emb)


def setup(bot):
    bot.add_cog(kiss(bot))