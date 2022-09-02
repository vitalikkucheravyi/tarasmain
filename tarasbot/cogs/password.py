import disnake
from disnake.ext import commands
from disnake.ui import Button, View
import random
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')

class password(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name = "password", description="Команди бота", aliases = ["пароль", "зфііцщкв"])
    async def passworde(self, ctx):
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        high_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        symbols = "!@#$%^&*()_-=+':;{[}]\/<>"

        button1 = Button(label="Легкий", emoji="1⃣", style=disnake.ButtonStyle.green)
        button2 = Button(label="Середній", emoji="2⃣", style=disnake.ButtonStyle.primary)
        button3 = Button(label="Тяжкий", emoji="3⃣", style=disnake.ButtonStyle.danger)

        async def button1_callback(interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.send_message("Це не твоя кнопка!", ephemeral=True)
            else:
                easy = high_case+lower_case
                length1 = 8
                passwe = "".join(random.sample(easy, length1))
                emb = disnake.Embed(title = "Генератор пароля", description= f"Ваш пароль: `{passwe}`", color= disnake.Color.random())
                emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
                await ctx.author.send(embed=emb)
                await interaction.response.send_message("Пароль було відправлено вам в приватні повідомлення!", ephemeral = True)
        async def button2_callback(interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.send_message("Це не твоя кнопка!", ephemeral=True)
            else:
                middle = high_case+lower_case+numbers
                length2 = 12
                passwm = "".join(random.sample(middle, length2))
                emb = disnake.Embed(title = "Генератор пароля", description= f"Ваш пароль: `{passwm}`", color= disnake.Color.random())
                emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
                await ctx.author.send(embed=emb)
                await interaction.response.send_message("Пароль було відправлено вам в приватні повідомлення!", ephemeral = True)
        async def button3_callback(interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.send_message("Це не твоя кнопка!", ephemeral=True)
            else:
                high = high_case+lower_case+numbers+symbols
                length3 = 16
                passwh = "".join(random.sample(high, length3))
                emb = disnake.Embed(title = "Генератор пароля", description= f"Ваш пароль: `{passwh}`", color= disnake.Color.random())
                emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
                await ctx.author.send(embed=emb)
                await interaction.response.send_message("Пароль було відправлено вам в приватні повідомлення!", ephemeral = True)

        button1.callback = button1_callback
        button2.callback = button2_callback
        button3.callback = button3_callback

        view = View()
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)

        emb = disnake.Embed(title = "Помилка", color= disnake.Color.red())
        emb.add_field(name = "Вкажіть тип пароля!", value = "Типи:\n1 - легкий пароль(8 символів)\n2 - середній пароля(12 символів)\n3 - тяжкий пароль(16 символів)")
        emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
        await ctx.send(embed=emb, view = view)
        
def setup(bot):
    bot.add_cog(password(bot))