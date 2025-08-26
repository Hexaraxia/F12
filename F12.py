import discord

TOKEN = "YOUR_BOT_TOKEN"
VIDEO_PATH = "F:\Archive\Programs\F12 App\F12.mp4"

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = discord.app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = MyClient()

@client.tree.command(name="f12", description="F12")
async def f12(interaction: discord.Interaction):
    await interaction.response.send_message(file=discord.File(VIDEO_PATH))

client.run(TOKEN)