import discord
from discord.ext import commands, tasks
import creds

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', help_command=None, intents=intents)


bot.run(creds.apiKey)
