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


def divide_players_into_teams(data):
    # Sort the players by MMR
    sorted_data = sorted(data, key=lambda x: x["mmr"], reverse=True)

    # Initialize teams
    team1 = []
    team2 = []

    # Initialize class counts for both teams
    class_counts1 = {"Infantry": 0, "Cavalry": 0, "Ranged": 0}
    class_counts2 = {"Infantry": 0, "Cavalry": 0, "Ranged": 0}

    for player in sorted_data:
        # Determine which team has lower MMR and class count
        team1_mmr = sum(p["mmr"] for p in team1)
        team2_mmr = sum(p["mmr"] for p in team2)

        if team1_mmr <= team2_mmr:
            selected_team = team1
            class_counts = class_counts1
        else:
            selected_team = team2
            class_counts = class_counts2

        primary_class = player["class1"]
        secondary_class = player["class2"]

        # Prioritize primary class and check if it doesn't exceed the class count limit (6 players / 3 classes = 2 players per class)
        if class_counts[primary_class] < 2:
            selected_team.append(player)
            class_counts[primary_class] += 1
        elif class_counts[secondary_class] < 2:  # Use secondary class if primary class count limit is exceeded
            player["class1"] = secondary_class  # Update the primary class to secondary class for display purposes
            selected_team.append(player)
            class_counts[secondary_class] += 1
        else:  # If both primary and secondary classes are full, add the player to the team with lower MMR
            selected_team.append(player)
            class_counts[primary_class] += 1

    return [team1, team2]