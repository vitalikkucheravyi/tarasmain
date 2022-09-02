import disnake
from disnake.ext import commands
import random
import asyncio
from asyncio import sleep
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config
import main

prefix = config.prefix
bot = main.bot

class coin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name = "coin", description="Інформація о боті", aliases = ["монетка", "сщшт"])
    async def coin(self, ctx, arg=None):
      if arg == None:
          emb = disnake.Embed(title="Помилка", colour=disnake.Color.red())
          emb.add_field(name="Потрібно ввести що ви загадали!", value=f"{prefix}монетка 1/2\n1 - Орел, 2 - Решка")
          emb.set_image(url='https://steemitimages.com/DQmV7gkBhGo1kHP1UcWvTE7LmuYuBZqKSSbdkuWBZz9hnjq/dribbble_3.gif')
          emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
          await ctx.reply(embed=emb)
      else:
        if arg == "1":
            arg = "Орел"
        elif arg == "2":
            arg = "Решка"

        possible_responses = [
             'Решка',
             'Орел',
        ]
        pl1 = arg
        pl2 = random.choice(possible_responses)
        if pl1 == pl2:
            if pl2 == "Решка":
                emb = disnake.Embed(title="Зачейкайте, йде вибір!", colour=disnake.Color.green())
                emb.set_image(url='https://media.giphy.com/media/p9QEQ7UHzEQ1zoYjtN/giphy.gif')
                emb.set_author(name=ctx.command.description)
                emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                message = await ctx.reply(embed=emb)
                await asyncio.sleep(5)
                emb = disnake.Embed(title="Ти переміг! Вітаю!",colour=disnake.Color.green())
                emb.add_field(name="Ти загадав:", value=f"`{pl1}`")
                emb.add_field(name="Тобі випало:", value=f"`{pl2}`")
                emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                await message.edit(embed=emb)
            elif pl2 == "Орел":
                emb = disnake.Embed(title="Зачейкайте, йде вибір!", colour=disnake.Color.green())
                emb.set_image(url='https://media.giphy.com/media/IwZWmGU5QTWPsIJ2TG/giphy.gif')
                emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                message = await ctx.reply(embed=emb)
                await asyncio.sleep(5)
                emb = disnake.Embed(title="Ти переміг! Вітаю!", colour=disnake.Color.green())
                emb.add_field(name="Ти загадав:", value=f"`{pl1}`")
                emb.add_field(name="Тобі випало:", value=f"`{pl2}`")
                emb.set_footer(text="Відправлено " + ctx.author.display_name,icon_url=ctx.author.display_avatar.url)
                await message.edit(embed=emb)
        else:
            if pl2 == "Решка":
                emb = disnake.Embed(title="Зачейкайте, йде вибір!", colour=disnake.Color.green())
                emb.set_image(url='https://media.giphy.com/media/p9QEQ7UHzEQ1zoYjtN/giphy.gif')
                emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                message = await ctx.reply(embed=emb)
                await asyncio.sleep(5)
                emb = disnake.Embed(title="Ти програв :(", colour=disnake.Color.green())
                emb.add_field(name="Ти загадав:", value=f"`{pl1}`")
                emb.add_field(name="Тобі випало:", value=f"`{pl2}`")
                emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                await message.edit(embed=emb)
            elif pl2 == "Орел":
                emb = disnake.Embed(title="Зачейкайте, йде вибір!", colour=disnake.Color.green())
                emb.set_image(url='https://media.giphy.com/media/IwZWmGU5QTWPsIJ2TG/giphy.gif')
                emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                message = await ctx.reply(embed=emb)
                await asyncio.sleep(5)
                emb = disnake.Embed(title="Ти програв :(", colour=disnake.Color.green())
                emb.add_field(name="Ти загадав:", value=f"`{pl1}`")
                emb.add_field(name="Тобі випало:", value=f"`{pl2}`")
                emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                await message.edit(embed=emb)

def setup(bot):
    bot.add_cog(coin(bot))