import discord
from discord.ext import commands

TOKEN = "NzA1MTA1MzI1MTE5ODk3NzAy.Xqm2uA.25XCs9AGDuIQ_8tOqKPeVzCuaO8"

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("bot is ready.")

client.run(TOKEN)