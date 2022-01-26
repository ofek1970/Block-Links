import os 
import discord
from discord.ext import commands

client = commands.Bot(command_prefix=commands.when_mentioned_or("d/", "D/"),  help_command=None)

@client.event
async def on_ready():
  print('Bot Is Online And Ready to go!')

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
      return
    msg_content = message.content.lower()

    links = ['https://', '.com']

    if any(word in msg_content for word in links):
        await message.delete()
        await message.channel.send("No Links Allowed In This Channel!!")

client.run(os.getenv('TOKEN'))
