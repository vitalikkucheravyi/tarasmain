import disnake
from disnake.ext import commands
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config
import main

prefix = config.prefix
bot = main.bot

class onguildjion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        emb = disnake.Embed(title = "ТарасБот", description=f"Всім привіт!👋\nДякую що мене додали!❤\nМене звати Тарас!🤖 Я розважальний дискорд бот!🤪\nЯ один з ботів проекта [UKB project]({config.telegram})!", colour = disnake.Color.green())
        emb.add_field(name = "👤Мій розробник:", value = f"{config.bot_creator}", inline=False)
        emb.add_field(name = "⚙Мій функціонал:", value = f"💭Чат-бот, можу відповідати на багато [слів]({config.words})(маю різні типу відповідей)\n🗯Всі команди бота можна подивитися - {prefix}допомога або {prefix}help", inline=False)
        emb.add_field(name = "🔗Мої посилання:", value=f"Мій технічний сервер: [Перейти]({config.server_invite})\nМій телеграм: [Перейти]({config.telegram})\nМоє посилання на додавання: [Додати]({config.invite})\nВсі слова бота: [Подивитися]({config.words})", inline=False)
        emb.set_thumbnail(url = bot.user.display_avatar.url)
        emb.set_image(file=disnake.File("images/ukb.png"))
        emb.set_footer(text = "Бот був створений для підтримки українців під час війни!💙💛 #stopwarinukraine⛔ Слава Україні!🇺🇦")
        await guild.text_channels[0].send(embed = emb)

    @commands.slash_command(name = "test", description="njdxlkfjn ")
    async def test(self, ctx):
        emb = disnake.Embed(title = "ТарасБот", description=f"Всім привіт!👋\nДякую що мене додали!❤\nМене звати Тарас!🤖 Я розважальний дискорд бот!🤪\nЯ один з ботів проекта [UKB project]({config.telegram})!", colour = disnake.Color.green())
        emb.add_field(name = "👤Мій розробник:", value = f"{config.bot_creator}", inline=False)
        emb.add_field(name = "⚙Мій функціонал:", value = f"💭Чат-бот, можу відповідати на багато [слів]({config.words})(маю різні типу відповідей)\n🗯Всі команди бота можна подивитися - {prefix}допомога або {prefix}help", inline=False)
        emb.add_field(name = "🔗Мої посилання:", value=f"Мій технічний сервер: [Перейти]({config.server_invite})\nМій телеграм: [Перейти]({config.telegram})\nМоє посилання на додавання: [Додати]({config.invite})\nВсі слова бота: [Подивитися]({config.words})", inline=False)
        emb.set_thumbnail(url = bot.user.display_avatar.url)
        emb.set_image(file=disnake.File("images/ukb.png"))
        emb.set_footer(text = "Бот був створений для підтримки українців під час війни!💙💛 #stopwarinukraine⛔ Слава Україні!🇺🇦")
        await ctx.send(embed = emb)


def setup(bot):
    bot.add_cog(onguildjion(bot))