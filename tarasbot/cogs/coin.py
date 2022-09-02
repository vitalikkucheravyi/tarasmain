import disnake
from disnake.ext import commands
from disnake.ui import Button, View
import random
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
    async def coin(self, ctx):
        button1 = Button(label = "Орел", style = disnake.ButtonStyle.grey, emoji="🦅")
        button2 = Button(label = "Решка", style=disnake.ButtonStyle.grey, emoji="🥜")

        possible_responses = [
             'Решка',
             'Орел',
        ]
        
        pl2 = random.choice(possible_responses)

        async def button1_callback(interaction):
            if interaction.user.id == ctx.author.id:
                view.remove_item(button1)
                view.remove_item(button2)
                
                if pl2 == "Орел":
                    emb = disnake.Embed(title="Ти переміг! Вітаю!",colour=disnake.Color.green())
                    emb.add_field(name="Ти загадав:", value=f"`Орел`")
                    emb.add_field(name="Тобі випало:", value=f"`{pl2}`")
                    emb.set_image(url='https://media.giphy.com/media/IwZWmGU5QTWPsIJ2TG/giphy.gif')
                    emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                    await interaction.response.edit_message(embed=emb, view = view)
                if pl2 == "Решка":
                    emb = disnake.Embed(title="Ти програв :(",colour=disnake.Color.red())
                    emb.add_field(name="Ти загадав:", value=f"`Орел`")
                    emb.add_field(name="Тобі випало:", value=f"`{pl2}`")
                    emb.set_image(url='https://media.giphy.com/media/p9QEQ7UHzEQ1zoYjtN/giphy.gif')
                    emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                    await interaction.response.edit_message(embed=emb, view = view)
            else:
                await interaction.response.send_message("Це не твоя кнопка!", ephemeral=True)
            
        async def button1_callback2(interaction):
            if interaction.user.id == ctx.author.id:
                view.remove_item(button1)
                view.remove_item(button2)
                
                if pl2 == "Решка":
                    emb = disnake.Embed(title="Ти переміг! Вітаю!", colour=disnake.Color.green())
                    emb.add_field(name="Ти загадав:", value=f"`Решка`")
                    emb.add_field(name="Тобі випало:", value=f"`{pl2}`")
                    emb.set_image(url='https://media.giphy.com/media/p9QEQ7UHzEQ1zoYjtN/giphy.gif')
                    emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                    await interaction.response.edit_message(embed=emb, view = view)
                if pl2 == "Орел":
                    emb = disnake.Embed(title="Ти програв :(", colour=disnake.Color.red())
                    emb.add_field(name="Ти загадав:", value=f"`Решка`")
                    emb.add_field(name="Тобі випало:", value=f"`{pl2}`")
                    emb.set_image(url='https://media.giphy.com/media/IwZWmGU5QTWPsIJ2TG/giphy.gif')
                    emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                    await interaction.response.edit_message(embed=emb, view = view)
            else:
                await interaction.response.send_message("Це не твоя кнопка!", ephemeral=True)

        button1.callback = button1_callback
        button2.callback = button1_callback2

        view = View()
        view.add_item(button1)
        view.add_item(button2)

        emb = disnake.Embed(title="Виберіть Орел/Решку", colour=disnake.Color.red())
        emb.set_image(url='https://steemitimages.com/DQmV7gkBhGo1kHP1UcWvTE7LmuYuBZqKSSbdkuWBZz9hnjq/dribbble_3.gif')
        emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        await ctx.reply(embed=emb, view = view)

    

def setup(bot):
    bot.add_cog(coin(bot))