# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from os import listdir
from discord.ext import commands

image_path = "./trudeau_images/"

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')


@bot.command(name='trudeau')
async def post_pic(ctx):
    trudeau_image_names = listdir(image_path)

    image_name = random.choice(trudeau_image_names)
    await ctx.send(file=discord.File(image_path + image_name))


@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


bot.run(TOKEN)
