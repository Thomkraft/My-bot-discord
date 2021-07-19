import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="/", description="Bot de Thomkraft !")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Bot de thomkraft!"))
    print("Ready to use !")

@bot.event
async def on_message(message):
    if message.content.startswith("salut"):
        taille_message = len(message.content)
        if taille_message >= 20:
            return
        await message.add_reaction("👋")
        await message.channel.send("Coucou toi !")

    elif message.content == ("qui c'est le plus beau ?"):
        thomkraft_id = await bot.get_user(91499418383810561)
        print(thomkraft_id)
        #await message.channel.send(f"C'est @thomkraft bien sure !")




bot.run("ODQzNDUyNDM0NTg3NDUxNDQz.YKEESg.OcH4tmjBOfZfHHBotP5rKLcqC1g")
