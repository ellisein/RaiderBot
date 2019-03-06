import asyncio

import discord
from discord.ext import commands

import utils
from params import *
from api import RaiderIO, Blizzard, Warcraftlogs, Bloodmallet


bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="World of Warcraft"))
    print("Logged in as {}".format(bot.user.name))

@bot.command(name="명령어", pass_context=True)
async def _command(ctx):
    await bot.send_message(ctx.message.channel,
        embed=discord.Embed(
            title="명령어", color=COLOR_INFO,
            description=", ".join(COMMANDS)))

@bot.command(name="캐릭터", pass_context=True)
async def _character(ctx):
    pass

@bot.command(name="경매장", pass_context=True)
async def _auction(ctx):
    pass

@bot.command(name="어픽스", pass_context=True)
async def _affixes(ctx):
    pass

@bot.command(name="주차", pass_context=True)
async def _weekly_mythic_plus(ctx):
    pass

@bot.command(name="주사위", pass_context=True)
async def _dice(ctx):
    pass

@bot.command(name="로그", pass_context=True)
async def _raid_logs(ctx):
    pass

@bot.command(name="특성", pass_context=True)
async def _talents(ctx):
    pass

@bot.command(name="아제특성", pass_context=True)
async def _azerite_traits(ctx):
    pass

@bot.command(name="장신구", pass_context=True)
async def _trinkets(ctx):
    pass

@bot.command(name="스탯", pass_context=True)
async def _secondary_stats(ctx):
    pass


if __name__ == "__main__":
    keys = utils.get_keys()
    bot.run(keys["discord"]["beta"])
