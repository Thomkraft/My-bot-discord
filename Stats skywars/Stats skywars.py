import discord
import pickle
import os
import random
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix="/", description="Bot de Thomkraft !")

botgame = ["Bot de Thomkraft !",
           "Stats bedwars manuelle !"]


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Bot de thomkraft!"))
    print("Ready to use !")
    changestatus.start()


@tasks.loop(seconds=5)
async def changestatus():
    game = discord.Game(random.choice(botgame))
    await bot.change_presence(status=discord.Status.online, activity=game)


# pickle.dump(20, open("463804264083619841/toplvl.txt", "wb"))
# nombrewin = pickle.load(open("win.txt", "wb"))

@bot.event
async def on_message(message):
    if message.content == ("/register"):
        try:
            userid = message.author.id
            os.mkdir(str(message.author.id))
            pickle.dump(0, open(f"{userid}/toplvl.txt", "wb"))
            pickle.dump(0, open(f"{userid}/topwins.txt", "wb"))
            pickle.dump(0, open(f"{userid}/topkills.txt", "wb"))
            pickle.dump(0, open(f"{userid}/prestige.txt", "wb"))
            pickle.dump(0, open(f"{userid}/niveaux.txt", "wb"))
            pickle.dump(0, open(f"{userid}/bestwinstreak.txt", "wb"))
            pickle.dump(0, open(f"{userid}/kills.txt", "wb"))
            pickle.dump(0, open(f"{userid}/win.txt", "wb"))
            pickle.dump(0, open(f"{userid}/defaite.txt", "wb"))
            await message.channel.send("Vos dossier de stats on bien été crée faites /help pour voir les commandes ! ")
        except:
            await message.channel.send("Tu a deja effectué cette commande !")

    elif message.content.startswith("/register "):
        list_role = message.author.roles
        permission = False
        for role in list_role:
            namerole = role.name
            if namerole in ["Admin", "OWNER"]:
                permission = True
        if permission == True:
            try:
                test = message.content.split(" ")[2]
                await message.channel.send("Erreure dans la commande merci de recommencer !")
                return
            except:
                try:
                    user = message.content.split(" ")[1]
                    userid = message.content.split(" ")[1][3:-1]
                    os.mkdir(str(userid))
                    pickle.dump(0, open(f"{userid}/toplvl.txt", "wb"))
                    pickle.dump(0, open(f"{userid}/topwins.txt", "wb"))
                    pickle.dump(0, open(f"{userid}/topkills.txt", "wb"))
                    pickle.dump(0, open(f"{userid}/prestige.txt", "wb"))
                    pickle.dump(0, open(f"{userid}/niveaux.txt", "wb"))
                    pickle.dump(0, open(f"{userid}/bestwinstreak.txt", "wb"))
                    pickle.dump(0, open(f"{userid}/kills.txt", "wb"))
                    pickle.dump(0, open(f"{userid}/win.txt", "wb"))
                    pickle.dump(0, open(f"{userid}/defaite.txt", "wb"))
                    await message.channel.send(
                        f"Les dossier de {user} on bien été crée faites /help pour voir les commandes ! ")
                except:
                    await message.channel.send("Le joueur est deja enregisstré !")
        else:
            await message.channel.send(
                "Tu n'a pas le role nécessaire pour effectuer cette commande essaye **/register ci tu n'a pas encore fait** !")

    # HELP

    elif message.content == ("/help") or message.content == ("/aide"):
        username = message.author.name
        embed = discord.Embed(title=f"**Coucou {username}**",
                              description="**Voici la lisste des commandes du serveur !**",
                              colour=discord.Colour.blue())
        embed.set_author(name=username, icon_url=message.author.avatar_url)
        embed.set_thumbnail(url="https://emoji.gg/assets/emoji/2309-help.png")
        embed.add_field(name="**/register**",
                        value="Commande pour s'enregisstrer aupres du bot pour ensuite effectuer les autres commandes !")
        embed.add_field(name="**/stats**", value="Commande pour afficher tes propres stats !")
        embed.add_field(name="**+win [value] \n, -win [value] \n, /setwin [value]**",
                        value="+win : Permet de rajouter le nombre de win choisit a tes stats \n"
                              "-win : Permet de suprimer le nombre de win choisit a tes stats \n"
                              "/setwin : permet de set tes win au nombre choisi ")
        embed.add_field(name="**+defaite [value],  -defaite [value]**",
                        value="+defaite : Permet de rajouter le nombre de defaites choisit a tes stats \n"
                              "-defaite : Permet de suprimer le nombre de defaites choisit a tes stats \n")
        embed.add_field(name="**+kill [value],  -kill [value]**",
                        value="+kill : Permet de rajouter le nombre de kills choisit a tes stats \n"
                              "-kill : Permet de suprimer le nombre de kills choisit a tes stats \n")
        embed.add_field(name="**/setwinstreak [value]**", value="Permet de set ton winstreak")
        embed.add_field(name="**+niveau [value], -niveau [value]**",
                        value="+niveau : Permet de rajouter le nombre de niveaux choisit a tes stats \n"
                              "-niveau : Permet de suprimer le nombre de niveaux choisit a tes stats \n")
        embed.add_field(name="**/prestige**", value="Permet d'augmenter d'un prestige une fois le niveau 100 atteint")
        embed.add_field(name="**/settopkill [value]**",
                        value="Permet de set ton numéro dans le classement kill. ( la valeur ? signifie que ton top est inconnue)")
        embed.add_field(name="**/settopwin [value]**",
                        value="Permet de set ton numéro dans le classement win. ( la valeur ? signifie que ton top est inconnue)")
        embed.add_field(name="**/settoplvl [value]**",
                        value="Permet de set ton numéro dans le classement lvl. ( la valeur ? signifie que ton top est inconnue)")

        await message.channel.send(embed=embed)

    # HELP ADMIN

    elif message.content == ("/help admin") or message.content == ("/aide admin"):
        list_role = message.author.roles
        permission = False
        for role in list_role:
            namerole = role.name
            if namerole in ["Admin", "OWNER"]:
                permission = True
        if permission == True:
            username = message.author.name
            embed = discord.Embed(title=f"**Coucou {username}**",
                                  description="**Voici la lisste des commandes du serveur !**",
                                  colour=discord.Colour.blue())
            embed.set_author(name=username, icon_url=message.author.avatar_url)
            embed.set_thumbnail(url="https://emoji.gg/assets/emoji/2309-help.png")
            embed.add_field(name="**/register [@player]**",
                            value="Permet de register un utilisateur qui n'y arrive pas tout seul bahaha")
            embed.add_field(name="**/setwinadmin [@player] [nb de win a set]**",
                            value="Permet de set les win d(un utilisateur")

            await message.channel.send(embed=embed)

        else:
            await message.channel.send(
                "Tu n'a pas les permitions necessaire pour effectuer cette commande essaye **/help** ou **/aide** !")

    # WIN

    elif message.content.startswith("/setwinadmin "):
        list_role = message.author.roles
        permission = False
        for role in list_role:
            namerole = role.name
            if namerole in ["Admin", "OWNER"]:
                permission = True
        if permission == True:
            try:
                userid = message.content.split(" ")[1][3:-1]
                nb_win_a_set = int(message.content.split(" ")[2])
                if nb_win_a_set >= 0:
                    if os.path.isdir(userid):
                        pickle.dump(nb_win_a_set, open(f"{userid}/win.txt", "wb"))
                        await message.channel.send(f"**{nb_win_a_set}** win ont été set pour le joueur <@!{userid}> !")
                    else:
                        await message.channel.send("Le joueur a qui il faut set c'est win ne c'est pas regisster !")
                        return
                else:
                    await message.channel.send("Le nombre de win a set doit étre supérieur a **0** !")
                    return
            except:
                await message.channel.send("Une erreure est survenue merci de recommencer !")
                return
        else:
            await message.channel.send(
                "Tu n'a pas le role nécessaire pour effectuer cette commande essaye **/setwin [ton nb de win]** !")

    elif message.content.startswith("/setwin "):
        userid = str(message.author.id)
        if os.path.isdir(userid):
            try:
                check = message.content.split(" ")[2]
                await message.channel.send("Merci de ne pas metre de charactere apres le nb de win a set !")
                return
            except:
                userid = message.author.id
                nb_win_a_set = message.content.split(" ")[1]
                try:
                    if int(nb_win_a_set) >= 0:
                        pickle.dump(nb_win_a_set, open(f"{userid}/win.txt", "wb"))
                        await message.channel.send(f"{nb_win_a_set} win t'on été set <@!{userid}> !")
                except:
                    await message.channel.send("Une erreure est survenue merci de recommencer !")
        else:
            await message.channel.send("Tu ne tes pas encore enregisstré merci de faire **/register** !")

    elif message.content.startswith("+win "):
        userid = str(message.author.id)
        if os.path.isdir(userid):
            try:
                var = message.content.split(" ")[2]
                await message.channel.send("Merci de ne pas mettre de charactere apres le chiffre/nombre !")
                return
            except:
                pass
            try:
                win_a_ajouter = int(message.content.split(" ")[1])
                nombrewin = pickle.load(open(f"{userid}/win.txt", "rb")) + win_a_ajouter
                pickle.dump(nombrewin, open(f"{userid}/win.txt", "wb"))
                await message.channel.send(f"**{win_a_ajouter}** win ont bien été ajouté ! \n"
                                           f"**win** : *{nombrewin}* ")
            except:
                await message.channel.send("Le nombre de win a ajouter n'est pas correct merci de recommencer !")
                return
        else:
            await message.channel.send("Tu ne tes pas encore enregisstré merci de faire **/register** !")
    elif message.content.startswith("-win "):
        userid = str(message.author.id)
        if os.path.isdir(userid):
            try:
                var = message.content.split(" ")[2]
                await message.channel.send("Merci de ne pas mettre de charactere apres le chiffre/nombre !")
                return
            except:
                pass
            try:
                win_a_retirer = int(message.content.split(" ")[1])
                nombrewin = pickle.load(open(f"{userid}/win.txt", "rb")) - win_a_retirer
                pickle.dump(nombrewin, open(f"{userid}/win.txt", "wb"))
                if nombrewin < 0:
                    await message.channel.send("Le nombre de win doit étre superieure a **0** !")
                    nombrewin_return = pickle.load(open(f"{userid}/win.txt", "rb")) + win_a_retirer
                    pickle.dump(nombrewin_return, open(f"{userid}/win.txt", "wb"))
                    return
                else:
                    await message.channel.send(f"**{win_a_retirer}** win ont bien été retiré ! \n"
                                               f"**win** : *{nombrewin}* ")
            except:
                await message.channel.send("Le nombre de win a retirer n'est pas correct merci de recommencer !")
                return
        else:
            await message.channel.send("Tu ne tes pas encore enregisstré merci de faire **/register** !")

    # DEFAITES

    if message.content.startswith("+defaite "):
        userid = str(message.author.id)
        if os.path.isdir(userid):
            try:
                var = message.content.split(" ")[2]
                await message.channel.send("Merci de ne pas mettre de charactere apres le chiffre/nombre !")
                return
            except:
                pass
            try:
                defaite_a_ajouter = int(message.content.split(" ")[1])
                nombredefaite = pickle.load(open(f"{userid}/defaite.txt", "rb")) + defaite_a_ajouter
                pickle.dump(nombredefaite, open(f"{userid}/defaite.txt", "wb"))
                await message.channel.send(f"**{defaite_a_ajouter}** defaite ont bien été ajouté ! \n"
                                           f"**defaites** : *{nombredefaite}* ")
            except:
                await message.channel.send("Le nombre de defaite a ajouter n'est pas correct merci de recommencer !")
                return
        else:
            await message.channel.send("Tu ne tes pas encore enregisstré merci de faire **/register** !")

    elif message.content.startswith("-defaite "):
        userid = str(message.author.id)
        if os.path.isdir(userid):
            try:
                var = message.content.split(" ")[2]
                await message.channel.send("Merci de ne pas mettre de charactere apres le chiffre/nombre !")
                return
            except:
                pass
            try:
                defaite_a_retirer = int(message.content.split(" ")[1])
                nombredefaite = pickle.load(open(f"{userid}/defaite.txt", "rb")) - defaite_a_retirer
                pickle.dump(nombredefaite, open(f"{userid}/defaite.txt", "wb"))
                if nombredefaite < 0:
                    await message.channel.send("Le nombre de défaite doit étre superieure a **0** !")
                    nombredefaite_return = pickle.load(open(f"{userid}/defaite.txt", "rb")) + defaite_a_retirer
                    pickle.dump(nombredefaite_return, open(f"{userid}/defaite.txt", "wb"))
                    return
                else:
                    await message.channel.send(f"**{defaite_a_retirer}** defaite ont bien été retiré ! \n"
                                               f"**defaite** : *{nombredefaite}* ")
            except:
                await message.channel.send("Le nombre de defaite a retirer n'est pas correct merci de recommencer !")
                return
        else:
            await message.channel.send("Tu ne tes pas encore enregisstré merci de faire **/register** !")

    # KILLS

    if message.content.startswith("+kill "):
        userid = str(message.author.id)
        if os.path.isdir(userid):
            try:
                var = message.content.split(" ")[2]
                await message.channel.send("Merci de ne pas mettre de charactere apres le chiffre/nombre !")
                return
            except:
                pass
            try:
                kills_a_ajouter = int(message.content.split(" ")[1])
                nombrekills = pickle.load(open(f"{userid}/kills.txt", "rb")) + kills_a_ajouter
                pickle.dump(nombrekills, open(f"{userid}/kills.txt", "wb"))
                await message.channel.send(f"**{kills_a_ajouter}** kills ont bien été ajouté ! \n"
                                           f"**kills** : *{nombrekills}* ")
            except:
                await message.channel.send("Le nombre de kill a ajouter n'est pas correct merci de recommencer !")
                return
        else:
            await message.channel.send("Tu ne tes pas encore enregisstré merci de faire **/register** !")

    elif message.content.startswith("-kill "):
        userid = str(message.author.id)
        if os.path.isdir(userid):
            try:
                var = message.content.split(" ")[2]
                await message.channel.send("Merci de ne pas mettre de charactere apres le chiffre/nombre !")
                return
            except:
                pass
            try:
                kills_a_retirer = int(message.content.split(" ")[1])
                nombrekills = pickle.load(open(f"{userid}/kills.txt", "rb")) - kills_a_retirer
                pickle.dump(nombrekills, open(f"{userid}/kills.txt", "wb"))
                if nombrekills < 0:
                    await message.channel.send("Le nombre de kill doit étre superieure a **0** !")
                    nombrekills_return = pickle.load(open(f"{userid}/kills.txt", "rb")) + kills_a_retirer
                    pickle.dump(nombrekills_return, open(f"{userid}/kills.txt", "wb"))
                    return
                else:
                    await message.channel.send(f"**{kills_a_retirer}** kills ont bien été retiré ! \n"
                                               f"**kills** : *{nombrekills}* ")
            except:
                await message.channel.send("Le nombre de kill a retirer n'est pas correct merci de recommencer !")
                return
        else:
            await message.channel.send("Tu ne tes pas encore enregisstré merci de faire **/register** !")

    # BEST WINSTREAK

    if message.content.startswith("/setwinstreak "):
        userid = str(message.author.id)
        if os.path.isdir(userid):
            try:
                var = message.content.split(" ")[2]
                await message.channel.send("Merci de ne pas mettre de charactere apres le chiffre/nombre !")
                return
            except:
                pass
            try:
                nombrewinstreak = int(message.content.split(" ")[1])
                if nombrewinstreak >= 0:
                    pickle.dump(nombrewinstreak, open(f"{userid}/bestwinstreak.txt", "wb"))
                    await message.channel.send(f"Le best winstreak a été set a **{nombrewinstreak}** ! \n"
                                               f"**best winstreak** : *{nombrewinstreak}* ")
            except:
                await message.channel.send("Le nombre de winstreak a set n'est pas correcte !")
                return
        else:
            await message.channel.send("Tu ne tes pas encore enregisstré merci de faire **/register** !")

    # LVL

    if message.content.startswith("+niveau "):
        userid = str(message.author.id)
        if os.path.isdir(userid):
            try:
                var = message.content.split(" ")[2]
                await message.channel.send("Merci de ne pas mettre de charactere apres le chiffre/nombre !")
                return
            except:
                pass
            try:
                niveau_a_ajouter = int(message.content.split(" ")[1])
                nombreniveaux = pickle.load(open(f"{userid}/niveaux.txt", "rb")) + niveau_a_ajouter
                pickle.dump(nombreniveaux, open(f"{userid}/niveaux.txt", "wb"))
                if nombreniveaux == 100:
                    await message.channel.send(f"**{niveau_a_ajouter}** niveaux ont bien été ajouté ! \n"
                                               f"**niveaux** : *{nombreniveaux}* \n"
                                               "Bravo tu a ateint le niveau **100** merci de faire /prestige pour augmenter d'un prestige !")
                    return
                if nombreniveaux > 100:
                    nombreniveaux_return = pickle.load(open(f"{userid}/niveaux.txt", "rb")) - niveau_a_ajouter
                    pickle.dump(nombreniveaux_return, open(f"{userid}/niveaux.txt", "wb"))
                    if nombreniveaux_return == 100:
                        await message.channel.send(
                            "Tu a atteint le niveau **100** merci de faire /prestige pour passer un prestige !")
                        return
                    else:
                        await message.channel.send(
                            "Ton nombre de niveaux ne doit pas dépasser **100** verifie la commande !")
                        return
                await message.channel.send(f"**{niveau_a_ajouter}** niveaux ont bien été ajouté ! \n"
                                           f"**niveaux** : *{nombreniveaux}* ")
            except:
                await message.channel.send("Le nombre de niveaux a ajouter n'est pas correct merci de recommencer !")
                return
        else:
            await message.channel.send("Tu ne tes pas encore enregisstré merci de faire **/register** !")

    elif message.content.startswith("-niveau "):
        userid = str(message.author.id)
        if os.path.isdir(userid):
            try:
                var = message.content.split(" ")[2]
                await message.channel.send("Merci de ne pas mettre de charactere apres le chiffre/nombre !")
                return
            except:
                pass
            try:
                niveau_a_retirer = int(message.content.split(" ")[1])
                nombreniveau = pickle.load(open(f"{userid}/niveaux.txt", "rb")) - niveau_a_retirer
                pickle.dump(nombreniveau, open(f"{userid}/niveaux.txt", "wb"))
                if nombreniveau < 1:
                    await message.channel.send("Le niveau ne doit pas étre inferieur a **1** merci de recommencer !")
                    nombreniveau_return = pickle.load(open(f"{userid}/niveaux.txt", "rb")) + niveau_a_retirer
                    pickle.dump(nombreniveau_return, open(f"{userid}/niveaux.txt", "wb"))
                    return
                await message.channel.send(f"**{niveau_a_retirer}** niveaux ont bien été retiré ! \n"
                                           f"**niveaux** : *{nombreniveau}* ")
            except:
                await message.channel.send("Le nombre de niveaux a retirer n'est pas correct merci de recommencer !")
                return
        else:
            await message.channel.send("Tu ne tes pas encore enregisstré merci de faire **/register** !")

    # PRESTIGE

    elif message.content == ("/prestige"):
        userid = str(message.author.id)
        if os.path.isdir(userid):
            userid = message.author.id
            niveau = pickle.load(open(f"{userid}/niveaux.txt", "rb"))
            prestige = pickle.load(open(f"{userid}/prestige.txt", "rb"))
            if niveau == 100:
                if prestige < 5:
                    prestige = pickle.load(open(f"{userid}/prestige.txt", "rb")) + 1
                    pickle.dump(prestige, open(f"{userid}/prestige.txt", "wb"))
                    niveau = pickle.load(open(f"{userid}/niveaux.txt", "rb")) - 99
                    pickle.dump(niveau, open(f"{userid}/niveaux.txt", "wb"))
                    await message.channel.send(f"Bravo tu vien de prestige {prestige} !")
                else:
                    await message.channel.send("Tu a atteint le nombre de prestige maximum **GG** ( **5** ) !")
                    return
            else:
                niveau_resstant = 100 - niveau
                await message.channel.send(
                    f"Tu n'est pas niveau **100** donc tu ne peu pas prestige tu est niveau : **{niveau}** plus que **{niveau_resstant}** niveau pour prestige!")
        else:
            await message.channel.send("Tu ne tes pas encore enregisstré merci de faire **/register** !")

    # CLASSEMENT KILL

    elif message.content.startswith("/settopkill "):
        userid = str(message.author.id)
        if os.path.isdir(userid):
            top = message.content.split(" ")[1]
            try:
                if int(top) > 0:
                    if int(top) == 1:
                        top1er = "1er"
                        await message.channel.send(f"Ton classement est : **{top1er}**")
                        pickle.dump(top1er, open(f"{userid}/topkills.txt", "wb"))
                    else:
                        top_resste = f"{top}eme"
                        await message.channel.send(f"Ton classement est : **{top_resste}**")
                        pickle.dump(top_resste, open(f"{userid}/topkills.txt", "wb"))
            except:
                if top == "?":
                    await message.channel.send(f"Ton classement est inconnu dommage pour toi !")
                    pickle.dump(top, open(f"{userid}/topkills.txt", "wb"))
                else:
                    await message.channel.send("Une erreure c'est produite merci de réessayer")
        else:
            await message.channel.send("Tu ne tes pas encore enregisstré merci de faire **/register** !")

    # CLASSEMENT WINS

    elif message.content.startswith("/settopwin "):
        userid = str(message.author.id)
        if os.path.isdir(userid):
            top = message.content.split(" ")[1]
            try:
                if int(top) > 0:
                    if int(top) == 1:
                        top1er = "1er"
                        await message.channel.send(f"Ton classement est : **{top1er}**")
                        pickle.dump(top1er, open(f"{userid}/topwins.txt", "wb"))
                    else:
                        top_resste = f"{top}eme"
                        await message.channel.send(f"Ton classement est : **{top_resste}**")
                        pickle.dump(top_resste, open(f"{userid}/topwins.txt", "wb"))
            except:
                if top == "?":
                    await message.channel.send(f"Ton classement est inconnu dommage pour toi !")
                    pickle.dump(top, open(f"{userid}/topwins.txt", "wb"))
                else:
                    await message.channel.send("Une erreure c'est produite merci de réessayer")
        else:
            await message.channel.send("Tu ne tes pas encore enregisstré merci de faire **/register** !")

    # CLASSEMENT LVL

    elif message.content.startswith("/settoplvl "):
        userid = str(message.author.id)
        if os.path.isdir(userid):
            top = message.content.split(" ")[1]
            try:
                if int(top) > 0:
                    if int(top) == 1:
                        top1er = "1er"
                        await message.channel.send(f"Ton classement est : **{top1er}**")
                        pickle.dump(top1er, open(f"{userid}/toplvl.txt", "wb"))
                    else:
                        top_resste = f"{top}eme"
                        await message.channel.send(f"Ton classement est : **{top_resste}**")
                        pickle.dump(top_resste, open(f"{userid}/toplvl.txt", "wb"))
            except:
                if top == "?":
                    await message.channel.send(f"Ton classement est inconnu dommage pour toi !")
                    pickle.dump(top, open(f"{userid}/toplvl.txt", "wb"))
                else:
                    await message.channel.send("Une erreure c'est produite merci de réessayer")
        else:
            await message.channel.send("Tu ne tes pas encore enregisstré merci de faire **/register** !")

    # stats

    elif message.content.startswith("/stats"):
        try:
            var = message.content.split(" ")[2]
            await message.channel.send("__Merci de ne pas mettre de charactere apres le pseudo!__")
            return
        except:
            pass
        if message.content == ("/stats"):
            userid = str(message.author.id)
            if os.path.isdir(userid):
                username = message.author.name
                userid = str(message.author.id)
                authorname = message.author.name
                embed = discord.Embed(title=f"**Stats de {username}**", description="**Stats skywars rinaorc !**",
                                      colour=discord.Colour.blue())
                embed.set_author(name=authorname, icon_url=message.author.avatar_url)
            else:
                await message.channel.send("Tu ne tes pas encore enregisstré merci de faire **/register** !")
                return
        else:
            try:
                user = message.content.split(" ")[1]
                userid = message.content.split(" ")[1][3:-1]
                username = await bot.fetch_user(userid)
                authorname = message.author.name
                embed = discord.Embed(title=f"**Stats de {username.name}**", description="**Stats skywars rinaorc !**",
                                      colour=discord.Colour.blue())
                embed.set_author(name=authorname, icon_url=message.author.avatar_url)
            except:
                await message.channel.send("Une erreur est survenue merci de recommencer !")
                return
        if os.path.isdir(userid):
            toplvl = pickle.load(open(f"{userid}/toplvl.txt", "rb"))
            topwin = pickle.load(open(f"{userid}/topwins.txt", "rb"))
            topkill = pickle.load(open(f"{userid}/topkills.txt", "rb"))
            prestige = pickle.load(open(f"{userid}/prestige.txt", "rb"))
            niveau = pickle.load(open(f"{userid}/niveaux.txt", "rb"))
            bestwinstreak = pickle.load(open(f"{userid}/bestwinstreak.txt", "rb"))
            kills = pickle.load(open(f"{userid}/kills.txt", "rb"))
            win = pickle.load(open(f"{userid}/win.txt", "rb"))
            defaites = pickle.load(open(f"{userid}/defaite.txt", "rb"))

            embed.set_thumbnail(url="https://emoji.gg/assets/emoji/2391-newspaper1.png")
            embed.add_field(name="**win**", value=f"*{win}*")
            embed.add_field(name="**defaites**", value=f"*{defaites}*")
            embed.add_field(name="**kill**", value=f"*{kills}*")
            embed.add_field(name="**best winstreak**", value=f"*{bestwinstreak}*")
            embed.add_field(name="**niveaux**", value=f"*{niveau}*")
            embed.add_field(name="**prestige**", value=f"*{prestige}*")
            embed.add_field(name="**Classement kills**", value=f"*{topkill}*")
            embed.add_field(name="**Classement wins**", value=f"*{topwin}*")
            embed.add_field(name="**Classement lvl**", value=f"*{toplvl}*")

            await message.channel.send(embed=embed)
        else:
            await message.channel.send("Le joueur dont tu souhait voir les stats ne sait pas encore /register")


"""
 ❌  embeds
 ✅    ✅      /stats = s
 ✅          Gagné : 0
 ✅          Perdu : 0
 ✅          Kills : 0
 ✅          bestwinstreak : 0
 ✅          lvl : 0
 ✅          prestige : 0
 ✅          classement kill : 0
 ✅          classement win  : 0
 ✅          classement lvl : 0

 set ... pour chaque commande

 on ete ajoute a @joueur

 ✅ faire un /help de calité

 ✅ verifier si negatif ne pas faire

 ci erreure dans la commande repeter la commande avant de return

 mettre toute les commande [commande] [joueur] [valeur] en commande admin

 /lock qui verouille lutilisateur avec un role locked

 fais un /help admin reservé au admin avec les commm admin

 /reset @player ou /reset qui permet de reset cest stats

 /helpadmin [message] envoie un message dans un salon speciale pour une demande

 ✅ prestige max 5 

 ✅faire ci lvl 100 afficher merci de faire /prestige pour augmenter d'un prestige !
 ✅sinon e nombre de niveau ne doit pas dépasser 100 
 ✅dans le +niveau
"""
# ❌,✅
bot.run("NzQyNzI1NzkwMTIyMjQ2MjUw.XzKTSw.m7WxTCdMG3YWQ9L-8FxaosnqDvY")