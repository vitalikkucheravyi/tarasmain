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
        emb = disnake.Embed(title = "ТарасБот", colour = disnake.Color.green())
        emb.add_field(name = ":hugging: Всім привіт! \n:wave:Мене звати Тарас!\n:robot: Я discord-bot котрий зроблений для розважання людей!(інколи просто можу трішки спамити)", value = f"Команда допомоги: {prefix}допомога або {prefix}help")
        emb.add_field(name = ":face_with_monocle: Мої соц.мережі!", value = f"Технічний discord-сервер: [Перейти]({config.server_invite})\nМій телеграм: [UKB project - проект український ботів]({config.telegram})" )
        await guild.text_channels[0].send(embed = emb)


def setup(bot):
    bot.add_cog(onguildjion(bot))