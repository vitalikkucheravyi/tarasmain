import disnake
import config
from disnake.ext import commands
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config
import main

prefix = config.prefix
bot = main.bot


class idea(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="idea", aliases=["швуф", "ідея", "запропонуватиідею"])
    async def _idea(self, ctx, *, idea=None):
        if idea is None:
            emb = disnake.Embed(title="Помилка :(", colour=disnake.Color.red())
            emb.add_field(name="Напишіть вашу ідею!", value=f"Приклад: {prefix}ідея <ваша ідея/пропозиція>")
            emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
            await ctx.send(embed=emb)
        else:
            emb = disnake.Embed(title="Ваша пропозиція була відправлена на технічний сервер!", colour=disnake.Color.green())
            emb.add_field(name="Ідея:", value=idea, inline=False)
            emb.set_footer(text=bot.user.name, icon_url=bot.user.display_avatar.url)
            await ctx.send(embed=emb)

            channel = bot.get_channel(1005738931469422622)
            guild = bot.get_guild(ctx.guild.id)
            invite = await guild.text_channels[0].create_invite(max_age=0, max_uses=0, temporary=False)

            emb1 = disnake.Embed(title="Мені повідомили про помилку!", colour=disnake.Color.red())
            emb1.add_field(name="Ідея:", value=idea, inline=False)
            emb1.add_field(name="Запропонував:", value=f"{ctx.author.id} | {ctx.author.mention}", inline=False)
            emb1.add_field(name="Сервер:", value=f"{ctx.guild.id} | {invite} | {ctx.guild.name}", inline=False)
            #emb1.set_thumbnail(url=ctx.guild.display_icon.url)
            emb1.set_footer(text=bot.user.name, icon_url=bot.user.display_avatar.url)
            msg = await channel.send(embed=emb1)

            await msg.add_reaction("✅")
            await msg.add_reaction("❌")
    

def setup(bot):
    bot.add_cog(idea(bot))