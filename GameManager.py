import discord
from discord.ext import commands



def GetFactionData(factionName: str):
    factions = {
        "Vlandia": (0x8d2918, "Vlandian Faction", "https://static.wikia.nocookie.net/mountandblade/images/c/c4/Vlandia.jpg/revision/latest/scale-to-width-down/350?cb=20191125150828"),
        "Empire": (0x712b87, "Empire Faction", "https://static.wikia.nocookie.net/mountandblade/images/f/f2/Northern_Empire.jpg/revision/latest?cb=20200409234607"),
        "Sturgia": (0x294b78, "Sturgian Faction", "https://static.wikia.nocookie.net/mountandblade/images/8/88/Sturgia.jpg/revision/latest/scale-to-width-down/350?cb=20180531054519"),
        "Aserai": (0xb67a1e, "Aserai Faction", "https://static.wikia.nocookie.net/mountandblade/images/a/a1/Aserai.jpg/revision/latest/scale-to-width-down/350?cb=20191125150553"),
        "Battania": (0x275019, "Battanian Faction", "https://static.wikia.nocookie.net/mountandblade/images/e/e8/Battania.jpg/revision/latest/scale-to-width-down/350?cb=20200409234144"),
        "Khuzait": (0x429081, "Khuzait Faction", "https://static.wikia.nocookie.net/mountandblade/images/7/72/Khuzait.jpg/revision/latest/scale-to-width-down/350?cb=20191125155232"),
    }

    if factionName in factions:
        return factions[factionName]
    else:
        raise ValueError("Invalid faction name")