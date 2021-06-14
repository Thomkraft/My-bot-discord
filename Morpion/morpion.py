import discord
from discord.ext import commands
import pickle


bot = commands.Bot(command_prefix="/",description="Bot de Thomkraft !")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Bot de thomkraft!"))
    print("Ready to use !")


@bot.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith("/morpion ") or message.content.startswith("/m "):
        if message.author.id == bot.user.id:
            return
        channel = message.channel
        player1 = message.author
        player1id = message.author.id
        try:
            player2 = message.content.split(" ")[1]
            player2id = int(message.content.split(" ")[1][3:-1])
        except:
            await channel.send("Il manque le joueur 2 merci de le mentionner apres /morpion")
            return
        if player1.id == player2id: #or player2id == bot.user.id:
            await channel.send(f"Le joueur 1 et joueur 2 sont les meme personnes ou {bot.user.mention} est dans la partie merci de recommencer !")
            return
        casemorpion = "<:testmorpion:844660659585024061>"
        casecroix = "<:croixmorpion:844854506045833236>"
        casecercle = "<:cerclemorpion:844854320050339871>"
        list = [0,0,0,0,0,0,0,0,0]
        emojis = []
        for case in list:
            if case == 0:
                emojis.append(casemorpion)
            elif case == 1:
                emojis.append(casecercle)
            elif case == 2:
                emojis.append(casecroix)
        await channel.send(f"<:empty:844822245150556162> :regional_indicator_a: :regional_indicator_b: :regional_indicator_c: <:empty:844822245150556162>\n"
                           f":one: {emojis[0]}{emojis[1]}{emojis[2]} :one:\n"
                           f":two: {emojis[3]}{emojis[4]}{emojis[5]} :two:\n"
                           f":three: {emojis[6]}{emojis[7]}{emojis[8]} :three:\n"
                           f"<:empty:844822245150556162> :regional_indicator_a: :regional_indicator_b: :regional_indicator_c: <:empty:844822245150556162>")
        await channel.send(f"à {player1.mention} de commencer tape /play [lettre] [chiffre]!")
        pickle.dump(list, open("../BOT THOMGUERRE commandes/list.txt", "wb"))
        pickle.dump(player1id, open("player1id.txt", "wb"))
        turn = 1
        pickle.dump(turn, open("turn.txt", "wb"))
        pickle.dump(player2id, open("player2id.txt", "wb"))
    if message.content.startswith("/play ") or message.content.startswith("/p "): #message.author.id == player1.id:
        player1id = pickle.load(open("player1id.txt", "rb"))
        turn = pickle.load(open("turn.txt", "rb"))
        player2id = pickle.load(open("player2id.txt", "rb"))
        if turn == 1 and message.author.id == player1id:
            channel = message.channel
            casemorpion = "<:testmorpion:844660659585024061>"
            casecroix = "<:croixmorpion:844854506045833236>"
            casecercle = "<:cerclemorpion:844854320050339871>"
            list = pickle.load(open("../BOT THOMGUERRE commandes/list.txt", "rb"))
            print(list)
            lettretotal = ["a", "b", "c"]
            chiffretotal = [1,2,3]
            lettrecoordonnée = message.content.split(" ")[1]
            try:
                lettre = message.content.split(" ")[1]
                chiffre = message.content.split(" ")[2]
            except:
                await channel.send("Une erreur a été comise dans la saisi des coordonnées !")
                return
            if message.author.id == bot.user.id: #or message.author.id == player2.id:
                await channel.send("Le bot ou Le joueur 2 a effectuer la commande alors que ce n'était pas son tour !")
                return
            if lettre.lower() != "a" and lettre.lower() != "b" and lettre.lower() != "c":
                await channel.send("Tu t'es trompé dans les lettres !")
                return
            if chiffre != "1" and chiffre != "2" and chiffre != "3":
                await channel.send("Tu t'es trompé sur le chiffre !")
                return
            if lettrecoordonnée.lower() == "a" and chiffre == "1":
                list[0] = 1
            if lettrecoordonnée.lower() == "a" and chiffre == "2":
                list[3] = 1
            if lettrecoordonnée.lower() == "a" and chiffre == "3":
                list[6] = 1
            if lettrecoordonnée.lower() == "b" and chiffre == "1":
                list[1] = 1
            if lettrecoordonnée.lower() == "b" and chiffre == "2":
                list[4] = 1
            if lettrecoordonnée.lower() == "b" and chiffre == "3":
                list[7] = 1
            if lettrecoordonnée.lower() == "c" and chiffre == "1":
                list[2] = 1
            if lettrecoordonnée.lower() == "c" and chiffre == "2":
                list[5] = 1
            if lettrecoordonnée.lower() == "c" and chiffre == "3":
                list[8] = 1
            emojis = []
            for case in list:
                if case == 0:
                    emojis.append(casemorpion)
                elif case == 1:
                    emojis.append(casecercle)
                elif case == 2:
                    emojis.append(casecroix)
            await channel.send(f"<:empty:844822245150556162> :regional_indicator_a: :regional_indicator_b: :regional_indicator_c: <:empty:844822245150556162>\n"
                               f":one: {emojis[0]}{emojis[1]}{emojis[2]} :one:\n"
                               f":two: {emojis[3]}{emojis[4]}{emojis[5]} :two:\n"
                               f":three: {emojis[6]}{emojis[7]}{emojis[8]} :three:\n"
                               f"<:empty:844822245150556162> :regional_indicator_a: :regional_indicator_b: :regional_indicator_c: <:empty:844822245150556162>")
            await channel.send(f"Au tour de <@!{player2id}> de jouer !")
            print(list)
            pickle.dump(list, open("../BOT THOMGUERRE commandes/list.txt", "wb"))
            turn = 2
            pickle.dump(turn, open("turn.txt", "wb"))
        elif turn == 2 and message.author.id == player2id:
            channel = message.channel
            casemorpion = "<:testmorpion:844660659585024061>"
            casecroix = "<:croixmorpion:844854506045833236>"
            casecercle = "<:cerclemorpion:844854320050339871>"
            list = pickle.load(open("../BOT THOMGUERRE commandes/list.txt", "rb"))
            print(list)
            lettretotal = ["a", "b", "c"]
            chiffretotal = [1, 2, 3]
            lettrecoordonnée = message.content.split(" ")[1]
            try:
                lettre = message.content.split(" ")[1]
                chiffre = message.content.split(" ")[2]
            except:
                await channel.send("Une erreur a été comise dans la saisi des coordonnées !")
                return
            if message.author.id == bot.user.id:  # or message.author.id == player2.id:
                await channel.send("Le bot ou Le joueur 2 a effectuer la commande alors que ce n'était pas son tour !")
                return
            if lettre.lower() != "a" and lettre.lower() != "b" and lettre.lower() != "c":
                await channel.send("Tu t'es trompé dans les lettres !")
                return
            if chiffre != "1" and chiffre != "2" and chiffre != "3":
                await channel.send("Tu t'es trompé sur le chiffre !")
                return
            if lettrecoordonnée.lower() == "a" and chiffre == "1":
                if list[0] == 1 or list[0] == 2:
                    await channel.send("La case que vous voulez jouer est deja prise !")
                else :
                    list[0] = 2
            if lettrecoordonnée.lower() == "a" and chiffre == "2":
                if list[3] == 1 or list[3] == 2:
                    await channel.send("La case que vous voulez jouer est deja prise !")
                else:
                    list[3] = 2
            if lettrecoordonnée.lower() == "a" and chiffre == "3":
                if list[6] == 1 or list[6] == 2:
                    await channel.send("La case que vous voulez jouer est deja prise !")
                else:
                    list[6] = 2
            if lettrecoordonnée.lower() == "b" and chiffre == "1":
                if list[1] == 1 or list[1] == 2:
                    await channel.send("La case que vous voulez jouer est deja prise !")
                else:
                    list[1] = 2
            if lettrecoordonnée.lower() == "b" and chiffre == "2":
                if list[4] == 1 or list[4] == 2:
                    await channel.send("La case que vous voulez jouer est deja prise !")
                else:
                    list[4] = 2
            if lettrecoordonnée.lower() == "b" and chiffre == "3":
                if list[7] == 1 or list[7] == 2:
                    await channel.send("La case que vous voulez jouer est deja prise !")
                else:
                    list[7] = 2
            if lettrecoordonnée.lower() == "c" and chiffre == "1":
                if list[2] == 1 or list[2] == 2:
                    await channel.send("La case que vous voulez jouer est deja prise !")
                else:
                    list[2] = 2
            if lettrecoordonnée.lower() == "c" and chiffre == "2":
                if list[5] == 1 or list[5] == 2:
                    await channel.send("La case que vous voulez jouer est deja prise !")
                else:
                    list[5] = 2
            if lettrecoordonnée.lower() == "c" and chiffre == "3":
                if list[8] == 1 or list[8] == 2:
                    await channel.send("La case que vous voulez jouer est deja prise !")
                else:
                    list[8] = 2
            emojis = []
            for case in list:
                if case == 0:
                    emojis.append(casemorpion)
                elif case == 1:
                    emojis.append(casecercle)
                elif case == 2:
                    emojis.append(casecroix)
            await channel.send(
                f"<:empty:844822245150556162> :regional_indicator_a: :regional_indicator_b: :regional_indicator_c: <:empty:844822245150556162>\n"
                f":one: {emojis[0]}{emojis[1]}{emojis[2]} :one:\n"
                f":two: {emojis[3]}{emojis[4]}{emojis[5]} :two:\n"
                f":three: {emojis[6]}{emojis[7]}{emojis[8]} :three:\n"
                f"<:empty:844822245150556162> :regional_indicator_a: :regional_indicator_b: :regional_indicator_c: <:empty:844822245150556162>")
            await channel.send(f"Au tour de <@!{player2id}> de jouer !")
            print(list)
            turn = 1
            pickle.dump(turn, open("turn.txt", "wb"))
        else:
            await channel.send(f"Une personne vient deffectuer la commande alors que ce n'est pas a lui de jouer !")



"""

     
        await channel.send(f"à {player1.mention} de commencer tape /morpion play [lettre] [chiffre]!")


        @bot.event
        async def on_message(message):
            if message.content.startswith("/morpion play "):
                if message.author.id == bot.user.id:
                    return
                if message.author == player1:
                    lettre = message.content.split(" ")[2]
                    chiffre = message.content.split(" ")[3]
                    if lettre == "A" or lettre == "a" and chiffre == "1":
                        basemorpion = await message.channel.send(f"<:empty:844822245150556162> :regional_indicator_a: :regional_indicator_b: :regional_indicator_c: <:empty:844822245150556162>\n"
                                                                 f":one: {casecercle}{casemorpion}{casemorpion} :one:\n"
                                                                 f":two: {casemorpion}{casemorpion}{casemorpion} :two:\n"
                                                                 f":three: {casemorpion}{casemorpion}{casemorpion} :three:\n"
                                                                 f"<:empty:844822245150556162> :regional_indicator_a: :regional_indicator_b: :regional_indicator_c: <:empty:844822245150556162>")
                        await channel.send(f"Au tour de {player2} de jouer !")
                else:
                    await channel.send(f"C'est a {player1.mention} de jouer")

                1 2 0
                0 0 0
                0 0 0
                
                list = [rond,croix,casevide...]



"""





bot.run("NzQyNzI1NzkwMTIyMjQ2MjUw.XzKTSw.m7WxTCdMG3YWQ9L-8FxaosnqDvY")