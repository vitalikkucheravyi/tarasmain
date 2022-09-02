import disnake
from disnake.ext import commands
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config

prefix = config.prefix


class prapor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="prapor", aliases=["зкфзщк", "прапор"])
    async def _prapor(self, ctx, user: disnake.Member = None):
        if user is None:
            user = ctx.author

        prapor = Image.open('prapor.jpg')
        avatar = user.avatar.with_size(128)
        avt = BytesIO(await avatar.read())
        img = Image.open(avt)
        img = img.resize((280, 280))
        prapor.paste(img, (380, 80))
        width, height = prapor.size
        draw = ImageDraw.Draw(prapor)
        text = "Слава Україні!"
        font = ImageFont.truetype('arial.ttf', 60)
        textwidth, textheight = draw.textsize(text, font)
        x = 320
        y = 10  #290
        draw.text((x, y), text, font=font)
        prapor.save('image.jpg')
        await ctx.send(file=disnake.File("image.jpg"))

    

def setup(bot):
    bot.add_cog(prapor(bot))