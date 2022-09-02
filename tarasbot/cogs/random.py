import disnake
from disnake.ext import commands
import random
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config
import main

prefix = config.prefix
bot = main.bot

class randomn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name = "random", description="Інформація о боті", aliases = ["рандом", "кфтвщь"])
    async def random(self, ctx, number1 = None, number2 = None):
        if number1 is None:
            emb = disnake.Embed(title = "Помилка!", color= disnake.Color.red())
            emb.add_field(name = "Введіть 1 число!", value=f"Наприклад: {prefix}рандом **<1 число>** <2 число>")
            emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url= ctx.author.display_avatar.url)
            await ctx.send(embed = emb)
        elif number2 is None:
            emb = disnake.Embed(title = "Помилка!", color= disnake.Color.red())
            emb.add_field(name = "Введіть 2 число!", value=f"Наприклад: {prefix}рандом <1 число> **<2 число>**")
            emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url= ctx.author.display_avatar.url)
            await ctx.send(embed = emb)
        else:
            emb = disnake.Embed(title = "Рандомайзер чисел!", color= disnake.Color.random())
            emb.add_field(name = f"Вам випало: `{random.randint(int(number1), int(number2))}`", value=f"Вибір був з {number1} i {number2}!")
            emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url= ctx.author.display_avatar.url)
            await ctx.send(embed = emb)

def setup(bot):
    bot.add_cog(randomn(bot))