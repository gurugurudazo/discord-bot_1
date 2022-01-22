import nextcord
from nextcord.ext import commands
import os
import asyncio

bot = commands.Bot(command_prefix="!.")

@bot.event
async def on_ready():
  print('botが起動しました')

bot.run(os.getenv("token"))