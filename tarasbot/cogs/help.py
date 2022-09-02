import disnake
from disnake.ext import commands
from disnake.ui import Select, View
import datetime
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config
import main

prefix = config.prefix
bot = main.bot

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name = "help", description="Команди бота", aliases = ["допомога", "рудз"])
    async def help(self, ctx):
        select = Select(
            placeholder= "Виберіть тип допомоги",
            options=[
                disnake.SelectOption(label = "Інформаційні команди", emoji="📰"),
                disnake.SelectOption(label = "Розважальні команди", emoji="🤪"),
                disnake.SelectOption(label = "Утіліти", emoji="♻"),
                disnake.SelectOption(label = "Всі команди", emoji="🗂")
            ]
        )

        async def call_back(intaraction):
            if intaraction.author .id == ctx.author.id:
                value = select.values[0]
                view.remove_item(select)

                information = f"{prefix}допомога(help) - всі команди бота\n{prefix}бот(bot) - інформація о боті\n{prefix}аватар(avatar) - аватар користувача\n{prefix}війна(war) - вся інформація о війні"
                fun = f"{prefix}куля(ball) - відповіді на питання(8ball)\n{prefix}бен(ben) - відповідь на питання з гри Бен\n{prefix}попіт(popit) - попіт\n{prefix}монетка(coin) - гра в Орел/Решку\n{prefix}кості(dice) - гра в Кості(кубики)\n{prefix}кнп(knp) - гра Камінь-Ножниці-Папір\n{prefix}поцілунок(kiss) - поцілувати користувача\n{prefix}обійми(hug) - обійняти користувача\n{prefix}танці - почати танцювати\n{prefix}кохання(love) - надпис I LOVE YOU\n{prefix}аватарф(avatarf) - фільтр аватар\n{prefix}москаль(moskal) - на скільки % ти москаль\n{prefix}реверс(reverse) - перевертає текст"
                others = f"{prefix}рандом(random) - вибрати рандомне число з двух представленних\n{prefix}пароль(password) - генератор рандомних паролів різних складностей(Легкі/Середні/Тяжкі)\n{prefix}прапор(prapor) - вивести картинку з Слава Україні та аватаром користувача\n{prefix}кіт(cat) - показати кота\n{prefix}лис(fox) - показати лиса\n{prefix}пес(dog) - показати пса\n{prefix}панда(panda) - показати панду\n{prefix}ідея(idea) - запропонувати ідею ботові\n{prefix}помилка(mistake) - повідомити про помилку у ботові" 
                all = f"{prefix}допомога(help)\n{prefix}бот(bot)\n{prefix}війна(war)\n{prefix}ідея(idea)\n{prefix}помилка(mistake)\n{prefix}монетка(coin)\n{prefix}кості(dice)\n{prefix}куля(ball)\n{prefix}бен(ben)\n{prefix}кнп(knp)\n{prefix}попіт(popit)\n{prefix}поцілунок(kiss)\n{prefix}обійми(hug)\n{prefix}танці(dance)\n{prefix}кохання(love)\n{prefix}прапор(prapor)\n{prefix}пароль(password)\n{prefix}рандом(random)\n{prefix}аватар(avatar)\n{prefix}аватарф(avatarf)\n{prefix}кіт(cat)\n{prefix}пес(dog)\n{prefix}лис(fox)\n{prefix}панда(panda)\n{prefix}москаль(moskal)\n{prefix}реверс(revers)"

                if value == "Інформаційні команди":
                    emb = disnake.Embed(title = "📰Інформаційні команди:", description=information, colour = disnake.Color.random())
                    emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url = ctx.author.display_avatar)
                    await intaraction.response.edit_message(embed = emb)
                elif value == "Розважальні команди":
                    emb = disnake.Embed(title = "🤪Розважальні команди%", description=fun, colour = disnake.Color.random())
                    emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url = ctx.author.display_avatar)
                    await intaraction.response.edit_message(embed = emb)
                elif value == "Утіліти":
                    emb = disnake.Embed(title = "♻Інші команди:", description=others, colour = disnake.Color.random())
                    emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url = ctx.author.display_avatar)
                    await intaraction.response.edit_message(embed = emb)
                elif value == "Всі команди":
                    emb = disnake.Embed(title ="🗂Всі команди:", description=all, colour = disnake.Color.random())
                    emb.set_footer(text = f"Відправлено {ctx.author.display_name}", icon_url = ctx.author.display_avatar)
                    await intaraction.response.edit_message(embed = emb)
            else:
                 await intaraction.response.send_message("Це не твоя кнопка!", ephemeral=True)  
    
        select.callback = call_back
        view = View()
        view.add_item(select)

        emb = disnake.Embed(title = "📚Допомога", description="Виберіть тип", colour = disnake.Color.green())
        emb.set_footer(text="Відправлено " + ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        await ctx.reply(embed = emb, view = view)

def setup(bot):
    bot.add_cog(help(bot))