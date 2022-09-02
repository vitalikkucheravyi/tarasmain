from logging import PlaceHolder
import disnake
from disnake.ext import commands
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')


class popit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name = "popit", description="Команди бота", aliases = ["попіт", "зщзше"])
    async def popit(self, ctx):
        await ctx.reply("||:red_square:||||:red_square:||||:red_square:||||:red_square:||||:red_square:||||:red_square:||\n||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||\n||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||\n||:green_square:||||:green_square:||||:green_square:||||:green_square:||||:green_square:||||:green_square:||\n||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||\n||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||")
        

def setup(bot):
    bot.add_cog(popit(bot))