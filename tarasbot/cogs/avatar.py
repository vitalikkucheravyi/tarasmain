import disnake
from disnake.ext import commands
from disnake.ui import Button, View
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config
import main

prefix = config.prefix
bot = main.bot

class avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name = "avatar", description="Інформація о боті", aliases = ["аватар", "фмфефк"])
    async def avatar(self, ctx, member: disnake.Member = None):
        if member is None:
            member = ctx.author
        
        emb = disnake.Embed(title=f"Аватар користувача `{member.display_name}`", colour=disnake.Color.random())
        emb.set_image(url = member.display_avatar)
        emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url = ctx.author.display_avatar)
        await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(avatar(bot))