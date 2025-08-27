import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    try:
        await bot.tree.sync()
    except:
        pass

@app_commands.command(name="f12", description="*giggle*")
async def send_video(interaction: discord.Interaction):
    try:
        await interaction.response.send_message(file=discord.File("F12.mp4"))
    except:
        pass

send_video.dm_permission = True
bot.tree.add_command(send_video)

bot.run(TOKEN)
