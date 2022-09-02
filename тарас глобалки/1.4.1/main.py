from distutils import extension
import disnake
import asyncio
from asyncio import sleep
import os
import config
from disnake.ext import commands

prefix = config.prefix

bot = commands.Bot(command_prefix = prefix) #Interaction
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Start work!")

    await bot.change_presence(status=disnake.Status.idle, activity=disnake.Game(f".допомога | {len(bot.guilds)} серверів"))
    await asyncio.sleep(15) 

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

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and not filename.startswith("_"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(config.TOKEN)