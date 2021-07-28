import random
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="/", description="Bot de Thomkraft !")


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Bot de thomkraft!"))
    print("Ready to use !")


funFact = ["L'eau mouille",
           "Le feu brule",
           "Lorsque vous volez, vous ne touchez pas le sol",
           "Winter is coming", "Mon créateur est thomkraft",
           "Il n'est pas possible d'aller dans l'espace en restant sur terre",
           "La terre est ronde",
           "La moitié de 2 est 1",
           "7 est un nombre heureux",
           "Les allemands viennent d'allemagne",
           "Le coronavirus est un virus se répandant en Europe, en avez vous entendu parler ?",
           "J'apparais 2 fois dans l'année, a la fin du matin et au début de la nuit, qui suis-je ?",
           "Le plus grand complot de l'humanité est",
           "Pourquoi lisez vous ca ?"]


@bot.event
async def on_message(message):
    if message.content.startswith("salut"):
        taille_message = len(message.content)
        if taille_message >= 20:
            return
        await message.add_reaction("👋")
        await message.channel.send("Coucou toi !")

    elif message.content == "qui c'est le plus beau ?":
        thomkraft_id = await bot.get_user(91499418383810561)
        print(thomkraft_id)
        await message.channel.send(f"C'est @thomkraft bien sure !")

    # @commands.has_permissions(ban_members=True)
    # @commands.has_any_role("Admin", "OWNER")
    if message.content.startswith("/ban "):
        # utilisateur a ban :
        user: discord.User = message.content.split(" ")[1]
        # reason :
        reason = "Aucune raison n'a été donné"

        list_role = message.author.roles
        authorname = message.author.name
        await message.guild.ban(user, reason=reason)
        embed = discord.Embed(title="**Bannissement**", description="**Un modérateur a frappé !**",
                              url="https://www.youtube.com/watch?v=yw-tMwy216c", colour=discord.Colour.blue())
        embed.set_thumbnail(url="https://emoji.gg/assets/emoji/6623_banhammer.png")
        embed.set_author(name=authorname, icon_url=message.author.avatar_url)
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
        await message.send(embed=embed)


bot.run("ODQzNDUyNDM0NTg3NDUxNDQz.YKEESg.OcH4tmjBOfZfHHBotP5rKLcqC1g")
