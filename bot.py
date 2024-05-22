import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def start_server(ctx):
    response = requests.post('http://127.0.0.1:8000/start_server')
    if response.status_code == 200:
        await ctx.send('Minecraft server started successfully!')
    else:
        await ctx.send('Failed to start the Minecraft server.')

@bot.command()
async def stop_server(ctx):
    response = requests.post('http://127.0.0.1:8000/stop_server')
    if response.status_code == 200:
        await ctx.send('Minecraft server stopped successfully!')
    else:
        await ctx.send('Failed to stop the Minecraft server.')

bot.run('YOUR_DISCORD_BOT_TOKEN')

