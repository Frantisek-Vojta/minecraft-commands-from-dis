TOKEN = 'token-here' # discord bot token
RCON_HOST = 'ip-here' # ip serveru
RCON_PORT = 25575  # Port RCON vetsinou 25575
RCON_PASSWORD = 'pass-here' # heslo RCON
ALLOWED_CHANNEL_ID = 11111111111111111111 # id roomky na disu



import discord
from discord.ext import commands
from mcrcon import MCRcon
from flask import Flask
from threading import Thread

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="c!", intents=intents)


@bot.command()
async def command(ctx, *, command: str = None):
    if ctx.channel.id != ALLOWED_CHANNEL_ID:
        await ctx.send("Tento příkaz může být použit pouze v určeném kanálu!")
        return

    if not command:
        await ctx.send("Nezadal jsi žádný Minecraft příkaz! Použij příkaz takto: `c! <příkaz>`.")
        return

    try:
        with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
            response = mcr.command(command)
            await ctx.send(f"Příkaz `{command}` byl úspěšně odeslán. Odpověď serveru: {response}")
    except Exception as e:
        await ctx.send(f"Došlo k chybě při pokusu o připojení k RCON: {e}")



bot.run(TOKEN)