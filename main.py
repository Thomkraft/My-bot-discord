import discord
import asyncio
import random
from discord.ext import commands , tasks

bot = commands.Bot(command_prefix="/", description="Bot de Thomkraft !")

funFact = ["L'eau mouille",
           "Le feu brule",
           "Lorsque vous volez, vous ne touchez pas le sol",
           "Winter is coming", "Mon créateur est Titouan",
           "Il n'est pas possible d'aller dans l'espace en restant sur terre",
           "La terre est ronde",
           "La moitié de 2 est 1",
           "7 est un nombre heureux",
           "Les allemands viennent d'allemagne",
           "Le coronavirus est un virus se répandant en Europe, en avez vous entendu parler ?",
           "J'apparais 2 fois dans l'année, a la fin du matin et au début de la nuit, qui suis-je ?",
           "Le plus grand complot de l'humanité est",
           "Pourquoi lisez vous ca ?"]

botgame = ["Bot de thomkraft !",
           "Le feu brule",
           "Pourquoi lisez vous sa ?",
           "tu veu ma photo ?",
           "/help pour plus d'information !"]

bontoutoulink = "https://urlz.fr/fGJI"
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Bot de thomkraft!"))
    print("Ready to use !")
    changestatus.start()

@tasks.loop(seconds = 5)
async def changestatus():
    game = discord.Game(random.choice(botgame))
    await bot.change_presence(status = discord.Status.online, activity = game)

@tasks.loop(seconds = 10)
async def bontoutou():
    channel = bot.get_channel(844160100808654858)
    message = await channel.send(f"Clique sur ce lien n'aie pas peur :<{bontoutoulink}>")

@bot.command()
@commands.has_any_role("Admin", "OWNER")
async def startbtt(ctx,secondes = 5, minutes = 0, hours = 0):
    bontoutou.change_interval(seconds=secondes, minutes=minutes, hours=hours)
    bontoutou.start()
    await ctx.channel.send(f"La commande btt a bien commencée avec un intervalle de : {hours} heures,{minutes} minutes, {secondes} secondes!")

@bot.command()
@commands.has_any_role("Admin", "OWNER")
async def stopbtt(ctx):
    bontoutou.stop()
    await ctx.channel.send("La commande btt a bien été arétée !")



@bot.command()
@commands.has_any_role("Admin","OWNER")
async def csi(ctx, secondes = 5, minutes = 0, hours = 0): #change status interval
    changestatus.change_interval(seconds = secondes , minutes = minutes, hours = hours)
    await ctx.channel.send(f"L'intervalle de changement de jeu du bot est passé a : {hours} heures,{minutes} minutes, {secondes} secondes")


@bot.command()
async def aide(ctx):
    await ctx.send("**Voici la lisste de toute les commandes : **\n"
                   "```/coucou \n"
                   "/serverinfo \n"
                   "/bonjour \n"
                   "/say [texte...] \n"
                   "/chinese [texte...] \n"
                   "/says [chiffre...] [texte...] \n"
                   "/getinfo [texte...] \n"
                   "Fais /[commande] help pour plus dinformation ! \n ```")


@bot.command()
async def coucou(ctx):
    await ctx.send(f"coucou {ctx.author.name}!")


@bot.command()
async def serverinfo(ctx):
    server = ctx.guild
    numberoftextechannels = len(server.text_channels)
    numberofvoicechannels = len(server.voice_channels)
    serverdescription = server.description
    numberofpeople = server.member_count
    servername = server.name
    message = f"Le serveur **{servername}** contient *{numberofpeople}* personnes. \n" \
              f"La description du serveur : {serverdescription} \n" \
              f"Ce serveur possede {numberoftextechannels} salons écrit ainsi que {numberofvoicechannels} salons vocaux"
    await ctx.send(message)


@bot.command()
async def bonjour(ctx):
    serveurname = ctx.guild.name
    message = f"Bonjour jeune *padawan* ! Savais tu que tu te trouvais dans le serveur *{serveurname}*, c'est" \
              f" d'ailleurs un super serveur puisuqe **JE** suis dedans."
    await ctx.send(message)


@bot.command()
async def say(ctx, channel: discord.TextChannel, *texte):
    list_role = ctx.author.roles
    permission = False
    for role in list_role:
        namerole = role.name
        if namerole in ["Admin", "OWNER"]:
            permission = True
    if permission is True:
        await channel.send(" ".join(texte))
    else:
        await ctx.send("Nope mec t'es pas Admin !")


@bot.command()
async def chinese(ctx, *texte):
    chinesechar = "丹书ㄈ力已下呂廾工丿片乚爪ㄇ口尸厶尺ㄎ丁凵人山父了乙"
    chinesetext = []
    for word in texte:
        for char in word:
            if char.isalpha():
                index = ord(char) - ord("a")
                transformed = chinesechar[index]
                chinesetext.append(transformed)
            else:
                chinesetext.append(char)
        chinesetext.append("  ")
    await ctx.send("".join(chinesetext))


@bot.command()
async def says(ctx, number, *texte):
    for i in range(int(number)):
        await ctx.send(" ".join(texte))


@bot.command()
async def getinfo(ctx, texte):
    if texte == "membercount":
        await ctx.send(f"Il y a {ctx.guild.member_count} membres !")
    elif texte == "numberofchannel":
        await ctx.send(f"Il y a {len(ctx.guild.text_channels) + len(ctx.guild.voice_channels)} channels !")
    elif texte == "name":
        await ctx.send(f"Le nom du serveur est **{ctx.guild.name}**")
    else:
        await ctx.send("```La commande est fausse essaye avec : \n"
                       "/getinfo membercount \n"
                       "/getinfo numberofchannel \n"
                       "/getinfo name```")


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 5):
    await ctx.channel.purge(limit=amount + 1)


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.User, *, reason="Aucune raison n'a été donné"):
    #    await ctx.guild.kick(user, reason = reason)
    authorname = ctx.author.name
    embed = discord.Embed(title="**Kick**", description="**Un modérateur a frappé !**",
                          url="https://www.youtube.com/watch?v=yw-tMwy216c", colour=discord.Colour.blue())
    embed.set_thumbnail(url="https://emoji.gg/assets/emoji/6623_banhammer.png")
    embed.set_author(name=authorname, icon_url=ctx.author.avatar_url)
    embed.add_field(name="Membre Kick", value=user.name)
    embed.add_field(name="Raison", value=reason)
    embed.add_field(name="Modérateur", value=authorname)
    embed.set_footer(text=random.choice(funFact))
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(ban_members=True)
@commands.has_any_role("Admin", "OWNER")
async def ban(ctx, user: discord.User, *, reason="Aucune raison n'a été donné"):
    list_role = ctx.author.roles
    authorname = ctx.author.name
    #    await ctx.guild.ban(user, reason = reason)
    embed = discord.Embed(title="**Bannissement**", description="**Un modérateur a frappé !**",
                          url="https://www.youtube.com/watch?v=yw-tMwy216c", colour=discord.Colour.blue())
    embed.set_thumbnail(url="https://emoji.gg/assets/emoji/6623_banhammer.png")
    embed.set_author(name=authorname, icon_url=ctx.author.avatar_url)
    embed.add_field(name="Membre banni", value=user.name)
    embed.add_field(name="Raison", value=reason)
    for role in list_role:
        rolename = role.name
        if rolename == "OWNER":
            embed.add_field(name="OWNER", value=authorname)
            break
        elif rolename == "Admin":
            embed.add_field(name="Admin", value=authorname)
            break
    embed.set_footer(text=random.choice(funFact))
    await ctx.send(embed=embed)


"""
check les role de l'author
si == admin 
name = admin
si == Owner
name == Owner
"""


@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user, *reason):
    reason = " ".join(reason)
    username, userID = user.split("#")
    bannedUsers = await ctx.guild.bans()
    for i in bannedUsers:
        if i.user.name == username and i.user.discriminator == userID:
            await ctx.guild.unban(i.user, reason=reason)
            await ctx.send(f"{user} a été unban comme raison : {reason}.")
            return
    await ctx.send(f"L'utilisateur {user} n'est pas dans la lisste des personnes bannis !")


@bot.command()
@commands.has_permissions(ban_members=True)
async def banid(ctx):
    ids = []
    bans = await ctx.guild.bans()
    for i in bans:
        ids.append(str(i.user.id))
    await ctx.send("La lisste des id des utilisateurs bannis du serveur est :")
    await ctx.send("\n".join(ids))


@bot.command()
async def annonce(ctx, channel: discord.TextChannel, *texte):
    messagedelete = ctx.message
    message = " ".join(texte)
    await messagedelete.delete()
    await channel.send(f"**{message}**")


@bot.command()
async def cuisiner(ctx):
    await ctx.send("Envoyer le plat que vous voulez cuisiner.")

    def checkmessage(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel

    try:
        recette = await bot.wait_for("message", timeout=10, check=checkmessage)
    except:
        return
    message = await ctx.send(
        f"La préparation de {recette.content} va commencer. veuillez valider en réagissant avec ✅ ou annulé avec ❌")
    await message.add_reaction("✅")
    await message.add_reaction("❌")

    def checkemoji(reaction, user):
        return ctx.message.author == user and message.id == reaction.message.id and (
                    str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

    try:
        reaction, user = await bot.wait_for("reaction_add", timeout=10, check=checkemoji)
        if reaction.emoji == "✅":
            await ctx.send("La recette a démarré.")
        else:
            await ctx.send("La recette a bien été annulé.")
    except:
        await ctx.send("La recette a été annulé.")


@bot.command()
async def roulette(ctx, start):
    if start == "start":
        timetostart = 10
        await ctx.send(
            f"La roulette commencera dans {timetostart} secondes. Envoyer \"moi\" dans ce channel pour y participer !")
        player = []

        def check(message):
            return message.channel == ctx.message.channel and message.content == "moi" and message.author not in player

        try:
            while True:
                participation = await bot.wait_for("message", timeout=timetostart, check=check)
                player.append(participation.author)
                await ctx.send(
                    f"**{participation.author.name}** participe au tirage ! Le tirage commence dans {timetostart} secondes !")
        except:
            gagner = ["kick", "mute", "ban", "role perso"]
            await ctx.send("Inscription terminé ! Le tirage va commencé dans 3 secondes !")
            await asyncio.sleep(1)
            await ctx.send("2")
            await asyncio.sleep(1)
            await ctx.send("1")
            await asyncio.sleep(1)

            winner: discord.Member = random.choice(player)
            price = random.choice(gagner)

            await ctx.send(f"La personne qui a gagné un {price} est : ...")
            await asyncio.sleep(1)
            await ctx.send(f"**{winner.name}** !")

            if price == "kick":
                await ctx.guild.kick(winner, reason="dsl tu a gagné un kick !")
            elif price == "ban":
                await ctx.guild.ban(winner, reason="dsl tu a gagné un ban !")
            elif price == "mute":
                mutedrole = await getmutedrole(ctx)
                await winner.add_roles(mutedrole, reason = "dsl tu a gagné un mute !")


def isOwner(ctx):
    return ctx.message.author.id == 291499418383810561

@bot.command()
@commands.check(isOwner)
async def private(ctx):
    await ctx.send("Cette commande peut seulement etre effectué par le propriétaire du bot !")

async def createmuterole(ctx):
    mutedrole = await ctx.guild.create_role(name = "Mute server", permissions = discord.Permissions(send_messages = False, speak = False))
    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedrole, send_messages = False, speak = False)
    return mutedrole

async def getmutedrole(ctx):
    listroles = ctx.guild.roles
    for role in listroles:
        if role.name == "Mute server":
            return role
    return await createmuterole(ctx)

@bot.command()
async def mute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été donnée"):
    mutedrole = await getmutedrole(ctx)
    await member.add_roles(mutedrole, reason = reason)
    await ctx.channel.send(f"{member.mention} a été mute !")

@bot.command()
async def unmute(ctx, member : discord.Member, *, reason = "aucune raison n'a été donnée"):
    mutedrole = await getmutedrole(ctx)
    await member.remove_roles(mutedrole, reason = reason)
    await ctx.channel.send(f"{member.mention} a été unmute !")


'''
@bot.command()
async def giverole(ctx, membre = discord.Member, *,nom):
    givedrole = ""
    roles = ctx.guild.roles
    for role in roles:
        if role.name == nom:
            givedrole = role
    if givedrole == "":
        givedrole = await ctx.guild.create_role(name = nom, reason = "Un membre a fait la commande role.")
    await membre.add_roles(givedrole, reason = "commande")
'''
"""
commande /addrole @user role
commande /delrole @user role
embed pour le banid
embed pour la roulette
embed pour le mute
embed pour le unmute
embed pour le unban
mp lutilisateur dans les commandes ban,banid,mute,unmute,unban pour la raison

merci @bot  tg enfait @user

"""
bot.run("NzQyNzI1NzkwMTIyMjQ2MjUw.XzKTSw.m7WxTCdMG3YWQ9L-8FxaosnqDvY")
# ❌,✅
