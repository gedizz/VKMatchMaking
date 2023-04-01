import asyncio
import aiomysql


class DatabaseManager:

    def __init__(self):
        self.db = "vkmatchmaking"
        self.username = "root"
        self.password = "duke"
        self.hostname = "localhost"
        self.port = 3306

    @staticmethod
    async def RegisterPlayer(steamID, discordID):
        conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                          user='root', password='duke',
                                          db='vkmatchmaking')
        cur = await conn.cursor()
        async with conn.cursor() as cur:
            await cur.execute("INSERT INTO players (discord_id, steam_id) VALUES (%s, %s)", (discordID, steamID))
            await conn.commit()

        conn.close()
        return "Inserted"

    @staticmethod
    async def CheckExistence(steamID):
        conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                          user='root', password='duke',
                                          db='vkmatchmaking')
        async with conn.cursor() as cur:
            await cur.execute(f"SELECT * FROM players WHERE steam_id={steamID};")
            if await cur.fetchone() is not None:
                return True
        return False;



