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

class send(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name = "send", description="Сказати від імені бота")
    async def send(self, ctx, *, message):
        if ctx.author.id == 503904015638200340 or ctx.author.id == 660069567959400449:
            if message is None:
                await ctx.send(f"Приклад: {prefix}send Текст")
            else:
                for guild in bot.guilds:
                    try:
                        await guild.text_channels[0].send(message)
                    except:
                        await ctx.send("Вийшла помилка відправки!")
                await ctx.send("Повідомлення було відправлено!")
        else:
            await ctx.reply("Ви не маєте доступ до кмд!")


def setup(bot):
    bot.add_cog(send(bot))