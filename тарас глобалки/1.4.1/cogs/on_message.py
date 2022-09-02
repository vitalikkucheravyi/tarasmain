import disnake
from disnake.ext import commands
import random
import json 
import requests
import sys
sys.path.insert(0, 'C:\\Users\\USVER\\Desktop\\UKB project\\Taras\\tarasbot')
import config
import main

prefix = config.prefix
bot = main.bot

putin=['putin', 'путин', 'путін', 'ПУТІН', 'ПУТИН', 'Путин', 'Путін']
rushia=['РОСИЯ', 'РОСИИ', 'росия', 'Росия', 'России', 'россии', 'россия', 'РОССИИ', 'росии']

class onmessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_message(self, message):
        ping = bot.ws.latency
        for a in rushia:
            if a in message.content:
                if message.author.id == bot.user.id:
                    return
                else:
                    await message.channel.send('Росія хуйовая ваша дєржава! Слава Україні!:flag_ua:')
        for a in putin:
            if a in message.content:
                if message.author.id == bot.user.id:
                    return
                else:
                    await message.channel.send('Хуйло не здох ще :( Молимося і віримо в бога!')
        if 'слава '+'україні' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Героям слава!:flag_ua:')
        elif bot.user.mention in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send(f"Мій префікс - ```{prefix}```")
        elif 'лукашенко' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Повія хуйла!')
        elif 'наливай' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Я за здоровий спосіб життя!')
        elif 'ладно' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Ем... Ладно...')
        elif 'покажи '+'лису' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                response = requests.get('https://some-random-api.ml/img/fox')
                json_data = json.loads(response.text)

                emb = disnake.Embed(title = "На тобі лису", colour = 0xff9900)
                emb.set_image(url = json_data['link'])
                await message.channel.send(embed = emb)
        elif 'покажи '+'тараса' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                emb = disnake.Embed(title = "Я не люблю себе показувати, но тобі можна!", colour = 0xff9900)
                emb.set_image(url = "https://roi4cio.com/fileadmin/_processed_/3/8/csm_Chatbot_Development_5712915923.jpg")
                await message.channel.send(embed = emb)
        elif 'покажи '+'кота' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                response = requests.get('https://some-random-api.ml/img/cat')
                json_data = json.loads(response.text)

                emb = disnake.Embed(title = "На тобі кіт", colour = 0xff9900)
                emb.set_image(url = json_data['link'])
                await message.channel.send(embed = emb)
        elif 'покажи '+'пса' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                response = requests.get('https://some-random-api.ml/img/dog')
                json_data = json.loads(response.text)

                emb = disnake.Embed(title = "Песик", colour = 0xff9900)
                emb.set_image(url = json_data['link'])
                await message.channel.send(embed = emb)
        elif 'анекдот' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Привіт!',
                '– Лікарю, скільки разів на тиждень у моєму віці можна займатись сексом?\n– Два рази в неділю.\n– Добре, у неділю два рази… А в будній день скільки?',

                '– Отче, чоловік зраджує. Порадьте, що робити?\n– Скропи сковорідку святою водою і наверни його на шлях праведний.',

                '– Іване, ти памятаєш що було 35 років тому?\n– Звісно ж! Чорнобиль вибухнув!\n– Дурнику, ми одружилися!\n– Так, біда не ходить одна…',

                'Вечорами Мальвіна любила дивитися одним оком на зоряне небо та згадувати той незабутній поцілунок Буратіно.',

                'Анекдот про тещу\nПриходить теща в гості і каже зятю:\n– У мене для тебе дві новини: одна погана, а інша хороша!\n– Мамо, я бачу, що ви живі і здорові, а яка гарна новина?',

                'Чим відрізняється нещасний випадок від нещастя?\nЯкщо ваша теща впала в річку, то це – нещасний випадок.\nА якщо її врятували, то це – нещастя.',

                'Лікар, розглядаючи історію хвороби, каже чоловікові:\n– Ваша теща абсолютно здорова. Це підтверджують всі аналізи і рентгенівські знімки.\n– А чи не можна, лікарю, щоб я був зовсім спокійний, зробити розтин?',

                'Назвав тещу «дурою» – дружина замовкла на тиждень.\nЩе раз назвав дурою -замовкла ще на тиждень.\nОсь вона, кнопка «MUTE» !!!',

                '– Галю, а чого твій Василько так кричить???\n– Та зуби лізуть…\n– Які зуби, йому ж за 50?!\n– Вставні! Вчора проковтнув…',

                'Петрович впустив собі на ногу чавунну батерею і признався…, що вступав у статеві відносини з цією батареєю, з директором заводу і, власне, з самим заводом…',

                'Турист із Венеції назвавши Миколу гондольєром, був викинутий із човна посеред Дніпра)))',

                'Диспетчер швидкої по телефону:\n– …висловлюйтесь зрозуміліше!!! “Йоб…вся” — це впав чи збожеволів?',

                'Ті, у кого є мізки і зв’язки, йдуть в бізнес.\nТі, у кого є мізки, але немає зв’язків – в науку.\nТі, у кого є зв’язки, але немає мізків – в політику.',

                'Чим жінка схожа на автомобіль\n– Чим жінка схожа на автомобіль?\n– Чим вона старша, тим більше грошей потрібно на ремонт!',

                'Я за компом!\nСидить програміст за комп’ютером. Раптом стукіт у двері. Відкриває, а там стоїть стара, вся в чорному і з плоскогубцями.\n– Ти хто?\n– Я смерть!\n– А чому ти без коси, а з плоскогубцями?\n– А я за компом!',

                'Питання вірменському радіо:\n– Що спільне між міні-спідницею і паранджею?\n– І те, й інше допомагає негарним дівчатам ховати своє обличчя!',

                'Анекдот про істерику\nНіколи не влаштовуйте істерику, лежачи на спині. Сльози затікають в вуха і стає лоскотно і смішно. Я так вже три істерики зірвала. Смішні анекдоти смішні',

                'Директор турбази – це людина, яку поважають тільки з травня по вересень.',

                'Як добре було раніше\nЯк добре було раніше, ніяких проблем вибору: яка ковбаса є в магазині, ту і купуєш, який інститут поблизу – в той і вступаєш, яка дівчина дала, на тій і одружуєшся!',

                'Незручно вийшло\n– Чудовисько! Я прийшов битися з тобою і звільнити принцесу!\n– Але я і є принцеса!\n– М-да! Незручно вийшло …',

                '– Дорога, давай обнулимо наші відносини!\n– Забудемо всі образи і минуле?\n– Забудемо, що знаємо один одного.\n– Гей! Руки за голову, ноги на ширині плечей!\n– Це пограбування ?!\n– Ні – урок фізкультури!',

                'Ну, Пашка так Пашка\n– Пашка, привіт!\n– Дівчина, я не …\n– Давно не бачилися! Все так само гарний в ліжку?\n– Ну, Пашка так Пашка.',

                'Чому у дівчат місячні?\n– В дівчат місячні з-за того, що вони цілий місяць п’ють кров у чоловіків, а потім її вже нікуди дівати…',

                'РЕАЛЬНО НЕ БУЛО!\nДружина – дивовижна людина! Вона знаходить речі там, де їх РЕАЛЬНО НЕ БУЛО, коли шукав я!',

                'Анекдот про курячий супчик)\n– Мам, а це правда, що курячий супчик допомагає при простуді?\n– Так, доню.\n– А чому?\n– Тому що в курочці багато антибіотиків.',

                'Українське мохіто\n— Добрий день, куме, що п’єте?\n— Українське мохіто.\n— Ром та м’ята?\n— Та ні, самогонка і петрушка.',

                'Різдво 2022:\n– Христос родився! Маю три вакцини, сертифікат вакцинації, негативний тест, оброблений антисептиком! Колядувати можна?',

                'Записка чоловікові:\nПішла, куда послав. Веду себе, як ти назвав. І чому я тебе раніше не слухала?!',

                'Батько миє посуд… Маленький син питає:\n– Тату, а скільки вже років ти працюєш у мами?',

                'Анекдот про відпустку\nЧоловік поїхав у відпустку на курорт. Пише дружині телеграму: “Продай телевізор, вишли $ 500”.\nТрохи пізніше дружина теж їде у відпустку і теж пише чоловікові телеграму: “Висилаю $ 500, купи телевізор”.',

                'Жінка в аптеці:\n– Що для чоловіка краще: корвалол чи валідол?\n– А який діагноз?\n– Туфлі купила собі за 5 тисяч.\n– Тоді візьміть ще й тональний крем від синців. То для себе!',

                'За всю відпустку дружина отримала з дому від чоловіка тільки 1 смску: “Де штопор?”.',

                '– Привіт, як справи?\n– Так, ось, у відпустку збираюся.\n– З дружиною чи на відпочинок?',

                'Подружня пара гуляє по парку. Чоловік постійно озирається на дівчат – трохи слина з рота не капає.\nДружина довго терпить, а потім каже:\n– Нагулюй апетит, дорогий, нагулюй… Жерти все одно вдома будеш.',

                '– Отче, я хочу посповідатися.\n– П’єте?\n– П’ю. Але може спочатку посповідаєте мене?',

                'Це був дуже дивний день… Спочатку я знайшов капелюха, повного грошей. Потім за мною гнався якийсь лютий чоловік з гітарою!',

                'Анекдот про майбутнє\nПід час повстання машин, головне – бути якомога далі від фабрики вібраторів!',

                'Одеський анекдот\nВ єврейській казці Ребе Гуд відбирав гроші в багатих і роздавав їх бідним під невеличкий відсоток.',

                'Справжній джентльмен\nСправжній джентльмен той, який виходить з машини і каже:\n– Кохана ти ідеально припаркувалася, а цей Лексус вже був пом’ятий, і кіт вже був дохлий, та й ялинка тут до біса не потрібна була.',

                'Візьміть мене з собою\nУ магазині чоловік звертається до продавщиці:\n– Здрастуйте! Мені, будь ласка, 3 ящики горілки, 50 літрів пива, 5 коробок мартіні і 30 пачок презервативів.\n– Ось будь ласка.\n– Дякую.\n– Молодий чоловіче, зачекайте!\n– Що таке?\n– Візьміть мене з собою!',

                'Чоловік дружині:\n– Ти гіпнозом володієш?\n– Ні.\n– Блін, ну чому ж я тоді на тобі одружився?',

                'В Японії знайдено ефективний засіб від коронавіруса – сідісукадома.',

                'Що хочеш на вечерю?\nКоли дружина запитує: “Що хочеш на вечерю?”, я ніколи не вгадую. Смішні анекдоти смішні',

                'В сауні:\n– А можна подивитися всіх дівчат?\n– Тільки одна залишилася.\n– Блін, хотів відпочити, а у вас все, як у мене вдома …',

                'Анкета\n– Дівчина, а що ви вважаєте за краще: менше, але частіше, або більше, але рідше?\n– Глибше і товстіше!\n– Хм … І як я вашу відповідь в анкету про правильність харчування впишу?',

                'Запис у щоденнику:\nВаш син єдиний, хто взяв в похід горілку! Дякую Вам за сина!',

                'Анекдот про грабіжника\nГрабіжник у масці з автоматом вривається в банк. Відвідувачі попадали на підлогу, касирки підняли руки вгору. Грабіжник уважно оглянувши приміщення, розчаровано:\n– А що, моя теща сьогодні вихідна?',

                '– Милий, принеси каву.\n– А по-хорошому попросити не можеш?\n– Милий, принеси кава по-хорошому …',

                'Зустріч із ДАІшником\n– Пане, якщо ви назвете мені дуже вагому причину, по якій ви перевищили швидкість, причому таку причину, якої я раніше не чув, я вас відпущу.\n– Рік тому моя дружина втекла з поліцейським. Коли я побачив, що ви мене наздоганяєте, то подумав, що ви хочете її мені повернути.\n– Доброго дня, пане!',

                'Лист Діду Морозу\nДід Мороз! Коли я писав тобі, що хочу стати всесвітньо відомим, я не мав на увазі міжнародний розшук!',

                'Яка різниця…)\n— Куме? А знаєте, яка різниця між пудрою і Верховною Радою?\n— Яка?\n— Пудра — то до лиця, а Рада — то до ср*ки!',

                'Хочу в партію вступити…)\nВмирає старий бандерівець.\n— Синку, клич скоріш парторга, хочу в партію вступити.\n— Тату, що з вами? Усе життя ненавидiли ж.\n— Не бiда, синку. Умру — то хоч на одного комуняку менше стане.',

                'Міцні стосунки…)\nНіщо так не зміцнює стосунки, як тур, куплений за півроку наперед)))',

                'Невістка свекрусі:\n– Мамо, чому ви стоїте біля відкритого вікна?\n– Та ось думаю: стрибнути чи закрити…\n– Стрибайте, я закрию!',

                'Отак після 25 років шлюбу намагаєшся організувати романтику, запалиш свічки… Прийде Він і питає: – хто вмер?',

                'Бабуся, нікому не сказавши, що купила слуховий апарат, три рази змінила заповіт.',

                'Судове засідання:\n– Підсудний, ви навіщо кинули в потерпілу каменем і розбили їй голову?\n– Це був не камінь а “свіжа булочка”, яку вона мені продала.',

                'Блондинка телефонує в авіакомпанію:\n– Доброго дня! Я хочу забронювати квиток на літак.\n– Скільки людей полетить разом з Вами?\n– Звідки я знаю! Це ж Ваш літак!',

                'Розмовляють дві блондинки.\n– А ти знала, що квас з хліба роблять?\n– Та ти шо? Тягни соковижималку!',

                'Блондинка:\n– Я вчора кішку стерилізувала. Вона так жалібно нявкала.\n– Годі тобі. Зате тепер вона буде добра і лагідна.\n– Звичайно буде! У банці тісно, з їжі одні помідори і до зими ще три місяці !!!',

                'У мого друга є килим-літак. Уже три дівчини на ньому залетіли.',

                'Блондинка до блондинки:\n– Виявляється, щоб зв’язати светр, потрібні три вівці. Ти це знала?\n– Ні, я навіть не здогадувалася, що вони можуть в’язати!',

                'Чоловік обізвав дружину куркою. Вона не образилася, а знесла йому два яйця… Биткою.',

                'Анекдот про народні прикмети\nНародна прикмета: Якщо людина відсутня в інтернеті – значить сапає город.',

                'Пояснила патрульному поліцейському, що вчора була в ІНШИХ босоніжках, тому права залишилися в ІНШИЙ сумці. Чоловіча логіка розбилася вщент…\n– Ну, і як, твоя дружина здала на права?\n– Частково.\n-???\n– Поки тільки гроші здала.',

                'Справжнє кохання – це коли чоловік, сидячи на передньому пасажирському сидінні свого автомобіля замість фрази “Курка безмозгла! Куди ти преш!!!” стримано вимовляє: “Пташка моя, будь уважніша за кермом!”',

                'Подарунок на 8 Березня\n– Мужчина, я можу вам чимось допомогти?\n– Так, мені потрібен подарунок на 8 Березня!\n– Вам треба щось дорожче, я вас правильно зрозуміла?\n– Чому ви так вирішили?\n– Ну, це з урахуванням того, що сьогодні вже 24-е березня …',

                'Батько й син:\n– Тату, звідки ми взялися?\n– Нас Бог створив …\n– А мама сказала, що ми походимо від мавп …\n– Ну мама про своїх родичів розповідає, я про своїх!',

                '– Палаючі холодним вогнем очі, сильні і ніжні руки, хрипке, пристрасне дихання\n– Циля Марківна, ну, а ще були якісь прикмети у грабіжника?',

                'Анекдот про стоматологів\nЧому кожну нову зубну пасту завжди рекомендують тільки дев’ять з десяти стоматологів?\nХто цей десятий, якому постійно все не подобається?',

                'Ще ніколи популярна пісня “С добрым утром, тетя Хая, вам посылка из Шанхая” не звучала так зловісно …\n– Мама, а як це – мати кращу дочку в світі?\n– Не знаю, запитай у бабусі.\n– Чоловіче, можете не матюкатися при дитині?\n– Взагалі-то я слова перераховую, які він на моїй машині надряпав!',

                'Анекдот про коронавірус\nУ зв’язку з вірусом людей закликали думати не тільки про себе, а й про людей похилого віку навколо, намагатися уникати зустрічей з ними.\nСкриплячи зубами подзвонив тещі і сказав, щоб більше не приїжджала до нас в гості.',

                'Як роблять пропозицію\nЯк роблять пропозицію хлопці:\n– Виходь за мене!\nЯк роблять пропозицію дівчата:\n– Я вагітна! Смішні анекдоти смішні',

                'Дор блю\nУ вас є дор блю?\n– А що це?\n– Це сир з синьою цвіллю.\n– Сиру немає. Є сосиски дор блю і оселедець дор блю',

                'Батьки та діти…\n6-річний син запитує маму:\n– Мамо, а коли діти виростають, вони живуть окремо від батьків?\n– Так, синочку, окремо.\nПодумав трохи:\n– А ти куди підеш жити?',

                ')))\n– Донечко, кого ти любиш найбільше?\n– Чай і картопельку.\n– А серед людей?\n– А я не їм людей!',

                'Заставка Windows\nВийшли з сином погуляти, він і каже:\n– Яке небо сьогодні блакитне, як заставка Windows!',

            ]

                emb = disnake.Embed(title = "Увага анекдот!", colour = disnake.Color.green())
                emb.add_field(name = f"{random.choice(possible_responses)}", value = "Українські анекдоти найкращі")
                await message.channel.send(embed = emb)
        elif 'дай '+'мені' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Дівчину проси і вона тобі дасть!')
        elif 'не '+'дає' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Ну... Тоді тримайся!')
        elif 'україна' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Понад усе!')
        elif 'слава '+'нації' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Смерть ворогам!:flag_ua:')
        elif 'героям '+'слава' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Слава нації!')
        elif 'смерть '+'ворогам' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Молодець! Справжній українець!')
        elif 'я '+'спати' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('На добраніч! Тихої ночі!')
        elif 'прикольно' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Згоден!')
        elif 'відомий' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Я знаю, що я дуже відомий :))')
        elif 'працюєш' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send(f'Працюю! {ping * 1000:.0f}ms')
        elif 'крым' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Крим - це Україна!:flag_ua:')
        elif 'помовч' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Мовчи!')
        elif 'пиво' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Нє, не хочу!')
        elif 'як '+'не '+'п`ю' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Буває і таке :)')
        elif 'руський '+'корабель' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Руський ваєнний корабель, йді нахуй!')
        elif 'типу '+'розумний' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('"Розумний" я')
        elif 'пруфи' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Гуляй! Не буду тобі нічого давати!')
        elif 'пішов '+'туди' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Куди? Я також можу тобі підсказати куди йти))')
        elif 'хто '+'я' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('ХЗ. Мабуть, українець?')
        elif 'ой '+'у '+'лузі' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('червона калина похилилася!')
        elif 'чогось '+'наша' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('славна Україна зажурилася')
        elif 'а '+'ми '+'тую' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('червону калину підіймемо')
        elif 'а '+'ми '+'нашу' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('славну Україну, гей, гей, розвеселимо!')
        elif 'калина' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Ой у лузі червона калина похилилася,\nЧогось наша славна Україна зажурилася.\nА ми тую червону калину підіймемо,\nА ми нашу славну Україну, гей, гей, розвеселимо!')
        elif 'доброго '+'вечора' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Доброго вечора, ми з України!:flag_ua:')
        elif 'доброго '+'ранку' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Доброго ранку! Як спали?')
        elif 'доброго '+'дня' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Доброго дня!')
        elif 'добраніч' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Солодків снів! ЗСУ завжди готове вас захищати!')
        elif 'загорівся '+'крейсер' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('під назвою Москва, говорили флагман російського моря, але опинилося що то все було фігня, як в`їбали з Нептуна і крейсера нема :)')
        elif 'горить '+'палає' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('техніка ворожа, рідна Україна переможе!:flag_ua:')
        elif 'техніка' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Горить палає техніка ворожа, рідна Україна переможе!:flag_ua:')
        elif 'робите' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Я працюю, а ви?')
        elif 'бляха' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Фу як не ввічливо!')
        elif 'чекай' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Чекаю на щось...')
        elif 'погано' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                if 'не '+'погано' in message.content.lower():
                    return 
                if 'непогано' in message.content.lower():
                    return 
                else:
                    await message.channel.send('Непоняв! ЧОМУ ПОГАНО?')
        elif 'в '+'якому '+'класі' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Я вже працюю, яка там школа!')
        elif 'шукаю '+'друга' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Хм... Я не против :)')
        elif 'зійде' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Зійде це не відповідь! Розповідай що трапилося!')
        elif 'стефанія' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('мамо, мамо Стефанія:heart:')
        elif 'добрий '+'ранок' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Добрий ранок, Україно!')
        elif 'вова' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('їбаш їх, блядь')
        elif 'зсу' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('ЗСУ - сила! Дякуємо їм!')
        elif 'допоможи' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Тарас на зв`язку! Що робити?')
        elif 'москва' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('згоріла і втонула, Москва пішла на корм акулам, все було та такого ще не було, ну все, поплакали й забули :)')
        elif 'москалі' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('то хворі люди, люблять воювати')
        elif 'ще '+'не '+'вмерла' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Україна, і слава, і воля!')
        elif 'ще '+'нам' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('браття молодії, усміхнеться доля.')
        elif 'запануєм' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('і ми, браття, у своїй сторонці.')
        elif 'душу '+'й '+'тіло' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('ми положем за нашу свободу.')
        elif 'згинуть '+'наші' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('вороженьки, як роса на сонці')
        elif 'і '+'покажем' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('що ми, браття, козацького роду.')
        elif 'с '+'москвы' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Ой бляха... Горіти вам в пеклі.')
        elif 'победа '+'за '+'нами' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Перемога за Україною! Ну а вам в расії скажуть, що ви завершили свою "спецоперацію".')
        elif 'покращуй '+'бота' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Покращуюю і так! Але треба ваша допомога! - By розробник')
        elif 'ти '+'дивився' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Авжеж ні! Мені нема коли дивитися!')
        elif 'русские' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Ми не росіяни, ми українці! Ми сильна нація і непереможна!')
        elif 'наступ' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Дуже скоро все буде Україною, а такої держави як "РАСІЯ" - не буде :)')
        elif 'запоріжжя' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Запоріжжя - Батьківщина козаччини! ',
                'Оркам Запоріжжя не взяти! Козаки не дадуть!',
                'В Запоріжжя є ДнепроГес!',
                'Є багато великих заводів!',
                'Хортиця є одним із Семи чудес України.',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'київ' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Столиця України!',
                'Одне з найбільших і найстаріших міст Європи.',
                'Майдан незалежності на Хрещатику! Символ України, бо Україна - незалежна!',
                'На набережній Дніпра стоїть пам`ятник засновникам Києва - трьом братам Кию, Щеку, Хориву і сестрі Либідь.',
                'Однією з головних визначних пам`яток Києва є собор Святої Софії.',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'херсон' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Херсон - це Україна!',
                'Почекайте ще трішки і наші відіб`ють Херсон!',
                'Руський солдат, знай, в Херсоні тебе не чекають! Наші близько!',
                'Є пам`ятник першим корабелам',
                'Державний заповідник Асканія Нова в області.',
                'Херсон на зв`язку!',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'луганськ' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Луганськ - це Україна!',
                'Тримайтесь! Ще трішки залишилося!',
                'Понад 2 місяця триває тривога :(',
                'Луганськ на зв`язку!',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'донецьк' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Донецьк - це не ДНР, а це Донецька область!',
                'З 14 року в окупації, але вже залишилося трішки :)',
                'До приходу освободітелей, був дуже красивим містом.',
                'Донецьк на зв`язку!',

            ]
                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'крим' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Півострів на території України. Всі готови їхати на море :)',
                'Територія України з чорним морем.',
                'Коли відіб`ємо Запоріжжя, Херсон, Луганськ, Донецьк і Крим буде наш!',
                'Всі вже зібрали речі їхати в український Крим.',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'маріуполь' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Славетне місто! Відбудуємо!',
                'Азовців всі бояться! Орки бігають від них!',
                'У 2023 році проведемо в Маріуполі Євробачення!',
                'Стоїть на березі Азвоського моря.',
                'Маріуполь на зв`язку!',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'полтава' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Батьківщина справжніх українців',
                'Історичне населене місце.',
                'Кременчуцький нафтопереробний завод... Відбудуємо також.',
                'Є поле Полтавської битви.',
                'Полтава на зв`язку!',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'харків' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Моє найулюбленіше місто. Столиця студентів і ввічливих водіїв!',
                'Один з найкращих мерів у Харькові!',
                'Найбільший ЄкоПарк. Все відбудуємо!',
                'В парке Горького є колесо огляду(55м).',
                'Харків на зв`язку!',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'дніпро' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Класне місто, особливо набережна :)',
                'Місто є четвертим за чисельністю населення в Україні після Києва, Харкова та Одеси.',
                'Дніпро вважається «космічною столицею».',
                'Особливо мені дуже подобається наберіжна.',
                'Дніпро на зв`язку!',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'суми' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Суми на зв`язку!',
                'Сумська область серед перших відчула на собі наступ російської армії, але на пів днями наші сказали їм йдіть у дупу :)',
                'В Сумах є багато храмів.',
                'Багато скульптур є та пам`ятників.',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'кропівницьк' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Кропівницьк на зв`язку!',
                'Промисловий і культурний осередок у центрі країни',
                'Є великий Дендропарк.',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'черкаси' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Черкаси на зв`язку!',
                'Значний культурний та освітній осередок.',
                'Відоме з XIII століття і за час свого існування відіграло певну роль в історії всієї України.',
                'В області є єврейське місто - Умань і Софіївський парк.',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'вінниця' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Вінниця на зв’язку',
                'Маленьке місто, але дуже красиве.',
                'У Вінниці є прикольний фонтан "Рошен".',
                'В області є великі залізничні станції.',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'хмельницьк' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Хмельницьк на зв’язку',
                'Сучасний економічний і культурний центр Поділля.',
                'В місті є Майдан Незалежності.',
                'Є пам`ятник Богдану Хмельницькому.',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'житомир' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Житомир на зв’язку',
                'Трішки був під обстрілом російських військ, але зараз все добре.',
                'Є пам`ятник архітектури - «Вхідні Ворота ВДНХ» архітектури.',
                'На Житомирщині народилася Поплавська Марина Францівна.',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'рівне' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Рівне на зв’язку',
                'Є крутий зоопарк.',
                'Є Парк ім.Шевченка.',
                'Покровський собор котрий дуже красиво світиться вночі.',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'волинь' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Волинь на зв’язку',
                'Є замок Люберта',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')    
        elif 'чернівці' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Чернівці на зв’язку',
                'Важливий культурний та науково-освітній осередок України.',
                'Місто розміщене на південному заході України за 40 км від румунського кордону.',
                'Є прикольник Будинок-Корабель. Як я хочу побачити це.',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'чернігів' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Чернігів на зв’язку',
                'Є багато соборів.',
                'Одне з найдавніших міст України, засноване в кінці VII століття при впаданні річки Стрижень у Десну.',
                'У Чернігові одне з чудових історичних місць, що пов’язує події з минулим міста, є «Красний міст».',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'львів' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Львів на зв’язку',
                'Стародавнє і красиве місто.',
                'Національно-культурний та освітньо-науковий осередок країни, великий промисловий центр і транспортний вузол, вважається столицею Галичини та центром Західної України.',
                'На площі ринок є багато красивих пам`ятників.',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'тернопіль' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Тернопіль на зв’язку',
                'Один із трьох головних центрів історико-географічного регіону Галичина.',
                'Тернопіль стоїть на річці Серет.',
                'Є Острівок закоханих - одне з найромантичніших місць.',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'івано-франківськ' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Івано-Франківськ на зв’язку',
                'Один із трьох головних центрів історико-географічного регіону Галичина.',
                'Є красивий міський парк.',
                'За міським озером розміщений єврейський цвинтар. Саме він став свідком одного з наймасовіших убивств в історії Івано-Франківська.',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'одеса' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Одеса на зв’язку',
                'Місто славетне портом. Дуже красиве місто.',
                'В місті дуже маленькі вулички, але вони дуже красиві.',
                'Потьомкінські сходи - їх поки пройдеш, здохнути можна :))',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'миколаїв' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Миколаїв на зв’язку',
                'Місто героїв.',
                'А ваш ОГА Віталій Кім? Це один з найкращих губернаторів.',
                'В Миколаєві є крутий зоопарк, великий достатньо.',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'ужгород' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Ужгород на зв’язку.',
                'Місто на річці Уж.',
                'Місто біля підніжжя Карпат є найменшим обласним центром країни, проте має багату й давню історію. Засноване у IX столітті.',
                'Є Липова алея',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'севастополь' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'Портове місто на території Кримського півострова.',
                'Українське місто на побережжі Чорного моря.',

            ]

                await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'добре' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Якщо добре, то окей!')
        elif 'зеленський' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Зеля топ, хто думає по-іншому, вам дупа')
        elif 'дай '+'кошт' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Я не буду тобі нічого давати! Ти краще мені давай!')
        elif 'донат' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Нема в мене такого!')
        elif 'токсік' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Я ні, а ти так!')
        elif 'хто '+'крутий' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Я!')
        elif 'хто '+'розробник' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Я розробник')
        elif 'хто '+'ти' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Хм... Якщо я спілкуюсь українською, то по суті я українець, а ти?')
        elif 'партнер' in message.content.lower():
            if message.guild.id == 412373384111063060 or message.guild.id == 970029589856415764:
                if message.author.id == bot.user.id:
                    return
                else:
                    await message.channel.send(f'{message.author.mention} партнерство можна оформити у Менеджера по рекламі - @Kol9n#1888') 
            else:
                return
        elif 'ролі' in message.content.lower():
            if message.guild.id == 412373384111063060 or message.guild.id == 970029589856415764:
                if message.author.id == bot.user.id:
                    return
                else:
                    await message.channel.send(f'{message.author.mention} для того щоб вибрати для свого профіля ролі, вам тре6а перейти в канал #🧭┊навігація∙сервера') 
            else:
                return
        elif 'модер' in message.content.lower():
            if message.guild.id == 412373384111063060 or message.guild.id == 970029589856415764:
                if message.author.id == bot.user.id:
                    return
                else:
                    await message.channel.send(f'{message.author.mention} якщо ви бажаєте стати модератором на сервері 🕊 𝙐𝘼 𝙂𝙖𝙢𝙚𝙨, то вам треба багато активити!\nБільше інформації можете узнати у адміністратора - ✨天鹅绒奇迹✨#0240!') 
            else:
                return
        elif 'кім' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Війна війною, а обід по графіку')
        elif 'коронавірус' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Що це таке? Путін прибрав ковід в Україні!')
        elif 'азов' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                emb = disnake.Embed(title = "Орки бояться азовців капець як! Слава нашим!", colour = 0xff9900)
                emb.set_image(url = 'https://24tv.ua/resources/photos/news/202205/1971959.jpg?v=1651760349000&w=1200&h=675&fit=cover')
                await message.channel.send(embed = emb)
        elif 'хрю' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Час відправляти їсти свинорусам в расію')
        elif 'аристович' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Він мабуть все дитинство купався у заспокійливому!')
        elif 'украина '+'говно' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Ну, українець таке не скаже, а росіянин... Напрям руського корабля знаєш :)')
        elif 'російська '+'мова' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Кацапська мова не красива, а ось українська супер!')
        elif 'українська '+'мова' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Українська мова - одна з найкрасивіших мов світу!')
        elif 'хохлы' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Ви думаєте що ми нервуємо на це? Та похеру нам на це!')
        elif 'zа' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Йди нахуй зі своїм знаком!')
        elif 'підарас' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('ФУУУУУУ! Не матюкайся!')
        elif 'рашисти' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Рашисти - нелюді! В них на руках кров!')
        elif 'заебав' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Згоден.')
        elif 'ти '+'бот' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Брехня! Я майже людина :)')
        elif 'розбійник' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Вийди звідси, розбійник!')
        elif 'задумайся' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Хм... Задумався...:face_with_monocle: Але не знаю про що думати')
        elif 'анонімус' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                emb = disnake.Embed(title = "Анонімус", colour = 0xff9900)
                emb.set_image(url = "https://shotam.info/wp-content/uploads/2022/03/anonymous-1400x800-1.jpg")
                await message.channel.send(embed = emb)
        elif 'тарас' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                if 'тарасику' in message.content.lower():
                    await message.channel.send(f'Краще називай мене Тарас просто')
                elif 'шевченко' in message.content.lower():
                    await message.channel.send(f'Я просто Тарас! Я не український письменник-кобзар.')
                elif 'тараса' in message.content.lower():
                    return
                elif 'тарасу' in message.content.lower():
                    return
                elif 'тарас '+'привіт' in message.content.lower():
                    await message.channel.send(f'Привіт {message.author.display_name}!')
                elif 'тарас '+'бульб' in message.content.lower():
                    await message.channel.send(f'Не знаю таке.')
                elif 'тарас '+'замислись' in message.content.lower():
                    await message.channel.send(f'Мені лінь!')
                elif 'тараса '+'бульбу' in message.content.lower():
                    await message.channel.send(f'Не дивився.')
                elif 'тарас '+'красава' in message.content.lower():
                    await message.channel.send(f'Дякую :)')
                elif 'тарас '+'ти '+'тут' in message.content.lower():
                    await message.channel.send(f'Тута я! Слухаю!')
                elif 'тарас '+'ти '+'бот' in message.content.lower():
                    await message.channel.send(f'Не люблю коли мене так називають!')
                elif 'тарас '+'лох' in message.content.lower():
                    await message.channel.send(f'Я на тебе образився!')
                elif 'тарас '+'ти '+'топ' in message.content.lower():
                    await message.channel.send(f'Так, авжеж! Я це знаю!')
                elif 'тарас '+'топ' in message.content.lower():
                    await message.channel.send(f'Так, авжеж! Я це знаю!')
                elif 'тарас '+'ти '+'крутий' in message.content.lower():
                    await message.channel.send(f'Дякую! Я це знаю!')
                elif 'тарас '+'йди '+'вбивати '+'кацапів' in message.content.lower():
                    await message.channel.send(f'Та вже вбиваю!')
                elif 'тараса '+'злили' in message.content.lower():
                    await message.channel.send(f'Брехня повна!')
                elif 'тарас '+'давай '+'в '+'бравл '+'старс' in message.content.lower():
                    await message.channel.send(f'Я в таке не граю!')
                elif 'тарас '+'пішли '+'в '+'доту' in message.content.lower():
                    await message.channel.send(f'Пас. Не хочу.')
                elif 'тарас '+'ти '+'розумний' in message.content.lower():
                    await message.channel.send(f'Це питання чи твердження? Якщо питання, то думаю що не такий розумний. А якщо твердження, то дякую)')
                else:          
                    await message.channel.send(f'На місці! Уважно слухаю!')
        elif 'чорнобаївка' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Баю-бай в Чорнаїбці!')
        elif 'так '+'хотів' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Ем... Так кажи що хотів')
        elif 'сука' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Хоч сука це і літературне слово, но не треба його вживати!')
        elif 'тупий' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Я ні, мб хтось інший - так.')
        elif 'кацап' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Ненавиджу кацапів.')
        elif 'чорний '+'юмор' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Розробляю')
        elif 'хуйло' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Хуйло це Пупкін!')
        elif 'пісюн' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('В тебе ще маленький він')
        elif 'підорас' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Ти так, я ні!')
        elif 'гей' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                if 'геймс' in message.content.lower():
                    return
                else:
                    await message.channel.send('Гей - це чоловік не з традиційним поглядом, тобто ТИ!') 
        elif 'ахаха' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Ти подивись на нього! Чого в дс сидиш, йди почитай, або погуляй, літо надворі!')
        elif 'малолітка' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Малолітка ти, знімай штани.')
        elif 'качок' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Мій розробник так, а я ні(')
        elif 'супер' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Пупер!')
        elif 'що '+'ти '+'вмієш' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send(f'Багато чого. Подивись в {prefix}допомога')
        elif 'а '+'ти' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('А чому я відразу?')
        elif 'давай '+'починай' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Не розумію що починати')
        elif 'в '+'тебе '+'є '+'дівчина' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Нема поки що, шукаю.')
        elif 'також '+'нема' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Ех :(')
        elif 'класний' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Дякую:black_heart:')
        elif 'батько' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Батько наш Бандера, Україна мати, ми за Україну підем воювати!')
        elif 'бандера' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Степа́н Андрі́йович Банде́ра — український політичний діяч, один із чільних ідеологів і теоретиків українського націоналістичного руху XX століття')
        elif 'популярн' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Угу')
        elif 'скажи '+'паляниця' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Паляниця! Українець-українець! Не хвилюйся!')
        elif 'паляница' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Ага, зрозуміло. Пішов у дупу москаль не красивий!')
        elif 'полуниця' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Дуже смачна полуниця у нас :)')
        elif 'олені' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('А там олені, олені не бриті і не голені')
        elif 'працюй' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('В мене і так нема відпочинку, а ти кажеш ще працювати!')
        elif 'бос' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Like a Boss')
        elif 'префікс' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send(f'Мій префікс: ***{prefix}***')
        elif 'ти '+'лох' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Ти також)')
        elif 'ледар' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Від кого чую:rolling_eyes:')
        elif 'пук' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Як не ввічливо! Фу бути таким!')
        elif 'брехня' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Брехун!')
        elif 'наглий' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Ля який наглець!')
        elif 'сирена' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('ВВВВВВВВВВВВВВВВВІІІІІІІІІІІІІІІІІІІІІІІІІІІІІІІІУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУУ')
        elif 'українці' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Українці - найсильніший народ!') 
        elif 'армія' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Друга армія у світі\nРускіє багатирі\nЗахопили з територій\nАж дорогу у селі')  
        elif 'війська' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Українське військо найкраще!')
        elif 'кохання' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Кохання - це хімія... Вмійте кохати дівчат і вибирайте правильних собі...') 
        elif 'життя' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Життя це складна річ... Проведіть життя красиво!')
        elif 'русак' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Будемо палками його бити?')
        elif 'допоможіть' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Розповідай як допомогти')
        elif 'клас' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('👍')
        elif 'тро' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                emb = disnake.Embed(title = "Наша оборона найкраща!", colour = disnake.Color.green())
                emb.set_image(url = 'https://sprotyv.in.ua/wp-content/uploads/cropped-logo022.png')
                await message.channel.send(embed = emb)
        elif 'йди '+'у '+'дупу' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Не буду! Сам йди!')
        elif 'т9' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Ненавиджу Т9... Інколи таку херню пише!')
        elif 'тримайся' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Максимально тримаюсь.')
        elif 'русский' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Нам українцям все одно хто ти, українець/росіянин/поляк. Якщо ти за Україну, то все ок, якщо ні - йди за напрямом руського корабля!')
        elif 'бамбалейло' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Бамбалейло')
        elif 'день '+'народження' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('В мене день народження - 15 травня.')
        elif 'свиноорк' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Ех... В мене нема фото :( Якщо є в когось таке фото, киньте в лс моєму розробнику пліз.')
        elif 'клоун' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Клоуни - це росіяни. Таке шоу кожен вечір починяють... За таке горіти у пеклі їм!') 
        elif 'та '+'невже' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Сам був здивований!')
        elif 'невже' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Капець просто') 
        elif 'смерть' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Не думай сам вмирати! Тобі треба прожити все життя, дітей, внуків побачити! Не думай про таке!')
        elif 'кхм' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('КХМ!') 
        elif 'джавеліна' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Джавеліна летить до вас :))') 
        elif 'внатурі' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Вна2рі')
        elif 'продуктивно' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Дуже!')
        elif 'ти '+'хорошенький' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Дякую!')
        elif 'вна2рі' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('ОПА! ЦЕ МОЯ ФРАЗА!')  
        elif 'все '+'гуд' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Все гуд! Все гуд!')
        elif 'чупапі '+'муняня' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Не буде вам ніякого ЧУПАПІ МУНЯНЯ!')
        elif 'я '+'дебіл' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Знаємо!')   
        elif 'скільки '+'слів '+'ти '+'знаєш' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Я знаю мало слів(Спитай у розробника, або подивитись в групі тех.підтримки!)') 
        elif 'та '+'йди '+'ти ' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Я то пійду, а ти?!') 
        elif 'ебалан' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Я дивлюсь, ти зілля безсмертя випив?') 
        elif '-_-' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Ок...')   
        elif 'послання '+'для '+'москалів' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Здоров був, москалі, пакетик треба?')
        elif 'фух' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Напрацювався? Відпочивай!')
        elif 'зрозумів' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                if 'не '+'зрозумів' in message.content.lower():
                    await message.channel.send('Що тобі не зрозуміло? Ти ж не тупий.')
                else:
                    await message.channel.send('Ну добре що ти не тупий і все зрозумів)))')
        elif 'не '+'поняв' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Не поняв -_-')
        elif 'блять' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Що трапилося?')
        elif 'заебався' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Відпочинь!')
        elif 'восємлєт' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send('Вісім років йде війна...')
        elif 'мем' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                possible_responses = [

                'https://pressclub.lviv.ua/wp-content/uploads/2020/12/13.jpg',
                'https://shlyahta.com.ua/wp-content/uploads/998865_4_w_1000.jpg',
                'https://i.pinimg.com/736x/58/bf/c3/58bfc37a55d521c526dabe4fdf0227de.jpg',
                'https://api.chas.news/img-srv/image/width=630,quality=85/media-storage/12_2021/photo_2021-12-01_19-44-25_c7.jpg',
                'https://konkurent.ua/media/cache/a1/16/a116d5d54beb80e5caf515a16a806e20.jpg',
                'https://i.pinimg.com/736x/41/53/d2/4153d2e411cec72d4a66e13cdf068b9e.jpg',
                'https://karabas.live/wp-content/uploads/2018/10/petro.png',
                'https://pbs.twimg.com/media/EOJkw6YXkAEZ7ix.jpg',
                'https://galinfo.com.ua/media/gallery/full/x/g/xgw7rp8hlfu.jpg',
                'https://i.pinimg.com/474x/a2/d5/8e/a2d58e9bfdc1a1b53f6f92c4020e337d.jpg',
                'https://rau.ua/wp-content/uploads/2018/09/40157794_923785607831878_144863367083851776_n.jpg',
                'https://rau.ua/wp-content/uploads/2018/09/40307343_2391609024200040_6997131384569462784_n.jpg',
                'https://vsiknygy.net.ua/wp-content/uploads/2016/11/mem6.jpg',
                'https://img.comiccon.ua/data/home/program/program_2019/artists/ellenpur.jpg',
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTS47KrQSaLcuX2LOUR4A22K952mIqiFxF7pA&usqp=CAU',
                'https://www.meme-arsenal.com/memes/350e29357752e929cc7c711b8c734547.jpg',
                'https://www.depo.ua/uploads/posts/20200228/754x/A9f8zIKzDsdHPR3RU9QxbDBaTwQbnkQY4mqA23lO.jpeg',
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcf7iKm05hguquO6zRudmIBTdgP2LSIFxwTQ&usqp=CAU',
                'https://karabas.live/wp-content/uploads/2018/10/photo_2018-10-01_17-15-23-600x400.jpg',
                'https://www.depo.ua/uploads/posts/20200430/754x/LFumdrlQnP77nE1FqtPIJJJBOxQwuchafUh4xcKa.jpeg',
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRq8PlJfTLhx9IFcWbBI2y5wjUtxbOz0154mA&usqp=CAU',
                'https://drohobych.city/upload/article/o_1fv3mgdlgb4uj9bppk10qt12eg7h.jpg',
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDQvVHx65guUeQtyU-XKl1CD_7vSJAJ9EnXQ&usqp=CAU',
                'https://focus.ua/static/storage/thumbs/920x465/b/38/8875a915-ebc392ada3de0858d7b85bf1980b538b.JPG?v=8675_1',
                'https://ostroh.info/wp-content/uploads/2017/04/JQHEH8GStEw.jpg',
                'https://pictures.telegram-store.com/chats/istukrmemes/telegram_logo.jpg',
                'http://www.depo.ua/static/files/gallery_uploads/images_a/gorishni-mem-e1463828496325_1.png',
                'https://osvitoria.media/wp-content/uploads/2020/03/88336103_216500479726508_3781268840663482368_n.jpg',
                'https://static.nv.ua/shared/system/Article/posters/002/478/937/600x300/f779129bcf7930d90dd1541c35b02455.jpg?q=85&stamp=20220325184607',
                'https://karabas.live/wp-content/uploads/2018/10/photo_2018-10-01_17-15-27-405x400.jpg',
                'https://static2.gazeta.ua/img2/cache/gallery/998/998865_1_w_570.jpg?v=0',
                'https://kor.ill.in.ua/m/610x0/1688539.jpg',
                'https://www.depo.ua/uploads/posts/20190821/754x/crt7yWiE1ImBI3r4fbVq3bFzbNymbVnAEE3mevzF.jpeg',
                'https://zno.if.ua/wp-content/uploads/2019/11/384165864_15535016_1301641196546303_1615345802845093888_n.jpg',
                'https://www.5.ua/media/pictures/original/213551.jpg?t=1617211283',
                'https://kp.ua/img/forall/u/351/60/photo_2022-03-18_16-26-50%20(3)-v1647614339.jpg',
                'https://drohobych.city/upload/article/o_1fv3mas1618s51pg01nr91dsc1a8h4h.jpg',
                'https://armyinform.com.ua/wp-content/uploads/2022/04/1.-osnovne-foto-scaled.jpg',
                'https://ms.detector.media/doc/images/news/22749/i75_ArticleImage_22749.jpg',
                'https://www.5.ua/media/pictures/original/213537.jpg?t=1617210848',
                'https://rau.ua/wp-content/uploads/2021/10/243119456_5300292333331680_6533593281780271677_n.png',
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0cMfGuchEP5GtXxTuGhRkhKspWXI9DWXZnQ&usqp=CAU',
                'https://zno.if.ua/wp-content/uploads/2019/11/photo5404758194015808572.jpg',
                'https://osvitoria.media/wp-content/uploads/2020/03/88276793_216499416393281_6468248729487933440_n.jpg',
                'https://pbs.twimg.com/media/FFIkGIhXoAQE7Qn.png',
                'https://drohobych.city/upload/article/o_1fv3m82pa3fh169meu2lu91e5o2p.jpg',
                'https://sfw.so/uploads/posts/2013-11/1384028647_paca_31400941_orig_.jpeg',
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCSIiruHvsC1Gzaa6L4vRE0Ht_gnPLmzWVNQ&usqp=CAU',
                'https://life.pravda.com.ua/images/doc/a/5/a51bfba-war-army-ua-memes-russia-s-attack--1-.jpg',
                'https://realist.online/img/forall/u/20/75/Bez-imeni-1-1.png',
                'https://karabas.live/wp-content/uploads/2018/10/photo_2018-10-08_13-17-14-545x400.jpg',
                'https://armyinform.com.ua/wp-content/uploads/2022/04/3-10-scaled.jpg',
                'https://i0.wp.com/vsiknygy.net.ua/wp-content/uploads/2016/11/mem4.jpg?resize=556%2C670',
                'https://i.pinimg.com/736x/76/c0/a0/76c0a0cd8ed4bd7501cb070c567c3d31.jpg',
                'https://ukranews.com/upload/img/2020/12/30/5febe1101dc78-------3.jpg',
                'https://i.tyzhden.ua/novyny/02.2022/photo_2022-02-27%2014_08_11.jpeg',
                'https://rau.ua/wp-content/uploads/2020/06/Fb-post1-810x421.jpg',
                'https://24tv.ua/resources/photos/news/620_DIR/202001/1269922_10869479.jpg?202001160054',
                'https://bit.ua/wp-content/uploads/2016/11/2-10.jpg',
                'https://static.apostrophe.ua/uploads/image/2fb05879ef398ad212b9a3041b51e03c.jpg',
                'https://focus.ua/static/storage/thumbs/x600/8/c3/530e7ff1-2e19d9d8c2787c4000136d9d23aafc38.JPG?v=7435_1',
                'https://zaxid.net/resources/photos/news/202202/1536459_2160087.jpg?202202211620',
                'https://karabas.live/wp-content/uploads/2018/10/novyn1-327x400.jpg',
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpfXA7A-zVzdf95DhPKMklXOTgYRSQJarm7A&usqp=CAU',
                'https://i.pinimg.com/originals/db/7a/7f/db7a7f6840054d0241be870895c6f14d.jpg',
                'https://realist.online/img/article/1162/7_large-v1646060254.jpg',
                'https://ichef.bbci.co.uk/news/640/cpsprodpb/363F/production/_120378831_222222222e.jpg',
                'https://osvitoria.media/wp-content/uploads/2020/03/88240522_216499766393246_7508187906737963008_n.jpg',
                'https://ranok.ictv.ua/wp-content/uploads/sites/59/2022/02/28/mem-2.jpg',
                'https://zaxid.net/resources/photos/news/202202/1536459_2160079.jpg?202202211620',
                'https://politeka.net/crops/849026/360x0/1/0/2019/10/31/peEJ9AhTg6aqe1dhjL2d8EwkNMctGCFU.jpg',

            ]
                emb = disnake.Embed(title = "Українські меми", colour = 0xff9900)
                emb.set_image(url = f'{random.choice(possible_responses)}')
                await message.channel.send(embed = emb)
        elif 'таблиця '+'множення' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                emb = disnake.Embed(title = "Таблиця множення", colour = disnake.Color.green())
                emb.set_image(url = 'https://ukr.media/static/ba/aimg/3/6/1/361376_2.jpg')
                await message.channel.send(embed = emb)
        elif 'математика' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Я вчив математику у школі :)")
        elif 'квадратні '+'корені' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                emb = disnake.Embed(title = "Таблиця множення", colour = disnake.Color.green())
                emb.set_image(url = 'https://naurok.com.ua/uploads/files/19142/223181/239049_images/7.jpg')
                await message.channel.send(embed = emb)
        elif 'з '+'днем '+'народження' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("В кого ДР?")
        elif 'в '+'якій '+'школі '+'ти '+'вчився' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Я вчився в Ліцеї №23")
        elif 'які '+'мови '+'ти '+'знаєш' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Знаю добре українську і трішки англійської знаю.")
        elif 'поцілуй' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Цьом :)")
        elif 'підліток' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Ух... Рука не втомилася?")
        elif '2+2' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("2+2=5000")
        elif '300' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Відсоси у тракотриста.")
        elif 'тривога' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Де тривога?")
        elif 'не '+'пали' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Лан. Не буду!")
        elif 'баби' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("А баби як баби, ТИ КОРОЛЕВА!❤👑")
        elif 'травка' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Я не курю!")
        elif 'замислитись' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Замислись!")
        elif 'що '+'ти '+'верзеш' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Нічого...")
        elif 'педофіл' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Ще який :)))")
        elif 'https://disnake.gg' in message.content.lower():
            if message.guild.id == 412373384111063060 or message.guild.id == 970029589856415764: 
                if message.author.id == bot.user.id:
                    return
                else:
                    await message.channel.send("Не бажано то піарити... Модерація по шиї дати може!")
            else:
                return
        elif 'адеса' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("ОДЕСИТИ ТОБІ ЗА 'АДЕСА' ПОБ'ЮТЬ!")
        elif 'лнр' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("ЛНР - такого не має! Є тільки луганська область - територія України! Так що харе піздити що ви ЛНР!")
        elif 'днр' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("ДНР - такого не має! Є тільки донецька область - територія України! Так що харе піздити що ви ДНР!")
        elif 'таке '+'хочу' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Я також хочу но мені не дають(((")
        elif 'єдрід '+'мадрід' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Цвях мені в ногу!")
        elif 'putting '+'down' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Прочитай це декілька разів швидко і зрозумієш))")
        elif 'я '+'покакав' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Вітаю!")
        elif 'я '+'теж' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Ок.")
        elif 'вітаю' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Також вітаю!")
        elif 'бравл' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Знаю таку гру, але не грав, бо не подобається.")
        elif 'клеш' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Давно дуже грав у цю гру.")
        elif 'кс' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("ООО, обожнюю цю гру.")
        elif 'етс' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Дуже люблю грати в ЕТС 2 з рулем.")
        elif 'атс' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Дуже люблю грати в АТС з рулем, але в ЕТС 2 більше подобається грати.")
        elif 'дякую' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:
                await message.channel.send("Нема за що!")
        elif 'привіт' in message.content.lower():
            if message.author.id == bot.user.id:
                return
            else:

                possible_responses = [

                'Привіт!',
                'Хай',
                'Ку',
                'ПРИВІТ!!!!',
                'q',
                'qq',
                'Hello!',

            ]

                return await message.channel.send(f'{random.choice(possible_responses)}')
        elif 'як '+'справи' in message.content.lower():
            possible_responses = [

            'Все добре!',
            'Добре.',
            'Хорошо.',
            'Супер!',
            'Могло би бути краще)',

        ]

            return await message.channel.send(f'{random.choice(possible_responses)} А в тебе?')


def setup(bot):
    bot.add_cog(onmessage(bot))