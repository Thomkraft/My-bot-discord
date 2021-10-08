import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="/",description="Bot de Thomkraft !")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Bot de thomkraft!"))
    print("Ready to use !")

@bot.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel):
        if message.author.id == bot.user.id:
            return
        Owner = await bot.fetch_user(291499418383810561)
        await Owner.send(f" {message.author.mention} a mp le bot et lui a envoyé : \n **{message.content}**")

    elif message.content == "ping":
        await message.channel.send("pong")

    elif message.content.startswith("/sm "):

        list_role = message.author.roles
        permission = False

        for role in list_role:
            namerole = role.name

            if namerole in ["Admin", "OWNER"]:
                permission = True

        if permission is True:

            second = message.content.split(" ")
            message_len = len(second)
            time = second[1]

            if message_len > 2:
                await message.channel.send("Il y a trop d'arguments")
                return

            if second[1] == "reset":
                await message.channel.edit(slowmode_delay=0)
                await message.channel.send("Slowmode reset")
                return

            elif time.isdigit():
                await message.channel.edit(slowmode_delay=time)
                await message.channel.send(f"Slowmode fixée a : {time} secondes")
                return

            else:
                await message.channel.send("L'argument n'est pas un nombre")
                return
        else:
            await message.channel.send("Tu na pas la permission d'utiliser cette commande")
            return



    else:
        channellog = await bot.fetch_channel(896032871410704484)
        messageinsulte = message.content.split(" ")
        userid = message.author.id
        insulte = ["tg", "fdp", "connard", "fils de pute"]
        if bot.user.id == message.author.id:
            return
        for i in insulte:
            if i in messageinsulte:
                await message.delete()
                await channellog.send(f"<@!{userid}> a envoyé un message contenant une insulte :\n"
                                      f"**\"{message.content}\"**")
                return








bot.run("ODk2MDMwNzExMDQyMTU4NjYy.YWBLoA.SKI5uICGFCmTwFHXgNpDIO8z8GM")