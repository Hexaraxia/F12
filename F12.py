import discord, os, sys
from pathlib import Path

TOKEN = os.getenv("DISCORD_TOKEN")
VIDEO = Path(__file__).with_name("F12.mp4")
if not VIDEO.exists(): sys.exit()

class Bot(discord.Client):
    def __init__(self): super().__init__(intents=discord.Intents.default()); self.tree = discord.app_commands.CommandTree(self)
    async def setup_hook(self): await self.tree.sync()

bot = Bot()

@bot.tree.command(name="f12", description="Send the F12 video")
async def f12(interaction: discord.Interaction): await interaction.response.send_message(file=discord.File(str(VIDEO)))

bot.run(TOKEN)
