TOKEN = 'token-here' # discord bot token, discord bot token
RCON_HOST = 'ip-here' # ip serveru, ip of the server
RCON_PORT = 25575  # Port RCON vetsinou 25575, port RCON mostly 25575
RCON_PASSWORD = 'pass-here' # heslo RCON, password of RCON
ALLOWED_CHANNEL_ID = 11111111111111111111 # id roomky na discordu, room id on discord



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
        await ctx.send("spatny kanal pro prikaz, wrong channel for command")
        return

    if not command:
        await ctx.send("Nezadal jsi žádný Minecraft příkaz! Použij příkaz takto: `c!command <příkaz>`, You have not entered any Minecraft command! Use the command like this: `c!command <command>`")
        return

    try:
        with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
            response = mcr.command(command)
            await ctx.send(f"Příkaz `{command}` byl úspěšně odeslán. Odpověď serveru: {response}, The command `{command}` was sent successfully. Server response: {response}.")
    except Exception as e:
        await ctx.send(f"Došlo k chybě při pokusu o připojení k RCON: {e}, An error occurred while trying to connect to RCON: {e}")



bot.run(TOKEN)
