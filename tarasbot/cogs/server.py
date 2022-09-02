import disnake
from disnake.ext import commands
import random
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config
import main

prefix = config.prefix
bot = main.bot

class server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.slash_command(name = "server", description="Інформація про сервер")
    async def server(self, ctx):
        emb = disnake.Embed(title=f"Інформація о сервері `{ctx.guild.name}`",
                            colour=disnake.Color.random(),
                            timestamp=ctx.created_at)
        emb.add_field(name = "Власник сервера:", value = f"{ctx.guild.owner}")
        emb.add_field(name="Сервер:",
                      value=f"`{ctx.guild.name}` | {ctx.guild.id}",
                      inline=False)
        emb.add_field(name="Дата створення:",
                      value=ctx.guild.created_at.strftime('%d.%m.%Y %H:%M:%S'),
                      inline=False)
        emb.add_field(name="Зображення сервера:", value=f"[Посилання]({ctx.guild.icon})", inline=False)
        emb.add_field(name="Користувачів:",
                      value=f"{ctx.guild.member_count}| {ctx.guild.bot_count}",
                      inline=False)
        emb.add_field(
            name="Канали:",
            value=
            f"Всього: {len(ctx.guild.channels)} | Категорій: {len(ctx.guild.categories)} | Текстових: {len(ctx.guild.text_channels)} | Голосових: {len(ctx.guild.voice_channels)}",
            inline=False)
        emb.add_field(name="Всього ролей:",
                      value=f"{len(ctx.guild.roles)}",
                      inline=False)
        emb.add_field(
            name="AFK канал:",
            value=
            f"{ctx.guild.afk_channel} | {ctx.guild.afk_channel.id} | {ctx.guild.afk_channel.mention}"
            if ctx.guild.afk_channel is not None else
            "На данному сервері не встановлений канал для AFK!",
            inline=False)
        emb.add_field(name="Рівень верифікації:",
                      value=f"{ctx.guild.verification_level}")
        emb.set_thumbnail(url=ctx.guild.icon)
        emb.set_footer(text="Відправлено " + ctx.author.display_name,
                       icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed=emb)
        
def setup(bot):
    bot.add_cog(server(bot))