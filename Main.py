import os
from cProfile import label

import discord
from discord.ext import commands

token = ""
intents = discord.Intents.all()
intents.message_content = True
intents.dm_messages = True
intents.emojis = True
intents.members = True
intents.guilds = True
bot = commands.Bot(command_prefix="/", intents=intents)

#Variables utiles
#Users
lcmvwb = 1276143606536863786
magnifiqueid = 1157663620671488001
ledevprimeid = 1128719599811178577
#GeneralsChannels
rules = 1276472259145502742
annonces_discord = 1280860306113040384
annonces_jeu = 1280860214479949854
reseaux = 1280857647351988314
bonjour_aurevoir = 1276278528845021185
general = 1276471754688303197
commandes_bots = 1276480057141100630
memes = 1276480542237266052
debats = 1276481096661602386
aide = 1276474446429028404
idees = 1280861182797807728
ticket = 1283669981384413234
compte = 1295122739471843379

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
    synced = await bot.tree.sync()
    print(f"{len(synced)} commande(s) synchronisée(s)")


@bot.tree.command(name="bonjour", description="Le bot te dit bonjour")
async def bonjour(interaction: discord.Interaction):
    await interaction.response.send_message(f"Bonjour ! {interaction.user}")


@bot.tree.command(name="list", description="Donne la liste des commandes disponibles")
async def list(interaction: discord.Interaction):
    await interaction.response.send_message("Liste de mes commandes:\n- /bonjour\n  - Le bot te dit bonjour\n- /list\n  - Ce que tu vois\n- /graphistes\n  - Ping les graphistes (ne pas abuser)\n- /devs\n  - Ping les devs (ne pas abuser)\n- /goat\n  - Ping le goat (ne surtout pas abuser)\n- /reseaux\n  - Affiche les réseaux du jeu")


@bot.tree.command(name="graphistes", description="Ping les graphistes (l'abus est sanctionné)")
async def graphistes(interaction: discord.Interaction, arg: str):
    await interaction.response.send_message("<@&1276277931714412557>, \n" + arg)


@bot.tree.command(name="devs", description="Ping les devs (l'abus est sanctionné)")
async def devs(interaction: discord.Interaction, arg: str):
    await interaction.response.send_message("<@&1276277118250254378>, \n" + arg)


@bot.tree.command(name="goat", description="Ping le goat (l'abus est sanctionné)")
async def goat(interaction: discord.Interaction, arg: str):
    await interaction.response.send_message("<@&1276276439892889651>, \n" + arg)


@bot.command()
async def compterendu(ctx):
    await ctx.send(
        "||@here|| \nCompte rendu du 23/08/24 : \n - Lundi réunion 11h \n - Fusillades \n - Accidents de voitures \n - Univers gratuit \n - Bateaux \n - Fusées \n - Métiers: \n	Banquiers \n	Pompiers \n	Policiers \n	Militaire \n	Artificiers \n	Agriculteurs \n	DJ \n - Iles \n - Evènement JO 2028: \n	Surf \n	Escrime \n	Football \n	Athlétisme \n	Cérémonie d'ouverture et de clotûre \n - Illerio graphisme [Free] : 'https://discord.gg/graph' \n  - Vidéo chat gpt: \n	Je ne peux pas générer de vidéos directement, mais je peux t'aider à concevoir un script pour une bande-annonce vidéo de ton jeu de simulation de vie LifeCraft: My Virtual World. Voici une idée de script que tu pourrais utiliser : \n	 \n[Ouverture] \n	Scène : Un ciel bleu clair avec des nuages doux, transitionnant vers un monde virtuel vibrant. \n	Voix Off (douce et engageante): Bienvenue dans LifeCraft: My Virtual World, où chaque jour est une nouvelle aventure.	 \n[Scène 1] \n	Montrer un personnage personnalisé se réveillant dans une maison cosy. \n	Voix Off: Créez votre ropre avatar et personnalisez chaque détail de votre maison.	 \n[Scène 2] \n	Le personnage sort de la maison, saluant des voisins dans une communauté virtuelle animée.	Voix Off: Explorez un monde vivant, où chaque voisin est un nouvel ami.	 \n[Scène 3] \n	Plan rapproché sur le personnage travaillant, jardinant, et participant à diverses activités communautaires. \n	Voix Off: Vivez la vie que vous avez toujours rêvé, avec des milliers de possibilités à portée de main.	 \n[Scène 4] \n	Montrer des scènes de construction, avec des maisons et des jardins prenant vie sous les mains du joueur. \n	Voix Off: Bâtissez, créez, et faites grandir votre monde, un bloc à la fois. \n	 \n[Scène 5] \n	Transition vers une scène de célébration avec des feux d'artifice et des personnages dansant ensemble. \n	Voix Off: Rejoignez une communauté mondiale, où chaque décision compte et chaque moment est spécial. \n \n")
    await ctx.send(
        "        \n[Clôture] \n	Affichage du logo LifeCraft: My Virtual World avec un fond coloré et énergique. \n	Voix Off: Téléchargez LifeCraft: My Virtual World aujourd hui, et commencez votre nouvelle vie virtuelle. \n||@here||")


@bot.tree.command(name="reseaux", description="Affiche les réseaux du jeu")
async def reseaux(interaction: discord.Interaction):
    await interaction.response.send_message("Les réseaux du jeu : https://bit.ly/m/Life-Craft-My-Virtual-World \n Allez y faire un tour ! 😉")


@bot.tree.command(name="ok", description="Demande si le bot est en marche")
async def ok(interaction: discord.Interaction):
    await interaction.response.send_message(f"Je suis là, merci de demander {interaction.user.mention} ! 😁")

@bot.tree.command(name="aider", description="Rejoins l'équipe du jeu")
async def aider(interaction: discord.Interaction):
    interaction.response.send_message(f"Si tu veux nous rejoindre {interaction.user.mention}, remplis ce formulaire : https://forms.gle/QDU5R8H3jTzHnNtbA et demande au staff de regarder ton profil dans un ticket ensuite ! :grin:")

@bot.tree.command(name="mp", description="Envoie un message dans un salon spécifié (admins seulement)")
async def mp(interaction: discord.Interaction, member: discord.Member, message: str):
    await interaction.response.defer()
    idUser = interaction.user.id
    if idUser == magnifiqueid or idUser == ledevprimeid:
        chars = '(\'\',)'
        await interaction.followup.send(f"Un mp à bien été envoyé à {member.display_name} de ma part pour {interaction.user.display_name}")
        translatedMessage = str(message).translate(str.maketrans('', '', chars))
        await member.send(f"Salut {member.mention}, \n{translatedMessage}")
    else:
        await interaction.followup.send("Désolé, vous n'avez pas la permission d'exécuter cette commande :man_shrugging:")


@bot.tree.command(name="message", description="Envoie un message dans un salon spécifié (admins seulement)")
async def message(interaction: discord.Interaction, channel: discord.TextChannel, mention: discord.Role, message: str):
    await interaction.response.defer()
    idUser = interaction.user.id
    if idUser == magnifiqueid or idUser == ledevprimeid:
        chars = '(\'\',)'
        translatedMessage = str(message).translate(str.maketrans('', '', chars))
        await channel.send(f"{mention.mention}, \n{translatedMessage}")
    else:
        await interaction.followup.send("Désolé, vous n'avez pas la permission d'exécuter cette commande :man_shrugging:")

@bot.tree.command(name="debat", description="Lance un débat (admins seulement)")
async def debat(interaction: discord.Interaction, rappeler: bool, titre: str, description: str ):
    await interaction.response.defer()
    idUser = int(interaction.user.id)
    channel = int(interaction.channel_id)
    if idUser == magnifiqueid or idUser == ledevprimeid:
        reponse = await interaction.followup.send(f"<@&1283128903082315816> \n**Sujet du jour : {titre}** \nDescription : {description}")
        if os.path.exists("debats.txt"):
            fichierAppend = open("debats.txt", "a")
            fichierRead = open("debats.txt", "r")
            fichierAppend.write('\n' + f"{interaction.created_at} Sujet du jour : {titre}, description : {description}")
        else:
            fichierCreate = open("debats.txt", "x")
            fichierAppend = open("debats.txt", "a")
            fichierRead = open("debats.txt", "r")
            nblignes = 1
            for line in fichierRead:
                nblignes += 1
            fichierAppend.write(f"{interaction.created_at} Sujet du jour : {titre}, description : {description}")
    elif rappeler == True:
        await interaction.followup.send(f"**Sujet du jour : {titre}** \nDescription : {description}")
    else:
        await interaction.followup.send("Désolé, vous n'avez pas la permission d'exécuter cette commande :man_shrugging:")

@bot.tree.command(name="signaler", description="Signale une personne (ne surtout pas abuser)")
async def signaler(interaction: discord.Interaction, membre: discord.Member, raison: str):
    idUser = int(interaction.user.id)
    goat = bot.get_channel(1276469579131912283)
    await interaction.response.defer()
    if membre.id != idUser:
        await interaction.followup.send(f"*{membre.display_name}* à bien été signalé, les admins vont observer cela !")
        if os.path.exists("signalements" + str(membre) + ".txt"):
            fichierAppend = open("signalements" + str(membre) + ".txt", "a")
            fichierRead = open("signalements" + str(membre) + ".txt", "r")
            nblignes = 1
            for line in fichierRead:
                nblignes += 1
            fichierAppend.write('\n' + f"{interaction.created_at} Signalement: raison: {raison}, auteur: {interaction.user.name}")
            if nblignes > 4:
                await goat.send(f"<@{magnifiqueid}><@{ledevprimeid}>, \nAllez voir le fichier **{fichierRead.name}** !")
        else:
            fichierCreate = open("signalements" + str(membre) + ".txt", "x")
            fichierAppend = open("signalements" + str(membre) + ".txt", "a")
            fichierRead = open("signalements" + str(membre) + ".txt", "r")
            nblignes = 1
            for line in fichierRead:
                nblignes += 1
            fichierAppend.write(f"{interaction.created_at} Signalement: raison: {raison}, auteur: {interaction.user.name}")
            if nblignes > 4:
                await goat.send(f"<@{magnifiqueid}><@{ledevprimeid}>, \nAllez voir le fichier **{fichierRead.name}** !")
    else:
        await interaction.followup.send("Vous ne pouvez pas vous signaler vous même ! :man_shrugging:")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(bonjour_aurevoir)
    await channel.send(f"Bienvenue à {member.mention} sur le serveur ! \nOn espère que tu t'amuseras bien ! :grin:")


@bot.event
async def on_message(message):
    idUser = int(message.author.id)
    canalMessageId = message.channel.id
    canalMessage = bot.get_channel(message.channel.id)
    #Magnifique
    if '@here' in message.content or '@everyone' in message.content and idUser == magnifiqueid:
        await message.delete()
        await canalMessage.send(f"<@{magnifiqueid}>, \n**Arrête les teaser, tu ping tout le monde pour rien, sinon je vais partir de l'équipe du jeu !**")
    #Compte
    if canalMessageId == compte and idUser != lcmvwb:
        fichierCompteRead = open("compte.txt", "r")
        fichierCompteAppend = open("compte.txt", "a")
        nblignes = 0
        for line in fichierCompteRead:
            nblignes += 1
        nbline1 = nblignes + 1
        #derniereligne = str(fichierCompteRead.readlines()[int(nblignes)])
        fichierCompteRead.close()
        if int(message.content) == nbline1: #and message.author.id in derniereligne == false:
            thumbsup = '\N{THUMBS UP SIGN}'
            await message.add_reaction(thumbsup)
            fichierCompteAppend.write('\n' + message.content)
        else:
            await message.delete()
    #Detection de liens
    if 'https://' in message.content and idUser != lcmvwb and idUser != ledevprimeid and idUser != magnifiqueid and canalMessageId != annonces_jeu and canalMessageId != annonces_discord and canalMessageId != general and canalMessageId != aide and canalMessageId != debats:
        await message.delete()
        await message.channel.send(f"🛑 Pas de pub ici {message.author.mention} ! 🛑")
        if os.path.exists("data" + str(message.author) + ".txt"):
            fichierAppend = open("data" + str(message.author) + ".txt", "a")
            fichierRead = open("data" + str(message.author) + ".txt", "r")
            nblignes = 1
            for line in fichierRead:
                nblignes += 1
            fichierAppend.write('\n' + f"pub(s): {int(nblignes)}")
        else:
            fichierCreate = open("data" + str(message.author) + ".txt", "x")
            fichierAppend = open("data" + str(message.author) + ".txt", "a")
            fichierRead = open("data" + str(message.author) + ".txt", "r")
            nblignes = 1
            for line in fichierRead:
                nblignes += 1
            fichierAppend.write(f"pub(s): {int(nblignes)}")

bot.run(token)
