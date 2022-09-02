import disnake
from disnake.ext import commands
import datetime
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config
import main

prefix = config.prefix
bot = main.bot

class boti(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name = "bot", description="Інформація о боті", aliases = ["бот", "ище"])
    async def bot(self, ctx):
        member = ctx.author
        memberlist = []
        for guild in ctx.bot.guilds:
            for member in guild.members:
                memberlist.append(member.id)

        emb = disnake.Embed(title = "Інформація про боті", colour = disnake.Color.green())
        emb.add_field(name="Про бота:", value= f"{bot.user.name} | {bot.user.id}", inline=False)
        emb.add_field(name="Версія бота:", value= f"{config.versionb}", inline=False)
        emb.add_field(name="Префікс бота:", value=f"{prefix}", inline=False)
        emb.add_field(name="Затримка бота:", value=f"{int(bot.ws.latency * 1000)}ms", inline=False)
        emb.add_field(name="Кількість серверів:", value=f"{len(bot.guilds)}", inline=False)
        #emb.add_field(name="Користувачі", value=f"{len(memberlist)}")
        emb.add_field(name="Розробник бота:", value=f"{config.bot_creator}", inline=False)
        emb.add_field(name="Мова:", value=f"{config.lang}", inline=False)
        emb.add_field(name="Мова програмування:", value = f"{config.langpr}", inline=False)
        emb.add_field(name="Бібліотека:", value=f"{config.library}", inline=False)
        emb.add_field(name="Посилання на бота:", value=f"[Додати бота]({config.invite})", inline=False)
        emb.add_field(name="Посилання на технічний сервер:", value=f"[Перейти]({config.server_invite})", inline=False)
        emb.add_field(name="Наш телеграм канал:", value=f"[Перейти]({config.telegram})", inline=False)
        emb.set_thumbnail(url = bot.user.display_avatar.url)
        emb.set_footer(text="Відправлено " + member.display_name, icon_url= member.display_avatar.url)
        emb.set_image(file=disnake.File("ukb.png"))
        await ctx.reply(embed = emb)

def setup(bot):
    bot.add_cog(boti(bot))