from typing import Optional
from dotenv import load_dotenv
import aiohttp
import os
import discord
from discord import app_commands

load_dotenv()

MY_GUILD = discord.Object(id=932674444583911474)  # replace with your guild id


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        self.http_client = aiohttp.ClientSession()
        super().__init__(intents=intents)
        # A CommandTree is a special type that holds all the application command
        # state required to make it work. This is a separate class because it
        # allows all the extra state to be opt-in.
        # Whenever you want to work with application commands, your tree is used
        # to store and work with them.
        # Note: When using commands.Bot instead of discord.Client, the bot will
        # maintain its own tree instead.
        self.tree = app_commands.CommandTree(self)

    # In this basic example, we just synchronize the app commands to one guild.
    # Instead of specifying a guild to every command, we copy over our global commands instead.
    # By doing so, we don't have to wait up to an hour until they are shown to the end-user.
    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
client = MyClient(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')


@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')


@client.tree.command()
async def data_list(interaction: discord.Interaction):
    """Says hello!"""
    data = None
    async with client.http_client.get('http://127.0.0.1:8000') as req:
      data = await req.json()
      print (data)
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')

client.run(os.environ.get("DISCORD_TOKEN"))
