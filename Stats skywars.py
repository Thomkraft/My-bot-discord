import discord
import pickle
import os
import random
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix="/", description="Bot de Thomkraft !")

bottest = ["aaaaaa",
           "bbbbbb",
           "cccccc"]

botgame = ["Bot de Thomkraft !",
           "Stats bedwars manuelle !"]

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Bot de thomkraft!"))
    print("Ready to use !")
    changestatus.start()

@tasks.loop(seconds = 5)
async def changestatus():
    game = discord.Game(random.choice(botgame))
    await bot.change_presence(status = discord.Status.online, activity = game)


#pickle.dump(20, open("463804264083619841/toplvl.txt", "wb"))
#nombrewin = pickle.load(open("win.txt", "wb"))

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
            try:
                test = message.content.split(" ")[2]
                await message.channel.send("Erreure dans la commande merci de recommencer !")
                return
            except:
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
                await message.channel.send(f"Les dossier de {user} on bien été crée faites /help pour voir les commandes ! ")

        # WIN

        elif message.content.startswith("+win "):
            userid = message.author.id
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
        elif message.content.startswith("-win "):
            userid = message.author.id
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

        # DEFAITES

        if message.content.startswith("+defaite "):
            userid = message.author.id
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
        elif message.content.startswith("-defaite "):
            userid = message.author.id
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

        # KILLS

        if message.content.startswith("+kill "):
            userid = message.author.id
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
        elif message.content.startswith("-kill "):
            userid = message.author.id
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

        # BEST WINSTREAK

        if message.content.startswith("/setwinstreak "):
            userid = message.author.id
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

        # LVL
        if message.content.startswith("+niveau "):
            userid = message.author.id
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
                        await message.channel.send("Tu a atteint le niveau **100** merci de faire /prestige pour passer un prestige !")
                        return
                    else:
                        await message.channel.send("Ton nombre de niveaux ne doit pas dépasser **100** verifie la commande !")
                        return
                await message.channel.send(f"**{niveau_a_ajouter}** niveaux ont bien été ajouté ! \n"
                                           f"**niveaux** : *{nombreniveaux}* ")
            except:
                await message.channel.send("Le nombre de niveaux a ajouter n'est pas correct merci de recommencer !")
                return

        elif message.content.startswith("-niveau "):
            userid = message.author.id
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

        # PRESTIGE

        elif message.content == ("/prestige"):
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
                await message.channel.send(f"Tu n'est pas niveau **100** donc tu ne peu pas prestige tu est niveau : **{niveau}** plus que **{niveau_resstant}** niveau pour prestige!")

        # CLASSEMENT KILL

        elif message.content.startswith("/settopkill "):
            userid = message.author.id
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

        # CLASSEMENT WINS

        elif message.content.startswith("/settopwin "):
            userid = message.author.id
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

        # CLASSEMENT LVL

        elif message.content.startswith("/settoplvl "):
            userid = message.author.id
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

        elif message.content.startswith("/stats"):
            try:
                var = message.content.split(" ")[2]
                await message.channel.send("__Merci de ne pas mettre de charactere apres le pseudo!__")
                return
            except:
                pass
            if message.content == ("/stats"):
                userid = str(message.author.id)
            else:
                try:
                    user = message.content.split(" ")[1]
                    userid = message.content.split(" ")[1][3:-1]
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
                await message.channel.send(f"__Les stats skywars de <@!{userid}> sont : __\n"
                                           f"**win** : *{win}* \n"
                                           f"**defaites** : *{defaites}* \n"
                                           f"**kill** : *{kills}* \n"
                                           f"**best winstreak** : *{bestwinstreak}* \n"
                                           f"**niveaux** : *{niveau}* \n"
                                           f"**prestige** : *{prestige}* \n"
                                           f"**classement kills** : *{topkill}* \n"
                                           f"**classement wins** : *{topwin}* \n"
                                           f"**classement lvl** : *{toplvl}*")
            else:
                await message.channel.send(f"{user} ne c'est pas enregisstré !")





"""
 ❌  embeds
 ✅    ❌       /stats = s
 ✅   ❌       Gagné : 0
 ✅   ❌       Perdu : 0
 ✅   ❌       Kills : 0
 ✅   ❌       bestwinstreak : 0
 ✅   ❌       lvl : 0
 ✅   ❌       prestige : 0
 ✅   ❌       classement kill : 0
 ✅   ❌       classement win  : 0
 ✅   ❌       classement lvl : 0
 
 set ... pour chaque commande
 
 on ete ajoute a @joueur
 
 faire un /help de calite
 
 ✅ verifier si negatif ne pas faire
 
 
 ✅ prestige max 5 
 
 ✅faire ci lvl 100 afficher merci de faire /prestige pour augmenter d'un prestige !
 ✅sinon e nombre de niveau ne doit pas dépasser 100 
 ✅dans le +niveau
"""
# ❌,✅
bot.run("NzQyNzI1NzkwMTIyMjQ2MjUw.XzKTSw.m7WxTCdMG3YWQ9L-8FxaosnqDvY")