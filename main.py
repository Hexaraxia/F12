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

@bot.tree.command(name="f12", description="*giggle*")
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def f12(interaction: discord.Interaction):
    try:
        await interaction.response.send_message(file=discord.File("F12.mp4"))
    except:
        pass

bot.run(TOKEN)
