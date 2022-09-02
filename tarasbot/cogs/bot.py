import disnake
from disnake.ext import commands
from disnake.ui import Button, View
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
        button1 = Button(label = "Додати бота", url = config.invite, emoji="🔗")
        button2 = Button(label = "Технічний сервер", url = config.server_invite, emoji="🔗")
        button3 = Button(label = "UKB project", url = config.telegram, emoji="🔗")

        view = View()
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)

        memberlist = []
        for guild in ctx.bot.guilds:
            for member in guild.members:
                memberlist.append(member.id)

        emb = disnake.Embed(title = "Інформація про боті", description="`ТарасБот - український discord бот, котрий був створений для підтримки українців під час війни! Бот входить до проекту - UKB preject! Бот знає деяку кількість слів і вміє на них відповідати!`", colour = disnake.Color.green())
        emb.add_field(name="🤖Про бота:", value= f"{bot.user.name} | {bot.user.id}", inline=False)
        emb.add_field(name="🛠Бот був створений:", value= f"15.08.2022", inline=False)
        emb.add_field(name="🆙Версія бота:", value= f"{config.versionb}", inline=False)
        emb.add_field(name="🖊Префікс бота:", value=f"{prefix}", inline=False)
        emb.add_field(name="📛Затримка бота:", value=f"{int(bot.ws.latency * 1000)}ms", inline=False)
        emb.add_field(name="♾Кількість серверів:", value=f"{len(bot.guilds)}", inline=False)
        #emb.add_field(name="Користувачі", value=f"{len(memberlist)}", inline=False)
        emb.add_field(name="👤Розробник бота:", value=f"{config.bot_creator}", inline=False)
        emb.add_field(name="🇺🇦Мова:", value=f"{config.lang}", inline=False)
        emb.add_field(name="🐍Мова програмування:", value = f"{config.langpr}", inline=False)
        emb.add_field(name="📕Бібліотека:", value=f"{config.library}", inline=False)
        emb.set_thumbnail(url = bot.user.display_avatar.url)
        emb.set_footer(text=f"Всі команди можете подивитися в {prefix}допомога", icon_url= ctx.author.display_avatar.url)
        emb.set_image(file=disnake.File("images/ukb.png"))
        await ctx.reply(embed = emb, view = view)

def setup(bot):
    bot.add_cog(boti(bot))