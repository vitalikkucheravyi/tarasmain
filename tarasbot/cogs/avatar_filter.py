from urllib import response
import disnake
from disnake.ext import commands
from disnake.ui import Button, View
import io
import aiohttp
from io import BytesIO
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config
import main

prefix = config.prefix
bot = main.bot

class avatarfilter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name = "avatarf", description="Інформація о боті", aliases = ["аватарф", "фмфефкф"])
    async def avatarf(self, ctx,):
        button1 = Button(label = "WASTED", emoji="❌")
        button2 = Button(label = "Jail", emoji="#⃣")
        button3 = Button(label = "Triggered", emoji="⭕")
        button4 = Button(label = "Mission Pased", emoji="✅")

        async def button_callback1(interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.send_message("Це не твоя кнопка!", ephemeral=True)
            else:
                filter = "https://some-random-api.ml/canvas/wasted?avatar="
                async with aiohttp.ClientSession() as filterSession:
                    async with filterSession.get(f'{filter}{ctx.author.display_avatar}') as filterImage:

                        imageData = io.BytesIO(await filterImage.read())

                        await filterSession.close()
                        emb = disnake.Embed(title = "Фільтр `WASTED`", colour = disnake.Color.random())
                        emb.set_image(file=disnake.File(imageData, 'newavatar.png'))
                        emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
                        await interaction.response.send_message(embed=emb)

        async def button_callback2(interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.send_message("Це не твоя кнопка!", ephemeral=True)
            else:
                filter = "https://some-random-api.ml/canvas/jail?avatar="
                async with aiohttp.ClientSession() as filterSession:
                    async with filterSession.get(f'{filter}{ctx.author.display_avatar}') as filterImage:

                        imageData = io.BytesIO(await filterImage.read())

                        await filterSession.close()
                        emb = disnake.Embed(title = "Фільтр `Jail`", colour = disnake.Color.random())
                        emb.set_image(file=disnake.File(imageData, 'newavatar.png'))
                        emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
                        await interaction.response.send_message(embed=emb)

        async def button_callback3(interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.send_message("Це не твоя кнопка!", ephemeral=True)
            else:
                filter = "https://some-random-api.ml/canvas/triggered?avatar="
                async with aiohttp.ClientSession() as filterSession:
                    async with filterSession.get(f'{filter}{ctx.author.display_avatar}') as filterImage:

                        imageData = io.BytesIO(await filterImage.read())

                        await filterSession.close()
                        emb = disnake.Embed(title = "Фільтр `Triggered`", colour = disnake.Color.random())
                        emb.set_image(file=disnake.File(imageData, 'newavatar.png'))
                        emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
                        await interaction.response.send_message(embed=emb)

        async def button_callback4(interaction):
            if interaction.user.id != ctx.author.id:
                await interaction.response.send_message("Це не твоя кнопка!", ephemeral=True)
            else:
                filter = "https://some-random-api.ml/canvas/passed?avatar="
                async with aiohttp.ClientSession() as filterSession:
                    async with filterSession.get(f'{filter}{ctx.author.display_avatar}') as filterImage:

                        imageData = io.BytesIO(await filterImage.read())

                        await filterSession.close()
                        emb = disnake.Embed(title = "Фільтр `Mission Passed`", colour = disnake.Color.random())
                        emb.set_image(file=disnake.File(imageData, 'newavatar.png'))
                        emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
                        await interaction.response.send_message(embed=emb)

        button1.callback = button_callback1
        button2.callback = button_callback2
        button3.callback = button_callback3
        button4.callback = button_callback4

        view = View()
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        view.add_item(button4)

        emb = disnake.Embed(title = "Виберіть фільтр!", colour=disnake.Color.random())
        emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url=ctx.author.display_avatar)
        await ctx.reply(embed=emb, view = view)

def setup(bot):
    bot.add_cog(avatarfilter(bot))