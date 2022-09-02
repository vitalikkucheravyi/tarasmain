from logging import PlaceHolder
import disnake
from disnake.ext import commands
import random
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')

class dance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name = "dance", description="Команди бота", aliases = ["танці", "вфтсу"])
    async def dance(self, ctx):
        dances = [
          "https://media.giphy.com/media/cklPOHnHepdwBLRnQp/giphy.gif",
          "https://media.giphy.com/media/DhstvI3zZ598Nb1rFf/giphy.gif",
          "https://media.giphy.com/media/tsX3YMWYzDPjAARfeg/giphy.gif",
          "https://media.giphy.com/media/8m4R4pvViWtRzbloJ1/giphy.gif",
          "https://media.giphy.com/media/RX7N03MEUafW8/giphy.gif",
          "https://media.giphy.com/media/13hxeOYjoTWtK8/giphy.gif",
        ]

        emb = disnake.Embed(title=f"Користувач `{ctx.author.display_name}` почав танцювати!", colour=disnake.Color.random())
        emb.set_image(url=random.choice(dances))
        await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(dance(bot))