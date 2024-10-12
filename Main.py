from dataclasses import replace

import discord
from discord.ext import commands

token = "MTI3NjE0MzYwNjUzNjg2Mzc4Ng.GCUmTf.pdtFm9h3yFYP7QBzD2PnTgXera_C66CMMdaKc0"
intents = discord.Intents.all()
intents.message_content = True
intents.dm_messages = True
intents.emojis = True
intents.members = True
intents.guilds = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
    synced = await bot.tree.sync()
    print(f"{len(synced)} commande(s) synchronisée(s)")


@bot.tree.command(name="bonjour")
async def bonjour(interaction: discord.Interaction):
    await interaction.response.send_message(f"Bonjour ! {interaction.user}")


@bot.command()
async def list(ctx):
    await ctx.send(
        "Liste des commandes : \n- !bonjour \n  - Le bot te dit bonjour \n \n- !list \n  - La liste des commandes \n \n- !info \n  - Ping tout le monde \n \n- !graphistes \n  - Ping les graphistes \n \n- !devs \n  - Ping les développeurs \n \n- !goat \n  - Ping le goat (Ne pas abuser) \n \n- !idee \n  - Ping tout le mode et les gens doivent réagir \n \n- !invite nom métier  \n  - Demande aux gens si la personne peut inviter quelqu'un \n- !reseaux \n - Affiche les réseaux du jeu")


@bot.command()
async def info(ctx):
    await ctx.send("@everyone, \n")


@bot.command()
async def graphistes(ctx, arg):
    await ctx.send("<@&1276277931714412557>, \n" + arg)


@bot.command()
async def devs(ctx, arg):
    await ctx.send("<@&1276277118250254378>, \n" + arg)


@bot.command()
async def goat(ctx, arg):
    await ctx.send("<@&1276276439892889651>, \n" + arg)


@bot.command()
async def idee(ctx):
    await ctx.send("@everyone ✔ ou ❌ :point_up: ! Réagissez !")


@bot.command()
async def compterendu(ctx):
    await ctx.send(
        "||@here|| \nCompte rendu du 23/08/24 : \n - Lundi réunion 11h \n - Fusillades \n - Accidents de voitures \n - Univers gratuit \n - Bateaux \n - Fusées \n - Métiers: \n	Banquiers \n	Pompiers \n	Policiers \n	Militaire \n	Artificiers \n	Agriculteurs \n	DJ \n - Iles \n - Evènement JO 2028: \n	Surf \n	Escrime \n	Football \n	Athlétisme \n	Cérémonie d'ouverture et de clotûre \n - Illerio graphisme [Free] : 'https://discord.gg/graph' \n  - Vidéo chat gpt: \n	Je ne peux pas générer de vidéos directement, mais je peux t'aider à concevoir un script pour une bande-annonce vidéo de ton jeu de simulation de vie LifeCraft: My Virtual World. Voici une idée de script que tu pourrais utiliser : \n	 \n[Ouverture] \n	Scène : Un ciel bleu clair avec des nuages doux, transitionnant vers un monde virtuel vibrant. \n	Voix Off (douce et engageante): Bienvenue dans LifeCraft: My Virtual World, où chaque jour est une nouvelle aventure.	 \n[Scène 1] \n	Montrer un personnage personnalisé se réveillant dans une maison cosy. \n	Voix Off: Créez votre ropre avatar et personnalisez chaque détail de votre maison.	 \n[Scène 2] \n	Le personnage sort de la maison, saluant des voisins dans une communauté virtuelle animée.	Voix Off: Explorez un monde vivant, où chaque voisin est un nouvel ami.	 \n[Scène 3] \n	Plan rapproché sur le personnage travaillant, jardinant, et participant à diverses activités communautaires. \n	Voix Off: Vivez la vie que vous avez toujours rêvé, avec des milliers de possibilités à portée de main.	 \n[Scène 4] \n	Montrer des scènes de construction, avec des maisons et des jardins prenant vie sous les mains du joueur. \n	Voix Off: Bâtissez, créez, et faites grandir votre monde, un bloc à la fois. \n	 \n[Scène 5] \n	Transition vers une scène de célébration avec des feux d'artifice et des personnages dansant ensemble. \n	Voix Off: Rejoignez une communauté mondiale, où chaque décision compte et chaque moment est spécial. \n \n")
    await ctx.send(
        "        \n[Clôture] \n	Affichage du logo LifeCraft: My Virtual World avec un fond coloré et énergique. \n	Voix Off: Téléchargez LifeCraft: My Virtual World aujourd hui, et commencez votre nouvelle vie virtuelle. \n||@here||")


@bot.command()
async def reseaux(ctx):
    await ctx.send("Les réseaux du jeu : https://bit.ly/m/Life-Craft-My-Virtual-World \n Allez y faire un tour ! 😉")


@bot.command()
async def ok(ctx):
    await ctx.send(f"Je suis là, merci de demander {ctx.author} ! 😁")


@bot.command()
async def mp(ctx, member: discord.Member, *message):
    magnifiqueid = 1157663620671488001
    ledevprimeid = 1128719599811178577
    idUser = ctx.author.id
    if idUser == magnifiqueid or idUser == ledevprimeid:
        chars = '(\'\',)'
        await ctx.send(f"Un mp à bien été envoyé à {member.display_name} de ma part pour {ctx.author}")
        print(message)
        translatedMessage = str(message).translate(str.maketrans('', '', chars))
        print(translatedMessage)
        await member.send(f"Salut {member.mention}, \n{translatedMessage}")
    else:
        await ctx.send("Désolé, vous n'avez pas la permission d'exécuter cette commande")

bot.run(token)
