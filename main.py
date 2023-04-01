import discord
from discord.ext import commands, tasks
import creds
from Manager import BannerlordBot, setup
from DatabaseManager import DatabaseManager

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.members = True
bot = commands.Bot(command_prefix='!', help_command=None, intents=intents)


####################
###  Task Loops  ###
####################
@tasks.loop(seconds=3.0)
async def guild_tasks():
    return



##############
##  Events  ##
##############
@bot.event
async def on_ready():
    # await setup(bot)
    print(f'{bot.user.name} has connected to Discord!')




################
##  Commands  ##
################

@bot.command()
async def channel(ctx):
    await ctx.send(ctx.channel.id)


# User enters !register
# - Bot PM's the user instructions
#
#
@bot.command()
async def register(ctx, *args: str):
    arguments = list(args)
    # Check for invalid steamID cases
    if len(arguments) != 1 or len(arguments[0]) != 17:
        await ctx.send("Please provide a valid steamID")
        return
    # Check if the ID is already registered or not
    if await DatabaseManager.CheckExistence(arguments[0]) is True:
        await ctx.send("Steam ID already registered")
        return

    result = await DatabaseManager.RegisterPlayer(arguments[0], ctx.message.author.id)
    await ctx.send(result)



bot.run(creds.apiKey)
