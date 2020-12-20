import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
from database import Session
from searchengine.google_search import Google
from search.search import search, get_recent_search
from setup_db import init_db

init_db()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
bot = commands.Bot(command_prefix='!')
session = Session()
google_search = Google(host="https://www.google.com", path="search", query_params="q")


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.strip().lower() == 'hi':
        await message.channel.send("hey")


@bot.command(name='google', help='search on google')
async def google(ctx, keyword):
    print(ctx)
    result = search(google_search, keyword)
    for res in result:
        await ctx.send(res)


@bot.command(name='recent', help='show recent search keywords')
async def recent(ctx, keyword):
    result = get_recent_search(keyword, session)
    for res in result:
        await ctx.send(res)


bot.run(TOKEN)

if __name__ == "__main__":
    pass
