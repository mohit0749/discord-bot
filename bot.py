import os

from discord.ext import commands
from dotenv import load_dotenv

from database import Session
from search.search import search, get_recent_search, save_search_history
from searchengine.google_search import Google
from setup_db import init_db

init_db()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
session = Session()
google_search = Google(host="https://www.google.com", path="search", query_params="q")

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_message(message):
    if message.content.strip().lower() == 'hi':
        await message.channel.send("hey")
    await bot.process_commands(message)


@bot.command(name='google', help='search on google')
async def google(ctx, keyword):
    result = search(google_search, keyword)
    save_search_history(keyword, session)
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
