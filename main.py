import discord
import random
from discord.ext import commands

config = {
    'token': 'token',
    'prefix': '$',
}

bot = commands.Bot(command_prefix=config['prefix'])

@bot.command()
async def rand(ctx):
    await ctx.reply(random.randint(0, 100))


bot.run(config['token'])