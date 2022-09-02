import disnake
import random
from disnake.ext import commands
from disnake.ui import Button, View
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config
import main

prefix = config.prefix
bot = main.bot

class knp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = "knp", aliases=["кнп", "лтз"])
    async def knp(self, ctx):
        button1 = Button(label="Камінь", style = disnake.ButtonStyle.grey, emoji="🪨")
        button2 = Button(label="Ножиці", style = disnake.ButtonStyle.grey, emoji="✂️")
        button3 = Button(label="Папір", style = disnake.ButtonStyle.grey, emoji="📰")

        async def button_callback1(interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.send_message("Це не твоя кнопка!", ephemeral=True)
            else:
                view.remove_item(button1)
                view.remove_item(button2)
                view.remove_item(button3)

                button = "Камінь"
                buttonans = random.choice(["Папір", "Камінь", "Ножиці"])

                if button == buttonans:
                    emb = disnake.Embed(title = "Нічия!", description=f"Ти вибрав: `{button}`\nЯ вибрав: `{buttonans}`", colour = disnake.Color.yellow())
                    emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url = ctx.author.display_avatar)
                    await interaction.response.edit_message(embed = emb, view = view)
                elif buttonans == "Ножиці" and button == button:
                    emb = disnake.Embed(title = "Ти переміг!", description=f"Ти вибрав: `{button}`\nЯ вибрав: `{buttonans}`", colour=disnake.Color.green())
                    emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url = ctx.author.display_avatar)
                    await interaction.response.edit_message(embed = emb, view = view)
                elif buttonans == "Папір" and button == button:
                    emb = disnake.Embed(title = "Ти програв:(", description=f"Ти вибрав: `{button}`\nЯ вибрав: `{buttonans}`", colour=disnake.Color.red())
                    emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url = ctx.author.display_avatar)
                    await interaction.response.edit_message(embed = emb, view = view)

        async def button_callback2(interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.send_message("Це не твоя кнопка!", ephemeral=True)
            else:
                view.remove_item(button1)
                view.remove_item(button2)
                view.remove_item(button3)

                button = "Ножиці"
                buttonans = random.choice(["Папір", "Камінь", "Ножиці"])

                if button == buttonans:
                    emb = disnake.Embed(title = "Нічия!", description=f"Ти вибрав: `{button}`\nЯ вибрав: `{buttonans}`", colour = disnake.Color.yellow())
                    emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url = ctx.author.display_avatar)
                    await interaction.response.edit_message(embed = emb, view = view)
                elif buttonans == "Папір" and button == button:
                    emb = disnake.Embed(title = "Ти переміг!", description=f"Ти вибрав: `{button}`\nЯ вибрав: `{buttonans}`", colour=disnake.Color.green())
                    emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url = ctx.author.display_avatar)
                    await interaction.response.edit_message(embed = emb, view = view)
                elif buttonans == "Камінь" and button == button:
                    emb = disnake.Embed(title = "Ти програв:(", description=f"Ти вибрав: `{button}`\nЯ вибрав: `{buttonans}`", colour=disnake.Color.red())
                    emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url = ctx.author.display_avatar)
                    await interaction.response.edit_message(embed = emb, view = view)

        async def button_callback3(interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.send_message("Це не твоя кнопка!", ephemeral=True)
            else:
                view.remove_item(button1)
                view.remove_item(button2)
                view.remove_item(button3)

                button = "Папір"
                buttonans = random.choice(["Папір", "Камінь", "Ножиці"])
                
                if button == buttonans:
                    emb = disnake.Embed(title = "Нічия!", description=f"Ти вибрав: `{button}`\nЯ вибрав: `{buttonans}`", colour = disnake.Color.yellow())
                    emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url = ctx.author.display_avatar)
                    await interaction.response.edit_message(embed = emb, view = view)
                elif buttonans == "Камінь" and button == button:
                    emb = disnake.Embed(title = "Ти переміг!", description=f"Ти вибрав: `{button}`\nЯ вибрав: `{buttonans}`", colour=disnake.Color.green())
                    emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url = ctx.author.display_avatar)
                    await interaction.response.edit_message(embed = emb, view = view)
                elif buttonans == "Ножиці" and button == button:
                    emb = disnake.Embed(title = "Ти програв:(", description=f"Ти вибрав: `{button}`\nЯ вибрав: `{buttonans}`", colour=disnake.Color.red())
                    emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url = ctx.author.display_avatar)
                    await interaction.response.edit_message(embed = emb, view = view)
        
        button1.callback = button_callback1
        button2.callback = button_callback2
        button3.callback = button_callback3

        view = View()
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)

        emb = disnake.Embed(title = "Камінь-Ножиці-Папір", description="Вибери: <Камінь> <Ножиці> <Папір>!", colour=disnake.Color.random())
        emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url = ctx.author.display_avatar)

        await ctx.send(embed = emb, view=view)
    
        

def setup(bot):
    bot.add_cog(knp(bot))