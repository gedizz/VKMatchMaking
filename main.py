import string
from collections import Counter
import discord
from discord import Embed
from discord.ext import commands, tasks
import creds
from Manager import BannerlordBot, setup
from DatabaseManager import DatabaseManager
import random
import itertools
from GameManager import GetFactionData



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


@bot.command()
async def genteam(ctx):
    classes = ["Infantry", "Cavalry", "Ranged"]
    data = [
        {
            "username": f"user{i + 1}",
            "steamid": "".join(random.choices(string.ascii_letters + string.digits, k=17)),
            "mmr": random.randint(2000, 5000),
            "class1": random.choice(classes),
            "class2": random.choice([x for x in classes if x != classes[0]]),
        }
        for i in range(12)
    ]

    teams = divide_players_into_teams(data)
    team1, team2 = teams

    team1_mmr = sum(player["mmr"] for player in team1) / 6
    team2_mmr = sum(player["mmr"] for player in team2) / 6
    mmr_difference = team1_mmr - team2_mmr

    faction1 = GetFactionData("Khuzait")
    faction2 = GetFactionData("Aserai")

    # Team 1 embed
    embed1 = Embed(title=f"Team 1 - {faction1[1]}", color=faction1[0])
    embed1.set_thumbnail(url=faction1[2])
    for player in team1:
        embed1.add_field(name=f"{player['username']} ({player['steamid']})", value=f"MMR: {player['mmr']} - Class: {player['class1']}", inline=False)

    # Team 2 embed
    embed2 = Embed(title=f"Team 2 - {faction2[1]}", color=faction2[0])
    embed2.set_thumbnail(url=faction2[2])
    for player in team2:
        embed2.add_field(name=f"{player['username']} ({player['steamid']})", value=f"MMR: {player['mmr']} - Class: {player['class1']}", inline=False)

    # MMR difference and class count difference embed
    class_counts1 = {"Infantry": 0, "Cavalry": 0, "Ranged": 0}
    class_counts2 = {"Infantry": 0, "Cavalry": 0, "Ranged": 0}
    for player in team1:
        class_counts1[player["class1"]] += 1
    for player in team2:
        class_counts2[player["class1"]] += 1

    embed3 = Embed(title="MMR Difference and Class Count", color=0x808080)
    embed3.add_field(name="MMR Difference", value=f"{mmr_difference}", inline=False)
    embed3.add_field(name="Team 1 Class Count", value=f"Infantry: {class_counts1['Infantry']} | Cavalry: {class_counts1['Cavalry']} | Ranged: {class_counts1['Ranged']}", inline=True)
    embed3.add_field(name="Team 2 Class Count", value=f"Infantry: {class_counts2['Infantry']} | Cavalry: {class_counts2['Cavalry']} | Ranged: {class_counts2['Ranged']}", inline=True)

    await ctx.send(embed=embed1)
    await ctx.send(embed=embed2)
    await ctx.send(embed=embed3)





bot.run(creds.apiKey)
