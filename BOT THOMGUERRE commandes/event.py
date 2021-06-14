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
        channel = await bot.fetch_channel(844130740404355072)
        await channel.send(f"{message.author.mention} a mp le bot et lui a envoyé : \n **{message.content}**")

    elif message.content == "ping":
        await message.channel.send("pong")

    elif message.content.startswith("/mp "):
        channel = await bot.fetch_channel(844130740404355072)
        userid = int(message.content.split(" ")[1][3:-1])
        user = await bot.fetch_user(userid)
        mess = message.content.split(f"/mp <@!{userid}> ")[1]
        await user.send(content=mess)
        await channel.send(f"Le message **{mess}** a bien été envoyé a <@!{userid}>")
    else:
        channellog = await bot.fetch_channel(844130740404355072)
        messageinsulte = message.content.split(" ")
        userid = message.author.id
        channel = message.channel
        insulte = ["tg", "fdp", "connard", "fils de pute"]
        if bot.user.id == message.author.id:
            return
        for i in insulte:
            if i in messageinsulte:
                await channel.send(f"Toi tg {message.author.name}! ")
                await message.delete()
                await channellog.send(f"<@!{userid}> a envoyé un message contenant une insulte !")
                return












"""
@bot.event
async def on_typing(channel : discord.TextChannel,user,when):
    print(channel,  user.name,when)
    await channel.send(f"{user.name} a commencé a écrire dans ce salon le {when}")

@bot.event
async def on_message(message):
    channel = message.channel
    if message.author.id == bot.user.id:
        return
    messageemoji = await channel.send(f"> {message.content} \n {message.author}")
    if message.content == "mouais":
        message = messageemoji
        await messageemoji.add_reaction("✅")
"""
@bot.event
async def on_message_edit(before, after):
    channel = before.channel
    user = before.author
    await channel.send(f"{user} a édité son message : \n Avant :> {before.content} \n Apres :> {after.content}")

bot.run("NzQyNzI1NzkwMTIyMjQ2MjUw.XzKTSw.m7WxTCdMG3YWQ9L-8FxaosnqDvY")




