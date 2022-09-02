import disnake
import random
from disnake.ext import commands
from disnake.ui import Button, View
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config
import main

prefix = config.prefix
bot = main.bot

class month(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "war", aliases=["війна", "цфк"])
    async def war(self, ctx):
        war = "Близько 4 години за київським часом 24 лютого президент РФ В. Путін оголосив про [«спеціальну воєнну операцію»](https://www.youtube.com/watch?v=DtmqamWO7DQ) з метою нібито «демілітаризації та денацифікації України». Уже за кілька хвилин почалися ракетні удари по всій території [України](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/2022_Russian_invasion_of_Ukraine.svg/languk-525px-2022_Russian_invasion_of_Ukraine.svg.png)\
, у тому числі неподалік від Києва. Російські війська вдерлися до України поблизу Харкова, Херсона, Чернігова[, Сум, увійшовши з Росії, Білорусі й тимчасово окупованого Росією Криму"
        kronology = "[00:00](https://www.pravda.com.ua/news/2022/02/24/7325221/) - Міжнародні аеропорти Харькова, Дніпра, Запоріжжя закрилися до 7 ранку 24 числа.\n[00:20](https://suspilne.media/210076-terminove-zasidanna-radbezu-oon-sodo-ukraini-nazivo/) - Україна ініціювала термінове засідання Ради Безпеки ООН\n[00:50](https://www.youtube.com/watch?v=RbSN3GTTtTo) - Зверененя Володимира Зеленського\n01:31 - Росія закриває кілька ділянок повітряного простору\n[03:25](https://www.youtube.com/watch?v=DBSXdL5IsB0) - Обстріл Маріуполя\n03:40 - Перша колона РФ перетнула Луганську область\n[04:50](https://www.youtube.com/watch?v=taYTXHsUU5w) - звернення Путіна\n[04:55](https://chasdiy.org/wp-content/uploads/2022/02/photo_2022-02-24_07-44-54.jpg) - перші ракетні області всієї території України"
        kronology2 = "05:00 - Перший бій зі сторони Білорусі\n[5:30](https://cutt.ly/zXYMiRV) - Аеропорт Жуляни скасував рейси\n[06:50](https://t.me/V_Zelenskiy_official/725) - Звернення Володимира Зеенського\n[08:10](https://cutt.ly/SXYMbyx) - Введення Військового стану\n11:00 - Розпочато бій під Харьковом\n[11:30](https://www.pravda.com.ua/news/2022/02/24/7325342/) - Україна розірвала дипломатичні відносини з Росією\n[12:50](https://www.president.gov.ua/documents/692022-41413) - Законопроект про загальну мобілізацію\n[13:12](https://cutt.ly/cXYMZk9) - Висадка десанта РФ у Гостомелі\n[13:21](https://cutt.ly/GXYMVLb) - РФ захопила Північно-Кримський канала та Каховську ГЕС"
        knology2 = "[15:42](https://cutt.ly/bXYM75G) - Вторгення російського війська до Сум\n[16:30](https://www.unn.com.ua/uk/news/1965246-rosiyski-viyska-z-bilorusi-uviyshli-do-zoni-chaes) - Війська РФ увійшло до зони ЧАЕС\n[16:35](https://lb.ua/news/2022/02/24/506706_okupanti_vzyali_pid_kontrol.html) - РФ взяла під контроль аеропорт Антонов за 25км від Києва"
        knology3 = "[17:50](https://lb.ua/society/2022/02/24/506675_ostriv_zmiiniy_atakuvali_z.html) - Обстріл прикордонників та бійців ЗСУ а о.Зміїний\n18:10 - ЗСУ успішно відбили атаки російських військ на Харків, Суми та Київ\n[19:00](https://www.dw.com/uk/u-kyievi-oholosyly-komendantsku-hodynu/a-60897984) - РФ захопили ЧАЕС\n[20:30](https://www.youtube.com/watch?v=GKgY3Ojn4Yc) - заява президента США Джо Байдена\n[22:00](https://suspilne.media/210607-zmiinij-jmovirno-zahoplenij-zvazku-z-prikordonnikami-nemae-dpsu/) - РФ захопила о.Зміїний\n[22:37](https://www.pravda.com.ua/news/2022/02/24/7325572/) - Українські десантники зачистили від ворога аеродром у Гостомелі\n[00:00](https://www.president.gov.ua/documents/692022-41413) - Президент України В.Зеленський підписав про загальну мобілізацію"
        
        button1 = Button(label = "Російське вторгнення", url = "https://cutt.ly/jXY1FY6")
        button2 = Button(label = "Хронологія", url = "https://cutt.ly/uXY1KKx")
        button3 = Button(label = "Обличчя Азовсталі", url = "https://suspilne.media/240821-oblicca-azovstali-istorii-zahisnikiv-mariupola/")
        button4 = Button(label = "Володимир Зеленський", url = "https://t.me/V_Zelenskiy_official")
        button5 = Button(label = "Офіційні новини телеграм каналу:", url = "https://t.me/u_now")
        button6 = Button(label = "#stopwarinukraine", url = "https://www.youtube.com/watch?v=p5Yai_x18wU")
        button7 = Button(label = "Герої України!", url = "https://uk.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%93%D0%B5%D1%80%D0%BE%D1%97%D0%B2_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8")
        button8 = Button(label = "Карта повітряних тривог", url = "https://alerts.in.ua/")

        view = View()
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        view.add_item(button4)
        view.add_item(button5)
        view.add_item(button6)
        view.add_item(button7)
        view.add_item(button8)

        emb = disnake.Embed(title = "22.08.2022 - 180 днів", description=war, colour=disnake.Color.red())
        emb.add_field(name = "Хронологія 24 числа:", value=kronology)
        emb.add_field(name = "Продовження", value=kronology2)
        emb.add_field(name = "Продовження", value=knology2)
        emb.add_field(name = "Продовження", value=knology3)
        emb.add_field(name = "Присвячується містам:", value = "Запоріжжя, Харків, Маріуполь, Донецьк, Херсон, Київ, Чернігів, Суми, Луганськ", inline=False)
        emb.set_image(file=disnake.File("images/war.png"))
        emb.set_footer(text = "Слава Україні! Вічна пам'ять всім героям! #героїневмирають", icon_url=ctx.author.display_avatar)
        await ctx.send(embed = emb, view = view)
        

def setup(bot):
    bot.add_cog(month(bot))