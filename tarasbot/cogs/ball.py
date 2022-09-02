import disnake
from disnake.ext import commands
import random
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config
import main

prefix = config.prefix
bot = main.bot

class ball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name = "ball", description="Інформація о боті", aliases = ["куля", "ифдд"])
    async def ball(self, ctx, *, arg=None):
        if arg is None:
            emb = disnake.Embed(title='Помилка', colour=disnake.Color.red())
            emb.add_field(name='Введіть запитання!(Питання можуть бути будь-які і відповідь буде рандомна!)', value=f'Приклад: {prefix}куля <питання>')
            emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
            await ctx.reply(embed=emb)
        else:
            possible_responses = [
                'Точно!',
                'Точно ні :(',
                'Так!',
                'Ні :(',
                'Дуже сумнівно...',
                'Безумовно так!',
                'Безумовно ні :(',
                'Швидше за все',
                'Зараз не можу передбачити',
                'Не знаю',
                'За моїми даними - ні :(',
                'За моїми даними - так!',
                'Мені здається так!',
                'Мені здається ні:(',
                'Моя відповідь ні',
                'Моя відповідь так',
                'Краще промовчу',
                'Навіть не думай',
                'Думаю ні!',
                'Думаю так!',
            ]

            emb = disnake.Embed(title=f"{random.choice(possible_responses)}", colour=disnake.Color.random())
            emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
            await ctx.reply(embed=emb)
        

def setup(bot):
    bot.add_cog(ball(bot))