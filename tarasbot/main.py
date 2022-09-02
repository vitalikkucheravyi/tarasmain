import disnake
import asyncio
from asyncio import sleep
import os
import random
import config
from disnake.ext import commands

prefix = config.prefix

bot = commands.Bot(command_prefix = prefix) #Interaction
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f"Почав роботу, {bot.user.name}!")
    guilds = await bot.fetch_guilds(limit=None).flatten()

    status=[
            f"{prefix}допомога",
            "Слава Україні!🇺🇦",
            f"{len(guilds)} серверів",
            "Піду вас розважати :)",
            "Не ображайтеся на мене будь-ласка!",
            f"Всю інформацію про мене можете дізнатися в {prefix}бот"
        ]

    while True:
        await bot.change_presence(status=disnake.Status.idle,activity=disnake.Game(name=f"{random.choice(status)}"))
        await asyncio.sleep(20)

@bot.command()
async def load(ctx, extension):
    if ctx.author.id == 503904015638200340 or ctx.author.id == 660069567959400449:
        extension = extension.lower()
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} завантажено!')
    else:
        await ctx.send("Ви не маєте доступу!")

@bot.command()
async def unload(ctx, extension):
    if ctx.author.id == 503904015638200340 or ctx.author.id == 660069567959400449:
        extension = extension.lower()
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} вивантажано!')
    else:
        await ctx.send("Ви не маєте доступу!")

@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == 503904015638200340 or ctx.author.id == 660069567959400449:
        extension = extension.lower()
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} перезавантажено!!')
    else:
        await ctx.send("Ви не маєте доступу!")

@bot.slash_command(name = "cogs")
async def cogs(ctx):
    if ctx.author.id == 503904015638200340:
        dirname = './cogs'
        files = os.listdir(dirname)
        emb = disnake.Embed(title = "Всі когі", description=f"{list(files)}", color=disnake.Color.random())
        await ctx.send(embed = emb)
    else:
        await ctx.send("Ви не маєте доступу до цієї команди!")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and not filename.startswith("_"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(config.TOKEN)